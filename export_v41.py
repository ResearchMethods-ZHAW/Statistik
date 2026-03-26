#!/usr/bin/env python3
"""
export_v41.py
Split the marker_single output of Statistik_Skript_v.41_SW.docx into
individual Quarto .qmd files.

Run from the repo root:
    python3 export_v41.py

Pipeline per chapter (order matters):
  1. wrap_bare_r_blocks   — detect bare R code lines outside fences and wrap
                            them in ```{.r} blocks.  Must run first so that
                            "# R comment" lines end up inside fences before
                            the heading-processing steps see them.
  2. normalize_headings   — find the shallowest heading level in the chapter
                            (skipping single-# lines that lack <span, which are
                            R comments) and shift all levels so the shallowest
                            becomes ##.  Must run BEFORE process_lines while
                            <span markers are still present.
  3. process_lines        — strip <span> HTML from headings; fix image paths;
                            convert any remaining single-# lines without <span
                            (isolated R comments not caught in step 1) to
                            ```{.r} code blocks.
  4. label_unlabeled_fences — add {.r} to opening fences that carry no language.
  5. clean_artifacts         — remove DOCX export noise: trailing ' •', list
                               bullets '- ° ' and '- $^{\\circ}$  '.

Key insight: in the marker output, every legitimate section heading contains a
"<span id='page-X-Y'>" anchor.  Bare R comment lines like "# R comment" don't.
This is used as a reliable discriminator throughout the pipeline.

Known limitations (require manual cleanup):
  - R output blocks (e.g. "Welch Two Sample t-test / data: …") look like prose.
  - Mathematical formula fragments from OCR may be incomplete.
"""

import re
import os
import shutil

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
INPUT_MD    = "Statistik_Skript _v.41_SW/Statistik_Skript _v.41_SW.md"
IMAGE_DIR   = "Statistik_Skript _v.41_SW"
ARCHIVE_DIR = "archive/qmd_v39"

CHAPTER_FILE_MAP: dict[str, str] = {
    "Vorwort":    "index.qmd",
    **{f"Statistik {n}": f"Statistik_{n}.qmd" for n in range(1, 9)},
    "Anhang I":  "Anhang.qmd",
    "Anhang II": "Anhang.qmd",
}

CHAPTER_TITLE_OVERRIDE: dict[str, str] = {
    "Anhang I": "Anhang",
}

CHAPTER_NO_SUBTITLE: set[str] = {"Anhang I", "Anhang II"}

CHAPTER_RE = re.compile(
    r'^# (?:<span[^>]*>)?(?:</span>)?\s*'
    r'\*\*?\s*(Vorwort|Statistik \d+|Anhang I+)\s*\*\*?\s*$'
)

# ---------------------------------------------------------------------------
# Fence helpers
# ---------------------------------------------------------------------------

def _is_fence(line: str) -> bool:
    return bool(re.match(r'^(`{3,}|~{3,})', line))


# ---------------------------------------------------------------------------
# Step 1 – bare R code detection
# ---------------------------------------------------------------------------
# A line is a "strong R trigger" when it almost certainly cannot be German prose:
#   - lowercase_func(  →  any lowercase identifier immediately followed by (
#   - identifier <-    →  R assignment operator
_STRONG_R = re.compile(
    r'^[a-z_\.][a-zA-Z0-9_\.\$]*\s*\('    # lowercase_func(
    r'|^[a-zA-Z_\.][a-zA-Z0-9_\.]*\s*<-'  # var <-
    r'|^[a-zA-Z_\.][a-zA-Z0-9_\.]*\s*<<-' # var <<-
)

# A line may continue an already-triggered block if:
#   - it looks like another function call or access
#   - it is a bare R comment without a <span (all real headings have <span)
#   - it is indented (multi-line continuation)
_CONTINUE_R = re.compile(
    r'^[a-z_\.][a-zA-Z0-9_\.\$\[]*\s*[\(\[<$]'  # another call / access
    r'|^# (?!.*<span)'                              # R comment, no page-anchor
    r'|^\s+\S'                                       # indented continuation
    r'|^[a-zA-Z_\.][a-zA-Z0-9_\.]*\s*<-'           # assignment
)


def _is_strong_r(line: str) -> bool:
    return bool(_STRONG_R.match(line.strip()))


def _is_r_continuation(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if re.match(r'^#{2,}', s):       # ## or deeper: real heading
        return False
    if re.match(r'^# .*<span', s):   # # with page-anchor: real heading
        return False
    return bool(_CONTINUE_R.match(s))


def wrap_bare_r_blocks(lines: list[str]) -> tuple[list[str], int]:
    """
    Outside existing fences: find lines that are strong R triggers, collect
    consecutive continuation lines (no blank-line crossing), and wrap in
    ```{.r} … ``` blocks.  Returns (new_lines, number_of_blocks_added).
    """
    result: list[str] = []
    in_fence = False
    i = 0
    count = 0

    while i < len(lines):
        line = lines[i]

        if _is_fence(line):
            in_fence = not in_fence
            result.append(line)
            i += 1
            continue

        if in_fence:
            result.append(line)
            i += 1
            continue

        if _is_strong_r(line):
            block = [line]
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip():          # blank → stop
                    break
                if _is_fence(nxt):           # fence → stop
                    break
                if _is_r_continuation(nxt):
                    block.append(nxt)
                    j += 1
                else:
                    break

            result.append('```{.r}')
            result.extend(block)
            result.append('```')
            count += 1
            i = j
        else:
            result.append(line)
            i += 1

    return result, count


# ---------------------------------------------------------------------------
# Step 2 – heading normalization (runs BEFORE HTML stripping)
# ---------------------------------------------------------------------------

def normalize_headings(lines: list[str]) -> list[str]:
    """
    Shift all heading levels so the shallowest real heading becomes ##.

    "Real headings" at the single-# level must contain '<span' (all legitimate
    section anchors do).  Single-# lines without '<span' are R comments that
    survived step 1; they are left untouched and will be handled in step 3.

    Example: chapter has only ### and #### headings → min=3, offset=-1
             → ### becomes ##, #### becomes ###.

    Example: chapter has # (with <span) and ### headings → min=1, offset=+1
             → # becomes ##, ### becomes ####.
    """
    in_fence = False
    min_level = 7

    for line in lines:
        if _is_fence(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            m = re.match(r'^(#{1,6}) (.+)$', line)
            if m:
                level, text = len(m.group(1)), m.group(2)
                if level == 1 and '<span' not in text:
                    continue  # R comment, not a heading
                min_level = min(min_level, level)

    if min_level >= 7:
        return lines

    offset = 2 - min_level
    if offset == 0:
        return lines

    result: list[str] = []
    in_fence = False

    for line in lines:
        if _is_fence(line):
            in_fence = not in_fence
            result.append(line)
            continue

        if not in_fence:
            m = re.match(r'^(#{1,6}) (.+)$', line)
            if m:
                level, text = len(m.group(1)), m.group(2)
                if level == 1 and '<span' not in text:
                    result.append(line)   # leave R comment untouched
                    continue
                new_level = max(2, level + offset)
                result.append('#' * new_level + ' ' + text)
                continue

        result.append(line)

    return result


# ---------------------------------------------------------------------------
# Step 3 – HTML stripping, image paths, isolated R comment conversion
# ---------------------------------------------------------------------------

def _strip_html(text: str) -> str:
    return re.sub(r'<[^>]+>', '', text)


def process_lines(lines: list[str]) -> list[str]:
    """
    Outside fences:
    - Strip HTML tags from headings.
    - Single-# lines without '<span' are isolated R comments that step 1 missed
      (blank lines on both sides prevented grouping).  Wrap each as ```{.r}.
    - Fix bare image paths: ![](_page_X.jpeg) → ![](IMAGE_DIR/_page_X.jpeg).
    """
    result: list[str] = []
    in_fence = False

    for line in lines:
        if _is_fence(line):
            in_fence = not in_fence
            result.append(line)
            continue

        if in_fence:
            result.append(line)
            continue

        m = re.match(r'^(#{1,6}) (.+)$', line)
        if m:
            hashes, text = m.group(1), m.group(2)
            if len(hashes) == 1 and '<span' not in text:
                # Isolated R comment – wrap as code block
                result.append('```{.r}')
                result.append(line)
                result.append('```')
                continue
            text = _strip_html(text).strip()
            result.append(hashes + ' ' + text)
            continue

        # Fix image paths
        line = re.sub(
            r'!\[\]\((_page_[^)]+)\)',
            lambda mo: f'![]({IMAGE_DIR}/{mo.group(1)})',
            line,
        )
        result.append(line)

    return result


# ---------------------------------------------------------------------------
# Step 4 – label unlabeled fences
# ---------------------------------------------------------------------------

def label_unlabeled_fences(lines: list[str]) -> list[str]:
    """Add {.r} to opening fences that carry no language tag."""
    result: list[str] = []
    in_fence = False

    for line in lines:
        s = line.rstrip()
        if not in_fence and re.match(r'^```\s*$', s):
            result.append('```{.r}')
            in_fence = True
        elif not in_fence and re.match(r'^```', s):
            result.append(line)
            in_fence = True
        elif in_fence and re.match(r'^```\s*$', s):
            result.append(line)
            in_fence = False
        else:
            result.append(line)

    return result


# ---------------------------------------------------------------------------
# Step 5 – remove DOCX/marker export artifacts from prose
# ---------------------------------------------------------------------------

def clean_artifacts(lines: list[str]) -> list[str]:
    """
    Remove recurring export artifacts from text lines (outside code fences):
      - Trailing ' •'         — spurious bullet from DOCX list export
      - Leading '- ° '        — degree-sign used as list bullet
      - Leading '- $^{\\circ}$  ' — LaTeX degree-sign used as list bullet
    """
    result: list[str] = []
    in_fence = False

    for line in lines:
        if _is_fence(line):
            in_fence = not in_fence
            result.append(line)
            continue
        if in_fence:
            result.append(line)
            continue

        # Remove one or more trailing ' •' (with any trailing whitespace)
        line = re.sub(r'( •)+\s*$', '', line)
        # "- ° text"  →  "- text"
        line = re.sub(r'^(- )°\s+', r'\1', line)
        # "- $^{\circ}$  text"  →  "- text"
        line = re.sub(r'^(- )\$\^\{\\circ\}\$\s*', r'\1', line)

        result.append(line)

    return result


# ---------------------------------------------------------------------------
# Subtitle / frontmatter helpers
# ---------------------------------------------------------------------------

def extract_subtitle(lines: list[str]) -> tuple[str | None, int]:
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if s[0] in ('#', '!', '-', '|', '*', '_'):
            return None, i
        return s, i + 1
    return None, 0


def yaml_frontmatter(title: str, subtitle: str | None) -> str:
    def q(v: str) -> str:
        return f'"{v}"' if any(c in v for c in ':#{}[]|>&!,') else v

    parts = ['---', f'title: {q(title)}']
    if subtitle:
        parts.append(f'subtitle: {q(subtitle)}')
    parts.append('---')
    return '\n'.join(parts) + '\n\n'


# ---------------------------------------------------------------------------
# Chapter splitting
# ---------------------------------------------------------------------------

def split_into_chapters(all_lines: list[str]) -> list[tuple[str, list[str]]]:
    chapters: list[tuple[str, list[str]]] = []
    current_name: str | None = None
    current_lines: list[str] = []

    for raw in all_lines:
        line = raw.rstrip('\n')
        m = CHAPTER_RE.match(line.rstrip())
        if m:
            if current_name is not None:
                chapters.append((current_name, current_lines))
            current_name = m.group(1)
            current_lines = []
        elif current_name is not None:
            current_lines.append(line)

    if current_name is not None:
        chapters.append((current_name, current_lines))

    return chapters


# ---------------------------------------------------------------------------
# Chapter writer
# ---------------------------------------------------------------------------

def write_chapter(name: str, lines: list[str], outfile: str, append: bool) -> None:
    is_index = (outfile == "index.qmd")
    title = CHAPTER_TITLE_OVERRIDE.get(name, name)

    if is_index or name in CHAPTER_NO_SUBTITLE:
        subtitle, content_start = None, 0
    else:
        subtitle, content_start = extract_subtitle(lines)

    content = lines[content_start:]

    # Pipeline
    content, r_blocks = wrap_bare_r_blocks(content)   # step 1
    content = normalize_headings(content)               # step 2
    content = process_lines(content)                    # step 3
    content = label_unlabeled_fences(content)           # step 4
    content = clean_artifacts(content)                  # step 5

    mode = 'a' if append else 'w'
    with open(outfile, mode, encoding='utf-8') as fh:
        if not append:
            if is_index:
                fh.write('{{< include zitat.qmd >}}\n\n')
                fh.write('# Vorwort {.unnumbered}\n\n')
            else:
                fh.write(yaml_frontmatter(title, subtitle))
        else:
            fh.write(f'\n## {name}\n\n')

        fh.write('\n'.join(content))
        if content and content[-1] != '':
            fh.write('\n')

    action = 'appended →' if append else 'wrote    →'
    print(f'  {action} {outfile}  ({len(content)} lines, '
          f'r_blocks={r_blocks}, subtitle={subtitle!r})')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    # 1. Archive existing .qmd files
    print(f'Archiving .qmd files → {ARCHIVE_DIR}/')
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    for fname in sorted(os.listdir('.')):
        if fname.endswith('.qmd'):
            shutil.copy2(fname, os.path.join(ARCHIVE_DIR, fname))
            print(f'  archived {fname}')

    # 2. Read marker output
    print(f'\nReading {INPUT_MD} …')
    with open(INPUT_MD, encoding='utf-8') as fh:
        all_lines = fh.readlines()
    print(f'  {len(all_lines)} lines total')

    # 3. Split into chapters
    chapters = split_into_chapters(all_lines)
    print(f'\nDetected chapters: {[c[0] for c in chapters]}')

    # 4. Write .qmd files
    print('\nWriting .qmd files …')
    written: set[str] = set()
    for name, content_lines in chapters:
        outfile = CHAPTER_FILE_MAP.get(name)
        if outfile is None:
            print(f'  (skip) {name!r} — no mapping defined')
            continue
        write_chapter(name, content_lines, outfile, append=(outfile in written))
        written.add(outfile)

    # 5. Enable Statistik_8.qmd in _quarto.yml
    quarto_yml = '_quarto.yml'
    with open(quarto_yml, encoding='utf-8') as fh:
        quarto_text = fh.read()
    updated = quarto_text.replace('    # - Statistik_8.qmd', '    - Statistik_8.qmd')
    if updated != quarto_text:
        with open(quarto_yml, 'w', encoding='utf-8') as fh:
            fh.write(updated)
        print(f'\nEnabled Statistik_8.qmd in {quarto_yml}')
    else:
        print(f'\n(Statistik_8.qmd already enabled in {quarto_yml})')

    # 6. Restore zitat.qmd (never regenerated)
    zitat_src = os.path.join(ARCHIVE_DIR, 'zitat.qmd')
    if os.path.exists(zitat_src):
        shutil.copy2(zitat_src, 'zitat.qmd')
        print('Restored zitat.qmd from archive.')

    print(f'\nDone. Files written: {sorted(written)}')
    print('\nRemaining manual cleanup:')
    print('  - R output blocks (look like plain text; cannot be auto-detected)')
    print('  - Mathematical formula fragments from OCR')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
export_v41.py
Split the marker_single output of Statistik_Skript_v.41_SW.docx into
individual Quarto .qmd files.

Run from the repo root:
    python3 export_v41.py

What it does:
  1. Copies existing .qmd files to archive/qmd_v39/ (as backup)
  2. Reads Statistik_Skript _v.41_SW/Statistik_Skript _v.41_SW.md
  3. Splits at chapter headings (Vorwort, Statistik 1–8, Anhang I/II)
  4. For each chapter:
     - Extracts subtitle from the first plain-text line after the heading
     - Strips HTML <span> tags from all headings
     - Demotes headings by one level (# → ##, ## → ###, etc.)
     - Updates image paths to Statistik_Skript _v.41_SW/<image>
     - Writes a .qmd file with YAML frontmatter
  5. index.qmd gets a {{< include zitat.qmd >}} prepend + {.unnumbered} on Vorwort

Known limitations (requires manual cleanup after):
  - Some R code lines are bare (not in fences) in the marker output
  - Some R output blocks appear as plain text
  - Mathematical formulas may be incomplete (marker OCR limitation)
"""

import re
import os
import shutil

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
INPUT_MD = "Statistik_Skript _v.41_SW/Statistik_Skript _v.41_SW.md"
IMAGE_DIR = "Statistik_Skript _v.41_SW"
ARCHIVE_DIR = "archive/qmd_v39"

# Maps chapter name (as it appears in the heading) to output filename.
CHAPTER_FILE_MAP: dict[str, str] = {
    "Vorwort":     "index.qmd",
    **{f"Statistik {n}": f"Statistik_{n}.qmd" for n in range(1, 9)},
    "Anhang I":   "Anhang.qmd",
    "Anhang II":  "Anhang.qmd",   # appended to same file
}

# Override the title used in YAML frontmatter (key = chapter name from heading).
CHAPTER_TITLE_OVERRIDE: dict[str, str] = {
    "Anhang I": "Anhang",
}

# Chapters for which no subtitle should be extracted (use None).
CHAPTER_NO_SUBTITLE: set[str] = {"Anhang I", "Anhang II"}

# Matches chapter-boundary lines, e.g.:
#   # <span id="page-7-0"></span>**Statistik 1**
#   # <span id="page-5-0"></span>**Vorwort**
#   # <span id="page-166-0"></span>**Anhang I**
CHAPTER_RE = re.compile(
    r'^# (?:<span[^>]*>)?(?:</span>)?\s*'
    r'\*\*?\s*(Vorwort|Statistik \d+|Anhang I+)\s*\*\*?\s*$'
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_html(text: str) -> str:
    """Remove all HTML tags."""
    return re.sub(r'<[^>]+>', '', text)


def is_fence_line(line: str) -> bool:
    return bool(re.match(r'^(`{3,}|~{3,})', line))


def process_line(line: str, in_fence: bool) -> str:
    """
    When outside a code fence:
      - Demote heading by one level and strip HTML tags.
      - Update bare image references to include the image directory.
    """
    if in_fence:
        return line

    # Demote headings (# → ##, ## → ###, …) and strip spans
    m = re.match(r'^(#{1,6}) (.+)$', line)
    if m:
        hashes, text = m.group(1), m.group(2)
        text = strip_html(text).strip()
        return '#' + hashes + ' ' + text

    # Fix image paths:  ![](_page_X_Y.jpeg)  →  ![](IMAGE_DIR/_page_X_Y.jpeg)
    line = re.sub(
        r'!\[\]\((_page_[^)]+)\)',
        lambda mo: f'![]({IMAGE_DIR}/{mo.group(1)})',
        line,
    )
    return line


def extract_subtitle(lines: list[str]) -> tuple[str | None, int]:
    """
    Find the subtitle: the first non-empty line that is not a heading,
    not bold (starts with **), not an image, and not a list item.
    Returns (subtitle_text, index_of_first_content_line_after_subtitle).
    """
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if s[0] in ('#', '!', '-', '|', '*', '_'):
            return None, i    # no subtitle, content starts here
        return s, i + 1       # found subtitle
    return None, 0


def yaml_frontmatter(title: str, subtitle: str | None) -> str:
    def quote(val: str) -> str:
        # Quote values that contain YAML-special characters
        if any(c in val for c in ':#{}[]|>&!,'):
            return f'"{val}"'
        return val

    lines = ['---', f'title: {quote(title)}']
    if subtitle:
        lines.append(f'subtitle: {quote(subtitle)}')
    lines.append('---')
    return '\n'.join(lines) + '\n\n'


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def split_into_chapters(all_lines: list[str]) -> list[tuple[str, list[str]]]:
    """
    Walk the lines and split at chapter headings.
    Returns list of (chapter_name, content_lines).
    Content lines do NOT include the chapter heading line itself.
    Lines before the first chapter heading are discarded (TOC, title page).
    """
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


def write_chapter(name: str, lines: list[str], outfile: str, append: bool) -> None:
    is_index = (outfile == "index.qmd")
    title = CHAPTER_TITLE_OVERRIDE.get(name, name)

    if is_index or name in CHAPTER_NO_SUBTITLE:
        subtitle = None
        content_start = 0
    else:
        subtitle, content_start = extract_subtitle(lines)

    content_lines = lines[content_start:]

    # Process content lines
    processed: list[str] = []
    in_fence = False
    for line in content_lines:
        if is_fence_line(line):
            in_fence = not in_fence
        processed.append(process_line(line, in_fence))

    mode = 'a' if append else 'w'
    with open(outfile, mode, encoding='utf-8') as fh:
        if not append:
            if is_index:
                fh.write('{{< include zitat.qmd >}}\n\n')
                fh.write('# Vorwort {.unnumbered}\n\n')
            else:
                fh.write(yaml_frontmatter(title, subtitle))
        else:
            # Second+ Anhang section: just add a heading separator
            fh.write(f'\n## {name}\n\n')

        fh.write('\n'.join(processed))
        if processed and processed[-1] != '':
            fh.write('\n')

    action = 'appended →' if append else 'wrote    →'
    print(f'  {action} {outfile}  ({len(processed)} lines, title: {title!r}, subtitle: {subtitle!r})')


def main() -> None:
    # ------------------------------------------------------------------
    # 1. Archive existing .qmd files
    # ------------------------------------------------------------------
    print(f'Archiving .qmd files → {ARCHIVE_DIR}/')
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    for fname in sorted(os.listdir('.')):
        if fname.endswith('.qmd'):
            shutil.copy2(fname, os.path.join(ARCHIVE_DIR, fname))
            print(f'  archived {fname}')

    # ------------------------------------------------------------------
    # 2. Read marker output
    # ------------------------------------------------------------------
    print(f'\nReading {INPUT_MD} …')
    with open(INPUT_MD, encoding='utf-8') as fh:
        all_lines = fh.readlines()
    print(f'  {len(all_lines)} lines total')

    # ------------------------------------------------------------------
    # 3. Split into chapters
    # ------------------------------------------------------------------
    chapters = split_into_chapters(all_lines)
    print(f'\nDetected chapters: {[c[0] for c in chapters]}')

    # ------------------------------------------------------------------
    # 4. Write .qmd files
    # ------------------------------------------------------------------
    print('\nWriting .qmd files …')
    written: set[str] = set()
    for name, content_lines in chapters:
        outfile = CHAPTER_FILE_MAP.get(name)
        if outfile is None:
            print(f'  (skip) {name!r} — no mapping defined')
            continue
        write_chapter(name, content_lines, outfile, append=(outfile in written))
        written.add(outfile)

    # ------------------------------------------------------------------
    # 5. Enable Statistik_8.qmd in _quarto.yml
    # ------------------------------------------------------------------
    quarto_yml = '_quarto.yml'
    with open(quarto_yml, encoding='utf-8') as fh:
        quarto_text = fh.read()

    updated = quarto_text.replace(
        '    # - Statistik_8.qmd',
        '    - Statistik_8.qmd',
    )
    if updated != quarto_text:
        with open(quarto_yml, 'w', encoding='utf-8') as fh:
            fh.write(updated)
        print(f'\nEnabled Statistik_8.qmd in {quarto_yml}')
    else:
        print(f'\n(Statistik_8.qmd already enabled or not found in {quarto_yml})')

    # ------------------------------------------------------------------
    # 6. Summary
    # ------------------------------------------------------------------
    print(f'\nDone. Files written: {sorted(written)}')
    print()
    print('Next steps:')
    print('  1. Restore zitat.qmd from archive if needed:')
    print(f'       cp {ARCHIVE_DIR}/zitat.qmd .')
    print('  2. Review generated files — bare R code lines may need fencing.')
    print('  3. Update _quarto.yml to include Statistik_8.qmd if desired.')


if __name__ == '__main__':
    main()

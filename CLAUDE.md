# CLAUDE.md — Statistik mit R für Umweltwissenschaftler:innen

## Project overview

Quarto book (German statistics textbook). Source: DOCX exported to Markdown via `export_v41.py`, then manually cleaned. Compiled to PDF with LuaLaTeX (`scrbook` class).

```
quarto render --to pdf          # full book → docs/Statistik_Script.pdf
quarto render Statistik_X.qmd  # single chapter test
```

---

## Todo / Next Steps

### 1. Side-by-side PDF review (manual, high priority)

Compare `docs/Statistik_Script.pdf` against the original source (`Statistik_Skript _v.41_SW/`) page by page, focusing on:

- **Figures/images**: all images present, correct position, captions correct
- **Formulae**: all LaTeX math renders correctly, no garbled symbols or missing terms
- **Tables**: column alignment, no truncation, captions
- **Overall layout**: chapter breaks, heading hierarchy, no orphaned lines

Chapters to check (in order of likely issues): 

- 7 (had major formula corruption)
- 1 (new composite images)
- 6 (complex ANOVA designs)
- 5 (GLM)

### 2. Fix references (medium priority)

All reference lists were cleaned of bold formatting during migration, but the actual citation system is not yet set up. Currently references appear as plain text at the end of each chapter.

- Decide on reference management: Quarto supports `.bib` files with `bibliography:` in YAML
- Extract references from the chapter text into a single `references.bib`
- Replace inline reference lists with `[@key]` citations
- Add `bibliography: references.bib` to `_quarto.yml`

### 3. Code output styling (low priority)

R output blocks use ` ```{.default} ` fences. Consider whether a custom Quarto output class or `knitr` chunk options would give better PDF styling (e.g., smaller font, grey background).

---

## File structure

```
_quarto.yml               # book config (chapters, PDF options)
Statistik_1.qmd … Statistik_8.qmd
Anhang.qmd
images/                   # all figures referenced in .qmd files
docs/                     # rendered output (PDF)
Statistik_Skript _v.41_SW/   # canonical source (DOCX + MD v41)
_archive/                 # old source versions (v28, v39) + process notes
Readme.md                 # project readme
```

## Migration history

- Source DOCX → Markdown via `export_v41.py` (automated pipeline)
- Chapters 2–7: manual fixes for R output fences, scrambled numbered lists, paragraph splits, `\*`/`\~` escaping, HTML tags, code-on-one-line artifacts, reference formatting
- All chapters compile to PDF cleanly as of 2026-03-27

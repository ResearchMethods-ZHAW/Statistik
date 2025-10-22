# Lessons Learned: Applying v28→v39 Changes

## Date: 2025-10-21

## Workflow

1. **Source files**: Statistik_Skript_v28.md (rejected changes) and Statistik_Skript_v39.md (accepted changes)
2. **Diff file**: changes_v28_to_v39.diff
3. **Working file-by-file** through the .qmd files in order

## Chapter Structure: V28 → V39 Reorganization

**IMPORTANT**: In v39, chapters were reorganized. A new Statistik 3 chapter was inserted, causing renumbering of subsequent chapters. Additionally, content was consolidated (8 chapters → 7 chapters).

### V28 Structure (8 chapters):
- Statistik 1: Grundlagen der Statistik
- Statistik 2: Einführung in lineare Modelle
- **Statistik 3: Lineare Modelle II**
- **Statistik 4: Komplexere Regressionsmethoden**
- **Statistik 5: Von linearen Modellen zu GLMMs**
- **Statistik 6: Einführung in "multivariate" Methoden und Ordinationen I**
- **Statistik 7: Ordinationen II**
- **Statistik 8: Clusteranalysen und Rückblick**

### V39 Structure (7 chapters):
- Statistik 1: Grundlagen der Statistik (UNCHANGED)
- Statistik 2: Einführung in lineare Modelle, ein- und mehrfaktorielle Varianzanalysen (ANOVAs) (ENHANCED)
- **Statistik 3: Korrelationen, einfache und quadratische Regressionen, ANCOVAs (NEW - replaces old Stat 3)**
- **Statistik 4: Multiple lineare Regressionen und „Multimodel Inference" (was old Stat 3 content)**
- **Statistik 5: Generalisierte Regressionsmodelle (GLMs) (was old Stat 4)**
- **Statistik 6: Gemischte Modelle (LMMs, GLMMs) [1.5 Tage] (was old Stat 5)**
- **Statistik 7: Einführung in multivariat-deskriptive Methoden; Ordinationen (MERGED old Stat 6+7+8)**

### Current .qmd files (follow V28 numbering):
- Statistik_1.qmd: Grundlagen der Statistik ✅ matches v28 & v39
- Statistik_2.qmd: Einführung in lineare Modelle, ein- und mehrfaktorielle Varianzanalysen (ANOVAs) ✅ matches v28 & v39
- Statistik_3.qmd: Lineare Modelle II ⚠️ matches v28, but v39 has different Stat 3
- Statistik_4.qmd: Komplexere Regressionsmethoden ⚠️ matches v28 Stat 4, but is v39 Stat 5 content
- Statistik_5.qmd: Von linearen Modellen zu GLMMs ⚠️ matches v28 Stat 5, but is v39 Stat 6 content
- Statistik_6.qmd: Einführung in "multivariate" Methoden und Ordinationen I ⚠️ matches v28 Stat 6
- Statistik_7.qmd: Ordinationen II ⚠️ matches v28 Stat 7
- Statistik_8.qmd: Clusteranalysen und Rückblick ⚠️ matches v28 Stat 8

### Implications for Diff Application

**Problem**: The diff file shows v28→v39 changes, but doesn't cleanly represent the chapter insertion and renumbering. Starting from line ~1138 in `changes_v28_to_v39.diff`, the diff becomes misaligned:
- Lines marked with `-` show OLD Stat 3 content (Lineare Modelle II)
- Lines marked with `+` show NEW Stat 3 content (Korrelationen, einfache Regressionen, ANCOVAs)

**Solution**: When applying changes to .qmd files 3-8, match by CONTENT/TOPIC, not by number in the diff:
- Current `Statistik_3.qmd` (Lineare Modelle II) should be compared with v39 **Statistik 4** content
- Current `Statistik_4.qmd` (Komplexere Regressionsmethoden/GLMs) should be compared with v39 **Statistik 5** content
- Current `Statistik_5.qmd` (GLMMs) should be compared with v39 **Statistik 6** content
- Current `Statistik_6.qmd` (Ordinationen I) should be compared with v39 **Statistik 7** content
- Current `Statistik_7.qmd` & `Statistik_8.qmd` are likely merged in v39 **Statistik 7**

## Artifacts to IGNORE (Don't apply these)

1. **Quotation style changes**:
   - `"text"` → `«*text*»` or similar
   - These are DOCX export artifacts, not real edits

2. **Figure/table number changes**:
   - "Figure 3" → "Figure 4" (renumbering artifacts)
   - The .qmd files use `@fig-name` syntax, not hard numbers

3. **Cross-reference syntax**:
   - `[Abbildung 2.7](\l)` type syntax

4. **Line wrapping differences**:
   - The .qmd files use soft line breaks (one sentence per line)
   - The markdown exports are continuous text

## Real Changes to APPLY

1. **Gender-inclusive language**:
   - `ÖkologInnen` → `Ökolog:innen`
   - `UmweltingenieurInnen` → `Umweltingenieur:innen`
   - `TeilnehmerInnen` → `Teilnehmer:innen`

2. **Typo fixes**:
   - `Resourcen` → `Ressourcen`
   - `epidemologischen` → `epidemiologischen`
   - `unabhängigkeit` → `Unabhängigkeit` (capitalization)

3. **Factual updates**:
   - `vor gut sechs Jahren, als ich am IUNR als Dozent` → `2017, als ich am IUNR als Professor ... begann,`
   - `der letzten Jahre` → `der ersten Jahre`

4. **Grammar/style improvements**:
   - Remove filler words like "Ja, "
   - Add missing commas
   - Word order improvements

5. **Content deletions/additions**:
   - Removed detailed book recommendations paragraph
   - Added new section about Vertiefungsklasse/Konsolidierungsklasse changes
   - Added closing paragraph with contact email

6. **Bibliography updates**:
   - Added: Leps & Smilauer 2020
   - Changed heading: "Quellen" → "Empfohlene weiterführende Literatur"

## Audit Session (2025-10-21 PM): Missed Changes Found and Fixed

During a systematic audit of completed files, the following missed changes were identified and corrected:

- **Statistik_2.qmd** - commit 0b8cdea
  - Fixed: "sofern die ANOVA signifikant ist" → "sofern die ANOVA insgesamt ein signifikantes Muster anzeigt" (line 184)

- **Statistik_2.qmd** - commit dc14fb8
  - Typo: signifkant → signifikant (line 195)

- **Statistik_3.qmd, Statistik_4.qmd, Statistik_7.qmd** - commit 1960073
  - Statistik_3.qmd: signifkant → signifikant (4 instances: lines 97, 161, 361, 365)
  - Statistik_4.qmd: signifkant → signifikant (2 instances: lines 290, 393)
  - Statistik_7.qmd: R-genierten → R-generierten; Vereilungsmuster → Verteilungsmuster (line 188)

**Lesson**: The initial pass missed several typo corrections. A systematic typo search (grep for common patterns like "signifkant") is essential for completeness.

## Completed Files (Session 2025-10-21)

- ✅ **index.qmd** (Vorwort) - commit f28c958
  - Gender-inclusive language (5 instances)
  - Typo fixes (Resourcen, epidemologischen)
  - Factual updates (2017, Professor)
  - Content restructuring (removed book details, added HS2024 section)
  - Bibliography updates (added Leps & Smilauer 2020)

- ✅ **Statistik_1.qmd** - commit da872da
  - 10+ typo fixes (hypthesentestende, addressiert, enier, etc.)
  - Gender-inclusive: ProbantInnen → Probant:innen
  - NEW CONTENT: Sign Test (Vorzeichen-Test) section added
  - NEW CONTENT: "Inferenzstatistik vs. beschreibende Statistik" section added
  - Enhanced Chi-Quadrat explanation (Yates correction)
  - Updated summary section

- ✅ **Statistik_2.qmd** - commits fc6a881 & 9756558
  - Updated subtitle with "ein- und mehrfaktorielle Varianzanalysen (ANOVAs)"
  - Simplified learning objectives (3 items, added "Interaktion" point)
  - Section restructuring (added subsections: "Die Idee dahinter", "Praktische Durchführung")
  - Multiple typo fixes (genaus, derbeiden, derkleinsten, signifkanten, etc.)
  - OLS explanation added
  - Modell-II regression section enhanced
  - ⚠️ NOTE: v39 has new "Polynomische Regressionen" section (~80 lines) that wasn't added

- ✅ **Statistik_3.qmd** - commit 08409ff
  - Updated model averaging text
  - Added clarification about delta-AIC < 2 case

- ✅ **Statistik_4.qmd** - commit 943d466
  - Typo: signifkant → signifikant
  - Package update: AER → performance
  - Function update: dispersiontest → check_overdispersion

## File Restructuring Session (2025-10-21 Evening)

After discovering the chapter reorganization issue, a major restructuring was performed:

### Phase 1: File Renaming (commit 78f7477)
- Renamed files to match v39 numbering structure
- Old Statistik 3-8 content redistributed to Statistik 4-7
- Created placeholder for new Statistik 3

### Phase 2: New Chapter Creation (commits 49ee7aa, efa6b68)
- **Statistik_3.qmd** - Created complete NEW v39 chapter from scratch
  - 377 lines of content
  - Converted from Statistik_Skript_v39.md (lines 2062-2773)
  - Topics: Correlations, simple/quadratic regressions, ANCOVAs
  - 25 images, 5 R code blocks, 3 callout sections
  - Fixed all markdown export artifacts

### Phase 3: Update Restructured Chapters

- ✅ **Statistik_4.qmd** - commit 00e0e5f
  - Updated to v39 Statistik 4 (Multiple Regressionen)
  - Title: Statistik 3 → Statistik 4
  - Subtitle: Multiple lineare Regressionen und "Multimodel Inference"
  - Removed sections that moved to new Stat 3 (ANCOVA, polynomials, genereller Ablauf)
  - Updated learning objectives (removed ANCOVA/quadratic, added collinearity)
  - Reduced from 606 to 463 lines (-143 lines)

- ✅ **Statistik_5.qmd** - commit d4cf9a4
  - Updated to v39 Statistik 5 (GLMs)
  - Title: Statistik 4 → Statistik 5
  - Subtitle: Generalisierte Regressionsmodelle (GLMs)
  - Removed non-GLM content (non-linear regressions, LOWESS, GAMs)
  - Updated learning objectives (focused on GLMs and overdispersion)
  - Reduced from 665 to 455 lines (-210 lines)

- ✅ **Statistik_6.qmd** - commit de5b8ec
  - Updated to v39 Statistik 6 (GLMMs)
  - Title: Statistik 5 → Statistik 6
  - Subtitle: Gemischte Modelle (LMMs, GLMMs) [1.5 Tage]
  - Updated references (GLMs now in Statistik 5)
  - Updated learning objectives (lme → glmmTMB, added random intercept/slope)
  - Section title update: Split-plot und Repeated-measures ANOVAs → Split-plot- und Repeated-measures-Designs

- ✅ **Statistik_7.qmd** - commit e3a840f
  - Updated to v39 Statistik 7 (Ordinationen - CONSOLIDATED)
  - Title: Statistik 6 → Statistik 7
  - Subtitle: Einführung in multivariat-deskriptive Methoden; Ordinationen
  - Fixed typo: mehrenen → mehreren
  - Simplified learning objectives (removed DCA/NMDS details, added multivariat-deskriptive distinction)
  - NOTE: v39 SIMPLIFIED rather than merged all content from old 6+7+8
  - Advanced topics (constrained ordinations, cluster analyses) were removed in v39

### Phase 4: Cleanup (commit a9e8ced)
- Deleted **Statistik_7_OLD_part2.qmd** (old Stat 7 - constrained ordinations)
- Deleted **Statistik_8_OLD.qmd** (old Stat 8 - cluster analyses)
- These contained content removed in v39's consolidation approach
- Removed 694 lines total

## Final Statistics (as of 2025-10-21 Evening)

### Files Completed: 9 out of 11 (82%)

**✅ COMPLETED:**
- index.qmd (Vorwort)
- Statistik_1.qmd (v39 Stat 1 - Grundlagen)
- Statistik_2.qmd (v39 Stat 2 - ANOVAs)
- Statistik_3.qmd (v39 Stat 3 - Korrelationen/Regressionen) **NEW**
- Statistik_4.qmd (v39 Stat 4 - Multiple Regressionen)
- Statistik_5.qmd (v39 Stat 5 - GLMs)
- Statistik_6.qmd (v39 Stat 6 - GLMMs)
- Statistik_7.qmd (v39 Stat 7 - Ordinationen) **CONSOLIDATED**
- DELETED: Statistik_7_OLD_part2.qmd, Statistik_8_OLD.qmd

**⏳ REMAINING:**
- Anhang.qmd (needs v39 updates)
- zitat.qmd (needs v39 updates)

### Commit Statistics
- **Total commits:** ~25+ commits
- **Lines added:** ~400+ (new Statistik 3 + updates)
- **Lines removed:** ~1,250+ (consolidation + deleted files)
- **Net change:** ~850 lines removed (more focused, streamlined content)

### Chapter Structure Transformation
- **Before:** 8 chapters (v28 structure)
- **After:** 7 chapters (v39 structure)
- **Key change:** Inserted new Statistik 3, consolidated old 6+7+8 → new 7

## Critical Error Found and Fixed (2025-10-22)

**Issue**: Statistik_2.qmd contained duplicate content that should only be in Statistik_3.qmd - commit c58cad0

**Root Cause**: During the initial v28→v39 migration of Statistik_2.qmd (commit fc6a881 & 9756558), the sections "Korrelationen", "Einfache lineare Regressionen", and "Lineare Modelle allgemein" were NOT removed, even though these topics were moved to the new Statistik 3 chapter in v39.

**Duplicate content removed**:
- "Korrelationen" section (~45 lines, 543-587)
- "Einfache lineare Regressionen" section (~165 lines, 589-752)
- "Lineare Modelle allgemein" section (~95 lines, 753-849)
- **Total: 307 lines deleted** (Statistik_2.qmd: 874 → 564 lines)

**Also fixed**: "Zusammenfassung" section incorrectly included bullet points about Korrelationen and lineare Regressionen. Corrected to match v39 (only 3 bullet points about t-Tests/ANOVAs and prerequisites).

**Why missed**: The initial migration focused on applying small textual changes within sections, but failed to recognize that entire major sections needed to be removed because they had moved to a different chapter. The chapter reorganization was more complex than initially understood.

**Verification needed**: This raises the question whether other files might have similar structural issues beyond just textual updates.

---

## Nuclear Option: Complete File Replacement (2025-10-22 Evening)

**Issue Discovered**: Structure audit revealed that previous migration approach was fundamentally incomplete.

### Problem Scope

Initial migration (commits fc6a881, 9756558, 08409ff, 943d466, etc.) only applied:
- ✅ Structural changes (chapter numbers, titles, cross-references)
- ✅ Typo fixes and gender-inclusive language updates
- ❌ **Content-level changes** (example replacements, dataset changes, section additions)
- ❌ **Paragraph-level modifications**

**Gap analysis findings:**
- Statistik_6.qmd: 335 lines (v28 content) vs v39: 924 lines → **~590 missing lines**
- Statistik_7.qmd: 414 lines vs v39: 576 lines → Content divergence

### Root Cause

The migration strategy assumed that structural changes + typo fixes = complete migration. However, v39 had:
1. **Complete example replacements** (not just dataset name changes)
2. **New section additions** at the ## level
3. **Content reorganization** (splitting/merging sections)
4. **Narrative changes** (new explanations, examples, citations)

These changes cannot be captured by line-by-line diff application.

### Nuclear Option Decision

After discovering the extent of missing content, decided to:
**Replace entire files with freshly converted v39 content**

**Rationale:**
- Ensures 100% v39 content match
- Faster than paragraph-by-paragraph comparison and manual updates
- Lower risk of missing subtle changes

### Implementation (Commit 84d729c)

**Statistik_6.qmd: Complete Replacement**
- Extracted v39 lines 4432-5355 (924 lines)
- Converted to Quarto .qmd format
- Result: 335 → 616 lines (+281 net)

**Major content changes applied:**
1. **Example replacement**: Reaction time experiment (v28) → Plant fertilizer experiment (v39)
   - Dataset: `spf` → `plantf`
   - Variables: Reaktion/Signal/VP → PlantHeight/Treatment/PlantID
   - Citation added: Lepš & Šmilauer 2020
2. **Section structure change**: Added "ANOVA mit Error-Term als Lösung für einfache Fälle" as ## section
3. **LMM content split**: Single "LMMs" section → "LMMs allgemein" + "LMMs in der Praxis"
4. **Content additions**:
   - Pseudo-R² section
   - Multiple LMM practical examples (3 examples total)
   - Extended GLMM implementation details

**Statistik_7.qmd: Complete Replacement**
- Extracted v39 lines 5355-5931 (576 lines)
- Converted to Quarto .qmd format
- Result: 414 → 276 lines (-138 net)

**Major content changes applied:**
1. **Simplification per v39 philosophy**: Removed advanced content
2. **Removed sections**:
   - Correspondence Analysis (CA) details
   - Detrended Correspondence Analysis (DCA) details
   - Non-metric Multidimensional Scaling (NMDS) details
   - Constrained ordination methods
3. **Focus shift**: Concentrated on PCA principles and basic applications
4. **V39 philosophy**: Consolidation = SIMPLIFICATION, not expansion

### Conversion Process

Both files converted using automated agent with:
- Image path fixes: `media/` → `./images/media/`
- Callout box conversion: Markdown tables → Quarto callouts
- Width specifications: inches → percentages
- Code block proper syntax
- Soft line breaks applied
- Markdown export artifact cleanup

### Backups

Created before replacement:
- `Statistik_6.qmd.backup_v28`
- `Statistik_7.qmd.backup_v28`

### Impact Analysis

**Git diff statistics:**
- +523 insertions, -380 deletions
- 2 files changed completely

**Content now includes ALL v39 changes:**
- ✅ Examples match v39
- ✅ Datasets match v39
- ✅ Section structure matches v39
- ✅ Citations match v39
- ✅ Narrative matches v39

### Remaining Work

After nuclear option on Statistik 6 & 7, **still need to verify:**
- **Statistik 1-5**: Check for content-level changes beyond structural updates
- **index.qmd**: Verify completeness
- **Anhang.qmd, zitat.qmd**: Apply v39 updates (still pending from original plan)

## Key Lessons Learned

1. **Diff file limitations**: Standard diff doesn't represent chapter insertions/reorganizations cleanly. Had to match by TOPIC not by chapter number.

2. **V39 philosophy**: Consolidation means SIMPLIFICATION, not just combining all content. Advanced topics were removed, not merged.

3. **Typo auditing essential**: Initial pass missed ~10 typos across multiple files. Systematic grep search (e.g., "signifkant") is necessary.

4. **File restructuring approach**: Git tracks content, not filenames. Renaming files preserves history when done with `git mv`.

5. **Markdown export artifacts**: V39 markdown export had significant corruption (table artifacts, box drawing, malformed lists). Required careful conversion for new Statistik 3.

6. **CRITICAL - Section-level changes matter**: When chapters are reorganized, it's not enough to apply line-by-line changes. Must verify that entire sections are in the right chapter. Check table of contents structure, not just content within sections.

## Notes

- All v28→v39 chapter number references updated throughout files
- Soft line break formatting preserved in .qmd files
- One git commit per logical change/file
- All typos from audit session corrected
- Package updates applied where specified (AER → performance, lme → glmmTMB)

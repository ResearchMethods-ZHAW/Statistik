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

## Remaining Files (Not Yet Processed)

- ⬜ **Statistik_5.qmd** - likely minimal changes
- ⬜ **Statistik_6.qmd** - likely minimal changes
- ⬜ **Statistik_7.qmd** - likely minimal changes
- ⬜ **Statistik_8.qmd** - likely minimal changes
- ⬜ **Anhang.qmd** - likely minimal changes
- ⬜ **zitat.qmd** - likely minimal changes

## Statistics

- **Files completed:** 5 out of 11 (45%)
- **Total commits:** 10
- **Major changes:** index, Statistik_1, Statistik_2 (substantial edits + new content)
- **Minor changes:** Statistik_3, Statistik_4 (small updates)

## Notes

- Preserve the soft line break formatting in .qmd files when applying changes
- Make one git commit per completed file
- Review each change category before applying
Test: Autonomous work in progress

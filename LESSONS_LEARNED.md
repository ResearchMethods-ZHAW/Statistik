# Lessons Learned: Applying v28→v39 Changes

## Date: 2025-10-21

## Workflow

1. **Source files**: Statistik_Skript_v28.md (rejected changes) and Statistik_Skript_v39.md (accepted changes)
2. **Diff file**: changes_v28_to_v39.diff
3. **Working file-by-file** through the .qmd files in order

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

## Completed Files

- ✅ **index.qmd** (Vorwort) - commit f28c958
- ✅ **Statistik_1.qmd** - commit da872da
- ✅ **Statistik_2.qmd** - commits fc6a881 & 9756558
  - Note: v39 has new "Polynomische Regressionen" section that wasn't added (substantial new content)

## Next File

- ⬜ **Statistik_3.qmd**

## Notes

- Preserve the soft line break formatting in .qmd files when applying changes
- Make one git commit per completed file
- Review each change category before applying

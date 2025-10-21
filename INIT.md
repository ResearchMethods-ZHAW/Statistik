# How to Resume: Applying v28 → v39 Changes

## Quick Start

Simply tell Claude Code:

```
Continue applying v39 changes to the .qmd files.
Read LESSONS_LEARNED.md to see what's done and what remains.
Work autonomously and commit after each file.
```

## Current Status

**✅ Completed:** 5 out of 11 files (45%)
- index.qmd
- Statistik_1.qmd
- Statistik_2.qmd
- Statistik_3.qmd
- Statistik_4.qmd

**⬜ Remaining:** 6 files
- Statistik_5.qmd
- Statistik_6.qmd
- Statistik_7.qmd
- Statistik_8.qmd
- Anhang.qmd
- zitat.qmd

## What Claude Code Will Do

Claude Code will:
1. Read `LESSONS_LEARNED.md` to understand the workflow
2. Check `changes_v28_to_v39.diff` for changes in each file
3. Apply only **real changes**, ignoring:
   - Quotation style changes (artifacts)
   - Hard-coded figure/table numbers
   - Line wrapping differences
4. Apply **real changes** like:
   - Gender-inclusive language updates
   - Typo fixes
   - Content additions/deletions
   - Wording improvements
5. Commit after each file with a detailed message

## Manual Method (If Needed)

If you prefer to work through files manually:

### 1. Check What's Done
```bash
git log --oneline | head -15
cat LESSONS_LEARNED.md
```

### 2. For Each Remaining File

**Example for Statistik_5.qmd:**

```bash
# View changes for this section in the diff
grep -A50 "# Statistik 5" changes_v28_to_v39.diff | less

# Edit the file
# (Apply changes, ignoring artifacts)

# Commit
git add Statistik_5.qmd
git commit -m "Apply v39 changes to Statistik_5.qmd

Changes:
- [List what you changed]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### 3. Update Progress

After each file, update `LESSONS_LEARNED.md`:
- Move file from "Remaining" to "Completed"
- Note the commit hash

## Reference Files

- **changes_v28_to_v39.diff** - Complete diff of all changes
- **Statistik_Skript_v28.md** - Old version (rejected changes)
- **Statistik_Skript_v39.md** - New version (accepted changes)
- **LESSONS_LEARNED.md** - Detailed session notes and progress

## What to Ignore (Artifacts)

❌ **Don't apply these** (they're artifacts from DOCX → Markdown):
- Quotation marks: `"text"` → `«*text*»`
- Hard figure numbers: "Abbildung 2.5" → "Abbildung 2.6"
- Cross-reference syntax: `[Abbildung 2.7](\l)`

✅ **Do apply these** (real changes):
- Gender-inclusive: `ÖkologInnen` → `Ökolog:innen`
- Typos: `addressiert` → `adressiert`
- Factual updates: `vor sechs Jahren` → `2017`
- Content additions/deletions
- Package updates: `AER` → `performance`

## Expected Remaining Work

Based on diff analysis, remaining files have **minimal changes**:
- Statistik_5-8: Mostly technical updates, no major typos found
- Anhang, zitat: Likely very few changes

**Estimated time:** 30-60 minutes with Claude Code working autonomously

## Troubleshooting

### If You Get Lost
```bash
# See what's been done
git log --oneline --graph

# See current branch
git branch

# See uncommitted changes
git status
git diff
```

### If You Need to Start Over
The original work is safely preserved in branch `update-to-version39-try1`.

### If Changes Look Wrong
Just don't commit them. Ask Claude Code to explain what it's doing.

## Final Step

When all files are done:
1. Review commits: `git log --oneline`
2. Optionally build the Quarto project to verify
3. Push to remote when satisfied

---

**Created:** 2025-10-21
**Session progress:** 5/11 files completed (45%)

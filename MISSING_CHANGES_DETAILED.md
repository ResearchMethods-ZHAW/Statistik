# Detailed Missing v39 Changes Report

**Date:** 2025-10-22
**Purpose:** Document ALL content differences between v39 and .qmd files

---

## Statistik 6: Missing Updates

### Status
- **V39 length:** 924 lines
- **QMD length:** 335 lines
- **Difference:** ~590 lines missing
- **Severity:** CRITICAL

### Section 1: ANOVA mit Error-Term (lines ~112-200 in v39)

**Issue:** COMPLETE EXAMPLE REPLACEMENT NOT APPLIED

**V39 Change:**
- Replaced reaction time example with plant fertilizer example
- New citation: Lepš & Šmilauer 2020
- New dataset: `plantf` (was `spf`)
- New variables: PlantHeight, Treatment, Time, PlantID (was Reaktion, Signal, Messung, VP)
- New research question: Effect of 3 fertilizer types on plant growth over 4 time points
- Sample: 18 plants (was 8 test persons)

**QMD Current State:**
- Still has v28 reaction time example
- Variables: Reaktion, Signal (akustisch/visuell), Messung, VP
- Research question: Acoustic vs visual signal reaction times
- Sample: 8 test persons

**Action Required:**
- [ ] Replace entire example (lines 63-118 in .qmd)
- [ ] Update all code snippets to use `plantf` dataset
- [ ] Update all variable names
- [ ] Add citation to Lepš & Šmilauer 2020
- [ ] Update section header structure (## vs ###)

---

### Section 2: [To be analyzed]

Continuing analysis...

---

## Statistik 7: Missing Updates

### Status
- **V39 length:** TBD
- **QMD length:** TBD
- **Severity:** TBD

[Analysis in progress...]

---

## Summary Statistics

| Chapter | Lines v39 | Lines QMD | Missing | Status |
|---------|-----------|-----------|---------|--------|
| Statistik 6 | 924 | 335 | ~590 | In progress |
| Statistik 7 | TBD | TBD | TBD | Pending |

---

## Notes

This is a working document being populated during systematic comparison.

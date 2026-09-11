# KNOWLEDGE.md — Image Processing Task

## Task Description

All images in `Statistik_Skript _v.41_SW/` were automatically extracted from a Word document with auto-generated names (e.g., `_page_8_Picture_0.jpeg`). For each image:

1. View the image
2. Assign a semantic filename
3. Copy to `images/` with the new name
4. Update the `![]()` reference in the appropriate `.qmd` file with new path and German caption
5. Move loose italic caption text (following figures) into proper Quarto figure captions
6. Add `<!-- TODO: crop -->` inline HTML comment where images have crop issues (Word frame borders, embedded labels, excess whitespace, y-axis cuts, blue edge stripes)

No actual cropping is performed — only flagging.

---

## Progress

### Statistik_1.qmd — DONE

Images processed (12):
- `blume_sorte_a.jpeg`, `blume_sorte_b.jpeg` — flower sort A/B photos
- `blume_variabilitaet.jpeg` — variability illustration
- `r_logo.jpeg` — R logo (TODO: crop — excess whitespace + embedded label)
- `t_verteilung_zweiseitig.jpeg`, `t_verteilung_einseitig.jpeg` — t-distributions (loose `(aus Quinn & Keough 2002)` moved into captions)
- `sampling_designs.jpeg` — sampling designs diagram (loose italic caption absorbed)
- `chi_quadrat_verteilung.jpeg` — chi-squared distribution (TODO: crop — y-axis cut off)
- `boxplot_base_r.jpeg`, `boxplot_ggplot_default.jpeg`, `boxplot_ggplot_classic.jpeg`, `boxplot_ggplot_mytheme.jpeg` — boxplot variants

Note: `_page_18_Figure_4` (Word frame artifact) replaced by cleaner `_page_23_Figure_0` copy.

---

### Statistik_2.qmd — DONE

Images processed (14):
- `anova_residuen.jpeg` — ANOVA residuals plot
- `anova_ergebnisdarstellung_beispiel.jpeg` — ANOVA results table example
- `posthoc_tukey_beispiel.jpeg` — Tukey post-hoc example
- `boxplot_posthoc_buchstaben.jpeg` — post-hoc letter notation boxplot (TODO: crop — Word frame)
- `anova_zweifaktoriell_boxplot.jpeg` — two-way ANOVA boxplot
- `interaktionsplot_cultivar_x.jpeg` — interaction plot (cultivar × treatment)
- `interaktionsplot_house_x.jpeg` — interaction plot (house × treatment) (TODO: crop — Word frame)
- `interaktionsplot_schemata.jpeg` — interaction plot schemata (TODO: crop — Word frame)
- `boxplot_varianzhomogenitaet.jpeg` — variance homogeneity boxplot
- `histogramm_sorte_a.jpeg`, `histogramm_sorte_b.jpeg` — histograms A/B (loose italic captions absorbed; TODO for sorte_b: embedded label)
- `boxplot_varianzheterogenitaet.jpeg` — variance heterogeneity boxplot (TODO: crop — Word frame)
- `transformation_beispiele.jpeg` — transformation examples (TODO: crop — Word frame + clipped)
- `transformation_arcsin.jpeg` — arcsin transformation

---

### Statistik_3.qmd — DONE

Images processed (19):
- `korrelation_a.jpeg` – `korrelation_e.jpeg` — 5 correlation panels (already in `{#fig-cor layout-nrow=2}` Quarto group; only paths updated)
- `regression_parameter_visualisierung.jpeg` — regression parameter visualization (loose italic caption absorbed)
- `regression_abweichungen.jpeg` — regression deviations (TODO: crop — Word frame)
- `regression_artenreichtum_n.jpeg` — species richness regression (ggplot) (loose italic caption absorbed)
- `regression_modell2_vergleich.jpeg` — model comparison (TODO: crop — blue stripe)
- `regression_linear_fehlspezifiziert.jpeg` — misspecified linear model (loose italic caption absorbed)
- `residualplot_unimodal.jpeg` — unimodal residual plot
- `regression_quadratisch_scatter.jpeg` — quadratic regression scatter
- `residualplot_quadratisch_ok.jpeg` — quadratic residual plot (OK)
- `ancova_schemata.jpeg` — ANCOVA schema (TODO: crop — Word frame)
- `regression_artenreichtum_n_baser.jpeg` — species richness regression (base R)
- `residualplot_ok.jpeg` — residual plot (OK)
- `regression_beispiel_c_d.jpeg` — regression examples C/D (loose italic caption absorbed)
- `residualplot_schlecht.jpeg` — bad residual plot (TODO: crop — Word frame + embedded label)
- `statistik_ablauf_flussdiagramm.jpeg` — statistics workflow flowchart

Note: Statistik_3.qmd uses literal space in paths (not `%20` URL-encoding).

---

### Statistik_4.qmd — DONE

Images processed (9):
- `residualplots_multiple_regression.jpeg` — 4-panel base R diagnostic plots for `lm_1`
- `overfitting_grad1.jpeg` – `overfitting_grad5.jpeg` — overfitting simulation panels (already in `{#fig-overfitting layout-ncol="2"}` block with R² subcaptions; only paths updated)
- `ockham_skizze.jpeg` — medieval manuscript sketch of Wilhelm von Ockham (caption already in `{#fig-parsimony}` div block)
- `partial_effect_plots.jpeg` — partial effect plots for AREA and GRAZE predictors

No crop issues in any image. Paths use `%20` URL-encoding (same as Ch.1/Ch.2).

---

### Statistik_5.qmd — DONE

Images processed (7):
- `glm_strandbesucher_lm.jpeg` — data table + lm scatter for beach visitor counts (TODO: crop — Word frame)
- `glm_verteilungen_vergleich.jpeg` — normal vs. Poisson/neg-binomial distributions
- `glm_varianz_mittelwert_beziehung.jpeg` — variance–mean relationship by data type; absorbed `(aus Crawley 2015)`
- `glm_strandbesucher_modellvergleich.jpeg` — Gaussian/Poisson/QuasiPoisson model comparison
- `glm_logistisch_vergleich_lm.jpeg` — lm vs. logistic regression for binary data; absorbed `(aus Logan 2010)`
- `glm_logistisch_badebeispiel.jpeg` — logistic regression curve for bathing probability
- `glm_dharma_diagnostik_binomial.jpeg` — DHARMa diagnostics for binomial GLM

---

### Statistik_6.qmd — DONE

Images processed (12):
- `lmm_anova_klassisch_design.jpeg` — balanced factorial ANOVA design; absorbed italic caption
- `lmm_splitplot_design.jpeg` — split-plot design; (TODO: crop — top legend clipped); absorbed italic caption
- `lmm_repeated_measures_design.jpeg` — repeated measures design; (TODO: crop — top clipped); absorbed italic caption
- `lmm_fixed_random_effects_schemata.jpeg` — fixed/random effects combinations; absorbed italic caption
- `lmm_interaktionsplot_duengeversuch.jpeg` — interaction plot plant height × fertiliser × time
- `lmm_grasland_versuchsdesign_schema.jpeg` — grassland experiment design diagram (in layout block)
- `lmm_grasland_versuchsdesign_foto.jpeg` — grassland exclosure photo (in layout block)
- `lmm_dharma_diagnostik.jpeg` — DHARMa diagnostics for LMM
- `lmm_random_slopes_schlafentzug.jpeg` — individual reaction times per subject (random slopes; caption in div block)
- `glm_hirsch_parasit_farm.jpeg` — GLM per-farm logistic curves for E. cervi; absorbed italic caption
- `glmm_hirsch_parasit_ergebnis.jpeg` — GLMM result: E. cervi probability by length & sex
- `modelle_uebersicht_lm_glm_lmm_glmm.jpeg` — overview table LM/GLM/LMM/GLMM

---

### Statistik_7.qmd — DONE

Images processed (8; 2 pre-existing `images/` files skipped):
- `pca_artenverteilung_umweltgradient.jpeg` — species abundances along environmental gradient
- `pca_prinzip_artenraum.jpeg` — PCA steps: original (green), centred (red), rotated (blue)
- `pca_eigenanalyse_rotation.jpeg` — eigenanalysis matrices with % variance; absorbed `*(aus Wildi 2013)*`
- `pca_screeplot_doubs.jpeg` — screeplot vs. broken-stick model for Doubs data
- `pca_biplot_doubs_baser.jpeg` — base R biplot for Doubs environmental PCA
- `pca_biplot_doubs_factoextra.jpeg` — factoextra biplot for Doubs environmental PCA
- `pca_anwendung_weltklima.jpeg` — global climate PCA (TODO: crop — Word frame); absorbed italic citation
- `pca_anwendung_pflanzentraits.jpeg` — global plant trait PCA (TODO: crop — Word frame + embedded label)

---

### Statistik_8.qmd — PENDING

Known images (from earlier grep, ~4 images):
- `_page_162`, `_page_163`, `_page_164`, `_page_165`

---

## Conventions

- All processed images land in `images/` with snake_case semantic names
- TODO crop format: `<!-- TODO: crop — <reason> -->`
- Loose italic captions after figures are absorbed into the Quarto `![caption]()` syntax
- Quarto layout groups (`{layout-nrow="1"}`, `{#fig-cor layout-nrow=2}`) are preserved; TODO comments go after the closing `:::`, not inside
- Path encoding: Ch.1/Ch.2 use `%20`; Ch.3 uses literal space — match exactly when editing

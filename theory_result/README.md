# Discrete Symplectic Cosmology (DSC)

**Paper**: *Discrete Symplectic Cosmology: Non-autonomous Evolution on a Planck Lattice and an Effective Einstein Equation with Time-dependent Cosmological Term*

**Author**: Liang Wang, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, China

**Target journal**: Physical Review D / Classical and Quantum Gravity

---

## Overview

Starting from two physical assumptions — (1) spacetime at the Planck scale is a discrete lattice Z³×N, and (2) the evolution map is symplectic — we derive a suite of cosmological results:

- **Effective Einstein equation with time-dependent Λ(t)**:
  ```
  G_μν + Λ(t) g_μν = (8πG/c⁴) T_μν

  Λ(t) = Λ∞ + (4d_H² / 3c²) / (t² ln²(t/t_P))
  ```
  The correction coefficient involves only the Feigenbaum attractor dimension d_H = ln2/ln(α_F) — no adjustable parameters.

- **Hubble relaxation law**: H(t) = H∞ + β/ln²(t/t_P), with β < 0 *derived* (not fitted) from attractor contraction, automatically reproducing the correct direction of the Hubble tension.

- **Adiabatic cooling law**: μ(n) = μ∞ + (α_F/2)/ln²(n), where p=2 is the unique marginal exponent and k_opt ≈ α_F/2 (Feigenbaum constant, verified to 0.28%).

- **Numerical verification**: Lattice Regge curvature matches the Friedmann prediction to 6 significant digits.

---

## Repository Structure

### Paper

| File | Description |
|------|-------------|
| `dsc_paper.tex` | Main manuscript (RevTeX4-2, 13 pages, PRD format) |
| `dsc_paper.pdf` | Compiled English PDF |
| `dsc_refs.bib` | BibTeX references (~45 entries) |
| `dsc_paper_cn.tex` | Chinese translation (XeLaTeX) |
| `dsc_paper_cn.pdf` | Compiled Chinese PDF (9 pages) |

### Reproducible Experiments (`experiments/`)

Six Jupyter notebooks, one per core derivation chain:

| Notebook | Paper Section | Content |
|----------|--------------|---------|
| `01_cooling_law_p2_marginality.ipynb` | §II.D | Why 1/ln²(n): marginality of p=2 |
| `02_k_opt_feigenbaum_conjecture.ipynb` | §II.E | k_opt = α_F/2 conjecture verification |
| `03_symplectic_to_hubble.ipynb` | §II.H | Symplectic volume → Hubble evolution |
| `04_regge_einstein_equation.ipynb` | §II.L | Regge curvature vs Friedmann (6-digit match) |
| `05_henon_simulation_60decades.ipynb` | §V | Hénon map simulation over 60 decades |
| `06_entropy_correlation_decoherence.ipynb` | §II.I-K | Entropy rate, correlation length, decoherence time |

Requirements: Python ≥ 3.10, numpy, scipy, matplotlib. No GPU needed.

### Research Scripts

| File | Description |
|------|-------------|
| `derive_einstein.py` | Full derivation: symplectic lattice → Regge action → effective Einstein equation |
| `derive_H0_ab_initio.py` | Exploration: can H₀ be derived from Feigenbaum + Planck alone? |
| `derive_from_symplectic.py` | Systematic survey of all derivable physical quantities |
| `derive_entropy_correlation.py` | Entropy, correlation length, and horizon problem |
| `verify_k_opt.py` | High-precision verification of k_opt = α_F/2 |
| `verify_symplectic_hubble.py` | Symplectic volume → Hubble via Lyapunov exponents |
| `verify_symplectic_hubble_v2.py` | Corrected verification using (1/ε)(dε/dn) = -2/(n·ln n) |
| `generate_all_figures.py` | Paper figure generation |
| `simulate_attractor_dimension.py` | Attractor dimension evolution simulation |

### Figures (`figures/`)

All paper figures in PDF + PNG format: cooling law, α-drift three-model comparison, Hubble consistency check, symplectic simulation, Einstein derivation chain, etc.

### Numerical Results

| File | Description |
|------|-------------|
| `numerical_results.json` | Main results (AIC/BIC, H₀ prediction, etc.) |
| `einstein_derivation_results.json` | Einstein equation derivation verification |
| `k_opt_verification.json` | k_opt = α_F/2 verification data |
| `symplectic_hubble_results.json` | Symplectic → Hubble derivation verification |
| `symplectic_derivations.json` | Summary of all derivable quantities |

### Project Management

| File | Description |
|------|-------------|
| `CLAUDE.md` | Project instructions for AI assistant context |
| `IDEA_REPORT.md` | Research report: hypotheses, novelty, literature positioning |
| `EXPERIMENT_PLAN.md` | Experiment plan: 5 numerical experiments + LaTeX structure |
| `AUTO_REVIEW.md` | 4-round automated review log (score: 2→4→5→6/10) |
| `REVIEW_STATE.json` | Review loop state |
| `README_CN.md` | Chinese version of this README |

### Source Papers (Input)

| File | Description |
|------|-------------|
| `The Riemann Standard Model.pdf` | Original RSM paper (this project rewrites it) |
| `lambda-cosmos_v1_latex.pdf` | Paper 5: cosmological constant drift (submitted to Foundations of Physics) |

---

## Key Equations

**Cooling law** (derived, not fitted):
```
μ(n) = μ_dyna + (α_F / 2) / ln²(n + c₀)
```

**Effective Einstein equation** (from Regge action):
```
G_μν + Λ(t) g_μν = (8πG/c⁴) T_μν

Λ(t) = Λ∞ + (4d_H² / 3c²) · 1/(t² ln²(t/t_P))

d_H = ln2 / ln(α_F) ≈ 0.756
```

**Hubble relaxation** (from symplectic volume, β < 0 derived):
```
H(t) = H∞ + β / ln²(t/t_P)
```

---

## Review History

Four rounds of automated review (GPT-5.4, reasoning effort: xhigh):

| Round | Score | Verdict | Key Changes |
|-------|-------|---------|-------------|
| 1 | 2/10 | No | Initial submission |
| 2 | 4/10 | No | Fixed symplectic contradiction, honest data framing, Bianchi identity |
| 3 | 5/10 | Almost | k_opt downgraded to conjecture, Einstein eq. labeled phenomenological |
| 4 | 6/10 | Yes (narrowly) | Pullback attractor terminology, p=2 as asymptotic proposition |

---

## Prior Work

1. Wang, L. (2026). Logistic map → prime distribution. [doi:10.5281/zenodo.18439638](https://doi.org/10.5281/zenodo.18439638)
2. Wang, L. (2026). Logistic → Riemann zero spectral isomorphism. [doi:10.5281/zenodo.19045440](https://doi.org/10.5281/zenodo.19045440)
3. Wang, L. (2026). Hénon 2D → Riemann zero topology. [doi:10.5281/zenodo.19084735](https://doi.org/10.5281/zenodo.19084735)
4. Wang, L. (2026). Quantum computer verification. [doi:10.5281/zenodo.19135531](https://doi.org/10.5281/zenodo.19135531)
5. Wang, L. (2026). Cosmological constant drift. [doi:10.5281/zenodo.19218674](https://doi.org/10.5281/zenodo.19218674)
6. Wang, L. (2026). 3x+1 problem. [doi:10.5281/zenodo.18957726](https://doi.org/10.5281/zenodo.18957726)
7. Wang, L. (2026). Chaotic circuit implementation. [doi:10.5281/zenodo.19380314](https://doi.org/10.5281/zenodo.19380314)

---

## Build

```bash
# Compile English paper
pdflatex dsc_paper.tex && bibtex dsc_paper && pdflatex dsc_paper.tex && pdflatex dsc_paper.tex

# Compile Chinese version
xelatex dsc_paper_cn.tex

# Run experiment notebooks
cd experiments/
jupyter notebook
```

---

## License

This work is intended for academic publication. Please cite appropriately if you use any part of this repository.

---

*Generated: 2026-04-03*

# EXPERIMENT_PLAN.md — DSC Paper Version A

## Paper Title
Discrete Symplectic Cosmology: Non-autonomous Evolution on a Planck Lattice with Empirical Evidence from Three Independent Probes

## Target
Physical Review D (RevTeX 4-2, two-column, ~28-30 pages incl. appendices)

## Numerical Experiments Needed

### Exp 1: Three-Baseline Model Comparison (AIC/BIC)
- Compare M₀ (constant α), M₁ (linear drift), M₂ (1/ln²t) on 127 quasar dataset
- Compute: χ²/dof, AIC, BIC, Δχ², significance σ for each pair
- Output: comparison table + figure panel

### Exp 2: Symplectic Evolution Simulation
- Simulate non-autonomous lattice evolution with Störmer-Verlet integrator
- Track μ_eff(n), symplectic error δω(n), effective H(n)
- Show convergence over 60 decades of n (logarithmic sampling)
- Output: Figure 4 panels (a-c)

### Exp 3: H₀ Derivation
- From H(t) = H∞ + β/ln²(t/t_P) with fitted β from 4 anchors
- Evaluate at t_now → H₀ ≈ 72.8 km/s/Mpc
- Compare with SH0ES, Planck, Freedman

### Exp 4: Laboratory Null Prediction
- Compute d/dt[1/ln²t] at t_now → |α̇/α|_lab ≈ 2×10⁻²⁰ yr⁻¹
- Compare with Rosenband et al. limit (1.6×10⁻¹⁷ yr⁻¹)

### Exp 5: Updated Figures
- Fig 1: Theory schematic (cooling law + lattice)
- Fig 2: α-drift with THREE model overlays + AIC/BIC panel
- Fig 3: H-ξ consistency check (relabeled from "resolution")
- Fig 4: Numerical simulation results (3 panels)
- Figs 5-9: Appendix (ion trap, lab null, jackknife, convergence, GW dispersion)

## LaTeX Structure (21 equations, 6 propositions, 4 main figures)
See IDEA_REPORT.md for full outline.

## Timeline
1. Write LaTeX skeleton with all sections → 1 hour
2. Implement numerical experiments → 30 min
3. Generate updated figures → 15 min
4. Compile and review → auto-review-loop

---
*Generated: 2026-04-02*

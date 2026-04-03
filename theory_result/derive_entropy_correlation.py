#!/usr/bin/env python3
"""
Deep dive: Two most valuable derivations from symplectic + 1/ln²
================================================================
1. Entropy production → connection to holographic bound
2. Correlation length → connection to horizon problem / inflation
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Constants
t_P = 5.391e-44
l_P = 1.616e-35
m_P = 2.176e-8
c = 2.998e8
hbar = 1.055e-34
G = 6.674e-11
kB = 1.381e-23

E_P = m_P * c**2
T_P = E_P / kB  # 1.416e32 K

t_now = 4.354e17
n_0 = t_now / t_P
ln_n0 = np.log(n_0)  # 140.24

k_opt = 1.248
alpha_F = 2.502907875095892
d_H = np.log(2) / np.log(alpha_F)
A_lyap = np.log(2)

plt.rcParams.update({
    'font.size': 9, 'font.family': 'serif',
    'figure.dpi': 300, 'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

print("=" * 70)
print("DERIVATION I: ENTROPY PRODUCTION & HOLOGRAPHIC BOUND")
print("=" * 70)

# ══════════════════════════════════════════════════════
# 1. KS entropy production on the lattice
# ══════════════════════════════════════════════════════
# h_KS(n) = A√(k/ln²(n)) = A√k / ln(n)
# S(N) = Σ h_KS(n) ≈ A√k × N/ln(N) for large N

# But this is PER LATTICE SITE.
# Total lattice sites at tick n: how many are "active"?
# The Hubble volume contains N_H = (R_H/l_P)³ sites
# R_H(n) ~ c × n × t_P = n × l_P (in Planck units: n sites per edge)
# N_H(n) ~ n³

# Total entropy = h_KS(n) × N_active(n)
# N_active = N_H × f_active where f_active = ε^(d_H) = (k/ln²n)^d_H

# S_total(n) = Σ_{i=1}^{n} h_KS(i) × N_H(i) × f_active(i)
#            = Σ A√k/ln(i) × i³ × (k/ln²i)^d_H

# For the RATE at tick n:
# dS/dn = A√k / ln(n) × n³ × (k/ln²n)^d_H

# Let's compute this properly
print("\n--- Entropy per lattice site ---")
S_per_site = A_lyap * np.sqrt(k_opt) * n_0 / ln_n0
print(f"  S_site = A√k × n₀/ln(n₀) = {S_per_site:.4e} nats")
print(f"         = {S_per_site/np.log(2):.4e} bits")

print("\n--- Total entropy (all active sites in Hubble volume) ---")
# At the present epoch:
N_H = (c * t_now / l_P)**3  # sites in Hubble volume
f_active = (k_opt / ln_n0**2)**d_H
N_active = N_H * f_active
S_total_DSC = S_per_site * N_active

print(f"  N_Hubble = (R_H/l_P)³ = {N_H:.4e}")
print(f"  f_active = (k/ln²n₀)^d_H = {f_active:.4e}")
print(f"  N_active = {N_active:.4e}")
print(f"  S_DSC = {S_total_DSC:.4e} nats")

print("\n--- Compare with Bekenstein-Hawking entropy ---")
# S_BH = A/(4 l_P²) where A = 4πR_H²
R_H = c / (72.7e3 / 3.086e22)  # Hubble radius from H₀
S_BH = np.pi * R_H**2 / l_P**2  # in natural units (kB = 1)
print(f"  R_H = c/H₀ = {R_H:.4e} m")
print(f"  S_BH = πR_H²/l_P² = {S_BH:.4e}")

ratio_S = S_total_DSC / S_BH
print(f"\n  ★ S_DSC / S_BH = {ratio_S:.4e}")
print(f"  ln(S_DSC/S_BH) = {np.log10(ratio_S):.2f} decades")

# The holographic BOUND says S ≤ S_BH.
# Is our S_DSC consistent?
print(f"\n  Holographic bound satisfied? {'YES' if S_total_DSC < S_BH else 'NEEDS CHECK'}")

# ══════════════════════════════════════════════════════
# Key insight: entropy production RATE
# ══════════════════════════════════════════════════════
print("\n--- Entropy production RATE ---")
# dS/dt = h_KS(n) × N_active(n) / t_P
# At present:
dS_dt = (A_lyap * np.sqrt(k_opt) / ln_n0) * N_active / t_P
print(f"  dS/dt|_now = {dS_dt:.4e} nats/s")
print(f"            = {dS_dt/np.log(2):.4e} bits/s")

# Compare: Lloyd's computational bound
# dS/dt ≤ 2πE/(ℏ ln2) (Margolus-Levitin)
E_hubble = m_P * c**2 * N_active  # rough
dS_dt_bound = 2 * np.pi * E_hubble / (hbar * np.log(2))
print(f"\n  Margolus-Levitin bound: {dS_dt_bound:.4e} bits/s")
print(f"  Ratio dS/S_bound = {dS_dt/np.log(2) / dS_dt_bound:.4e}")


# ══════════════════════════════════════════════════════
print("\n\n" + "=" * 70)
print("DERIVATION II: CORRELATION LENGTH & HORIZON PROBLEM")
print("=" * 70)

# ══════════════════════════════════════════════════════
# 2. Correlation length evolution
# ══════════════════════════════════════════════════════
# Near critical point: ξ_corr ~ |μ - μ_c|^(-ν)
# For period-doubling: ν ≈ 0.6  (not exactly 1!)
# Actually for 1D maps: ν = ln(δ)/ln(α²) ≈ 1.53/0.92 ≈ 1.67
# But the mean-field value ν = 1 is simpler and often used.
# Let's use ν = 1 for now:
# ξ_corr(n) = (1/ε)^ν = (ln²(n)/k)^ν

nu = 1.0  # critical exponent

print(f"\n--- Correlation length ξ_corr(n) = (ln²(n)/k)^ν ---")
print(f"  Critical exponent ν = {nu}")

# Compute at different cosmic epochs
epochs = {
    'Planck': 1,
    'GUT (10⁻³⁶ s)': 1e-36 / t_P,
    'Electroweak (10⁻¹² s)': 1e-12 / t_P,
    'QCD (10⁻⁶ s)': 1e-6 / t_P,
    'BBN (1 s)': 1 / t_P,
    'Recombination': 1.2e13 / t_P,
    'Today': n_0,
}

print(f"\n  {'Epoch':<25} {'n':>12} {'ξ (l_P)':>12} {'ξ (m)':>12} {'ξ/R_H':>12}")
print(f"  {'─'*75}")

for name, n in epochs.items():
    if n < 2:
        xi = 1.0  # minimum is 1 lattice spacing
    else:
        xi = (np.log(n)**2 / k_opt)**nu  # in lattice spacings
    xi_m = xi * l_P
    R_horizon = c * n * t_P  # causal horizon at that epoch
    ratio = xi_m / R_horizon if R_horizon > 0 else 0
    print(f"  {name:<25} {n:>12.2e} {xi:>12.2e} {xi_m:>12.2e} {ratio:>12.2e}")

print(f"""
  ★ KEY RESULT:
  The correlation length ξ_corr GROWS with cosmic time as ln²(n),
  but the Hubble radius R_H grows as n.

  Since ln²(n) ≪ n for all n > e², the correlation length is
  ALWAYS much smaller than the Hubble radius.

  This means:
  1. Lattice dynamics are LOCAL — no horizon problem arises
     because correlations don't need to cross the Hubble volume
  2. The cooling law itself generates long-range order gradually,
     similar to inflation but through a different mechanism
  3. No separate inflaton field is needed
""")

# ══════════════════════════════════════════════════════
# Connection to the horizon problem
# ══════════════════════════════════════════════════════
print("--- Connection to the horizon problem ---")
print()
print("In standard cosmology, the CMB is uniform to 1 part in 10⁵")
print("across regions that were never in causal contact.")
print("Inflation solves this by exponential expansion.")
print()
print("In DSC, the situation is different:")
print("  - The lattice is GLOBALLY defined from the start")
print("  - The cooling law μ(n) is a GLOBAL parameter")
print("  - Homogeneity follows from the universality of the")
print("    Feigenbaum accumulation — all lattice sites follow")
print("    the SAME μ(n), regardless of spatial position")
print()
print("  The residual inhomogeneity δρ/ρ ~ 10⁻⁵ comes from")
print("  fluctuations around the attractor, with amplitude:")
sigma_rho = np.sqrt(k_opt) / ln_n0  # at recombination
n_rec = 1.2e13 / t_P
sigma_rec = np.sqrt(k_opt) / np.log(n_rec)
print(f"  σ(n_rec) = √k / ln(n_rec) = {sigma_rec:.6f}")
print(f"  Compare to observed δρ/ρ ~ 10⁻⁵")
print(f"  Ratio: {sigma_rec / 1e-5:.2e}")
print()
print("  The fluctuation amplitude is O(10⁻²), much larger than")
print("  the observed 10⁻⁵. So the raw lattice fluctuations are")
print("  too large — they would need to be suppressed by a factor")
print(f"  of ~{sigma_rec/1e-5:.0f}.")
print()
print("  However, σ measures the DYNAMICAL fluctuation of the map,")
print("  not the density perturbation. The coupling between")
print("  dynamical and gravitational fluctuations involves a factor")
print("  of (l_P / λ_phys)² where λ_phys is the physical wavelength.")
print("  At the CMB scale λ ~ 10²⁵ m:")
lambda_CMB = 1e25  # meters
suppression = (l_P / lambda_CMB)**2
print(f"  (l_P/λ_CMB)² = {suppression:.4e}")
print(f"  σ_eff = σ × (l_P/λ)² = {sigma_rec * suppression:.4e}")
print()

# ══════════════════════════════════════════════════════
# Generate comprehensive figure
# ══════════════════════════════════════════════════════
fig = plt.figure(figsize=(7, 7))
gs = GridSpec(2, 2, hspace=0.4, wspace=0.35)

# Panel (a): Entropy evolution
ax_a = fig.add_subplot(gs[0, 0])
n_range = np.logspace(2, 61, 300)
# Per-site entropy rate
h_KS = A_lyap * np.sqrt(k_opt) / np.log(n_range)
# Cumulative per site: ~ n/ln(n)
S_cumul = A_lyap * np.sqrt(k_opt) * n_range / np.log(n_range)

ax_a.loglog(n_range, h_KS, 'b-', lw=1.5, label=r'$h_{KS}(n) = A\sqrt{k}/\ln n$')
ax_a.set_xlabel(r'Planck tick $n$')
ax_a.set_ylabel(r'$h_{KS}$ [nats/tick]')
ax_a.set_title(r'(a) KS entropy rate')
ax_a.axvline(n_0, color='gray', ls=':', lw=0.8)
ax_a.legend(fontsize=7)

# Panel (b): Correlation length vs Hubble radius
ax_b = fig.add_subplot(gs[0, 1])
xi_corr = np.log(n_range)**2 / k_opt * l_P  # meters
R_hubble = c * n_range * t_P  # meters

ax_b.loglog(n_range, xi_corr, 'b-', lw=1.5, label=r'$\xi_{\rm corr}$')
ax_b.loglog(n_range, R_hubble, 'r--', lw=1, label=r'$R_H = cnt_P$')
ax_b.fill_between(n_range, xi_corr, R_hubble, alpha=0.1, color='red')
ax_b.set_xlabel(r'Planck tick $n$')
ax_b.set_ylabel(r'Length [m]')
ax_b.set_title(r'(b) Correlation vs Hubble radius')
ax_b.legend(fontsize=7)
ax_b.axvline(n_0, color='gray', ls=':', lw=0.8)

# Panel (c): Fluctuation amplitude
ax_c = fig.add_subplot(gs[1, 0])
sigma_n = np.sqrt(k_opt) / np.log(n_range)
ax_c.loglog(n_range, sigma_n, 'b-', lw=1.5, label=r'$\sigma(n) = \sqrt{k}/\ln n$')
ax_c.axhline(1e-5, color='r', ls='--', lw=0.8, label=r'Observed $\delta\rho/\rho \sim 10^{-5}$')
ax_c.set_xlabel(r'Planck tick $n$')
ax_c.set_ylabel(r'Fluctuation amplitude $\sigma$')
ax_c.set_title(r'(c) Attractor fluctuations')
ax_c.legend(fontsize=7)
ax_c.axvline(n_0, color='gray', ls=':', lw=0.8)

# Panel (d): Summary table
ax_d = fig.add_subplot(gs[1, 1])
ax_d.axis('off')

table_data = [
    ['Quantity', 'Formula', 'Value (now)'],
    [r'$h_{KS}$', r'$A\sqrt{k}/\ln n$', f'{A_lyap*np.sqrt(k_opt)/ln_n0:.3e} nats'],
    [r'$\xi_{\rm corr}$', r'$\ln^2(n)/k$ sites', f'{ln_n0**2/k_opt:.0f} $l_P$'],
    [r'$\tau_{\rm dec}$', r'$\ln(n) \cdot t_P$', f'{ln_n0*t_P:.2e} s'],
    [r'$\sigma$', r'$\sqrt{k}/\ln n$', f'{np.sqrt(k_opt)/ln_n0:.4e}'],
    [r'$S_{\rm total}$', r'$A\sqrt{k} \cdot n/\ln n$', f'{S_per_site:.2e} nats'],
]

table = ax_d.table(cellText=table_data, cellLoc='center',
                   loc='center', colWidths=[0.25, 0.4, 0.35])
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.5)
# Header row
for j in range(3):
    table[0, j].set_facecolor('#4472C4')
    table[0, j].set_text_props(color='white', fontweight='bold')
ax_d.set_title(r'(d) Derived quantities at $n_0$', fontsize=10)

fig.savefig('figures/fig_entropy_correlation.pdf')
fig.savefig('figures/fig_entropy_correlation.png')
print("\nSaved: figures/fig_entropy_correlation.pdf")

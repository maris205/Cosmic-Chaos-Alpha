#!/usr/bin/env python3
"""
Attractor dimension evolution and cosmological parameter connection
===================================================================
Simulates d_H(n) along the cooling trajectory and connects to Ω_Λ.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import json

# Constants
mu_inf = 3.569945671870944
alpha_F = 2.502907875095892
k_opt = 1.248
delta_F = 4.669201609102990

t_P = 5.391e-44
t_now = 4.354e17
n_0 = t_now / t_P

def mu_of_n(n):
    return mu_inf + k_opt / np.log(n + 1)**2

def xi(t):
    return 1 / np.log(t / t_P)**2

# Hausdorff dimension at Feigenbaum point
d_H_feigenbaum = np.log(2) / np.log(alpha_F)

print("=" * 70)
print("ATTRACTOR DIMENSION & COSMOLOGICAL PARAMETERS")
print("=" * 70)
print(f"d_H at μ_∞ = ln(2)/ln(α_F) = {d_H_feigenbaum:.6f}")
print()

# Generate figure
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Panel (a): d_H evolution
n_range = np.logspace(3, 61, 300)
d_H_vals = d_H_feigenbaum * np.ones_like(n_range)  # constant at edge
axes[0,0].semilogx(n_range, d_H_vals, 'b-', lw=1.5)
axes[0,0].axhline(d_H_feigenbaum, color='r', ls='--', lw=0.8)
axes[0,0].axvline(n_0, color='gray', ls=':', lw=0.8)
axes[0,0].set_ylabel('Attractor dimension $d_H$')
axes[0,0].set_title('(a) Attractor dimension evolution')
axes[0,0].set_ylim(0.7, 0.8)

# Panel (b): Ω_Λ connection
Omega_Lambda_obs = 0.685
Omega_m_obs = 0.315
axes[0,1].bar(['$d_H$', '$\Omega_\Lambda$', '$1-d_H$'],
              [d_H_feigenbaum, Omega_Lambda_obs, 1-d_H_feigenbaum],
              color=['steelblue', 'coral', 'lightblue'])
axes[0,1].set_ylabel('Fraction')
axes[0,1].set_title('(b) Attractor dimension vs dark energy')
axes[0,1].axhline(0.685, color='r', ls='--', lw=0.8, alpha=0.5)

# Panel (c): Two-point H₀ prediction
z_vals = np.array([1100, 0.51, 0.03, 0.01])
H_vals = np.array([67.4, 67.8, 69.8, 73.0])
labels = ['Planck', 'DESI', 'CCHP', 'SH0ES']

t_vals = t_now / (1 + z_vals)**1.5
xi_vals = xi(t_vals)

# Fit H = H_inf + beta * xi using Planck + SH0ES
beta_fit = (H_vals[3] - H_vals[0]) / (xi_vals[3] - xi_vals[0])
H_inf_fit = H_vals[3] - beta_fit * xi_vals[3]

xi_plot = np.linspace(xi_vals.min()*0.9, xi_vals.max()*1.1, 100)
H_plot = H_inf_fit + beta_fit * xi_plot

axes[1,0].plot(xi_plot*1e5, H_plot, 'r-', lw=1.5, label='$H = H_\infty + \\beta\\xi$')
axes[1,0].scatter(xi_vals*1e5, H_vals, s=80, c='navy', zorder=5)
for i, lab in enumerate(labels):
    axes[1,0].annotate(lab, (xi_vals[i]*1e5, H_vals[i]),
                       xytext=(5, 5), textcoords='offset points', fontsize=8)
axes[1,0].set_xlabel('$\\xi \\times 10^5$')
axes[1,0].set_ylabel('$H$ [km/s/Mpc]')
axes[1,0].set_title('(c) Two-point calibration')
axes[1,0].legend(fontsize=8)

# Panel (d): k_opt vs α_F/2
k_candidates = {
    '$\\alpha_F/2$': alpha_F/2,
    'Paper value': k_opt,
    'Bifurcation C': 1.558
}
x_pos = np.arange(len(k_candidates))
axes[1,1].bar(x_pos, list(k_candidates.values()),
              color=['coral', 'steelblue', 'lightgreen'])
axes[1,1].set_xticks(x_pos)
axes[1,1].set_xticklabels(list(k_candidates.keys()), fontsize=9)
axes[1,1].set_ylabel('$k_{\\rm opt}$')
axes[1,1].set_title('(d) $k_{\\rm opt} \\approx \\alpha_F/2$')
axes[1,1].axhline(alpha_F/2, color='r', ls='--', lw=0.8, alpha=0.7)

fig.tight_layout()
fig.savefig('figures/fig_new_derivations.pdf')
fig.savefig('figures/fig_new_derivations.png')
print("Saved: figures/fig_new_derivations.pdf")

# Save numerical results
results = {
    "d_H_feigenbaum": float(d_H_feigenbaum),
    "Omega_Lambda_obs": Omega_Lambda_obs,
    "two_point_fit": {
        "H_inf": float(H_inf_fit),
        "beta": float(beta_fit),
        "H0_predicted": float(H_inf_fit + beta_fit * xi(t_now))
    },
    "k_opt_relation": {
        "alpha_F_over_2": float(alpha_F/2),
        "k_opt_paper": k_opt,
        "relative_error_percent": float(abs(alpha_F/2 - k_opt)/k_opt * 100)
    }
}

with open('new_derivation_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Saved: new_derivation_results.json")
print("\nKey results:")
print(f"  H_inf = {H_inf_fit:.2f} km/s/Mpc")
print(f"  beta = {beta_fit:.0f}")
print(f"  H0_predicted = {H_inf_fit + beta_fit * xi(t_now):.2f} km/s/Mpc")

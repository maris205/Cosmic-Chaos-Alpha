# Discrete Symplectic Cosmology (DSC)

**论文标题**: Discrete Symplectic Cosmology: Non-autonomous Evolution on a Planck Lattice and an Effective Einstein Equation with Time-dependent Cosmological Term

**作者**: Liang Wang, 华中科技大学 人工智能与自动化学院

**投稿目标**: Physical Review D / Classical and Quantum Gravity

---

## 项目概述

从两个物理假设出发——(1) 时空在 Planck 尺度是离散格点 Z³×N，(2) 演化映射保辛——推导出一系列宇宙学结论，核心成果包括：

- **含时宇宙学项的有效 Einstein 方程**：Λ(t) = Λ∞ + (4d_H²/3c²)/(t²ln²(t/t_P))，系数仅含 Feigenbaum 吸引子维数，无可调参数
- **Hubble 演化律**：H(t) = H∞ + β/ln²(t/t_P)，β < 0 由吸引子收缩推导（非拟合），自动给出 Hubble 张力的正确方向
- **冷却律**：μ(n) = μ∞ + (α_F/2)/ln²(n)，p=2 为唯一边际指数，k_opt ≈ α_F/2（Feigenbaum 常数）
- 数值验证：格点 Regge 曲率与 Friedmann 预言匹配到 6 位有效数字

---

## 目录结构

### 论文（投稿版）

| 文件 | 说明 |
|------|------|
| `dsc_paper.tex` | 英文正文（RevTeX4-2，13页，PRD 格式） |
| `dsc_paper.pdf` | 编译好的英文 PDF |
| `dsc_refs.bib` | BibTeX 参考文献（~45 条） |
| `dsc_paper_cn.tex` | 中文翻译版（XeLaTeX） |
| `dsc_paper_cn.pdf` | 编译好的中文 PDF（9页） |

### 可复现实验 (`experiments/`)

6 个 Jupyter Notebook，对应论文每条核心推导链：

| Notebook | 论文章节 | 内容 |
|----------|---------|------|
| `01_cooling_law_p2_marginality.ipynb` | §II.D | 为什么冷却律必须是 1/ln²(n)（p=2 边际性） |
| `02_k_opt_feigenbaum_conjecture.ipynb` | §II.E | k_opt = α_F/2 猜想的数值验证（精度 0.28%） |
| `03_symplectic_to_hubble.ipynb` | §II.H | 辛体积守恒 → Hubble 演化律的关键公式验证 |
| `04_regge_einstein_equation.ipynb` | §II.L | Regge 曲率 vs Friedmann 的 6 位有效数字验证 |
| `05_henon_simulation_60decades.ipynb` | §V | Hénon 映射 60 个数量级的辛模拟 |
| `06_entropy_correlation_decoherence.ipynb` | §II.I-K | 熵产生率、关联长度、退相干时间 |

运行环境：Python ≥ 3.10 + numpy + scipy + matplotlib，无需 GPU。

### 推导脚本（研究过程）

| 文件 | 说明 |
|------|------|
| `derive_H0_ab_initio.py` | 探索能否从 Feigenbaum + Planck 常数推出 H₀（结论：不能推绝对值，能推函数形式） |
| `derive_einstein.py` | 从辛格点 → Regge 作用量 → 有效 Einstein 方程的完整推导与数值验证 |
| `derive_from_symplectic.py` | 辛几何 + 冷却律能推导的所有物理量的系统探索 |
| `derive_entropy_correlation.py` | 熵、关联长度与视界问题的数值计算 |
| `verify_k_opt.py` | k_opt = α_F/2 的高精度数值验证 |
| `verify_symplectic_hubble.py` | 辛体积 → Hubble 的 Lyapunov 指数验证 |
| `verify_symplectic_hubble_v2.py` | 修正版：用 (1/ε)(dε/dn) = -2/(n·ln n) 做核心验证 |
| `generate_all_figures.py` | 论文主图生成脚本 |
| `simulate_attractor_dimension.py` | 吸引子维数演化模拟 |

### 图表 (`figures/`)

论文用图（PDF + PNG 双格式），包括冷却律、α 漂移三模型比较、Hubble 一致性检查、辛模拟、Einstein 推导链等。

### 数值结果

| 文件 | 说明 |
|------|------|
| `numerical_results.json` | 主要数值结果（AIC/BIC、H₀ 预测等） |
| `einstein_derivation_results.json` | Einstein 方程推导的数值验证结果 |
| `k_opt_verification.json` | k_opt = α_F/2 验证数据 |
| `symplectic_hubble_results.json` | 辛→Hubble 推导验证 |
| `symplectic_derivations.json` | 辛几何可推导量汇总 |

### 项目管理

| 文件 | 说明 |
|------|------|
| `CLAUDE.md` | 项目指令文件（AI 助手上下文） |
| `IDEA_REPORT.md` | 研究思路报告：假设、新发现、文献定位 |
| `EXPERIMENT_PLAN.md` | 实验计划：5 项数值实验 + LaTeX 结构 |
| `AUTO_REVIEW.md` | 4 轮自动审稿记录（GPT-5.4 审稿，分数 2→4→5→6/10） |
| `REVIEW_STATE.json` | 审稿循环状态 |

### 原始论文（输入）

| 文件 | 说明 |
|------|------|
| `The Riemann Standard Model.pdf` | 原始 RSM 论文（本项目基于此改写） |
| `lambda-cosmos_v1_latex.pdf` | Paper 5：宇宙学常数漂移（已投 Foundations of Physics） |

---

## 核心公式速查

**冷却律**（推导，非拟合）：
```
μ(n) = μ_dyna + (α_F / 2) / ln²(n + c₀)
```

**有效 Einstein 方程**（从 Regge 作用量推导）：
```
G_μν + Λ(t) g_μν = (8πG/c⁴) T_μν

Λ(t) = Λ∞ + (4d_H² / 3c²) · 1/(t² ln²(t/t_P))

d_H = ln2 / ln(α_F) ≈ 0.756
```

**Hubble 弛豫律**（从辛体积推导，β < 0）：
```
H(t) = H∞ + β / ln²(t/t_P)
```

---

## 审稿历程

经 4 轮 GPT-5.4 xhigh 自动审稿，分数从 2/10 提升至 6/10（"narrowly submittable"）。主要改进：

1. 解决辛体积守恒 vs 吸引子收缩的表面矛盾（用拉回吸引子理论）
2. 合成数据诚实标注为 mock-data
3. 补充 Bianchi 恒等式守恒方程
4. k_opt = α_F/2 降级为猜想
5. Einstein 方程标注为"唯象映射"

---

## 前置论文

1. Wang, L. (2026). Logistic → 素数分布. Zenodo. doi:10.5281/zenodo.18439638
2. Wang, L. (2026). Logistic → 黎曼零点谱同构. Zenodo. doi:10.5281/zenodo.19045440
3. Wang, L. (2026). Hénon 2D → 黎曼零点拓扑. Zenodo. doi:10.5281/zenodo.19084735
4. Wang, L. (2026). 量子计算机验证. Zenodo. doi:10.5281/zenodo.19135531
5. Wang, L. (2026). 宇宙学常数漂移. Zenodo. doi:10.5281/zenodo.19218674
6. Wang, L. (2026). 3x+1 问题. Zenodo. doi:10.5281/zenodo.18957726
7. Wang, L. (2026). 混沌电路实现. Zenodo. doi:10.5281/zenodo.19380314

---

## 运行

```bash
# 编译英文论文
pdflatex dsc_paper.tex && bibtex dsc_paper && pdflatex dsc_paper.tex && pdflatex dsc_paper.tex

# 编译中文版
xelatex dsc_paper_cn.tex

# 运行实验 notebook
cd experiments/
jupyter notebook
```

---

*Generated: 2026-04-03*

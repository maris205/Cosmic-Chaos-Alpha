# CLAUDE.md — RSM Version A: Discrete Symplectic Cosmology

## Project Goal
基于论文内容：The Riemann Standard Model.pdf,当前目录下
写 RSM (Riemann Standard Model) 的期刊投稿版 (构建新版本 A)，聚焦物理，删掉计算机类比。


## 核心公式
冷却律: μ(n) = μ_dyna + k_opt / ln(n + c_offset)²
常数漂移: Δα/α ~ 1/ln²(t), H(t) = H∞ + β/ln²(t)

## 前置论文 (同一作者 Wang L., 2026)
1. Paper 1: Logistic → 素数分布 (Zenodo)
2. Paper 2: Logistic → 黎曼零点谱同构 (Zenodo)
3. Paper 3: Hénon 2D → 黎曼零点拓扑 (Zenodo)
4. Paper 4: 量子计算机验证 (Zenodo)
5. Paper 5: 宇宙学常数漂移 (Foundations of Physics 在审)
6. Paper 6: 3x+1 问题 (Zenodo)
7. Paper 7: 混沌电路实现 (准备投 Nature Comm)

具体的，可按需下载：
1 wang, . liang . (2026). The Emergence of Prime Distribution from Low-Dimensional Deterministic Chaos (v3.0). Zenodo. https://doi.org/10.5281/zenodo.18439638
logistic映射和素数分布同构。读博士的时候一个论文，拿来搞ai for science的，起点
2 wang, . liang . (2026). Spectral Isomorphism between Renormalization Flow in Non-Autonomous Quadratic Maps and Riemann Zeros (v4.0). Zenodo. https://doi.org/10.5281/zenodo.19045440
logistic的谱分析，拟合黎曼零点，希尔伯特-波利亚猜想的推论。
3 wang, . liang . (2026). The Physical Topology of Riemann Zeros: Dual Evidence from Quantum Coherence and Macroscopic Dissipation (v1.0). Zenodo. https://doi.org/10.5281/zenodo.19084735
把logistic映射升级为二维henon映射，满足可逆性、熵不变等希尔伯特-波利亚猜想条件。
4 wang, . liang . (2026). Ab Initio Quantum Emulation of the Riemann Zeros: Semiclassical Aliasing and Subspace Embedding (v1.0). Zenodo. https://doi.org/10.5281/zenodo.19135531
henon映射中有个量子算法求解谱分析，用aws真量子计算机实现。
5 wang, . liang . (2026). Cosmological Evolution as a Non-autonomous Dynamical System: Empirical Evidence from the Fine-Structure Constant, Hubble Tension, and Riemann Zeros (v1.0). Zenodo. https://doi.org/10.5281/zenodo.19218674
根据黎曼零点到量子能级的关联，研究宇宙常数问题
6 Wang, L. (2026). Spectral Analysis of the Transfer Operator in the Period-3 Logistic Sandbox: A Dynamical Heuristic for the $3x+1$ Problem (v1.0). Zenodo. https://doi.org/10.5281/zenodo.18957726
把符符号动力学连接动力学系统和算术系统，然后进行谱分析、统计分析的思路，应用到新问题
7 Wang, L. (2026). Physical Emergence of Riemann Zeros in Dissipative Chaotic Circuits (v1.0). Zenodo. https://doi.org/10.5281/zenodo.19380314
用电路来输出黎曼零点


## Paper 5 关键数据 (版本 A 需要引用)
- 127 个类星体 α 漂移: 5.6σ, χ²=1.32
- 4 个 JWST H₀ 锚点: R²=0.907
- USTC 量子截断: T_cut ≈ 73.3 吻合
- 零自由参数
论文5内容：lambda-cosmos_v1_latex.pdf，当前目录下

## 新版本 A，就是基于The Riemann Standard Model.pdf修改， 保留
- 离散 Planck lattice + 辛几何
- 非自治冷却 1/ln²(t)
- 三组独立数据验证
- 数值仿真 (从 Planck epoch 演化)
- 可证伪预测 (计算冻结)

## 版本 A 删掉
- ECS 架构类比
- LOD 渲染类比
- 内存映射类比
- "Riemann Standard Model" 名字
- 游戏/计算机工程术语

## 关键修订（基于 GPT-5.4 评审）：
  1. 理论推导改用 Proposition 格式，加显式假设
  2. "零自由参数" → "无数据集特定拟合参数"，加参数审计表
  3. Hubble tension 从 "resolution" 降级为 "consistency check"
  4. α漂移加三基线对比 (constant/linear/1/ln²t) + AIC/BIC
  5. 实验室零结果作为定量预测先给出，再对比
  6. 离子阱截断加不确定度区间
  7. 新增 §II.E 讨论 Z³ 格点 Lorentz 不变性恢复
  8. 加强前人工作定位（变常数模型 + 离散时空文献）
  9. 主文压缩到 4 图，其余移入附录
  10. H∞ 预测框定为 "可证伪预测"

## 希望新增内容：
- 进一步强化物理严谨性，同时融入 RSM 中的离散辛几何框架，彻底剥离所有计算机类比。
- 是否能从新的框架，理论推导、或者数值模拟，得到哈勃常数，或者精细化常数，或者一些物理学相关的基本理论公式。

## 投稿目标
Physical Review D 或 Classical and Quantum Gravity 等长论文

## 作者信息
Liang Wang*
School of Artificial Intelligence and Automation,
Huazhong University of Science and Technology, 430070, P.R. China
*Corresponding author: wangliang.f@gmail.com

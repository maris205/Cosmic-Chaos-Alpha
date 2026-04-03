# experiments/ — 可复现实验 Jupyter Notebooks

## 论文：离散辛宇宙学（DSC）

对应论文每条核心推导链，共 6 个 notebook，可独立运行。

| # | 文件 | 对应论文章节 | 内容 |
|---|------|-------------|------|
| 1 | `01_cooling_law_p2_marginality.ipynb` | §II.D | 冷却律 $p=2$ 边际性验证 |
| 2 | `02_k_opt_feigenbaum_conjecture.ipynb` | §II.E | $k_{\rm opt} = \alpha_F/2$ 猜想验证 |
| 3 | `03_symplectic_to_hubble.ipynb` | §II.H | 辛体积 → Hubble 演化推导验证 |
| 4 | `04_regge_einstein_equation.ipynb` | §II.L | Regge 作用量 → 有效 Einstein 方程 |
| 5 | `05_henon_simulation_60decades.ipynb` | §V | Hénon 映射 60 decade 模拟 |
| 6 | `06_entropy_correlation_decoherence.ipynb` | §II.I-K | 熵、关联长度、退相干时间 |

## 运行环境

```
Python >= 3.10
numpy, scipy, matplotlib
```

所有 notebook 无需 GPU，普通笔记本即可运行。

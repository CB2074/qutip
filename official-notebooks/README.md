# QuTiP 官方 `.ipynb` 学习资料

本目录是本仓库的核心学习资料，不是外部参考链接。Notebook 均从 QuTiP 官方发布位置直接下载，保留官方运行输出。

## 来源

1. **100 个 QuTiP 5 Notebook**：直接下载自 `https://qutip.org/qutip-tutorials/tutorials-v5/`。这些文件对应 QuTiP 官方教程站和 `qutip/qutip-tutorials` 的 v5 内容；其中包括官方原生的 cuQuantum Notebook。
2. **9 个官网仍列出的专题 Notebook**：断层成像 1 个、PIQS 8 个，直接下载自官方 `qutip/qutip-notebooks` 仓库提交 `1286d50d476b20f41f7edeff4af1a1508f93f10d`。

总计 **109 个官方 `.ipynb`**。`DOWNLOAD_MANIFEST.json` 记录每个文件的原始下载 URL、字节数、SHA-256 和单元格数量；两份 `LICENSE-*.txt` 保存对应上游许可证。

## 运行

从仓库根目录启动：

```powershell
pip install -r requirements.txt
jupyter lab
```

然后进入 `official-notebooks`，按照根目录 [`STUDY_PLAN.md`](../STUDY_PLAN.md) 的日期打开当天 Notebook。

部分高级 Notebook 需要额外包，例如 `qutip-qip`、`qutip-qoc`、`qutip-jax`、PIQS 或 cuQuantum。学习到相应专题时再根据 Notebook 配置；不建议第一天全部安装。

## 目录

- `python-introduction`：Python、NumPy、Matplotlib 基础
- `time-evolution`：QuTiP 动力学求解器
- `visualization`：Bloch 球、Wigner 函数等可视化
- `lectures`：量子力学与量子光学专题
- `quantum-circuits`：量子线路
- `pulse-level-circuit-simulation`：脉冲级仿真
- `optimal-control`：GRAPE、CRAB 等最优控制
- `heom`：层级运动方程
- `miscellaneous`：JAX、cuQuantum、JC 晶格等
- `tomography`：量子态断层成像
- `piqs`：置换对称开放量子系统

学习顺序已按依赖关系重新安排，但 Notebook 内容保持官方原样。

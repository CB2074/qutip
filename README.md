# QuTiP 5 官方教程中文学习计划

本仓库直接保存 QuTiP 官方 v5 教程的 `.ipynb` 学习资料，并将它们整理成一条可以每天执行的中文学习路线。学习时无需跳转到外部教程仓库。

## 从这里开始

- [16 周逐日学习日历](STUDY_PLAN.md)：从 **2026-08-12** 到 **2026-12-01**，每天都有官方教程、任务和产出。
- [官方 Notebook 学习资料](official-notebooks)：直接包含 **109 个官方 `.ipynb`**、原始运行输出及所需图片/QASM 资源。
- [官方教程完整索引](OFFICIAL_TUTORIAL_INDEX.md)：按主题列出本地 Notebook，并标出计划日期。
- [学习记录模板](notes/TEMPLATE.md)：每天复制一份，用于记录模型、API、结果和疑问。
- [第一个可运行示例](examples/01_two_level_rabi.py)：二能级系统的 Rabi 振荡。

其中 100 个 QuTiP 5 Notebook 从 `qutip.org` 官方教程站直接下载；另外收录官网仍列出的 1 个断层成像和 8 个 PIQS Notebook，它们直接来自官方 `qutip/qutip-notebooks` 仓库。每个文件的来源和 SHA-256 都记录在 [`DOWNLOAD_MANIFEST.json`](official-notebooks/DOWNLOAD_MANIFEST.json)。

## 今天的任务

如果你从计划制定日开始，先完成 [2026-08-12：环境与 Python 热身](STUDY_PLAN.md#2026-08-12周三环境与-python-热身)。如果开始日期已经过去，仍建议从第一天顺序学习，不要直接跳到日历当天。

每天建议投入 60–90 分钟：

1. 运行官方教程的全部单元格。
2. 不看原文重写最关键的 10–20 行代码。
3. 改动一个参数并解释结果。
4. 用模板留下当天的学习记录。

## 安装

推荐使用 Python 3.11 或 3.12，并创建独立环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

测试环境：

```powershell
python -c "import qutip; print(qutip.__version__)"
python examples/01_two_level_rabi.py
```

启动 Jupyter 后，直接打开本仓库内的官方 Notebook：

```powershell
jupyter lab
```

然后从 `official-notebooks` 进入当天资料。量子线路、最优控制、JAX 和 cuQuantum 教程需要额外扩展包；安装要求写在对应学习日或 Notebook 内。

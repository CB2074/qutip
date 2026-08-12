# QuTiP 5 官方教程中文学习计划

本仓库把 [QuTiP 官方 v5 教程](https://github.com/qutip/qutip-tutorials/tree/main/tutorials-v5)重新整理成一条可以每天执行的中文学习路线。

## 从这里开始

- [16 周逐日学习日历](STUDY_PLAN.md)：从 **2026-08-12** 到 **2026-12-01**，每天都有官方教程、任务和产出。
- [官方教程完整索引](OFFICIAL_TUTORIAL_INDEX.md)：收录官方 v5 的 **99 个分类条目 + 1 个贡献模板**，按主题分类并标出计划日期。
- [学习记录模板](notes/TEMPLATE.md)：每天复制一份，用于记录模型、API、结果和疑问。
- [第一个可运行示例](examples/01_two_level_rabi.py)：二能级系统的 Rabi 振荡。

计划基于官方教程仓库提交 [`97d7d09`](https://github.com/qutip/qutip-tutorials/commit/97d7d09baaa926c6604bb75e4f139c7bea74ee5e)（2026-07-21）整理。教程后续可能更新，因此索引同时提供固定版本链接和官方 `main` 目录入口；`official-tutorials` 子模块保存了这份固定快照。

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

官方教程以 Jupytext Markdown 保存。若想在本地运行完整官方教程，可以另行克隆：

```powershell
git clone https://github.com/qutip/qutip-tutorials.git
cd qutip-tutorials
jupytext --to notebook tutorials-v5/time-evolution/002_larmor-precession.md
jupyter lab
```

> 注意：量子线路、最优控制和 JAX 教程需要额外扩展包；安装要求已经写在对应学习日中。旧的 `qutip-lectures` 仓库不再作为主线，本计划以官方 `qutip/qutip-tutorials` 的 v5 内容为准。

# QuTiP 5 中文学习路线

这是一条面向初学者的 QuTiP 5 学习路线。默认你会基本的 Python，并学过线性代数和量子力学中的态矢、算符与张量积。

QuTiP 主要用于模拟封闭和开放量子系统的动力学。建议先学“如何表达量子系统”，再学求解器，最后进入量子光学、耗散系统或量子计算等专题。

## 1. 安装与运行

推荐使用 Python 3.11 或 3.12，并为项目创建独立环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

运行本仓库的第一个示例：

```powershell
python examples/01_two_level_rabi.py
```

运行后会生成 `two_level_rabi.png`，展示二能级系统的 Rabi 振荡。

## 2. 推荐资料

以官方、QuTiP 5 兼容的资料为主：

- [QuTiP 官方教程仓库](https://github.com/qutip/qutip-tutorials)：首选教程，按 QuTiP 版本分类。
- [QuTiP 5 教程目录](https://github.com/qutip/qutip-tutorials/tree/main/tutorials-v5)：包含 Python 入门、时间演化、可视化、量子线路、HEOM 和最优控制等专题。
- [QuTiP 官方文档](https://qutip.readthedocs.io/en/stable/)：用于查 API、求解器参数和函数示例。
- [QuTiP 主仓库](https://github.com/qutip/qutip)：查看版本、安装方式、问题讨论和源代码。
- [QuTiP Lectures](https://github.com/jrjohansson/qutip-lectures)：经典量子光学 Notebook；内容直观，但比较旧，遇到接口差异时以 QuTiP 5 文档为准。

## 3. 四周学习计划

### 第 1 周：量子对象与复合系统

目标：能够用 `Qobj` 表示态、算符和密度矩阵。

学习内容：

1. `basis`、`ket2dm`、`qeye`、`destroy`、`create` 和 Pauli 算符。
2. `dag()`、`tr()`、`unit()`、`expect()` 等常用操作。
3. 使用 `tensor()` 构造复合系统。
4. 区分 ket、bra、operator 和 superoperator，并检查 `dims` 与 `shape`。

练习：

- 构造单量子比特的 `|0>`、`|1>`、`|+>` 状态。
- 计算 `|+>` 态下三个 Pauli 算符的期望值。
- 构造 Bell 态，并对其中一个子系统做偏迹 `ptrace()`。
- 构造截断到 20 个 Fock 态的相干态，计算平均光子数。

### 第 2 周：封闭系统的时间演化

目标：能够写出 Hamiltonian，并使用 `sesolve` 研究动力学。

学习内容：

1. 从物理模型写出 Hamiltonian。
2. `sesolve(H, psi0, tlist, e_ops=...)` 的输入与输出。
3. 期望值、布居数与 Bloch 球轨迹。
4. 常数 Hamiltonian 与含时 Hamiltonian。

练习：

- 运行 `examples/01_two_level_rabi.py`，改变驱动频率和初态。
- 加入失谐项 `delta * sigmaz() / 2`，比较共振与非共振结果。
- 模拟两个耦合量子比特之间的激发交换。

### 第 3 周：开放量子系统

目标：理解 Lindblad 主方程，并使用 `mesolve` 加入耗散和退相干。

学习内容：

1. 密度矩阵、纯态与混态。
2. 塌缩算符 `c_ops` 的物理含义。
3. `mesolve`、弛豫、纯退相干和热环境。
4. `mcsolve` 的量子轨迹方法，以及它与主方程方法的关系。

练习：

- 给 Rabi 模型加入能量弛豫 `sqrt(gamma) * sigmam()`。
- 加入纯退相干，并比较 Bloch 向量的衰减。
- 对同一个模型分别运行 `mesolve` 和 `mcsolve`，比较平均结果。

### 第 4 周：选择一个专题项目

根据研究方向选择一个分支：

- 量子光学：Jaynes-Cummings 模型、关联函数、功率谱、Wigner 函数。
- 超导量子比特：耦合量子比特、cQED 色散区、脉冲驱动和读出。
- 开放系统：非零温环境、稳态、量子轨迹、HEOM。
- 量子计算：`qutip-qip`、量子门、噪声和脉冲级线路模拟。
- 量子控制：`qutip-qoc` 或相关最优控制教程。

推荐结课项目：模拟一个有损 Jaynes-Cummings 系统，输出腔内光子数、原子激发概率和 Wigner 函数，并解释耦合强度与耗散率对结果的影响。

## 4. 建议掌握的核心接口

| 类别 | 常用接口 |
| --- | --- |
| 状态与算符 | `Qobj`, `basis`, `ket2dm`, `qeye`, `tensor` |
| 常用模型 | `sigmax`, `sigmaz`, `sigmam`, `destroy`, `num` |
| 状态构造 | `coherent`, `thermal_dm`, `fock_dm` |
| 计算 | `expect`, `ptrace`, `fidelity`, `entropy_vn` |
| 动力学 | `sesolve`, `mesolve`, `mcsolve` |
| 稳态与谱 | `steadystate`, `correlation_2op_1t`, `spectrum` |
| 可视化 | `Bloch`, `plot_wigner`, `matrix_histogram` |

不建议一开始背全部 API。每学一个物理模型，都按以下模板组织代码：

1. 定义 Hilbert 空间及截断维数。
2. 构造初态。
3. 构造 Hamiltonian。
4. 构造塌缩算符。
5. 选择时间点和观测量。
6. 调用求解器并检查结果。
7. 改变参数，验证极限情况和物理量纲。

## 5. 常见问题

- 维数错误：先打印每个对象的 `dims` 和 `shape`，复合系统的算符通常需要用 `tensor()` 补齐单位算符。
- Fock 空间截断过小：逐步增大截断维数，确认结果已经收敛。
- 把耗散率直接当作塌缩算符：通常应写成 `sqrt(rate) * operator`。
- 单位不统一：若令 `hbar = 1`，频率、耦合强度和耗散率必须采用一致单位。
- 旧教程不能运行：先确认教程对应 QuTiP 4 还是 QuTiP 5，并以当前稳定版文档为准。
- 只看曲线不验证：检查迹、概率范围、无耦合或无耗散极限，以及不同数值精度下的稳定性。

## 6. 学习完成标准

完成这条路线后，你应该能够：

- 将一个量子力学模型转换为 QuTiP 对象。
- 判断该使用 `sesolve`、`mesolve` 还是 `mcsolve`。
- 正确构造含耗散的主方程。
- 检查 Hilbert 空间维数、截断误差和数值收敛性。
- 独立绘制布居数、期望值、Bloch 球或 Wigner 函数。
- 阅读并修改官方 Notebook，把参数替换为自己的实验或论文参数。

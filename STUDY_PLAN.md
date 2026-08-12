# QuTiP 5 官方教程：16 周逐日学习日历

开始日期：**2026-08-12**　结束日期：**2026-12-01**　节奏：**每天 60–90 分钟，每 7 天复盘一次**。

官方教程不是按初学者的学习依赖排列的。本计划按“Python 与量子对象 → 动力学求解器 → 可视化 → 量子光学模型 → 量子线路 → 脉冲仿真 → 最优控制 → HEOM/JAX”的顺序重排。每次学习都应执行代码，而不只是阅读网页。

## 每日固定动作

1. 阅读当天链接的说明，运行全部代码。
2. 从空白文件重写当天最关键的模型。
3. 修改至少一个参数，先预测再观察结果。
4. 复制 [`notes/TEMPLATE.md`](notes/TEMPLATE.md) 写学习记录。
5. 提交记录：`git commit -m "Study YYYY-MM-DD: 主题"`。

标记方法：`[ ]` 未完成，`[x]` 已完成。日期已经过去但未学习时，不要直接跳过；按表格顺序补课即可。

## 第 1 周：环境、Python 与第一个量子模型（08-12—08-18）

### 2026-08-12（周三）：环境与 Python 热身

- [ ] 官方教程：[Introduction to Python](official-notebooks/python-introduction/001_Beginning_Python.ipynb)
- 目标：完成环境安装，复习变量、函数、循环与列表。
- 产出：运行 `python -c "import qutip; print(qutip.__version__)"`，在学习记录中写下 Python、QuTiP 版本。

### 2026-08-13（周四）：NumPy 数组

- [ ] 官方教程：[Introduction to NumPy Arrays](official-notebooks/python-introduction/002_NumPy_Array_Basics.ipynb)
- 目标：掌握数组、切片、矩阵乘法、特征值和复数数组。
- 产出：用 NumPy 构造 Pauli-X、Y、Z，验证各自平方等于单位矩阵。

### 2026-08-14（周五）：Matplotlib

- [ ] 官方教程：[Plotting in Python Using Matplotlib](official-notebooks/python-introduction/003_Matplotlib_Plotting.ipynb)
- 目标：会画单图、多子图、图例和坐标轴标签。
- 产出：画出 `sin(t)` 与 `cos(t)`，保存为 PNG。

### 2026-08-15（周六）：QuTiP 对象入门

- [ ] 官方入口：[Link to Lecture 0](official-notebooks/python-introduction/004_link_to_lecture_0.ipynb)
- [ ] 官方教程：[Lecture 0 — Introduction to QuTiP](official-notebooks/lectures/Lecture-0-Introduction-to-QuTiP.ipynb)
- 目标：理解 `Qobj`、ket、bra、operator、`dims`、`shape` 和 `tensor`。
- 产出：构造 `|0>`、`|1>`、`|+>` 与 Bell 态，打印对象类型和维数。

### 2026-08-16（周日）：相互作用量子比特

- [ ] 官方教程：[Interacting Qubits](official-notebooks/euroscipy2026/01_Qubits.ipynb)
- 目标：把 Hilbert 空间、Hamiltonian、初态、观测量和求解器连成完整流程。
- 产出：改变耦合强度，解释交换振荡周期如何变化。

### 2026-08-17（周一）：量子隐形传态

- [ ] 官方教程：[Teleportation Protocol](official-notebooks/euroscipy2026/02_Teleportation.ipynb)
- 目标：理解复合系统、测量与条件操作。
- 产出：验证输入态与输出态的保真度，并解释经典比特的作用。

### 2026-08-18（周二）：复盘 1

- [ ] 不看教程重写一个二能级模型；完成 `examples/01_two_level_rabi.py`。
- 检查点：能解释 `basis`、`tensor`、`dag`、`expect` 和 `sesolve`；整理本周疑问。

## 第 2 周：核心动力学求解器（08-19—08-25）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-08-19 周三 | [QobjEvo：含时量子对象](official-notebooks/time-evolution/001_qobjevo.ipynb) | 写出常数项加含时驱动项，比较函数系数与字符串/数组系数；记录 `QobjEvo` 的用途。 |
| 2026-08-20 周四 | [Larmor precession](official-notebooks/time-evolution/002_larmor-precession.ipynb) | 掌握 `sesolve`；画三个 Pauli 期望值并核对 Bloch 向量长度。 |
| 2026-08-21 周五 | [Single-Qubit Dynamics](official-notebooks/time-evolution/003_qubit-dynamics.ipynb) | 掌握 `mesolve` 与塌缩算符；分别关闭弛豫和退相干并比较。 |
| 2026-08-22 周六 | [Vacuum Rabi oscillations](official-notebooks/time-evolution/004_rabi-oscillations.ipynb) | 建立 Jaynes–Cummings 模型；检查激发数守恒及 Fock 截断收敛。 |
| 2026-08-23 周日 | [Dynamics of a Spin Chain](official-notebooks/time-evolution/005_spin-chain.ipynb) | 熟悉多体张量积；画出激发在链上的传播。 |
| 2026-08-24 周一 | [Photon Birth and Death](official-notebooks/time-evolution/006_photon_birth_death.ipynb) | 掌握 `mcsolve`；改变轨迹数，观察平均结果的统计收敛。 |
| 2026-08-25 周二 | **复盘 2** | 做一张 `sesolve` / `mesolve` / `mcsolve` 选择表；从零写一个有耗散二能级系统。 |

## 第 3 周：Bloch–Redfield 与 Floquet（08-26—09-01）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-08-26 周三 | [Bloch-Redfield: TLS](official-notebooks/time-evolution/007_brmesolve_tls.ipynb) | 理解频谱密度与 `brmesolve`；同 Lindblad 结果比较。 |
| 2026-08-27 周四 | [Bloch-Redfield: time dependence](official-notebooks/time-evolution/008_brmesolve_time_dependence.ipynb) | 加入含时算符；记录求解器的输入结构。 |
| 2026-08-28 周五 | [Dissipative Atom-Cavity](official-notebooks/time-evolution/009_brmesolve-cavity-QED.ipynb) | 比较腔损耗与原子耗散对动力学的影响。 |
| 2026-08-29 周六 | [Phonon-assisted initialization](official-notebooks/time-evolution/010_brmesolve_phonon_interaction.ipynb) | 理解声子谱密度；画出不同温度的初始化曲线。 |
| 2026-08-30 周日 | [Floquet Solvers](official-notebooks/time-evolution/011_floquet_solver.ipynb) | 求周期驱动系统的 Floquet 态与准能量。 |
| 2026-08-31 周一 | [Floquet Formalism](official-notebooks/time-evolution/012_floquet_formalism.ipynb) | 用自己的话写出 Floquet 方法适用条件，并复现一个图。 |
| 2026-09-01 周二 | **复盘 3** | 画决策树：Lindblad、Bloch–Redfield、Floquet 分别何时使用；列出各自假设。 |

## 第 4 周：非马尔可夫、随机求解器与稳态（09-02—09-08）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-09-02 周三 | [Non-Markovian Monte Carlo](official-notebooks/time-evolution/013_nonmarkovian_monte_carlo.ipynb) | 识别负速率与非马尔可夫效应；复现一个物理例子。 |
| 2026-09-03 周四 | [Heterodyne Detection](official-notebooks/time-evolution/015_smesolve-heterodyne.ipynb) | 入门 `smesolve`；保存一条测量记录和条件态轨迹。 |
| 2026-09-04 周五 | [Inefficient Detection](official-notebooks/time-evolution/016_smesolve-inefficient-detection.ipynb) | 改变探测效率，解释条件态纯度变化。 |
| 2026-09-05 周六 | [JC Photocurrent](official-notebooks/time-evolution/017_smesolve-jc-photocurrent.ipynb) | 模拟光电流；把测量记录与系统动力学对应起来。 |
| 2026-09-06 周日 | [Cats: stochastic vs Monte Carlo](official-notebooks/time-evolution/018_measures-trajectories-cats-kerr.ipynb) | 比较随机主方程与量子跳跃轨迹。 |
| 2026-09-07 周一 | [Optomechanical steady state](official-notebooks/time-evolution/019_optomechanical-steadystate.ipynb) | 使用 `steadystate`；检查密度矩阵迹、正定性与截断收敛。 |
| 2026-09-08 周二 | **复盘 4** | 总结无条件态、条件态、轨迹与稳态的区别；重做最困难的一张图。 |

## 第 5 周：稳态、传播子与 QuTiP 5 新求解器（09-09—09-15）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-09-09 周三 | [Homodyned JC emission](official-notebooks/time-evolution/020_homodyned-Jaynes-Cummings-emission.ipynb) | 计算稳态输出；识别 homodyne 信号中的量子特征。 |
| 2026-09-10 周四 | [Quasi-steady periodic system](official-notebooks/time-evolution/021_quasi-steadystate-driven-system.ipynb) | 理解周期驱动下的准稳态并验证周期性。 |
| 2026-09-11 周五 | [QuTiP 5 stochastic solver](official-notebooks/time-evolution/022_v5_paper-smesolve.ipynb) | 复现 homodyne 示例；记录 QuTiP 5 求解器接口。 |
| 2026-09-12 周六 | [Dysolve propagator](official-notebooks/time-evolution/023_dysolve_propagator.ipynb) | 计算传播子并与直接时间演化对照。 |
| 2026-09-13 周日 | [QuTiP 5 sesolve/mesolve classes](official-notebooks/time-evolution/024_v5_paper-mesolve.ipynb) | 比较函数式与求解器类接口；记录可复用求解器的优势。 |
| 2026-09-14 周一 | [Floquet speed test](official-notebooks/time-evolution/025_v5_paper-floquet-speed-test.ipynb)；[Non-Markovian MC solver](official-notebooks/time-evolution/026_v5_paper-nm_mcsolve.ipynb) | 这是加长日：分别记录速度测试条件和非马尔可夫轨迹核心接口。 |
| 2026-09-15 周二 | **复盘 5** | 制作“QuTiP 求解器速查表”，每个求解器写输入、输出、假设和一个应用。 |

## 第 6 周：可视化基础（09-16—09-22）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-09-16 周三 | [Animation demos](official-notebooks/visualization/animation-demo.ipynb) | 生成一个可重复播放的动力学动画。 |
| 2026-09-17 周四 | [Bloch Sphere animation](official-notebooks/visualization/bloch-sphere-animation.ipynb) | 把二能级演化映射到 Bloch 球轨迹。 |
| 2026-09-18 周五 | [Bloch Sphere with colorbar](official-notebooks/visualization/bloch_sphere_with_colorbar.ipynb) | 用颜色编码时间或另一个物理量。 |
| 2026-09-19 周六 | [Distributions](official-notebooks/visualization/distributions.ipynb) | 熟悉 `qutip.distributions`；解释所画分布的坐标。 |
| 2026-09-20 周日 | [Energy-level diagrams](official-notebooks/visualization/energy-levels.ipynb) | 画参数扫描的能谱，并标注避免交叉。 |
| 2026-09-21 周一 | [JC Wigner functions](official-notebooks/visualization/JC-model-wigner-function.ipynb) | 计算约化腔态的 Wigner 函数并解释负值。 |
| 2026-09-22 周二 | **复盘 6** | 为同一二能级模型输出时间曲线、Bloch 球和动画；统一图形风格。 |

## 第 7 周：高级可视化与量子光学起步（09-23—09-29）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-09-23 周三 | [Pseudo-probability functions](official-notebooks/visualization/pseudo-probability-functions.ipynb) | 比较 Wigner、Q 等准概率表示。 |
| 2026-09-24 周四 | [Quantum Process Tomography](official-notebooks/visualization/quantum-process-tomography.ipynb)；[Iterative MLE Tomography](official-notebooks/tomography/tomography-iMLE-photon-counting.ipynb) | 画过程矩阵并说明理想门的特征；再完成光子计数的迭代最大似然断层成像。 |
| 2026-09-25 周五 | [Qubism and Schmidt plots](official-notebooks/visualization/qubism-and-schmidt-plots.ipynb) | 可视化一个多体态，联系 Schmidt 分解与纠缠。 |
| 2026-09-26 周六 | [Visualization exposition](official-notebooks/visualization/visualization-exposition.ipynb) | 建立个人可视化速查页：函数、输入对象、适用场景。 |
| 2026-09-27 周日 | [Lecture 1: Jaynes–Cummings](official-notebooks/lectures/Lecture-1-Jaynes-Cumming-model.ipynb) | 系统推导 JC Hamiltonian；比较旋波近似前后结果。 |
| 2026-09-28 周一 | [Lecture 2A: Cavity-Qubit Gates](official-notebooks/lectures/Lecture-2A-Cavity-Qubit-Gates.ipynb) | 模拟谐振腔耦合的双量子比特门，计算末态保真度。 |
| 2026-09-29 周二 | **复盘 7** | 从 JC 模型出发，写清子系统顺序、截断、耦合项、耗散项和观测量。 |

## 第 8 周：关联函数、放大器与量子轨迹（09-30—10-06）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-09-30 周三 | [Lecture 2B: Single-Atom Lasing](official-notebooks/lectures/Lecture-2B-Single-Atom-Lasing.ipynb) | 计算稳态光子数和统计量，识别激光阈值行为。 |
| 2026-10-01 周四 | [Lecture 3A: Dicke model](official-notebooks/lectures/Lecture-3A-Dicke-model.ipynb) | 构造多原子模型，观察集体耦合。 |
| 2026-10-02 周五 | [Lecture 3B: Ultrastrong coupling](official-notebooks/lectures/Lecture-3B-Jaynes-Cumming-model-with-ultrastrong-coupling.ipynb) | 比较 RWA 与非 RWA 模型并说明失效条件。 |
| 2026-10-03 周六 | [Lecture 4: Correlation Functions](official-notebooks/lectures/Lecture-4-Correlation-Functions.ipynb) | 计算一阶/二阶关联及谱，解释 `g2(0)`。 |
| 2026-10-04 周日 | [Lecture 5: Parametric Amplifier](official-notebooks/lectures/Lecture-5-Parametric-Amplifier.ipynb) | 观察压缩与光子统计；改变泵浦强度。 |
| 2026-10-05 周一 | [Lecture 6: Quantum Monte Carlo](official-notebooks/lectures/Lecture-6-Quantum-Monte-Carlo-Trajectories.ipynb) | 比较单条轨迹、轨迹平均与主方程。 |
| 2026-10-06 周二 | **复盘 8** | 用关联函数判断一个场是反聚束、相干还是热统计；整理量子轨迹误差来源。 |

## 第 9 周：量子门、压缩态与 cQED（10-07—10-13）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-10-07 周三 | [Lecture 7: iSWAP and tomography](official-notebooks/lectures/Lecture-7-iSWAP-gate.ipynb) | 模拟 iSWAP，重建过程并评估门性能。 |
| 2026-10-08 周四 | [Lecture 8: Adiabatic sweep](official-notebooks/lectures/Lecture-8-Adiabatic-quantum-computing.ipynb) | 改变扫描时间，观察绝热条件何时成立。 |
| 2026-10-09 周五 | [Lecture 9: Squeezed states](official-notebooks/lectures/Lecture-9-Squeezed-states-of-harmonic-oscillator.ipynb) | 构造压缩态，画相空间分布和方差。 |
| 2026-10-10 周六 | [Lecture 10: cQED dispersive regime](official-notebooks/lectures/Lecture-10-cQED-dispersive-regime.ipynb) | 比较完整模型与色散近似，验证适用区间。 |
| 2026-10-11 周日 | [Lecture 11: Charge Qubits](official-notebooks/lectures/Lecture-11-Charge-Qubits.ipynb) | 计算能谱并识别 sweet spot。 |
| 2026-10-12 周一 | [Lecture 12: Squeezed vacuum decay](official-notebooks/lectures/Lecture-12-Decay-into-a-squeezed-vacuum-field.ipynb) | 比较普通真空与压缩真空中的衰减。 |
| 2026-10-13 周二 | **复盘 9** | 选一个本周模型写一页推导，并用数值结果验证至少一个近似。 |

## 第 10 周：非线性与光子模型（10-14—10-20）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-10-14 周三 | [Lecture 13: Resonance fluorescence](official-notebooks/lectures/Lecture-13-Resonance-flourescence.ipynb) | 计算荧光谱，识别 Mollow triplet。 |
| 2026-10-15 周四 | [Lecture 14: Kerr nonlinearities](official-notebooks/lectures/Lecture-14-Kerr-nonlinearities.ipynb) | 观察 Kerr 演化产生非经典态，画 Wigner 函数。 |
| 2026-10-16 周五 | [Lecture 15: Nonclassically driven atoms](official-notebooks/lectures/Lecture-15-Nonclassically-driven-atoms.ipynb) | 理解级联系统，标清输入输出通道。 |
| 2026-10-17 周六 | [Lecture 16: Wigner gallery](official-notebooks/lectures/Lecture-16-Gallery-of-Wigner-functions.ipynb) | 建立常见量子态的 Wigner 图鉴。 |
| 2026-10-18 周日 | [Excitation-restricted JC chain](official-notebooks/miscellaneous/excitation-number-restricted-states-jc-chain.ipynb) | 比较完整空间与受限空间的维数和运行时间。 |
| 2026-10-19 周一 | [Single-photon interference](official-notebooks/miscellaneous/single-photon-interference.ipynb) | 复现单光子干涉并解释可见度。 |
| 2026-10-20 周二 | **复盘 10** | 从本周选一个模型整理为独立脚本：参数集中、图形清晰、含物理说明。 |

## 第 11 周：量子线路（10-21—10-27）

本周安装：`pip install qutip-qip`。

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-10-21 周三 | [Quantum Gates](official-notebooks/quantum-circuits/quantum-gates.ipynb) | 构造常用门与线路，验证幺正性。 |
| 2026-10-22 周四 | [QASM import/export](official-notebooks/quantum-circuits/qasm.ipynb) | 导入并导出一条小线路，检查往返一致性。 |
| 2026-10-23 周五 | [Teleportation Circuit](official-notebooks/quantum-circuits/teleportation.ipynb) | 与第 1 周传态模型对照，验证输出保真度。 |
| 2026-10-24 周六 | [Toffoli decomposition](official-notebooks/quantum-circuits/qip-toffoli-cnot.ipynb) | 验证分解线路与 Toffoli 矩阵等价。 |
| 2026-10-25 周日 | [TextRenderer](official-notebooks/quantum-circuits/textrenderer-plot.ipynb)；[MatRenderer](official-notebooks/quantum-circuits/matrenderer-plot.ipynb) | 用两种渲染器显示同一线路，设置标签与颜色。 |
| 2026-10-26 周一 | [QuTiP 5 QIP example](official-notebooks/quantum-circuits/v5_paper-qip2.ipynb) | 完成 QuTiP 5 线路综合示例，记录核心类之间的关系。 |
| 2026-10-27 周二 | **复盘 11** | 从零构造 Bell 态制备线路，画线路并用态矢验证。 |

## 第 12 周：脉冲级线路仿真（10-28—11-03）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-10-28 周三 | [Gate scheduler](official-notebooks/pulse-level-circuit-simulation/qip-scheduler.ipynb) | 比较 ASAP/ALAP 调度，输出指令时间线。 |
| 2026-10-29 周四 | [Customize device](official-notebooks/pulse-level-circuit-simulation/qip-customize-device.ipynb) | 自定义处理器参数与本征门。 |
| 2026-10-30 周五 | [OptPulseProcessor](official-notebooks/pulse-level-circuit-simulation/qip-optpulseprocessor.ipynb) | 从目标操作生成控制脉冲并查看保真度。 |
| 2026-10-31 周六 | [Deutsch–Jozsa at pulse level](official-notebooks/pulse-level-circuit-simulation/qip-processor-DJ-algorithm.ipynb) | 比较理想线路与脉冲级结果。 |
| 2026-11-01 周日 | [Relaxation with idling gate](official-notebooks/pulse-level-circuit-simulation/qip-relaxation-measurement-with-the-idling-gate.ipynb) | 从空闲门实验提取弛豫行为。 |
| 2026-11-02 周一 | [Randomized benchmarking](official-notebooks/pulse-level-circuit-simulation/qip-randomized-benchmarking.ipynb)；[10-qubit QFT](official-notebooks/pulse-level-circuit-simulation/qip-10-qubit-QFT-algorithm.ipynb) | 加长日：理解 RB 工作流；观察大型线路编译与模拟成本。 |
| 2026-11-03 周二 | **复盘 12** | 画“线路 → 编译 → 调度 → 脉冲 → 含噪演化 → 测量”流程图。 |

## 第 13 周：量子最优控制（11-04—11-10）

本周按教程要求安装控制扩展包；遇到版本冲突时以教程中的安装单元为准。

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-11-04 周三 | [Optimal Control Overview](official-notebooks/optimal-control/01-optimal-control-overview.ipynb) | 理解目标、漂移 Hamiltonian、控制 Hamiltonian、代价函数与保真度。 |
| 2026-11-05 周四 | [GRAPE Hadamard](official-notebooks/optimal-control/02-cpo-GRAPE-Hadamard.ipynb) | 优化单比特 Hadamard，画控制脉冲和收敛曲线。 |
| 2026-11-06 周五 | [GRAPE QFT](official-notebooks/optimal-control/03-cpo-GRAPE-QFT.ipynb) | 优化双比特 QFT，记录迭代数与最终误差。 |
| 2026-11-07 周六 | [GRAPE Lindbladian](official-notebooks/optimal-control/04-cpo-GRAPE-Lindbladian.ipynb) | 比较封闭与开放系统控制目标。 |
| 2026-11-08 周日 | [Symplectic dynamics](official-notebooks/optimal-control/05-cpo-cpo-symplectic.ipynb)；[GRAPE CNOT](official-notebooks/optimal-control/08-cpo-GRAPE-cnot.ipynb) | 加长日：认识辛动力学控制；完成 CNOT 优化并比较目标类型。 |
| 2026-11-09 周一 | [CRAB state transfer](official-notebooks/optimal-control/06-CRAB-2qubit-state_to_state.ipynb)；[CRAB QFT](official-notebooks/optimal-control/07-CRAB-QFT.ipynb) | 比较 GRAPE 与 CRAB 的参数化和收敛行为。 |
| 2026-11-10 周二 | **复盘 13** | 制作优化实验表：算法、目标、边界、初始脉冲、终止条件、最终误差。 |

## 第 14 周：HEOM 基础与谱拟合（11-11—11-17）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-11-11 周三 | [HEOM index](official-notebooks/heom/heom-index.ipynb)；[1a Spin-Bath basic](official-notebooks/heom/heom-1a-spin-bath-model-basic.ipynb) | 理解层级方程、bath 与 terminator；跑通最小自旋浴模型。 |
| 2026-11-12 周四 | [1b Very strong coupling](official-notebooks/heom/heom-1b-spin-bath-model-very-strong-coupling.ipynb) | 改变耦合强度并检查层级截断收敛。 |
| 2026-11-13 周五 | [1c Underdamped spectral density](official-notebooks/heom/heom-1c-spin-bath-model-underdamped-sd.ipynb) | 理解欠阻尼谱密度参数和动力学特征。 |
| 2026-11-14 周六 | [1d Ohmic fitting](official-notebooks/heom/heom-1d-spin-bath-model-ohmic-fitting.ipynb) | 拟合谱与关联函数；记录拟合误差。 |
| 2026-11-15 周日 | [1e Pure dephasing](official-notebooks/heom/heom-1e-spin-bath-model-pure-dephasing.ipynb) | 对照解析或基准结果，验证纯退相干。 |
| 2026-11-16 周一 | [HEOM 2: FMO complex](official-notebooks/heom/heom-2-fmo-example.ipynb) | 模拟能量转移；画各位点布居。 |
| 2026-11-17 周二 | **复盘 14** | 写出 HEOM 相对 Lindblad 的优势、代价和收敛检查方法。 |

## 第 15 周：HEOM 应用与晶格模型（11-18—11-24）

| 日期 | 官方教程 | 当日任务与产出 |
| --- | --- | --- |
| 2026-11-18 周三 | [HEOM 3: Quantum Heat Transport](official-notebooks/heom/heom-3-quantum-heat-transport.ipynb) | 计算热流并检查符号与稳态能量守恒。 |
| 2026-11-19 周四 | [HEOM 4: Dynamical decoupling](official-notebooks/heom/heom-4-dynamical-decoupling.ipynb) | 改变脉冲间隔，评估非马尔可夫环境下的解耦效果。 |
| 2026-11-20 周五 | [HEOM 5a: Fermionic impurity](official-notebooks/heom/heom-5a-fermions-single-impurity-model.ipynb) | 入门费米浴，记录与玻色浴建模的差异。 |
| 2026-11-21 周六 | [HEOM 5b: Boson with fermionic leads](official-notebooks/heom/heom-5b-fermions-discrete-boson-model.ipynb) | 理解多环境组合，检查截断参数。 |
| 2026-11-22 周日 | [Jaynes–Cummings–Hubbard model](official-notebooks/miscellaneous/JCHM-tutorial.ipynb) | 建立三站点模型并观察光子/激发传播。 |
| 2026-11-23 周一 | [QuTiP 5 Optimal Control paper example](official-notebooks/miscellaneous/v5_paper-optimal-control.ipynb) | 用新接口重做控制示例，和第 13 周结果比较。 |
| 2026-11-24 周二 | **复盘 15** | 为 HEOM 与多体模型写性能记录：维数、层级深度、运行时间、收敛指标。 |

## 第 16 周：JAX、结课项目与总结（11-25—12-01）

| 日期 | 官方教程/任务 | 当日任务与产出 |
| --- | --- | --- |
| 2026-11-25 周三 | [QuTiP-JAX backend](official-notebooks/miscellaneous/JAX_backend.ipynb) | 按教程安装 `qutip-jax`；理解数据层、后端切换与适用场景。 |
| 2026-11-26 周四 | [QuTiP-JAX autodifferentiation](official-notebooks/miscellaneous/v5_paper-jax.ipynb)；[cuQuantum backend](official-notebooks/miscellaneous/cuQuantum_backend.ipynb) | 运行 `mesolve` 与自动微分示例；若有兼容的 NVIDIA GPU，再运行 cuQuantum Notebook，否则完整阅读并记录环境要求。 |
| 2026-11-27 周五 | [PIQS Overview](official-notebooks/piqs/piqs-overview.ipynb)；[Superradiant emission](official-notebooks/piqs/piqs-superradiant-light-emission.ipynb) | 理解 Dicke 基底和置换对称降维；复现超辐射发光。 |
| 2026-11-28 周六 | [Steady-state superradiance](official-notebooks/piqs/piqs-steadystate-superradiance.ipynb)；[Open Dicke model](official-notebooks/piqs/piqs-open-dicke-model.ipynb) | 比较瞬态与稳态超辐射，并模拟开放 Dicke 模型。 |
| 2026-11-29 周日 | [Spin squeezing with noise](official-notebooks/piqs/piqs-spin-squeezing-noise.ipynb)；[Boundary time crystals](official-notebooks/piqs/piqs-boundary-time-crystals.ipynb) | 研究噪声下的自旋压缩与边界时间晶体。 |
| 2026-11-30 周一 | [Multiple spin ensembles](official-notebooks/piqs/piqs-multiple-spin-ensembles.ipynb)；[Entropy and purity](official-notebooks/piqs/piqs-entropy_purity.ipynb) | 研究多自旋系综，并计算熵和纯度。 |
| 2026-12-01 周二 | **总复盘与结课整理** | 选择最有价值的一个官方 Notebook，加入自己的参数实验和中文说明；更新 README，列出已掌握能力、仍不清楚的问题和下一阶段方向。 |

## 结业标准

- [ ] 仓库内 109 个官方 `.ipynb` 全部运行或阅读，并完成一份带参数实验和中文说明的结课 Notebook。
- [ ] 能根据物理假设选择 `sesolve`、`mesolve`、`mcsolve`、`smesolve`、`brmesolve`、Floquet 或 HEOM。
- [ ] 能正确构造复合空间、Hamiltonian、塌缩算符和观测量。
- [ ] 能检查单位、迹、正定性、空间截断与数值收敛。
- [ ] 完成一个可复现的结课项目，并能解释数值结果的物理含义。

完整映射见 [官方教程完整索引](OFFICIAL_TUTORIAL_INDEX.md)。

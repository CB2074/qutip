# 项目所需 QuTiP Notebook

这个目录独立于 `official-notebooks/`，只保留当前超导量子电路、cavity-QED、qcMAP 与 Kerr-cat 项目直接需要的学习材料。

## 使用原则

1. `reference/` 中的 Notebook 是从官方教程复制得到的参考材料，不在原文件上继续堆项目代码。
2. 每完成一份参考 Notebook，都在 `personal-work/` 新建一个空白 Notebook，闭卷重写核心模型。
3. 重写时先写物理公式，再写 Hilbert 空间、算符、Hamiltonian、初态、求解器和观测量。
4. AI 只用于解释报错或给提示；不得直接生成当日完整答案。
5. 每个模型至少检查：`dims`、单位、归一化、厄米性、密度矩阵迹、Fock 截断和时间步长收敛。

## 学习顺序

| 阶段 | 参考 Notebook | 必须掌握 | 独立产出 |
| --- | --- | --- | --- |
| 1 | `reference/01-foundations/01_numpy_arrays.ipynb` | 复数数组、矩阵运算、切片、广播、数组复制 | Pauli 矩阵及其对易关系 |
| 1 | `reference/01-foundations/02_qutip_introduction.ipynb` | `Qobj`、ket、bra、operator、`dims`、`dag`、`tensor` | 单量子比特态和 Bell 态 |
| 1 | `reference/01-foundations/03_interacting_qubits.ipynb` | 复合空间、耦合项、初态、观测量 | 两量子比特交换模型 |
| 2 | `reference/02-dynamics/01_larmor_precession.ipynb` | `sesolve`、期望值、Bloch 向量 | 封闭二能级演化 |
| 2 | `reference/02-dynamics/02_open_qubit_dynamics.ipynb` | 密度矩阵、`mesolve`、`c_ops`、`T1/T2` | 有弛豫和退相干的二能级模型 |
| 2 | `reference/02-dynamics/03_time_dependent_qobjevo.ipynb` | 含时 Hamiltonian、脉冲系数、`QobjEvo` | 高斯 I/Q 驱动模型 |
| 3 | `reference/03-cavity-qed/01_vacuum_rabi.ipynb` | 腔截断、JC 交换、激发数守恒 | qubit-cavity 真空 Rabi 振荡 |
| 3 | `reference/03-cavity-qed/02_jaynes_cummings.ipynb` | JC Hamiltonian、RWA、失谐 | JC 参数扫描 |
| 3 | `reference/03-cavity-qed/03_dispersive_cqed.ipynb` | 色散近似、频移、适用条件 | 完整模型与色散模型对照 |
| 3 | `reference/03-cavity-qed/04_cavity_qubit_gates.ipynb` | 腔辅助门、脉冲和保真度 | 条件位移最小模型 |
| 3 | `reference/03-cavity-qed/05_jc_wigner.ipynb` | `ptrace`、Wigner 函数、约化态 | 相干态与猫态 Wigner 图 |
| 4 | `reference/04-kerr-cat/01_kerr_nonlinearity.ipynb` | Kerr 项、非线性相位演化 | Kerr 演化与猫态形成 |
| 4 | `reference/04-kerr-cat/02_cat_trajectories.ipynb` | 耗散、轨迹与主方程的物理区别 | 理想与有损猫态对比 |

## 每份 Notebook 的完成标准

- 能用自己的话写出模型 Hamiltonian，并解释每一项。
- 能说明每个 `tensor` 因子对应哪个子系统。
- 能不看参考资料重写 20 到 50 行最小代码。
- 能先预测、再改变一个参数并解释结果。
- 能指出至少一个数值风险或物理近似。
- 将个人重写版本保存在 `personal-work/`，文件名使用 `YYYY-MM-DD_主题.ipynb`。

## 8 月底总验收

从空白 Notebook 独立完成：Transmon-cavity 色散耦合、双频高斯驱动、Lindblad 耗散、约化腔态、光子数、保真度和 Wigner 函数，并完成 Fock 截断与时间步长收敛检查。


---
name: pde-model-audit
description: "Audit mathematical derivations, proofs and PDE models: definitions, hypotheses, units, boundary/initial conditions, singular decompositions and correspondence to code. Use for theorem/proof checking, professional mathematical review, Lean verification audits or model audits."
---

# 数学模型核对

把用户指定的数学问题、文稿和实现对应起来。推导、证明或证明纠错时读取 [数学严谨性](references/mathematical-rigor.md)，先核对条件、量词、变形合法性及边界，定位首个错误并给最小修正。数值现象和符号抽样不代替证明。

论文逻辑审查、证明完整性或 Lean 核验时，读取 [数学审稿与 Lean 核验](references/reviewer-and-lean.md)，建立主张依赖，定位具体缺口，核对形式化命题与论文是否一致；实际运行并审计公理后才能报告 Lean 通过。

只有用户要求学习训练时才读取 [训练与漏洞检测](references/learning-checks.md)；直接问解答时不强加练习。数学笔记排版由 manuscript-maintenance 处理。

1. **建模、推导和解释以先定义后使用为首要审查要求。** 按首次使用次序核对区域与测度、未知/已知场、指标与取值范围、物理单位、算子、参数、条件、分解与函数空间。不能只给参数起名字：说明物理含义、数学定义、单位与作用；区分同字母的不同系数，说明派生变量由谁定义、为什么引入。函数给出自变量和定义域，算子给出作用对象及适用条件。先用公式作定义时应明确“定义”，再用于后续推导；不能靠后面的附录或文献替代首次必要说明。修改后再做一次首次出现检查。原文英文改英文、中文改中文。
2. 从当前任务和实际文件确认研究对象。区分完整/简化模型、点源/有限源、稳态/非稳态、连续/离散问题。辅助实验必须说明验证范围。
3. 对每一项建立“数学项 → 实现函数 → 参数来源 → 验证依据”的对应。检查符号、投影权重、源强约定、积分可积性和边界项。
   从体积到曲面的等效模型，说明厚度 H、液体比例 epsilon、容量 sigma=H epsilon 及浓度的归一化；核对速度是 Darcy 通量还是孔隙平均速度，避免在对流项重复乘或漏乘液体比例。有限区域权的归一化应使用模型实际测度；区域尺度注明投影距离或曲面距离。
4. 检查弱形式的假设是否覆盖实际输入。有限能量、连续、C1 和更高正则性分别判断；不能由分离了 Dirac 项自动推断剩余载荷可积。
5. 逐个核对关键结论的充分条件和依赖；区分错误、缺条件、证明缺口与证据不足，明确缺哪个定义、估计或定理及最小修正。
6. 保留用户选定的模型与试探空间。需要改变时列清前后差别及影响，再按已有授权范围推进。

交付：直接回答当前数学问题，给出必要推导、已证/观测/待验证事项及代码对应。没有证据的原因不写成结论。查文献时核对原文适用条件；文稿和引用维护转 manuscript-maintenance。

---
name: weekly-research-report
description: "Create or update research weekly reports and Beamer slides from verified equations, parameters and results using the user-selected template. Use for scientific progress presentations, including failed experiments."
---

# 周报与科研汇报

先读取指定模板和目标 .tex 原件，再读取此次实际实验记录；源文档原位修改。用户未要求换格式时保留 Beamer，不另建 PPTX 或在线演示替代。

必须先定义后使用：每页首次出现的未知量、参数、单位、算子、缩写及误差范数，先给出读者理解该页所需的含义；不假定听众记得正文或上一份报告的定义。

每个实验说明：回答什么问题、使用什么方程与条件、固定哪些参数、改变什么、计算方法、得到什么、能说明什么。图像配文字公式，默认英文；根据用户要求决定页面数量和内容顺序。

调用 research-figures 生成或修改图，沿用语义颜色。仅引用有数据来源的结果；失败与未完成状态明确说明。不要把矩阵差异图改名为 PDE 误差图，也不要将局部块诊断表述为完整场结果。

页面叙述直接说做了什么、得到什么。优先准确图注、简明公式及必要参数，不堆执行过程和实现术语。清除用户已要求替换的旧展示，保留原数据。

沿用 manuscript-maintenance 的编译和渲染验证；检查文字溢出、图像大小、编号和跨页衔接。交付 .tex、对应 PDF 和关键结果来源。

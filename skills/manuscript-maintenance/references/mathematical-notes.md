# 数学笔记与 Markdown/LaTeX 输出

用户只问问题时直接作答；明确要求文件才生成文件。先确定 Markdown/LaTeX 以及速记/标准/深度，按任务选定义、条件、结果、证明、例子、反例、错误机制等组件，不机械套用全部标题。

数学笔记与问答同样必须先定义后使用。先说明符号、集合/指标集、空间、算子及参数的含义和取值范围，再代入公式或讨论性质；名字不能替代定义。移动段落或只摘取局部解释时，重新检查其必要定义是否仍在使用之前。

Markdown 使用目标阅读器支持的 $...$ 与 $$...$$；TeX 使用 \(...\)、\[...\]，需编号时用 equation/align。使用标准数学算子，核对括号、环境、公式分隔符和交叉引用。Markdown 图片链接需真实存在；交付时图片必须在清理临时目录后仍可用。

概念笔记说明对象、定义、直觉、适用范围及正反例；证明笔记列条件与结论，给关键逻辑链；错题笔记定位首个错误、根因、最小修正和可迁移的检查方式。仅在用户要求训练时调用模型核对技能中的 learning-checks，不默认考用户。

普通数学推导和证明读取 pde-model-audit/references/mathematical-rigor.md；数值图像和计算机代数不代替证明。能写出显式定义时不以“见文献”替代首次定义。

数学笔记模板：工作区 Templates/TemplateMathNotesMacStyle 存在时优先使用它。可移植后备为 assets/math-notes-template/MathNotesTemplate.tex，接口为 \defn、\prop、\pf、\conclusion、\note、\unresolved，保留接口而替换样例内容。学位论文规范不自动套到数学笔记。

编译按项目构建规则；biblatex 文献有变动时运行相应 Biber 流程，不对无文献文件机械跑 Biber。不默认启用 shell-escape。检查退出状态、未定义引用、溢出和渲染页。Markdown 检查正文公式、图片、表格、数据及单位。

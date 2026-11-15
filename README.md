# Research Skills

一组用于数学建模、PDE研究、受控数值实验、科研写作、文献与计算设备协作的agent skills。主要说明采用中文；图表及产物语言由具体项目决定。

## 技能

| Skill | 用途 |
|---|---|
| [pde-model-audit](skills/pde-model-audit/SKILL.md) | 数学模型、单位、条件、证明与Lean核验范围 |
| [numerical-experiment](skills/numerical-experiment/SKILL.md) | 参数管理、受控实验、运行身份、分块和进度 |
| [numerical-diagnosis](skills/numerical-diagnosis/SKILL.md) | 常数保持、积分、矩阵、收敛与异常定位 |
| [manuscript-maintenance](skills/manuscript-maintenance/SKILL.md) | 先定义后使用、正文和引用维护、编译与页面检查 |
| [research-figures](skills/research-figures/SKILL.md) | Python/TikZ绘图、语义配色与数据来源 |
| [weekly-research-report](skills/weekly-research-report/SKILL.md) | 方程、参数、结果和下一实验的科研汇报 |
| [research-compute-access](skills/research-compute-access/SKILL.md) | Tailscale/SSH/GitHub接入与Windows独立作业设计 |
| [research-literature-access](skills/research-literature-access/SKILL.md) | 论文原文、arXiv和Zotero获取 |
| [research-literature-synthesis](skills/research-literature-synthesis/SKILL.md) | 文献证据、研究动机、相关工作与检索管理 |

## 安装与使用

对Codex，可将需要的skills/<name>目录复制到自己的 ~/.codex/skills/<name>，先检查同名目录，备份并人工合并已有自定义内容，不覆盖设备配置。也可使用支持GitHub路径安装的skill-installer逐项安装。其他agent需将对应SKILL.md及其引用文件接入自身技能机制；仅克隆仓库不保证自动加载。

按具体任务自主选择技能；项目AGENTS.md、实际代码/配置和当前用户指令定义任务事实与权限。技能之间有引用，按工作需要安装相应配套技能；PDF/呈现工具、SymPy及单位工具等可能需要环境另行提供。

## 核心工作原则

先定义后使用；明确数学对象和实质变化；每个结论对应证据；控制变量；定位首个失败阶段；分别报告执行、代数、数值与物理验证。README和技能不是计算结果或数学正确性的保证。

## 设备配置与实现状态

真实hosts.json、密钥、凭据、本地库和项目数据不包含在仓库。使用research-compute-access/references/hosts.example.json配置自己的设备。公开文档删除了原机器的地址、用户名、绝对路径和历史在线记录，本地配置由使用者管理。

Windows的submit/status/logs/fetch/cancel目前是协议草案，尚未实现为作业调度器；不得按文档占位接口宣称队列已部署。现有windows_remote.py是短Python接入工具，不等于HPC调度器。

## 来源与发布范围

本次发布9项本地创建的工作流技能。系统/插件技能和标有第三方作者的sympy、uncertainty-and-units等未复制。外部工具、论文、字体、配色和模板引用保留各自来源与权利，不因链接而重新授权。

尚未选择开源许可证；公开可见不等于授予任意复制、修改或再分发许可。后续可由仓库所有者明确选择许可证。

---
name: research-compute-access
description: "Connect projects to the shared Windows research computer via Tailscale and SSH; inspect environments, transfer code, track remote jobs, and access or synchronize GitHub repositories. Use for cross-project remote-compute setup or connection failures."
---

# 跨项目 Windows / Tailscale / SSH / GitHub 接入

此技能管理接入与代码来源；实验参数和科学判据由 numerical-experiment 负责。不要把 示例项目 的路径或解释器当成所有项目的默认值。

## Windows 接入
读取 [连接配置与已知设备](references/windows-access.md) 和本地 `references/hosts.json`。首次使用需将 `references/hosts.example.json` 复制为本地 hosts.json 并填写已核验配置；公开仓库不提供真实连接信息。连接配置包含地址、用户名、密钥路径及已核验的主机别名，不含口令/私钥内容。每次检查当前可达性，不把上次在线当作当前在线。

用 `python3 scripts/windows_remote.py probe` 作只读 Tailscale 地址 SSH/Python 探测。失败按隧道/路由 → TCP/SSH 握手 → 主机密钥 → 用户认证 → 解释器区分，不在已配置成功后反复重装 SSH。Windows 本机握手成功不能证明 Mac 到 Windows 的连接成功。不要关闭主机验证或自动重建主机信任来绕过错误。

连接时整组读取主机、用户、端口、密钥、HostKeyAlias及其他已验证SSH选项，不只取host/user。若连接地址与known_hosts中的身份名不同，仅使用配置中已核验的HostKeyAlias；不可猜别名来绕过密钥不匹配。父进程链是独立启动的辅助证据，不要求固定为某一链；会话关闭后进程仍在且日志/状态推进才支持脱离。

## 项目接入
确认本地根目录、Windows 项目根目录、传输集合及输出位置。新项目建立自己的目录和运行输出；不能覆盖其他项目或正在运行的输入。先读取版本、模块、编译器和可用资源，优先使用已安装环境；只有必要且在任务授权内才补依赖。原生加速是否需要编译器由实际代码决定。

短 Python 探测可用 `scripts/windows_remote.py run FILE.py`；大项目用已验证 SFTP/SCP 或 Git 工作副本传输，不把大源码塞进远程命令。后台运行使用项目自己的运行器，记录 PID/任务名、最终参数、日志、状态与输出目录；断开 SSH 不应终止任务。

启动后另开连接核对进程身份、状态文件和日志进展，再报告“正在运行”。Windows SSH 中 `Popen` 返回 PID 不保证子进程在会话结束后存活；若实际发生此问题，可用任务计划程序或已验证的 WMI 启动方式脱离会话，并再次核验。完成结果回传后比较远端和本地文件哈希，再清理本任务的远程临时启动脚本。

## HPC 式作业提交

用户要求像HPC一样提交、稍后查询或多agent共用Windows时，读取 [独立作业协议与验收](references/windows-job-protocol.md)。优先复用项目已有工具，检查实际能力后再使用；文档中的submit/status/logs/fetch/cancel是目标接口，不能当成已经安装的命令。原生Windows优先PowerShell作业脚本+计划任务，Mac可提供shell命令包装；Bash或nohup本身不证明任务脱离。除明确需要Linux环境外，不为脚本风格额外安装WSL或迁移求解器。

只授权编写技能/离线设计且设备有重要运行时，只修改本地文档，不探测Windows、不上传、注册任务、改电源设置或启动测试。此限制针对当前设计阶段，不阻止用户后续明确授权的查询与测试。

## Mac 离线、Windows 独立计算与稍后查询

用户希望可合盖或关闭 Mac，让 Windows 独立运行，稍后回来再要求查询。对这样的任务，启动前将所需代码、配置和输入完整放在 Windows，本地 Mac 不应承担持续计算、文件供应或保活职责。

采用 Windows 计划任务或已验证的脱离会话启动方式。不能只看到计划任务已创建、启动命令成功或获得 PID 就宣称脱离完成：关闭启动用 SSH 会话后，另开连接检查任务状态、实际进程身份/父进程、状态文件和日志推进。计划任务返回 Ready 也不能单独证明计算结束，应检查子进程与最终状态。记录配置快照、任务名、运行目录、日志、状态文件和输出位置；任务名和路径按实际项目确定，不能固定为历史任务。

确认脱离后明确告诉用户：**Mac 合盖、断网或关机不影响这次 Windows 任务；Windows 自身须保持开机、可计算且不睡眠。** 检查计划任务的登录模式与电源设置，说明是否依赖用户保持登录、是否有运行时限及电池/空闲停止条件。不能把“仅在登录时运行”的限制推广为所有计划任务的性质；如未检查，明确该项尚未核实。用户注销、Windows 睡眠或重启的影响须按实际设置说明。不得将 Mac 离线与 Windows 离线混淆。

交付一段简短的离线交接：
- 已验证的独立启动方式与任务名。
- 当前阶段、已完成算例数及核查时刻。
- 基于实测阶段进度的剩余时间范围和估时的不确定性；无新实测时标为初估。
- 日志、状态与最终结果路径，以及 Windows 需保持的条件。
- 用户回来后可直接说“查询 Windows 任务”，无需保持 Mac 或聊天会话在线。

用户选择稍后回来查询时，不承诺离线持续监控、主动通知或自动拉回结果，也不为单次任务创建定时自动化。收到查询后重新连接，核对同一运行身份、进程、日志和状态，将执行完成、验证通过、失败及停滞分别报告；完成后回传预先约定的结果与指标，核对完整性和哈希。状态标为 running 但进程已退出时，按中断处理，不能照抄旧状态。重启前检查运行中的进程和检查点，避免重复启动；重新执行 schtasks /run 本身不保证从断点继续。

## 日志、查询与停止

Python后台输出显式设置-u、PYTHONUNBUFFERED=1或flush，按块/阶段写时间戳；状态字段与增量输出规范见numerical-experiment的分块指南。空日志本身不能证明未运行。用户选择稍后查询时不主动轮询；正在受托跟进任务时采用有依据的检查间隔和轻量元数据查询，不高频重复SSH。探测有开销，但不能未测量就称其导致计算变慢。

停止或重启按用户授权及任务约定进行。先核对任务名、命令行、启动时间与子进程，优先受控取消；必要时只终止该任务进程树，不能按python名称批量杀进程。停止后确认子进程已退出再重启。替代运行记录supersedes/superseded_by和原因；真实区分failed、stopped、superseded、abandoned，不能把所有旧运行一律废弃，也不删除原始证据。

## GitHub 联通
读取 [GitHub 与代码同步](references/github-sync.md)。优先可用 GitHub 连接器进行受支持查询；需要本地或 Windows 工作副本时用该机器上的 Git。分别验证连接器权限与远端 Git 认证，它们不互相证明。远端尚未安装/认证时明确记录，不声称联通已完成。

记录远端 URL（移除凭据）、分支、commit 和未提交文件；本地未提交研究代码必须额外传输并记录哈希，仅 git clone 不能复现它。禁止把 token、密码、私钥、含凭据 URL、实验私有输入意外提交。按用户任务范围操作；不得把连接权限理解为发布、强推、关机或停止其他任务的授权。

完成接入后交付可复用的启动/检查命令、实际环境、项目位置和状态。用户要求桌面启动器时放在该项目自己的桌面目录，保留日志入口。

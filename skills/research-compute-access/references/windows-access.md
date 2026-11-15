# Windows 接入配置（公开示例）

本仓库不包含任何真实设备配置、私钥或连接成功记录。将hosts.example.json复制为本地hosts.json，填写你自己的已核验主机、用户、密钥路径、解释器和SSH选项。hosts.json已被Git忽略，不提交。

先按可信渠道核实SSH主机指纹，再执行只读probe。保留StrictHostKeyChecking=yes。HostKeyAlias只在实际信任记录需要时配置，不用猜测别名绕过校验。

Tailscale/SSH在线、Python模块、Git和现有任务需逐次实查。新项目使用自己的Windows目录，记录输入/代码身份；任务独立运行规则见windows-job-protocol.md。旧版Windows OpenSSH若经实测不支持当前SCP协议，才考虑scp -O。

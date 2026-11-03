# 千瓜品牌笔记统计

版本：1.1.0。用于在 Codex 中查询、核对并比较千瓜收录的小红书品牌与产品笔记量。

**这是工作流技能，不是开箱即用的千瓜爬虫。**在线查询需要可用的浏览器或已授权连接器、千瓜账号及相应数据权限；也支持读取用户提供的千瓜导出或截图。当前没有随包提供或实测通过的千瓜 API 连接器。

## 使用

将本目录复制到 Codex 的 `skills/qiangua-brand-notes` 目录，并在支持技能的会话中调用：

> 用 $qiangua-brand-notes 查询赛奥金、蓁致、晤漾、赛莱拉、科洱美、银座近90天的千瓜笔记量，分别统计品牌总量与脐带面膜相关量，附证据。

也可以提供千瓜导出或截图，要求按统一口径汇总。未指定日期时，默认最近90个完整自然日，不含当天。

## 能力与边界

- 分开记录品牌量、产品相关量，以及平台实际显示的指标名称。
- 对通用名称和别名消歧，多关键词有完整笔记列表时才计算去重并集。
- 保留近似值及“+”下限；未登录、无权限、未采集均不写成零。
- 记录日期、筛选、页面链接及证据位置，便于复核。
- 不包含账号、Cookie、会员权限或绕过登录/付费限制的代码。

## 文件

| 文件 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | 运行指令与工具选择规则 |
| [六品牌示例](references/umbilical-mask-example.md) | 待验证的检索线索，不含虚构数量 |
| [结果字段](references/result-schema.md) | 状态及证据契约 |
| [版本记录](CHANGELOG.md) | 本次变更 |
| [校验脚本](scripts/validate.py) | 元数据、资源链接与基础结构检查 |

## 维护与 GitHub

结构参照 [Agent Skills 规范](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)，在 `SKILL.md` 中保留渐进式引用；Codex 界面信息放在 `agents/openai.yaml`。

本目录可作为独立公开仓库根目录。发布前在本机完成 GitHub 登录，再运行：

```powershell
git init -b main
git add .
git commit -m "Release qiangua-brand-notes v1.1.0"
gh repo create qiangua-brand-notes --public --source . --remote origin --push
```

运行前确认当前目录为本技能包且没有同名远程仓库。此命令会公开提交的内容，查询数据应另存。本包未指定开源许可证；公开可查看不等于已授予任意再分发许可，发布者可另行选择许可证。

## 校验

```powershell
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

本地包包含 GitHub Actions 配置。当前发布凭据不含 workflow 权限，远程自动校验尚未启用；可将 scripts/validate-workflow.yml 模板手动放入 .github/workflows/validate.yml。校验覆盖结构与元数据，不证明千瓜登录、权限或实时抓取已通过。真实查询验收需记录至少一个有来源的数量、一个明确的阻塞状态，以及日期与筛选证据；禁止用模拟结果冒充线上验证。

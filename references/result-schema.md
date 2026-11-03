# 结果字段契约

交付 CSV 使用 UTF-8，缺失数字留空。每行只表达一个品牌的一种查询范围；同品牌的品牌量、产品量分行。

| 字段 | 含义 |
|---|---|
| brand | 用户原始品牌名称 |
| scope | brand 或 product |
| query | 实际查询实体或关键词；未执行时标为拟查询 |
| start_date / end_date | YYYY-MM-DD；包含边界日期 |
| timezone | 查询日期采用的时区 |
| metric | 千瓜指标原名；未读取时留空 |
| raw_count | 页面显示原值，含单位及“+” |
| numeric_count | 可转换数值，缺失留空；不得当成精确值单独展示 |
| precision | exact / approximate / lower_bound / unknown |
| status | observed / not_collected / login_required / permission_denied / tool_blocked / ambiguous / not_indexed |
| filters | 实际筛选；未读取时明确未执行 |
| source_url | 实际结果页链接；只有入口时必须在备注说明 |
| evidence | 截图、导出行号或实际页面原文位置 |
| collected_at | 实际读取数量时间，未读取留空 |
| note | 消歧、缺口及不可比原因 |

`observed` 行需要 metric、raw_count、source_url、evidence、collected_at。精确 0 只允许在 observed 行记录。`not_indexed` 不是 0。登录标题只证明入口呈现登录状态，未必证明所有浏览器会话都未登录；不要扩大结论。

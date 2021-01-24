# MCMICM2020C

:ledger: ​Here is the process of solving the C problem of the 2020 MCM/ICM.

## Data Processing

1.清洗掉错误值，空白值等

2.清洗掉其他类别的商品，如在婴儿奶嘴的表格中，有婴儿床等干扰信息存在。

## Feature Engineering

1. 每种产品的词频图->词云图

2. 客户的helpfulness

3. 客户的是否为vine

4. 客户是否为veried customer的比率

5. 合并headline和body

6. 每个评论的情感得分

7. 评论产品属性特征词：找到特有高频词语

8. 评论修饰词数量：建立词库

9. 评论深度：$L_e = \frac{\ln(N_a+N_b)}{ln(N_t)}$,$L_e$是评论深度，$N_a$是情感词个数，$N_b$是属性词，$N_t$是评论总长度。

10. 本条评论是否为veried customer
11. 客户所有评论的平均置信度
12. 灰色关联分析
13. 时间分布图
14. 评分分布图
15. 种类分布饼状图

## Model


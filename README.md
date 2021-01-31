# MCMICM2020C

:ledger: ​Here is the process of solving the C problem of the 2020 MCM/ICM.

## Data Processing

1. 清洗掉错误值，空白值等；

2. 清洗掉其他类别的商品，如在婴儿奶嘴的表格中，有婴儿床等干扰信息存在。

## Feature Engineering

1. 每种产品的词云图；

2. 客户的 $helpfulness ratio$；

3. 客户是否为 $vine$；

4. 客户是否为 $verified$ 的比率；

5. 合并 $review\_headline$ 和 $review\_body$；

6. 每个评论的情感得分；

8. 评论的修饰词比率；

9. 评论深度：$L_e = \frac{\ln(N_a+N_b)}{ln(N_t)}$，$L_e$是评论深度，$N_a$是情感词个数，$N_b$是属性词，$N_t$是评论总长度；

10. 本条评论是否为 $verifird\_customer$；
11. 客户所有评论的平均置信度；
12. 灰色关联分析；
13. 时间分布图；
14. 评分分布图；
15. 种类分布饼状图；

## Model

**基于迭代信誉重分配的双置信度融合模型**



$$Q =\frac{\sum{Q_j}}{N} $$

$Q$ 是该种类商品综合评分，$N$ 代表不同品牌商品个数，$Q_j$ 代表不同品牌商品的综合得分。



$Q_j=max\left\{W_i\right\}\frac{\sum{r_i*W_i}}{\sum{W_i}}$

$W_i $代表每条评论的置信度，$r_i$ 为每条评论所打出的分数，$max\left\{W_i\right\}$ 为所有该商品评论中置信度最高的值。



$$W_i=w_i*\delta_i*t_i$$

$w_i $为评论人置信度，$\delta_i$ 为评论内容置信度，$t_i$ 为评论时效性。



$w_i=TR_i^\theta\frac{\sum TR_j}{\sum TR_j^\theta}$

$\theta $为可变参数，调控信誉重分配的权重，一般来说，$\theta$ 越大，信誉度高的人在重分配过程得到的信誉度越高。$TR$ 代表评论人所打出的分数和客观真实分数的相关系数。



$TR_i=\frac{lg(k_i)}{max\left\{ k_j \right\}} \cdot \frac{1}{k_i}\cdot\sum (\frac{r_{i\alpha}-\overline{r_{i}}}{\sigma_{r_i}})\cdot(\frac{Q_{\alpha}-\overline{Q_{i}}}{\sigma_{Q_i}})$

如果 $TR_i<0$ 则令其等于 $0$。

$k_i$ 是该评论者的所有评论数量，$max\left\{ k_j \right\}$ 是所有人中评论数量最大值，$r_{i\alpha}$ 是评论者 $i$ 对物品 $\alpha$ 的评分，$\overline{r_i}$ 是评论者 $i$ 的所有评分低平均值，$\sigma_{r_i}$ 是评分的标准差，$Q_\alpha$ 是该评论者评论过的所有商品的综合评分，$\overline{Q_{i}}$ 是平均值，$\sigma_{r_i}$ 是标准差。



$\delta_i$ 是通过模糊层次分析法 $(AHP)$ 确立权重，再通过理想解法确定置信度。

使用的指标如下：

有用性投标比 $ H_1 = \frac{helpful\_vote}{total\_vote}$

情感表达强度 $H_2 $

修饰词比例 $H_3 = \frac{N_b}{N_t}$

评论深度 $H_4 = \frac{ln(N_a+N_b}{N_t}）$

是否为 $verified\_customer$：$H_5$

是否为 $vine$：$H_6$



$t_i = \frac{365-\Delta t}{365}$

$\Delta t$为阅读评论时间和发表评论时间的差值。



让 $Q$ 和 $W$ 不停迭代，直到稳定为止，如当 $\Delta Q < 10^{-4}$ 时，停止迭代。
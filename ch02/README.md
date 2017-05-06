# Chapter 2 提供推荐
## 搜集偏好
### 数据集`critics.py`
```python
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}
```
## 寻找相近的用户
### 欧几里德距离评价
```python
#  欧几里德距离
def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        for item in prefs[person2]:
            si[item] = 1

    #  如果两人没有共同之处，返回0
    if len(si) == 0:
        return 0

    #  计算所有差值的平方和
    #  sum_of_squares = sum(pow(prefs[person1][item] - prefs[person2][item], 2)
        #  for item in prefs[person1] if item in prefs[person2])
    sum_of_squares = sum(pow(prefs[person1][item] - prefs[person2][item], 2)
                         for item in si)
    return 1 / (1 + sqrt(sum_of_squares))
```
### 皮尔逊相关度评价
```python
#  皮尔逊相关系数
def sim_person(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    n = len(si)

    #  如果两者没有相关性，返回0
    if n == 0:
        return 0

    #  求和
    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    #  求平方和
    sum1Sq = sum([pow(prefs[person1][item], 2) for item in si])
    sum2Sq = sum([pow(prefs[person2][item], 2) for item in si])

    #  求乘积之和
    pSum = sum([prefs[person1][item] * prefs[person2][item] for item in si])

    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0:
        return 0
    r = num / den
    return r
```
* 0.8-1.0 极强相关
* 0.6-0.8 强相关
* 0.4-0.6 中等程度相关
* 0.2-0.4 弱相关
* 0.0-0.2 极弱相关或无相关

### Jaccard系数
### 曼哈顿距离算法

### 为评论者打分
```python
#  根据评分寻找最佳匹配者
#  返回结果的个数和相似度函数均为可选参数
def topMatchs(prefs, person, n=5, similarity=sim_person):
    scores = sorted([(similarity(prefs, person, other), other)
                     for other in prefs if other != person])
    scores.reverse()
    return scores[0:n]
```
### 推荐物品
```python
#  利用其他人评价值的加权平均，为某人提供建议
def getRecommendations(prefs, person, similarity=sim_person):
    totals = {}
    simSums = {}

    for other in prefs:
        #  不要和自己做比较
        if other == person:
            continue
        sim = similarity(prefs, person, other)

        #  忽略评价值小于等于零的情况
        if sim <= 0:
            continue

        for item in prefs[other]:
            #  对自己还未看过的电影进行评价
            if item not in prefs[person] or prefs[person][item] == 0:
                #  相似度 * 评价值
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                #  相似度之和
                simSums.setdefault(item, 0)
                simSums[item] += sim

    #  建立一个归一化的列表
    rankings = sorted([(total / simSums[item], item)
                       for item, total in totals.items()])

    rankings.reverse()
    return rankings
```

## 测试
```python
if __name__ == '__main__':
    print '欧几里德距离：', sim_distance(critics.critics, 'Lisa Rose', 'Gene Seymour')
    #  0.294298055086

    print '皮尔逊相关系数：', sim_person(critics.critics, 'Lisa Rose', 'Gene Seymour')
    #  0.396059017191

    print '根据评分寻找最佳匹配者（采用皮尔逊系数）：', topMatchs(critics.critics, 'Toby', n=3)
    print '根据评分寻找最佳匹配者（采用欧几里德距离）：', topMatchs(critics.critics, 'Toby', n=3, similarity=sim_distance)
		# 根据评分寻找最佳匹配者（采用皮尔逊系数）： [(0.9912407071619299, 'Lisa Rose'), (0.9244734516419049, 'Mick LaSalle'), (0.8934051474415647, 'Claudia Puig')]
		# 根据评分寻找最佳匹配者（采用欧几里德距离）： [(0.4, 'Mick LaSalle'), (0.38742588672279304, 'Michael Phillips'), (0.3567891723253309, 'Claudia Puig')]

    print '加权平均，为某人提出建议（采用皮尔逊系数）：', getRecommendations(critics.critics, 'Toby')
    print '加权平均，为某人提出建议（采用欧几里德距离）：', getRecommendations(critics.critics, 'Toby', similarity=sim_distance)
		# 加权平均，为某人提出建议（采用皮尔逊系数）： [(3.3477895267131013, 'The Night Listener'), (2.8325499182641614, 'Lady in the Water'), (2.5309807037655645, 'Just My Luck')]
		# 加权平均，为某人提出建议（采用欧几里德距离）： [(3.457128694491423, 'The Night Listener'), (2.778584003814924, 'Lady in the Water'), (2.4224820423619167, 'Just My Luck')]
```

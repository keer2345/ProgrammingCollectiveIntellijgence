# Chapter 2 提供推荐
## 搜集偏好
### 数据集`critics.py`
```
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
```
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
```
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

## 为评论者打分


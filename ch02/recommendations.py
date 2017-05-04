# -*- coding:utf-8 -*-
from math import sqrt
import critics


#  欧几里德距离
def sim_distance(prefs, person1, person2):
    '''
    doc for
    sim distance
    '''
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
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


if __name__ == '__main__':
    print '欧几里德距离：', sim_distance(critics.critics, 'Lisa Rose', 'Gene Seymour')
    #  0.294298055086

    print '皮尔逊相关系数：', sim_person(critics.critics, 'Lisa Rose', 'Gene Seymour')
    #  0.396059017191

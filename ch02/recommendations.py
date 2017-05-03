# -*- coding:utf-8 -*-
from math import sqrt
import critics


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


if __name__ == '__main__':
    print sim_distance(critics.critics, 'Lisa Rose', 'Gene Seymour')
    #  0.294298055086
    print sim_distance(critics.critics, 'person1', 'person2')

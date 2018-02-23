# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[:][0]

# 根据名字排序
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[:][1]

# 根据成绩排序
L3 = sorted(L, key=by_score, reverse=True)
print(L3)

# 根据名字成绩排序
L4 = sorted(sorted(L, key=by_score, reverse=True), key=by_name)
print(L4)
# 去除首尾空格
def trim(s):
    if '' == s:
        print('1', s)
        return ''
    if s[:1] != ' ' and s[-1:] != ' ':
        print('2', s)
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[0:len(s) - 2])


# 使用迭代查找一个list中最小和最大值
def findMinAndMax(L):
    if [] == L or '' == L:
        return None,None
    y = L[0]  # 最大值
    x = L[0]  # 最小值
    for n in L:
        if x > n:
            x = n
        if y < n:
            y = n
    return x,y

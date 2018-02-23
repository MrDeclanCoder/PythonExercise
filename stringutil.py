from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


r = str2int('1596345654654564')
print(r)


def normalize(name):
    # return name[0].upper() + name[1:].lower()
    return name.title()


# 测试:-
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    def char2num(s):
        return DIGITS[s]

    def num2int(x, y):
        return x * 10 + y

    ss = s.split('.')
    s1 = ss[0]
    s2 = ss[1]
    print(s2)
    print(pow(10, len(s2)))
    num1 = reduce(num2int, map(char2num, s1))
    num2 = reduce(num2int, map(char2num, s2)) / pow(10, len(s2))
    return num1 + num2


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# -*- coding: utf-8 -*-
from square import power
from recursion import recursion
from variableparameter import calc, product
from util import findMinAndMax, trim
from collections import Iterable
import os


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)

print('***********************')


def createCounter():
    n = 0

    def counter():
        nonlocal n
        n = n + 1
        return n

    return counter


def createCounter2():
    n = [0]

    def counter():
        n[0] += 1

        return n[0]

    return counter


# 测试:
counterA = createCounter2()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter2()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print('**********************')


def f(x):
    return x * x


r = map(f, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(r))

print('**********************')
print(abs)
print(abs(-11))

# 首先获得一个Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环
while True:
    try:
        # 获得下一个值
        x = next(it)
        print(x)
    except StopIteration:
        print('StopIteration happened')
        break

print(iter('12345'))
print(x for x in range(10))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('56165564', Iterable))
print(isinstance(56165564, Iterable))
print(isinstance('fafagab', Iterable))

print('*******************')
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])

print('******************')
print([d for d in os.listdir('.')])

L = [x * y for x in range(1, 11) for y in range(1, 11, 2)]
print(len(L), L)
print('******************')
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')

print('******************')
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

print('******************')
# 测试:
if trim('hello  ') != 'hello':
    print('1测试失败!', trim('hello  '))
elif trim('  hello') != 'hello':
    print('2测试失败!', trim('  hello'))
elif trim('  hello  ') != 'hello':
    print('3测试失败!', trim('  hello  '))
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!', trim('  hello  world  '))
elif trim('') != '':
    print('5测试失败!', trim(''))
elif trim('    ') != '':
    print('6测试失败!', trim('    '))
else:
    print('测试成功!')

print('******************')

L = []
n = 1
i = 0
while n <= 99:
    L.insert(i, n)
    i += 1
    n += 2
print(L[-2:])
print([L[0], L[1], L[2]])  # 取出前三个元素笨方法
r = []
j = 3
for x in range(j):
    r.append(L[x])  # for取出前三个元素方法
print(r)

print('*******************')
print(recursion(5))
print(recursion(100))

print('*******************')

print(power(5))
print(power(5, 4))

print('*******************')

print(calc(1, 2, 3, 4, 5, 6, 7, 8))

print('*******************')

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

import math


def quadratic(a, b, c):
    if not isinstance(a | b | c, (int, float)):
        raise TypeError('bad operand type')
    else:
        type = b * b - 4 * a * c
        if type > 0:
            x1 = (-b + math.sqrt(type)) / (2 * a)
            x2 = (-b - math.sqrt(type)) / (2 * a)
            return x1, x2
        elif type == 0:
            x1 = x2 = (-b) / (2 * a)
            return x1, x2
        else:
            return '此方程无解'


# 测试:
# a = int(input('请输入a: '))
# b = int(input('请输入b: '))
# c = int(input('请输入c: '))


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


def product(x, *y):
    for n in y:
        x *= n
    return x

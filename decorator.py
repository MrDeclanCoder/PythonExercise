# _*_coding:utf-8 _*_
import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        # start_time = time.localtime(time.time())
        func = fn(*args, **kw)
        end_time = time.time()
        # end_time = time.localtime(time.time())
        print('%s executed in %s ms' % (fn.__name__, end_time - start_time))
        return func

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')


def log(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call', text)
                fn = func(*args, **kw)
                print('end call', text)
                return fn

            return wrapper

        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call')
            fn = text(*args, **kw)
            print('end call', text.__name__)
            return fn

        return wrapper


@log
def funcc():
    print('%s()' % funcc.__name__)


@log('ggggg')
def funccc():
    print('%s()' % funccc.__name__)

funcc()
funccc()

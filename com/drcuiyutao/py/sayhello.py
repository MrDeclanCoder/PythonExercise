# -*- coding: utf-8 -*-

' a test module '
from com.drcuiyutao.py.find import find_file_by_key

__author__ = 'Declan'

import sys
import os
import pickle
import json
import time
from io import BytesIO


def test():
    args = sys.argv
    argLength = len(args)
    if argLength == 1:
        print('Hello World!')
    elif argLength == 2:
        print('Hello, %s !' % args[1])
    else:
        print('too many arguments')


class Student(object):
    count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1

    def print_score(self):
        print('score = %i' % self.score)


class Human(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Human object (name = %s)' % self._name


class Fib(object):

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


if __name__ == '__main__':
    # a = int(time.mktime(time.strptime('YYYY-mm-dd HH:MM:SS', '%Y-%m-%d %H:%M:%S')))
    print(time.localtime(1520524800))

    human = Human('Mike')
    print(json.dumps(human, default=lambda human: human.__dict__))
    with open('human.txt', 'rb') as f:
        d = pickle.load(f)
        print(d)
    # print(human)
    # with open('abc', 'r') as f:
    #     print('aaa  %s ' % f.read())
    #     print(f.tell())
    #     f.seek(0)
    #     print('aaa  %s ' % f.read())

    f = BytesIO()
    f.write('aaa'.encode('utf-8'))
    print(f.getvalue())

    print(os.name)
    print(os.environ)
    find_file_by_key("find")

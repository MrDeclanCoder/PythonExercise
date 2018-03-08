# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, time, random,subprocess


def run_process(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 1)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))


def pro_write(q):
    print('pro_write pid : %s' % os.getpid())
    for value in ['a', 'b', 'c']:
        print('put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())


def pro_read(q):
    print('pro_read pid : %s' % os.getpid())
    while True:
        m = q.get(True)
        print('get %s from queue' % m)


if __name__ == '__main__':
    # q = Queue()
    # pw = Process(target=pro_read, args=(q,))
    # pr = Process(target=pro_read, args=(q,))
    # pw.start()
    # pr.start()
    # pw.join()
    # pr.terminate()

    # print('Parent process %s ' % os.getpid())
    # p = Pool(4)
    # for i in range(4):
    #     p.apply_async(long_time_task, args=(i,))
    # print('Waiting for all subrocesses done...')
    # # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    # p.close()
    # p.join()
    # print('All subprocesses done.')
    print('*******************************************')
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit coe:', r)

# p = Process(target=run_process, args=('test',))
# print('Child process will start')
# p.start()
# p.join()
# print('Child process end.')

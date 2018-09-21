#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
代码实现功能，将数据列表中的数据传入，使用四个线程处理，将结果保存在Queue中，线程执行完后，从Queue中获取存储的结果
"""

import threading
import time
from queue import Queue
import random


def job(l, q):
    """
    对列表的每个元素进行平方计算，将结果保存在队列中

    由于多线程执行的函数是没有返回值的, 所以需要提供容器, 将需要的数据进行存储
    :param l: 列表
    :param q: 队列
    :return: None
    """
    for i in range(len(l)):
        l[i] = l[i] ** 2  # 平方

    sleep_time = random.randint(0,3)
    print(sleep_time)
    time.sleep(sleep_time)
    q.put(l)

def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [5, 5, 5]]

    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results = []
    for _ in range(4):
        results.append(q.get())

    print(results)

if __name__ == '__main__':
    multithreading()
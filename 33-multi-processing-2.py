#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用multiprocessing的Queue进行进程数据存储
"""

import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue


if __name__ == '__main__':
    # 创建一个进程的队列
    q = mp.Queue()
    # 创建多个进程
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p3 = mp.Process(target=job, args=(q,))

    # 启动进程任务
    p1.start()
    p2.start()
    p3.start()
    # 加入到主线程
    p1.join()
    p2.join()
    p3.join()

    rest = 0
    while not q.empty():
        rest += q.get()

    print(rest)

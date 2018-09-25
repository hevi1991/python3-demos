#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
只有用共享内存才能让CPU之间有交流。
"""

import multiprocessing as mp
import time

def job(x, y, lock):
    for _ in range(10):
        # 加锁
        lock.acquire()
        time.sleep(0.1)
        # 共享内存数据赋值, 需要使用value属性取
        x.value += y
        print(x.value)
        # 解锁
        lock.release()

def core():
    # 使用进程锁进行控制写入
    lock = mp.Lock()

    # 我们可以通过使用Value数据存储在一个共享的内存表中。
    v_1 = mp.Value('i', 0)

    # 还有一个Array类，可以和共享内存交互，来实现在进程之间共享数据。
    # a_1 = mp.Array('i', [1, 2, 3, 4])

    p1 = mp.Process(target=job, args=(v_1, 1, lock))
    p2 = mp.Process(target=job, args=(v_1, 3, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('rest:', v_1.value)


if __name__ == '__main__':
    core()
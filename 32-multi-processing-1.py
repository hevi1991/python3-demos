#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import multiprocessing as mp


def job(a, d):
    """
    定义一个被线程和进程调用的函数
    :param a:
    :param d:
    :return:
    """
    print('aaaaa', a, d)


if __name__ == '__main__':
    # 创建一个进程
    p1 = mp.Process(target=job, args=(1, 2))
    # 启动进程任务
    p1.start()
    # 加入到主线程
    p1.join()

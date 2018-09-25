#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用进程池

进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题.

有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。

Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值。

接下来用map()获取结果，在map()中需要放入函数和需要迭代运算的值，然后它会自动分配给CPU核，返回结果.
"""

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    # 初始化
    # pool = mp.Pool()
    # 可以在初始化的时候, 填入关键字参数processes定义使用几个核.
    pool = mp.Pool(processes=3)

    # bif中的map使用方法相同, pool中的map使用了多进程然后进行了封装
    res = pool.map(job, range(10))

    print(res)

if __name__ == '__main__':
    multicore()
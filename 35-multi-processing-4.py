#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing as mp

"""
Pool除了map()外，还有可以返回结果的方式，那就是apply_async().

apply_async()中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的，
所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
"""

def job(x,y):
    return x * y

def multicore():
    pool = mp.Pool()
    res = pool.apply_async(job, (2,3))
    print(res.get())

    # 用apply_async()输出多个结果
    multi_res = [pool.apply_async(job, (i,i+1)) for i in range(1000)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
强化对async和await的认识
"""


def func():
    """
    普通函数
    :return:
    """
    return 1


def generator():
    """
    生成器函数
    :return:
    """
    count = 0
    while True:
        yield count
        count += 1


async def async_func():
    """
    异步函数(协程)
    :return:
    """
    return 2


async def async_generator():
    """
    异步生成器
    :return: 3
    """
    yield 3


async def await_coroutine():
    """
    使用await挂起当前任务, 去执行await后的异步函数
    :return: None
    """
    result = await async_func()
    print(result)


if __name__ == '__main__':

    # 调用普通函数
    print(func())

    # 调用生成器函数
    gen = generator()
    while True:
        n = next(gen)
        print(n)
        if n >= 10: break

    # 直接调用异步函数不会返回结果，而是返回一个coroutine对象 <coroutine object async_func at 0x109735048>
    result_of_using_directly_async_func = async_func()
    print(result_of_using_directly_async_func)
    # 协程需要通过其他方式来驱动
    try:
        # 因为生成器/协程在正常返回退出时会抛出一个StopIteration异常，而原来的返回值会存放在StopIteration对象的value属性中，通过以下捕获可以获取协程真正的返回值
        result_of_using_directly_async_func.send(None)
    except StopIteration as e:
        print(e.value)


    def run_async_func(corotine):
        """
        拦截StopIteration的函数, 简化异步函数调用
        :param corotine: 异步函数
        :return: 异步函数的返回值
        """
        try:
            corotine.send(None)
        except StopIteration as err:
            return err.value


    print(run_async_func(async_func()))

    # 在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果：
    run_async_func(await_coroutine())

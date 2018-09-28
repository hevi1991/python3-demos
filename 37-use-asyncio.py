#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用异步IO(协程)
"""

import time
import asyncio

now = lambda: time.time()


def define_a_async_job():
    """
    定义一个协程
    :return:
    """

    async def do_some_work(x):
        print('Waiting: ', x)

    start = now()

    # 写成执行的函数
    coroutine = do_some_work(2)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)

    print('TIME: ', now() - start)

    # 通过async关键字定义一个协程（coroutine），协程也是一种对象。协程不能直接运行，需要把协程加入到事件循环（loop），由后者在
    # 适当的时候调用协程。asyncio.get_event_loop方法可以创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，并
    # 启动事件循环。因为本例只有一个协程，于是可以看见输出


def define_a_task_for_async_job():
    """
    创建一个任务
    协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象。
    所谓task对象是Future类的子类。保存了协程运行后的状态，用于未来获取协程的结果。
    :return:
    """

    async def do_some_work(x):
        print('Waiting: ', x)

    start = now()

    coroutine = do_some_work(2)

    loop = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine) # 效果与以下create_task相同, 都是创建asyncio.Future对象
    task = loop.create_task(coroutine)

    print(task)
    loop.run_until_complete(task)
    print(task)
    print('TIME: ', now() - start)

    # 创建task后，task在加入事件循环之前是pending状态，因为do_some_work中没有耗时的阻塞操作，task很快就执行完毕了。后面打印的finished状态。
    # asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task，run_until_complete的参数是一个futrue对象。
    # 当传入一个协程，其内部会自动封装成task，task是Future的子类。isinstance(task, asyncio.Future)将会输出True。


def await_a_ayncio_job():
    """
    阻塞与await
    使用async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权。
    协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行。
    :return:
    """

    async def do_some_work(x):
        print('Waiting: ', x)
        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    start = now()
    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)

    print('Task ret: ', task.result())
    print('TIME: ', now() - start)


def await_some_asyncio_job():
    """
    并发协程
    :return:
    """

    async def do_some_work(x):
        print('Waiting: ', x)
        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    start = now()

    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(do_some_work(i)) for i in range(1, 5)]
    # 执行所有task, 等待所有协程任务结束 If any awaitable in fs is a coroutine, it is automatically scheduled as a Task. Returns two sets of Tasks/Futures: (done, pending).
    print('ddoig')
    task = asyncio.wait(tasks)
    print('enddd')

    loop.run_until_complete(task)
    for t in tasks:
        print('Task ret: ', t.result())
    loop.close()
    print('TIME: ', now() - start)


def await_some_asyncio_job_2():
    """
    协程嵌套
    :return:
    """
    async def do_some_work(x):
        print('Waiting: ', x)
        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    start = now()

    async def main(looop):
        """
        嵌套其他协程
        挂起, 等待多个写成完成.
        :param looop:
        :return:
        """
        tasks = [looop.create_task(do_some_work(i)) for i in range(1, 5)]
        # dones, pendings = await asyncio.wait(tasks)  # 执行所有tasks
        # for task in dones:
        #     print('Task ret: ', task.result)

        results = await asyncio.gather(*tasks)  # 执行所有tasks
        for result in results:
            print('Task ret: ', result)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))# 执行嵌套的协程
    loop.close()
    print('TIME: ', now() - start)


if __name__ == '__main__':
    # 定义一个协程
    # define_a_async_job()

    # 创建一个任务
    # define_a_task_for_async_job()

    # 阻塞和await
    await_some_asyncio_job()
    # await_some_asyncio_job_2()
    pass

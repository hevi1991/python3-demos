#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
多线程
"""

import threading
import time


def thread_job():

    """
    子线程做的活
    :return:
    """
    print('This is a thread of {0} start'.format(threading.current_thread()))
    time.sleep(2)
    print('This is a thread of {0} end'.format(threading.current_thread()))

def main():
    t = threading.Thread(target=thread_job)#定义线程
    t.start()
    # 使用join控制主程序运行
    t.join()

if __name__ == '__main__':
    main()

    print('------')
    print(threading.active_count())
    print(threading.enumerate())
    print('------')
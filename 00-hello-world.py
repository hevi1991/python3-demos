#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' cat a.txt | python3 /Users/Hevi/Playground/python3-demos/00-hello-world.py > b.txt '

import sys

if __name__ == '__main__':
    for line in sys.stdin.readlines():
        print("Hello %s!" % (line.strip()))
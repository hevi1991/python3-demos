#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' 反序列化 '

import os
import pickle

d = {}

if os.path.exists('serialization-1'):
    f = open('serialization-1', 'rb')
    d = pickle.load(f)
    f.close()
    print(d)
else:
    print('先运行 /Users/Hevi/Playground/python3-demos/24-pickling-01.py ')
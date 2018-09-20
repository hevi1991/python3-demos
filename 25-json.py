#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' info, todo '

import json

jsonObj1 = dict(name='Peter', age=19, score=98)
jsonObj2 = dict(name='Anne', age=19, score=92)
jsonObj3 = dict(name='Tom', age=19, score=100)

# object
jsonStr = json.dumps(jsonObj1)
print('obj:',jsonStr)

# array
jsonStr = json.dumps(list((jsonObj1, jsonObj2, jsonObj3)))
print('array:', jsonStr)

# class -> json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return dict(name=std.name, age=std.age, score=std.score)

s = Student('李富贵', 32, 99)
# jsonStr = json.dumps(s, default=student2dict)
# 采用__dict__特殊属性名取出公有变量的字典
jsonStr = json.dumps(s, default=lambda obj: obj.__dict__)
print(jsonStr)

# json -> class
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s1 = json.loads(jsonStr, object_hook=dict2student)
print(s1)
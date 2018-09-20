#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。'

import sys
import os

def findFile(targetDir, name=''):
        currentFileNames = os.listdir(targetDir)
        findList = []
        for filename in currentFileNames:
            filepath = os.path.join(targetDir, filename)
            if os.path.isfile(filepath):
                if filename.find(name) != -1:
                    findList.append(filepath)
            elif os.path.isdir(filepath):
                subTargetPath = os.path.join(targetDir, filename)
                subFindList = findFile(subTargetPath, name)
                for subfile in subFindList:
                    findList.append(subfile)
        return findList

if __name__ == '__main__':

    args = sys.argv

    name = ''
    currentPath = os.path.curdir

    if len(args) > 1:
        name = args[1]
    if len(args) > 2:
        currentPath = args[2]
        
    result = findFile(currentPath, name)
    print("\n".join(result))

    ''' 
    if len(args) < 2:
        print('请在命令后输入需要查找的文件名称!')
    else:
        currentPath = os.path.curdir
        name = args[1]
        result = findFileOutputString(currentPath, name)
        print(result) 
    '''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/6 19:34
# object.__del__ 运用

from os.path import join

class FileObject:
    '''给文件对象进行包装从而确认在删除时文件流已经关闭'''

    def __init__(self,filepath='./',filename='sample.txt'):
        #读写模式打开一个文件
        self.file = open(join(filepath,filename),'r+')
        print(self.file)

    def __del__(self):
        self.file.close()
        del self.file
    # def __eq__(self, other):
    #     pass
    # def __lt__(self, other):
    #     pass
    # def __gt__(self, other):
    #     pass

if __name__ == '__main__':
    FileObject()
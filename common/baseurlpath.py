#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/6 11:12
class Chain(object):
    '''自动拼接URI地址'''
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __call__(self,path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__


if __name__ == '__main__':
    print(Chain().users('michael').repos('hello'))
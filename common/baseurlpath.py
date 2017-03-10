#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/6 11:12
class Chain(object):

    def __init__(self, path=''):
        self._path = path
        print('1')
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
        print('2')
    def __call__(self,path):
        return Chain('%s/%s' % (self._path, path))
        print('3')
    def __str__(self):
        return self._path
        print('4')
    __repr__ = __str__


if __name__ == '__main__':
    print(Chain().users('michael').repos('hello'))
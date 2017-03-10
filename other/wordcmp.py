#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/7 10:23
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b

        if self.a >= 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item,int):
            a,b = 1,1
            for x in range(item):
                a,b = b,a+b
            return a
        elif isinstance(item,slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x > start:
                   L.append(a)
                a,b = b,a+b
            return L
        else:
            raise NotImplementedError
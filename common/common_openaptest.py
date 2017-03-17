#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/17 11:17
'''用于openapi单个接口调试用'''
from common.request2jvv import request2jvv

def openapitest():
    servicename = input('请输入接口名：')
    if servicename == 'exit0':
        exit()
    else:
        param = (input('请输入参数名（a=xx,b=xx）:'))
        paramlist = param.split(',')
        paramdict = {}
        for i in paramlist:
            paramdict[i.split('=')[0]] = i.split('=')[1]
        try:
            r = request2jvv(servicename,paramdict).send()
            print(r)
        except BaseException as e:
            print(e)
        finally:
            openapitest()



if __name__ == '__main__':
    openapitest()
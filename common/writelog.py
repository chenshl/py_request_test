#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/16 9:38
'''日志模块封装'''
import logging
import time,sys

class writelog(object):
    date = time.strftime('%Y-%m-%d')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%Y %b %d %a %H:%M:%S',
                        filename='./report/log/' + date + '.log',
                        filemode='a+'
                        )

    sys.path.append('./interface')

    def writelog(self,level,string,):
        if level == 'debug':
            logging.debug(string)
        else:
            logging.info(string)
    def __init__(self,level,string):
        self.writelog(level,string)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/2/28 15:09

import time,sys
sys.path.append('./interface')
from HTMLTestRunner import HTMLTestRunner
import unittest
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = './report/' +  u'接口测试报告_' + now + '.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'接口测试报告' + now,
                            description=u'''
                            内部接口测试报告结果（仅供参考）,
                            请只查看成功与失败的结果，错误的一般为脚本错误导致执行错误。''')
    runner.run(discover)
    fp.close()
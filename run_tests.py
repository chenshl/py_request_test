#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/2/28 15:09
import logging
import time,sys
date = time.strftime('%Y-%m-%d')
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y %b %d %a %H:%M:%S',
                    filename='./report/log/' + date + '.log',
                    filemode='a'
                    )

sys.path.append('./interface')
logging.info('=================')
logging.info(u'载入环境变量成功')
from HTMLTestRunner import HTMLTestRunner
import unittest
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
logging.info(u'搜寻测试脚本成功')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = './report/' + u'接口测试报告_' + now + '.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'接口测试报告' + now,
                            description=u'''
                            内部接口测试报告结果（仅供参考）,
                            请只查看成功与失败的结果，错误的一般为脚本错误导致执行错误。''')
    logging.info(u'开始执行测试脚本')
    runner.run(discover)
    logging.info(u'执行测试脚本结束')
    fp.close()
    logging.info(u'测试完成')
    logging.info('=================')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/10 10:26
'''使用线程池实现一个多并发请求'''

import time
import threading
import requests

def _get_baidu(url='http://www.baidu.com/'):
    starttime = time.time()
    r = requests.get(url)
    status = r.status_code
    usedtime = time.time()-starttime
    if str(status) == '200':
        print('请求百度首页成功，用时%s' % usedtime)
    else:
        print('请求百度首页失败，用时%s' % usedtime)

pool_num = 100
for i in range(100):
    i = threading.Thread(target=_get_baidu, args=())
    i.start()
    i.join()
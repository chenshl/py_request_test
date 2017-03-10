#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/10 11:28
'''threadlocal 线程全局变量与局部变量的优化使用'''

import threading

# 创建threadlocal对象，该对象是一个全局变量，但里面的子线程只能访问
# 相对应的局部数据
_threadinglocal = threading.local()

def _process_stu():
    std = _threadinglocal.stu
    print('子线程 %s中的stu参数是：%s' % (threading.current_thread().name,std))

def _run_process_thread(name):
    _threadinglocal.stu = name
    _process_stu()


t1 = threading.Thread(target=_run_process_thread,args=('hello1',),name='t1')
t2 = threading.Thread(target=_run_process_thread,args=('hello2',),name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/10 16:04

#服务器端
import random,time,queue
from multiprocessing.managers import BaseManager
task_send_queue = queue.Queue() #发送消息队列
task_rec_queue = queue.Queue() #接收消息队列
class QueueManager(BaseManager):
    pass
server_url = '127.0.0.1'
#注册queue到网络，callable实现关联
QueueManager.register('task_send_queue',callable=task_send_queue)
QueueManager.register('task_rec_queue',callable=task_rec_queue)

manager = QueueManager(address=(server_url,10008),authkey=b'123456')
manager.start()


send_obj = manager.task_send_queue()
rec_obj = manager.task_rec_queue()

for i in range(10):
    send_obj.put(i)
    print('发送消息：%s' % i)
for i in range(len(rec_obj.qsize())):
    r = rec_obj.get(i)
    print('接收消息：%s' % i)

manager.shutdown()
print('服务端结束')
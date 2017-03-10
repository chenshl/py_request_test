#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/10 16:23

import time,sys,queue
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass

server_url = '127.0.0.1'
slave = QueueManager(address=(server_url,10008),authkey=b'123456')
slave.connect()
rec = slave.task_send_queue() #接收队列的消息是服务器发送队列的消息，所以需要颠倒
send = slave.task_rec_queue

for i in range(len(rec.qsize())):
    try:
        r = rec.get(i)
        print('接收的数据：%s' % i)
        send.put(i)
    except queue.Empty:
        print('队列已空')


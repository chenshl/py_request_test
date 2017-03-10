#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/8 15:34

# from multiprocessing import Process,Queue
# import os,time,random
# def write(queue,list):
#     print('写进程开始写入数据：%s' % os.getpid())
#     for vaule in list:
#         print('放入队列：%s' % vaule)
#         queue.put(vaule)
#         time.sleep(random.random())
#
# def read(queue):
#     print('读进程开始读取数据:%s' % os.getpid())
#     while queue != None:
#         vaule = queue.get()
#         print('读出队列：%s' % vaule)
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write,args=(q,[1,2,3,4,5]))
#     pr = Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate() #强制结束进程
#     print('再次打印队列数据：%s' % q.get())


# import time,threading,random
#
# def loop_k(k):
#     print('线程%s开始执行' % threading.current_thread().name)
#     n = 0
#     while n <=k:
#         n += 1
#         print('线程%s开始执行：%s' % (threading.current_thread(),n))
#         time.sleep(random.random()*3)
#     print('线程%s停止' % threading.current_thread().name)
#
# if __name__ == '__main__':
#     print('线程%s开始执行' % threading.current_thread().name)
#     t = threading.Thread(group=None,target=loop_k,args=(5,),name='LoopThread1')
#     t1 = threading.Thread(group=None, target=loop_k, args=(10,), name='LoopThread2')
#     t.start()
#     t1.start()
#     t.join()
#     t1.join()
#     print('线程%s停止' % threading.current_thread().name)

import threading

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        lock.acquire() #获取线程锁
        change_it(n)
        lock.release() #释放线程锁
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
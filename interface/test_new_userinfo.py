#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/15 17:21
import unittest
from common.request2jvv import request2jvv
class new_userinfo(unittest.TestCase):
    '''新加密接口调试'''
    def setUp(self):
        self.service = 'test'
    def tearDown(self):
        pass

    def test_suc_userinfo(self):
        '''正确的请求'''
        self.param = {'userId':'201703010010000000457'}
        self.expt = {'message': '查询用户成功',
     'datas': {'username': 'test001', 'age': 12, 'userId': '20170301001000000001', 'status': 'CHECKING'},
     'orderNo': '39gOef7zIgbZxh177BuSMK', 'detailMessage': '查询用户成功', 'code': '200', 'status': 'success'}
        r = request2jvv(self.service,self.param).send()
        self.assertEqual(r,self.expt)

if __name__ == '__main__':
    new_userinfo().test_suc_userinfo
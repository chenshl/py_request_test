#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/2/28 15:23
import unittest
from common.request2jwwstrict import request2jwwstrict
class ChangePayword(unittest.TestCase):
    '''修改支付密码'''
    def setUp(self):
        self.apiname = '/m/php/shop/forgetPayPasswordPhp'
    def tearDown(self):
        pass


    def test_error_smscode(self):
        '''错误的验证码'''
        self.apiParam = {'userId': '000065bc-bcb2-11e5-b300-d89d672713e0',
                    'Password': 111111,
                    'repeatPayPassword': 543578,
                    'smsCode': 1234}
        self.expect = {'failureReason': '没有重置密码短信发送记录', 'result': '0'}

        r = request2jwwstrict(self.apiname, self.apiParam)
        self.assertEqual(r.send(),self.expect)


    def test_suc_smscode(self):
        '''正确的验证码'''
        self.apiParam = {'userId': '000065bc-bcb2-11e5-b300-d89d672713e0',
                    'Password': 111111,
                    'repeatPayPassword': 543578,
                    'smsCode': 1234}
        self.expect = {'failureReason': '没有重置密码短信发送记录', 'result': '0'}

        r = request2jwwstrict(self.apiname, self.apiParam)
        self.assertEqual(r.send(),self.expect)



if __name__ == '__main__':
    ChangePayword.test_error_smscode()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/2/28 15:23
import unittest
import requests

class Openbaidu(unittest.TestCase):
    '''百度测试'''
    def setUp(self):
        self.url = 'http://www.baidu.com/'

    def tearDown(self):
        pass

    def test_open_baidu(self):
        '''打开百度'''
        payload = {}
        r = requests.get(self.url,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['title'],'百度一下，你就知道')
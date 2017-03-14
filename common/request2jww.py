#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/14 14:32
import requests
class request2jww(object):
    global apiHeader
    apiHeader = 'http://192.168.1.8:9999'
    def __init__(self,apiName='',apiParam = {}):
        self.apiName = apiName
        self.apiParam = apiParam
        self.send()

    def get_fullAPIUrl(self,apiName):
        return apiHeader + apiName

    def send(self):
        self.sortapiParam = self.sortParam()
        # print(self.sortapiParam)
        r = requests.post(self.get_fullAPIUrl(self.apiName),self.sortapiParam)
        if r.status_code == 200:
            self.body = r.json()
            if self.body['result'] == str(1):
                print(self.body)
            else:
                print('请求失败')

    def sortParam(self):
        # sorted(self.apiParam.items())
        # for k,v in self.apiParam.items():
        #     if v is None:
        #         return False
        # return True
        return sorted(self.apiParam.items())

if __name__ == '__main__':
    apiname = '/s/shop/pay/wobi/qry'
    apiParam = {'userId':'000065bc-bcb2-11e5-b300-d89d672713e0'}
    request2jww(apiName=apiname,apiParam=apiParam)
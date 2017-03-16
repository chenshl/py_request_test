#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/14 16:00
from common.interfaceDes import interfaceDes
from common.request2jww import request2jww as baserequest
import hashlib,requests,json

class request2jwwstrict(baserequest):
    global key2,desKey,ivArray
    key2 = '23be21a033d59833d3d87426a869e5ec'
    desKey = '4bbd85de'
    ivArray = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]

    def send(self):
        self.sortapiParam = self.sortParam()
        self.sortPriParam = self.getPriParam()
        r = requests.post(self.get_fullAPIUrl(self.apiName), self.sortPriParam)
        if r.status_code == 200:
            self.body = r.json()
            # if self.body['result'] == str(1):
            #     print(self.body)
            # else:
            #     print('请求返回失败')
            #     print(self.body)
        print(self.body)
        return self.body


    def getPriParam(self):
        interfaceDestest = interfaceDes(desKey,ivArray)
        self.str = ''
        for i in self.sortapiParam:
            self.str += str(i[1])
        m = hashlib.md5()
        m.update(key2.encode('utf-8')+self.str.encode('utf-8'))
        sign = m.hexdigest()
        names = interfaceDestest.get_encrypt_data(json.JSONEncoder().encode(self.apiParam))
        return dict(sign=sign,names=names)

if __name__ == '__main__':
    apiname = '/m/php/shop/forgetPayPasswordPhp'
    apiParam = {'userId':'000065bc-bcb2-11e5-b300-d89d672713e0',
                'Password':111111,
                'repeatPayPassword':543578,
                'smsCode':1234}

    request2jwwstrict(apiName=apiname, apiParam=apiParam).send()
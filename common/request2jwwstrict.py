#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/14 16:00
import common.interfaceDes
import common.request2jww
import hashlib,requests,json

class request2jwwstrict(common.request2jww):
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
            if self.body['result'] == str(1):
                print(self.body)
            else:
                print('请求失败')


    def getPriParam(self):
        interfaceDestest = common.interfaceDes(desKey,ivArray)
        for i in self.sortapiParam.items():
            self.str += i
        m = hashlib.md5()
        m.update(key2+self.str)
        sign = m.hexdigest()
        names = interfaceDestest.get_encrypt_data(json.JSONEncoder().encode(self.apiParam))
        return dict(sign=sign,names=names)

if __name__ == '__main__':
    apiname = '/m/getUserInfo'
    apiParam = {'userId':'000065bc-bcb2-11e5-b300-d89d672713e0'}
    request2jwwstrict(apiName=apiname,apiParam=apiParam)
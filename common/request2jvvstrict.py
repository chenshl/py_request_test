#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/13 16:50
import common.interfaceDes
import common.request2jvv
import json,requests
import hashlib
class request2jvvstrict(common.request2jvv):
    key2 = '23be21a033d59833d3d87426a869e5ec'
    desKey = '4bbd85de'
    ivArray = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]
    API_MAP = {
    'callBackSyncNotice':'/m/isPhpUserSuc',
    'getLiveRoomsByStatus':'/m/live/getLiveRoomsByStatus',
    'editLive':'/m/live/closeLive',
    'getCourseware':'/m/live/getCourseware',
    'delCourseware':'/m/live/delCoursewareImg',
    'updateCourseware':'/m/live/updateCourseware',
    'addRoom':'/m/live/addRoom',
    'getUserByUsername':'/m/live/getUserByUsername',
    'modifierRoom':'/m/live/modifierRoom',
    'phpOpenLive':'/m/live/phpOpenLive',
    'getRoomByRoomId':'/m/live/getRoomByRoomId',
    'deleteRoom':'/m/live/deleteRoom',
    'upRoom':'/m/live/upRoom'
    }
    global key2,desKey,ivArray,API_MAP
    def send(self):
        if self.checkApiIsReg():
            self.sortParam()
            self.apiParam = self.getPriParam()
            r = requests.post(self.getFullApi(),self.apiParam)
            self.bodyArr = json.dump(r.content)
            if isinstance(self.bodyArr,dict):
                body = self.bodyArr
            else:
                return False

    def getPriParam(self):
        interfaceDestest = common.interfaceDes(desKey,ivArray)
        for i in super.apiParam.items():
            self.str +=i

        m = hashlib.md5()
        m.update(key2+self.str)
        sign = m.hexdigest()
        names = interfaceDestest.get_encrypt_data(json.JSONEncoder().encode(self.apiParam))
        return dict(sign=sign,names=names)

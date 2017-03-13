#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/13 15:29
import requests
import json
class request2jvv(object):

    apiHeader = '192.168.1.8:9999'

    API_MAP = {
    'uploadCourseware':'/m/live/uploadCourseware',
    'updateCourseware':'/m/live/updateCourseware',
    'addRoomImg':'/m/live/addRoomImg',
    'addRoom':'/m/live/addRoom',
    }

    http = None
    apiName = ''
    apiParam = {}
    body = ''
    bodyArr = {}
    token = ''

    global apiHeader,API_MAP,apiParam,bodyArr,body

    def __init__(self,name = '',param = {}):
        self.apiName = name
        self.apiParam = param
        if self.apiName != '' and self.apiParam !='':
            self.send()
            if ('login' == self.apiName):
                if self.getStatus():
                    self.token = self.bodyArr['token']

    def setApiName(self,name):
        self.apiName = name

    def setApiParam(self,param):
        self.apiParam = param

    def setApiHeader(self,url):
        self.apiHeader = url

    def send(self):
        if self.checkApiIsReg():
            self.sortParam()
            r = requests.post(self.getFullApi(),self.apiParam)
            self.bodyArr = json.dump(r.content)
            if isinstance(self.bodyArr,dict):
                body = self.bodyArr
            else:
                return False

    def checkApiIsReg(self,apiName = ''):
        api = apiName if True else self.apiName
        if api in API_MAP.keys():
            return True
        return False

    def sortParam(self):
        sorted(self.apiParam)
        for k,v in apiParam.items():
            if v is None:
                return False
        return True

    def getFullApi(self):
        return apiHeader+API_MAP[self.apiName]

    def gethostUrl(self):
        return apiHeader

    def getStatus(self):
        return bodyArr['result']

    def getToken(self):
        if ('login' == self.apiName):
            return self.token

    def getBody(self):
        return body
    def getBodyArr(self):
        return bodyArr
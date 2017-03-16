#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : mjc
# @Time    : 2017/3/16 15:41
'''excel读取器'''

import xlrd,xlwt
from xlutils.copy import copy
import os
testcasedir = '../interface/excelcase/'
global filename
filename = testcasedir + os.listdir(testcasedir)[0]

class excelreader(object):

    def __init__(self,path):
        self.book = xlrd.open_workbook(path)

    def reader(self):
        sh = self.book.sheet_by_index(0)
        list = []
        for i in range(1,sh.nrows):
            list.append(sh.row_values(i))
        print(list)
        return list

    def writer(self):
        wb = copy(self.book)
        s = wb.get_sheet(0)
        s.write(1,9,'PASS')
        s.save('test_excelcasedemo.xls')
        # todo:reader 方法完成




if __name__ == '__main__':
    excelreader('../interface/excelcase/test_excelcasedemo.xls').reader()
    #excelreader('../interface/excelcase/test_excelcasedemo.xls').writer()
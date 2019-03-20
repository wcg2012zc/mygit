#!/usr/bin/python
#encoding:utf-8

import HTMLTestRunner
import time
import os


class CreateTestReport(object):
    def CreateTestReport(self,Title,revDescr,revSuit):
        FileName = time.strftime("%Y%m%d%H%M%S")
        if not os.path.exists(r"D:\Ncme_Test_Report"):
            os.makedirs(r"E:\Ncme_Test_Report")
        htmlFileName = "../TestReport/TestReport" + FileName + '.html'
        with open(htmlFileName,'wb') as htmlstream:
            HTMLTestRunner.HTMLTestRunner(
                stream=htmlstream,
                verbosity=2,
                title=Title,
                description=revDescr
            ).run(revSuit)
        htmlstream.close()
#!/usr/bin/python
# encoding:utf-8

import unittest
import ctypes
from Utils.screenshot import screenshot
from TestCaseLayout import Back_stage
from TestCaseLayout import loginTestCase
from TestCaseLayout import Prontpage
from Utils.CreateTestReport import CreateTestReport


# 执行简单的用例
# class RegisterSuit(unittest.TestCase):
#     def RegisterSuit(self):
#         RegisterSuit = unittest.TestSuite()
#         RegisterSuit.addTest(RegisterTestcase('test_0001'))
#         RegisterSuit.addTest(RegisterTestcase('test_0002'))
#         RegisterSuit.addTest(RegisterTestcase('test_0003'))
#         RegisterSuit.addTest(RegisterTestcase('test_0004'))
#         RegisterSuit.addTest(RegisterTestcase('test_0005'))
#         #reportFileName = "RegisterTestReport"
#         RegisterTestReportTitle = "NCMEQiantaiAutoTestReport"
#         Description = "NCME前台测试用例执行情况"
#         CreateTestReport().CreateTestReport(RegisterTestReportTitle,Description,RegisterSuit)
#         #user = ctypes.windll.LoadLibrary("user32.dll")
#         #user.MessageBoxW(None, 'Par', '提示信息', 0)
#
# if __name__ == '__main__':
#     RegisterSuit().RegisterSuit()

# # 执行多个用例
# class RegisterSuit(unittest.TestCase):
#     def RegisterSuit(self):
#         RegisterSuit = unittest.TestSuite()
#         Testlist = ['test_0001', 'test_0002', 'test_0003', 'test_0004',  'test_0006', 'test_0007',
#                     'test_0008', 'test_0009', 'test_0010', 'test_0011', 'test_0012', 'test_0013', 'test_0014',
#                     'test_0015', 'test_0016', 'test_0017', 'test_0018', 'test_0019', 'test_0020', 'test_0021',
#                     'test_0022', 'test_0023', 'test_0024', 'test_0025', 'test_0026', 'test_0027', 'test_0028',
#                     'test_0029', 'test_0030', 'test_0031', 'test_0032', 'test_0033', 'test_0036', 'test_0037',
#                     'test_0038', ]
#         # 按列表顺数将用例添加至测试套件
#         for i in Testlist:
#             RegisterSuit.addTest(Back_stage.Back_stageTestcase(i))   #此处添加要执行的用例包名
#         print(RegisterSuit)
#         RegisterTestReportTitle = "NCMEQiantaiAutoTestReport"
#         Description = "NCME前台测试用例执行情况"
#         CreateTestReport().CreateTestReport(RegisterTestReportTitle,Description,RegisterSuit)

#
# if __name__ == '__main__':
#     RegisterSuit().RegisterSuit()


# 执行多个模块的用例
class RegisterSuit(unittest.TestCase):
    def RegisterSuit(self):
        RegisterSuit = unittest.TestSuite()
        # 将整套用例添加到测试套里
        RegisterSuit.addTests(unittest.makeSuite(Prontpage.Testcase))
        RegisterSuit.addTests(unittest.makeSuite(Back_stage.Back_stageTestcase))
        RegisterSuit.addTests(unittest.makeSuite(loginTestCase.RegisterTestcase))
        print(RegisterSuit)
        RegisterTestReportTitle = "NCMEQiantaiAutoTestReport"
        Description = "NCME前台测试用例执行情况"
        screenshot().screenshot()
        CreateTestReport().CreateTestReport(RegisterTestReportTitle, Description, RegisterSuit)


if __name__ == '__main__':
    RegisterSuit().RegisterSuit()

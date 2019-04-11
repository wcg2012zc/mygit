#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/9 9:56
# 文件     ：Test_Suite.py
# IDE      : PyCharm

# coding=utf-8
"""
Project:编写Web测试用例
"""
import unittest
import os
# from test_baidu import test_baidu
# from test_baidu import test_youdao
"""
构造测试集
方法1：执行整套用例集 unittest discover
"""
base_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]#获取需要执行用例集的路径
test_case_dir = os.path.join(base_dir,"test_baidu")#批量执行测试用例集
suite = unittest.TestSuite()
de = unittest.defaultTestLoader.discover(test_case_dir,pattern="test*.py",top_level_dir=None)
#print(test_case_dir)打印当前路径
"""方法2:执行单个或多个用例
"""
#suite.addTest(baidu.BaiduTest('test_case1')) #执行单个测试用例或多个
#suite.addTest(youdao.YoudaoTest('test_youdao'))#执行单个测试用例或多个

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(de)
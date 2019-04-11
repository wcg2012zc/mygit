#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/9 9:52
# 文件     ：youdao.py
# IDE      : PyCharm
"""
Project:使用有道翻译测试用例
"""
from selenium import webdriver
import unittest, time


class YoudaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "http://www.youdao.com" # 有道的url地址

    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u"你好，北京")
        driver.find_element_by_id("translateContent").submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
#!usr/bin/env python
#-*- coding:utf-8 _*-
# 作者     ：zhangchen
# 创建时间 ：2019/4/9 9:51
# 文件     ：baidu.py
# IDE      : PyCharm
# coding=utf-8
"""
Project:登录百度测试用例
"""
from selenium import webdriver
import unittest, time


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.taobao.com/"# url地址

    def test_case1(self):# 测试用例
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("冰裂茶具"),time.sleep(5)
        print("搜索成功")
        driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
        time.sleep(3)
        self.driver.quit()
    def test_case2(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("戴森吸尘器"),time.sleep(5)
        print("搜索成功")
        driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
        time.sleep(3)



def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()
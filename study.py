# coding=utf-8
# @Time    : 2018/12/28 13:12
# @Author  : ZC
# @Email   :13426230241@163.com
# @File    :test_001.py
# @Software:PyCharm
#导入unittest包
import unittest
#延时操作
from time import sleep
#下拉框选择select包导入
from selenium.webdriver.support.select import Select
#导入驱动
from selenium import webdriver
#鼠标悬停导入
from selenium.webdriver import ActionChains
#继承测试用例的类
class TestLogin (unittest.TestCase):
    #初始化操作
    def setUp(self):
        #驱动浏览器
        self.driver = webdriver.Chrome()
        url = "http://dev.ncme.org.cn/qiantai/"
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        print("开始用例执行")
    #前台登录学习项目
    def test_001(self):
        driver = self.driver
        driver.find_element_by_class_name("login_btn").click()
        driver.find_element_by_id("userdata").send_keys("13426230241")
        driver.find_element_by_id("password").send_keys("Zc123456")
        driver.find_element_by_id("yzmInput").send_keys("195753")
        driver.find_element_by_id("submit_btn") .click().sleep(1)
        driver.find_element_by_xpath("//*[@id='mooke']/ul/li[3]/div/h2").click().sleep(2)
        driver.find_element_by_name("study_begin").click().sleep(4)
        driver.find_element_by_class_name("go_back").click()
        hover_element = driver.find_element_by_css_selector("#hide > a.login_link")
        ActionChains(driver).move_to_element(hover_element).perform().sleep(3)
        driver.find_element_by_link_text("我的学习").click().sleep(3)
        driver.find_element_by_link_text( "学习报告").click()
        Select(driver.find_element_by_id( "year" ) ).select_by_value( "2019" ).sleep(2)
        Select(driver.find_element_by_id( "month" ) ).select_by_value( "2" ).sleep(2)
        js = "var q=document.documentElement.scrollTop=500"
        driver.execute_script(js)
    #结束测试
    def tearDown(self):
        sleep(3)
        self.driver.close()
        print("执行结束")

    #程序的入口
if __name__ == '__main__':
    #调用所有test方法
    unittest.main()



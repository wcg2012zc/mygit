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
#导入驱动
from selenium import webdriver
#继承测试用例的类
from selenium.webdriver.support.select import Select
class TestLogin (unittest.TestCase):
    #初始化操作
    def setUp(self):
        #驱动浏览器
        self.driver = webdriver.Chrome()
        url = "http://dev.ncme.org.cn/qiantai/"
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        print("setup")
    #测试用例：注册账号
    def test_001(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='fm1']/div/div[1]/div[1]/div/div/a[2]").click()
        sleep(2) #等待2秒给页面一个反应时间
        #填写相关注册信息
        Select(driver.find_element_by_id("certificate_type")).select_by_value("1")
        driver.find_element_by_id("certificate_no").send_keys("110101199110076857")
        driver.find_element_by_id("real_name").send_keys("菠萝包")
        Select(driver.find_element_by_id("region1")).select_by_value("111000001")
        Select(driver.find_element_by_id("region2")).select_by_value("111000032")
        Select(driver.find_element_by_id("rspropid")).select_by_value("111000379")
        driver.find_element_by_id("tt").send_keys("北京市顺义区高丽营镇张喜庄村第二卫生室")
        Select(driver.find_element_by_id("work_type")).select_by_value("1")
        Select(driver.find_element_by_id("work_unit")).select_by_value("610010659")
        Select(driver.find_element_by_id("xueke1")).select_by_value("510001")
        Select(driver.find_element_by_id("xueke2")).select_by_value("510002")
        Select(driver.find_element_by_id("xueke3")).select_by_value("510011")
        sleep(1)#等待下一步按钮亮起
        driver.find_element_by_id("tab_btn1").click()
    #结束测试
    def tearDown(self):
        sleep(3)
        self.driver.close()
        print("teardown")
    #程序的入口
if __name__ == '__main__':
    #调用所有test方法
    unittest.main()



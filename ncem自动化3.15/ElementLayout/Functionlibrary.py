import unittest, time, sys
from Utils.DriverHandle import DriverHandle
from Utils.readxmlData import xmlfile
from ElementLayout.Basiclibrary import Basic,Assertions
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support import expected_conditions as EC




class Function(unittest.TestCase):
    def __init__(self):
        self.dr = DriverHandle().driver
    def login_HT(self, username, password):
        Basic().inputtext_id('username', username)
        Basic().inputtext_id('password', password)
        code = Basic().getvalue_id('yzmCode', 'value')
        Basic().inputtext_id('yzmInput', code)
        Basic().clickelement_xpath('/html/body/div[5]/form/div/a')
        Basic().wait_xpath(30000, '/html/body/div[2]/div[2]')
        Assertions().assertEqual_xpath('培训后台', '/html/body/div[2]/div[2]')
# 后台退出
    def exit_HT(self,):
        # 退出系统
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[3]/p/span')
        Basic().clickelement_link_text('退出系统')
        Basic().wait_xpath(300, '/html/body/div[2]/div/a[2]')
        Assertions().assertEqual_xpath('教学管理', '/html/body/div[2]/div/a[2]')
# 前台登录
    def login_QT(self,username, password):
        Basic().clickelement_class('login_btn')
        Basic().inputtext_id('userdata', username)
        Basic().inputtext_id('password', password)
        code = Basic().getvalue_id('yzmCode', 'value')
        Basic().inputtext_id('yzmInput', code)
        Basic().clickelement_id('submit_btn')
        Basic().wait_class(30000, 'login_link')
        Assertions().assertEqual_class('个人中心', 'login_link')
# 前台退出
    def exit_QT(self):
        Basic().ActionChains_class('login_link')
        Basic().clickelement_link_text('安全退出')
        Basic().wait_class(30000, 'login_btn')
        Assertions().assertEqual_class('登录', 'login_btn')

# 获取网页上的警告信息
    def alert(self):
        if EC.alert_is_present:
            print("Alert exists")
            alert = DriverHandle().driver.switch_to_alert()
            print(alert.text)
            alert.accept()
        else:
            print("NO alert exists")

# 跳转到首页的操作
    def homepage_xpath(self):
        try:
            a = self.dr.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/ul/li[1]/a').click()
            return a
        except Exception as e:
            print(e, '返回首页操作失败')
    def homepage_text(self):
        try:
            a = self.dr.find_element_by_link_text('首页').click()
            return a
        except Exception as e:
            print(e, '返回首页操作失败')
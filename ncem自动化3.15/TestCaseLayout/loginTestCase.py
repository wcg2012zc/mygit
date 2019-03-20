#!/usr/bin/python
# encoding:utf-8
import unittest,time
from Utils.DriverHandle import DriverHandle
from Utils.readxmlData import xmlfile
from ElementLayout.Basiclibrary import Basic,Assertions
from ElementLayout.Functionlibrary import Function
from selenium.webdriver.common.action_chains import *
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dr = DriverHandle().driver
        self.dr.get(xmlfile().logindata("url", 0))
        self.dr.implicitly_wait(30)
        self.dr.maximize_window()

    def setUp(self):
        time.sleep(2)

    def test_0001(self):
        for cyclenumber in range(xmlfile().len("username")):
            aa = xmlfile().setupcourse("username", cyclenumber)
            print(xmlfile().logindata("username", cyclenumber))
            Function().login_HT(xmlfile().logindata("username", cyclenumber), xmlfile().logindata("password", cyclenumber))
            Function().exit_HT()

    # 创建课程
    def test_0002(self):
        for cyclenumber in range(xmlfile().len("coursetype")):
            aa = xmlfile().setupcourse("coursetype", cyclenumber)
            print(".......")
            if (aa == "点播"):
                print("......db.")
                # self.dr.delete_all_cookies()
                # print(loginElement().usrName())
                print(xmlfile().logindata("username", 0))
                Function().login_HT(xmlfile().logindata("username", 0), xmlfile().logindata("password", 0))
                # 项目管理
                Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[2]')
                Basic().clickelement_id('2-6')
                Basic().wait_xpath(500, '/html/body/div[5]/div/div[1]/a')
                # 点击课程管理
                Basic().clickelement_xpath('/html/body/div[5]/div/div[1]/a')
                # 输入课程名称
                Basic().inputtext_id('name', xmlfile().setupcourse("coursename", cyclenumber))
                # 选择学科
                Basic().clickelement_id('propNames01')
                Basic().clickelement_id('510001')
                # 课程标签—名师课程
                Basic().clickelement_id('510002')
                # 选择精神卫生学
                Basic().clickelement_xpath('/html/body/div[1]/div/div[3]/ul/span/li[7]/div[1]/input')
                Basic().clickelement_link_text('确定')
                Basic().clickelement_xpath('/html/body/div[2]/div[1]/form/div/div[4]/p/span[2]/input[3]')
                # 选择授课教师
                Basic().clickelement_id('teacher')
                time.sleep(2)
                Basic().inputtext_id('searchInput', xmlfile().setupcourse("surname", cyclenumber))
                # 选择张玲
                Basic().clickelement_xpath('/html/body/div[5]/div[2]/div/div[3]/input[1]')
                Basic().clickelement_link_text('添加')
                Basic().clickelement_link_text('确定')
                # 输入课程简介
                Basic().inputtext_id('introduction', xmlfile().setupcourse("courseinstr", cyclenumber))
                # 选择课程封面
                Basic().inputtext_id('matFile', xmlfile().setupcourse("coursepic", cyclenumber))
                # 点击下一步
                Basic().clickelement_xpath('/html/body/div[2]/div[1]/form/div/p[9]/a')
                # Basic().clickelement_link_text('下一步')
                time.sleep(3)
                self.dr.implicitly_wait(120)
                # 添加课程单元
                Basic().wait_link_text(60000, '添加单元')
                Basic().clickelement_link_text('添加单元')
                Basic().inputtext_id('unitName', xmlfile().setupcourse("unitname", cyclenumber))
                # 勾选任务点
                Basic().clickelement_id('point')
                Basic().clickelement_name('btn_confirm')
                time.sleep(3)
                # 点击编辑
                Basic().wait_xpath(6000, '/html/body/div[2]/div[2]/div[2]/span[7]/a')
                Basic().clickelement_xpath('/html/body/div[2]/div[2]/div[2]/span[7]/a')
                time.sleep(3)
                Basic().Switch(1)
                Basic().clickelement_id('tree_2_span')
                # 点击选择视频
                Basic().clickelement_xpath('/html/body/div[3]/div[3]/div/div[1]/div[1]/div/div/div[61]/div/div/div/div[1]')
                time.sleep(3)
                # 切入iframe的操作
                Basic().iframe_id('edui161_iframe')
                time.sleep(2)
                # 输入视频名称
                Basic().inputtext_name('name', xmlfile().setupcourse("videoname", cyclenumber))
                Basic().clickelement_link_text('查询')
                Basic().clickelement_link_text('选择')
                time.sleep(3)
                # 切入iframe的操作（填写视频时长）
                Basic().iframe(Basic().id('vedio_num'))    #此处特殊，这样写才能过
                Basic().cleartextbox_id('vedio_num')
                Basic().inputtext_id('vedio_num', xmlfile().setupcourse("progress", cyclenumber))
                time.sleep(2)
                Basic().clickelement_link_text('确认')
                Basic().clickelement_link_text('保存')
                time.sleep(3)
                # 获取网页上的警告信息
                Function().alert()
                time.sleep(2)
                Basic().Switch(0)
                Basic().clickelement_link_text('保存')
                time.sleep(2)
                # 获取网页上的警告信息
                Function().alert()
                time.sleep(5)
                Function().exit_HT()

            elif (aa == "面授"):
                print(".......ms")
                Function().login_HT(xmlfile().logindata("username", 0), xmlfile().logindata("password", 0))
                Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[2]')
                Basic().clickelement_id('2-6')
                Basic().wait_xpath(200, '/html/body/div[5]/div/div[1]/a')
                # 点击课程管理
                Basic().clickelement_xpath('/html/body/div[5]/div/div[1]/a')
                # 输入课程名称
                Basic().inputtext_id('name', xmlfile().setupcourse("coursename", cyclenumber))
                # 选择授课形式-面授
                Basic().clickelement_class('position01')
                Basic().clickelement_xpath('/html/body/div[2]/div[1]/form/div/div[1]/div/ul/li[2]')
                # 选择学科
                Basic().clickelement_id('propNames01')
                Basic().clickelement_id('510001')
                Basic().clickelement_id('510002')
                # 选择精神卫生学
                Basic().clickelement_xpath('/html/body/div[1]/div/div[3]/ul/span/li[7]/div[1]/input')
                Basic().clickelement_link_text('确定')
                # 课程标签—理论
                Basic().clickelement_xpath('/html/body/div[2]/div[1]/form/div/div[5]/p[1]/span[2]/input[1]')
                # 选择授课教师
                Basic().clickelement_id('teacher')
                time.sleep(2)
                Basic().inputtext_id('searchInput', xmlfile().setupcourse("surname", cyclenumber))
                # 选择张玲
                Basic().clickelement_xpath('/html/body/div[5]/div[2]/div/div[3]/input[1]')
                Basic().clickelement_link_text('添加')
                Basic().clickelement_link_text('确定')
                # 输入课程简介
                Basic().inputtext_id('introduction', xmlfile().setupcourse("courseinstr", cyclenumber))
                # 选择课程封面
                Basic().inputtext_id('matFile', xmlfile().setupcourse("coursepic", cyclenumber))
                # 点击保存
                Basic().clickelement_link_text('保存')
                # self.dr.implicitly_wait(120)
                time.sleep(40)
                # 获取网页上的警告信息
                Function().alert()
                time.sleep(5)
                # 退出
                Function().exit_HT()
    # 创建项目
    def test_0003(self):
        Function().login_HT(xmlfile().logindata("username", 0),xmlfile().logindata("password", 0))
        time.sleep(3)
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[2]')
        Basic().clickelement_id('2-3')
        Basic().wait_link_text(100,'创建项目')
        # 点击课程管理
        Basic().clickelement_link_text('创建项目')
        Basic().inputtext_id('name', '测试项目')
        # 选择授课形式-远程
        Basic().clickelement_id('lessonType')
        Basic().select_id_value('lessonType', '1')
        time.sleep(1)
        #选择人物画像
        Basic().clickelement_id('renWuImage')
        Basic().clickelement_xpath('/html/body/div[7]/div[2]/div[1]/div[4]/div/b')
        Basic().clickelement_xpath('/html/body/div[7]/div[2]/div[1]/div[4]/ul/li[1]')
        # 选择学科
        Basic().clickelement_id('propNames01')
        Basic().clickelement_id('510001')
        Basic().clickelement_id('510002')
        # 选择精神卫生学
        Basic().clickelement_xpath('/html/body/div[1]/div/div[3]/ul/span/li[7]/div[1]/input')
        Basic().clickelement_link_text('确定')
        # 选择人物画像
        Basic().clickelement_xpath('//*[@id="chk_ui"]')
        Basic().clickelement_link_text('添加')
        # 点击确定
        Basic().clickelement_xpath('/html/body/div[7]/div[2]/div[2]/a[1]')
        # 选择项目负责人
        time.sleep(1)
        Basic().clickelement_id('1')
        Basic().inputtext_id('teacher', '张')
        Basic().clickelement_id('chk_teacher_110022')
        Basic().clickelement_link_text('添加')
        Basic().clickelement_link_text('确定')
        # 选择项目机构
        Basic().clickelement_id('xiangmuOrg')
        Basic().inputtext_id('orgSearch', '中国继续医学教育网')
        time.sleep(2)
        Basic().clickelement_id('chk_teacher_210')
        Basic().clickelement_link_text('添加')
        Basic().clickelement_link_text('确定')
        # 简介
        Basic().inputtext_id('introduction', '项目简介项目简介项目简介')
        # 选择封面
        Basic().inputtext_id('matFile', 'D:\\aaa.jpg')
        Basic().clickelement_id('aid')
        #time.sleep(3)
        Basic().wait_link_text(10000, '添加课程')
        Basic().clickelement_link_text('添加课程')
        # 切换窗口
        Basic().Switch(1)
        time.sleep(2)
        # 克隆
        Basic().clickelement_xpath('/html/body/div[6]/div/table/tbody/tr[1]/td[11]/button')
        Basic().Switch(0)
        time.sleep(2)
        Basic().clickelement_link_text('提交审核')
        time.sleep(3)
        # 获取网页上的警告信息
        Function().alert()
        time.sleep(10)
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[3]/p/span')
        Basic().clickelement_link_text('退出系统')

    # 项目审核
    def test_0004(self):
        for cyclenumber in range(xmlfile().len("user")):
            aa = xmlfile().logindata("user", cyclenumber)
            print(aa)
            Function().login_HT(xmlfile().logindata("user", cyclenumber), xmlfile().logindata("password", cyclenumber))
            time.sleep(1)
            Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li')
            Basic().clickelement_id('1-1')
            Basic().wait_xpath(600, '/html/body/div[2]/div/form/p[3]/input')
            Basic().inputtext_xpath('/html/body/div[2]/div/form/p[3]/input', '测试项目')
            Basic().clickelement_link_text('查询')
            # 点击项目图片
            Basic().wait_xpath(600, '/html/body/div[4]/div/div[1]/div[1]/a/div[1]')
            Basic().clickelement_xpath('/html/body/div[4]/div/div[1]/div[1]/a/div[1]')
            Basic().wait_link_text(10, '下一步')
            Basic().clickelement_link_text('下一步')
            time.sleep(1)
            Basic().clickelement_link_text('下一步')
            time.sleep(3)
            Basic().clickelement_link_text('审核通过')
            time.sleep(1)
            # 点击确定
            Basic().clickelement_xpath('/html/body/div[4]/div[5]/div/div[2]/div[1]/p[2]/input[1]')
            # 再次确定
            Basic().clickelement_xpath('/html/body/div[9]/div[2]/a[1]')
            # 获取网页上的警告信息
            Function().alert()
            time.sleep(10)
            # Basic().wait_xpath(600, '/html/body/span/div[1]/div[1]/div[3]/p/span')
            Function().exit_HT()

    # 项目授权
    def test_0005(self):
        Function().login_HT(xmlfile().logindata("username", 0), xmlfile().logindata("password", 0))
        time.sleep(2)
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[2]')
        time.sleep(1)
        Basic().clickelement_id('2-5')
        Basic().inputtext_id('name', "测试项目")
        Basic().clickelement_link_text('查询')
        Basic().clickelement_xpath('/html/body/div[4]/div/table/tbody/tr[1]/td[11]/a[2]')
        # 授权站点
        Basic().clickelement_class('auth_site')
        Basic().clickelement_id('auth_site_list_1')
        Basic().clickelement_class('layui-layer-btn0')
        # 授权区域
        Basic().clickelement_id('propNames01')
        Basic().clickelement_xpath('/html/body/div[1]/div/div[3]/ul/span/li[4]/div[1]/input')
        Basic().clickelement_xpath('/html/body/div[1]/div/div[3]/div[1]/div[6]/a')
        # 项目学分
        Basic().clickelement_id('level')
        Basic().clickelement_xpath('/html/body/div[2]/form/div/div[1]/div[3]/p[2]/select/option[7]')
        # 时间
        Basic().clickelement_id('start_date')
        Basic().cleartextbox_id('end_date')
        Basic().inputtext_id('end_date', '2020-01-01')
        Basic().inputtext_id('break_days', '2')
        Basic().clickelement_xpath('//*[@id="item_9913799_start"]')
        self.dr.find_element_by_id('item_9913799_end').clear()
        self.dr.find_element_by_id('item_9913799_end').send_keys('2019-12-12')
        # Basic().cleartextbox_xpath('//*[@id="item_9913791_end"]')
        # Basic().inputtext_xpath('//*[@id="item_9913791_end"]', '2019-12-12')
        # 保存
        Basic().clickelement_xpath('/html/body/div[2]/form/div/div[1]/p[9]/a')
        time.sleep(3)
        # 退出
        Function().exit_HT()

    # 项目发布
    def test_0006(self):
        Function().login_HT(xmlfile().logindata("username", 0),  xmlfile().logindata("password", 0))
        time.sleep(2)
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[2]')
        time.sleep(1)
        Basic().clickelement_id('2-7')
        Basic().inputtext_id('name', "测试项目")
        # 查询
        Basic().clickelement_xpath('/html/body/form[2]/div/div/p[11]/a')
        # 发布
        Basic().clickelement_xpath('/html/body/div[4]/div/table/tbody/tr/td[12]/a[3]')
        time.sleep(3)
        # 获取网页上的警告信息
        Function().alert()
        time.sleep(2)
        # 获取网页上的警告信息
        Function().alert()
        time.sleep(5)
        # 退出登录
        Function().exit_HT()

    def tearDown(self):
        # self.dr.quit()
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.dr.quit()
        pass

if __name__ == '__main__':
    unittest.main()
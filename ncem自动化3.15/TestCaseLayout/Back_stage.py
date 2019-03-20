import unittest, time, sys
from Utils.DriverHandle import DriverHandle
from Utils.readxmlData import xmlfile
from Utils.screenshot import screenshot
from ElementLayout.Basiclibrary import Basic,Assertions
from ElementLayout.Functionlibrary import Function
from selenium.webdriver.common.action_chains import *


class Back_stageTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = DriverHandle().driver
        cls.dr.get(xmlfile().logindata("url", 0))
        cls.dr.implicitly_wait(30)
        cls.dr.maximize_window()

    def setUp(self):
        time.sleep(3)

    # 导航栏验证
    def test_0001(self):
        Function().login_HT('admin', '123456')
        time.sleep(2)
        Assertions().assertEqual_xpath('系统管理员', '/html/body/span/div[1]/div[1]/div[3]/p/span')
        Assertions().assertEqual_xpath('能力管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[1]')
        Assertions().assertEqual_xpath('项目管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[2]')
        Assertions().assertEqual_xpath('培训管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[3]')
        Assertions().assertEqual_xpath('考试管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[4]')
        Assertions().assertEqual_xpath('学习卡管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[5]')
        Assertions().assertEqual_xpath('客户管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[6]')
        Assertions().assertEqual_xpath('订单管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[7]')
        Assertions().assertEqual_xpath('内容管理', '/html/body/span/div[1]/div[1]/div[2]/ul/li[8]')
        Assertions().assertEqual_xpath('系统维护', '/html/body/span/div[1]/div[1]/div[2]/ul/li[9]')
        Assertions().assertEqual_xpath('数据统计', '/html/body/span/div[1]/div[1]/div[2]/ul/li[10]')
        Function().exit_HT()
    # 能力管理页验证
    def test_0002(self):
        # 人物画像
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[1]')
        Basic().clickelement_id('1-1')
        Assertions().assertEqual_xpath('人物类型：', '/html/body/div[2]/form/div/p[1]/span')
    def test_0003(self):
        # 能力模型
        Basic().clickelement_id('1-2')
        Assertions().assertEqual_xpath('能力模型类型：', '/html/body/div[2]/div/form/p/span')
    def test_0004(self):
        # 学习地图
        Basic().clickelement_id('1-3')
        Assertions().assertEqual_xpath('学习地图名字：', '/html/body/div[2]/form/div/p/span[1]')
        Function().exit_HT()
    # 项目管理页验证
    def test_0006(self):
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[2]')
        # 我的项目
        Basic().clickelement_id('2-1')
        Assertions().assertEqual_xpath('项目名称：', '/html/body/div[2]/div/form/div[1]/p[3]/span')
    def test_0007(self):
        # 我的学科
        Basic().clickelement_id('2-2')
        Assertions().assertEqual_xpath('学科：', '/html/body/div[3]/div/form/p[1]/span')
    def test_0008(self):
        # 项目管理
        Basic().clickelement_id('2-3')
        Assertions().assertEqual_xpath('项目名称：', '/html/body/div[3]/div/form/p[3]/span')
    def test_0009(self):
        # 项目审核
        Basic().clickelement_id('2-4')
        Assertions().assertEqual_xpath('项目状态：', '/html/body/div[2]/div/form/p[4]/span')
    def test_0010(self):
        # 项目授权
        Basic().clickelement_id('2-5')
        Assertions().assertEqual_xpath('项目列表', '/html/body/div[4]/div/ul/li[1]')
    def test_0011(self):
        # 课程管理
        Basic().clickelement_id('2-6')
        Assertions().assertEqual_xpath('课程名称：', '/html/body/div[2]/form/div/p[2]/span')
    def test_0012(self):
        # 项目发布
        Basic().clickelement_id('2-7')
        Assertions().assertEqual_xpath('已发布', '//*[@id="cvsetAlreadyRelease"]')
        Function().exit_HT()
    # 培训管理页验证
    def test_0013(self):
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[3]')
        Basic().clickelement_id('3-1')
        Assertions().assertEqual_xpath('培训管理>培训管理', '/html/body/form[2]/div[2]/div[1]/h3')
        Function().exit_HT()
    # 考试管理页验证
    def test_0014(self):
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[4]')
        Basic().clickelement_id('4-1')
        Assertions().assertEqual_xpath('试卷名称：', '/html/body/div[2]/form/div/p[1]/span')
        Function().exit_HT()
    # 学习卡管理页验证
    def test_0015(self):
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[5]')
        # 制卡管理
        Basic().clickelement_id('5-1')
        Assertions().assertEqual_xpath('卡数量', '/html/body/div[2]/div/table/thead/tr/th[5]')
    def test_0016(self):
        # 学习卡管理
        Basic().clickelement_id('5-2')
        Assertions().assertEqual_xpath('卡号：', '/html/body/div[2]/div[1]/form/div/p[1]/span[1]')
    def test_0017(self):
        # 卡类型管理
        Basic().clickelement_id('5-3')
        Assertions().assertEqual_xpath('卡类型：', '/html/body/div[2]/div[1]/form/div/p[1]/span')
    def test_0018(self):
        # 卡类型分配管理
        Basic().clickelement_id('5-4')
        Assertions().assertEqual_xpath('手动选择', '/html/body/div[3]/div[4]/div/div[1]/div[2]/span')
    def test_0019(self):
        # 卡状态管理
        Basic().clickelement_id('5-5')
        Assertions().assertEqual_xpath('卡状态', '/html/body/div[2]/div[4]/div/table/thead/tr/th[8]')
        Function().exit_HT()
    # 客户管理
    def test_0020(self):
        # 站点设置
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[6]')
        Basic().clickelement_id('6-1')
        Assertions().assertEqual_xpath('站点域名', '/html/body/div[2]/form/div[3]/div/table/thead/tr/th[4]')
        Function().exit_HT()
    # 订单管理
    def test_0021(self):
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[7]')
        Basic().clickelement_id('7-1')
        Assertions().assertEqual_xpath('订单号：', '/html/body/form[2]/div[1]/div[1]/p[1]/span')
        Function().exit_HT()
    # 内容管理
    def test_0022(self):
        # 文章管理
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[8]')
        Basic().clickelement_id('8-1')
        Assertions().assertEqual_xpath('标题', '/html/body/div[4]/div/table/thead/tr/th[2]')
    def test_0023(self):
        # 页面管理
        Basic().clickelement_id('8-2')
        Assertions().assertEqual_xpath('页面名称', '/html/body/form[2]/div[4]/div/table/thead/tr/th[2]')
    def test_0024(self):
        # Banner管理
        Basic().clickelement_id('8-3')
        Assertions().assertEqual_xpath('banner分类：', '/html/body/form[2]/div/div/p[4]/span')
    def test_0025(self):
        # 消息管理
        Basic().clickelement_id('8-4')
        Assertions().assertEqual_xpath('消息内容', '/html/body/div[4]/div/table/thead/tr/th[5]')
    def test_0026(self):
        # 反馈意见管理
        Basic().clickelement_id('8-5')
        Assertions().assertEqual_xpath('反馈内容', '/html/body/div[4]/div/table/thead/tr/th[5]')
    def test_0027(self):
        # 内容分类
        Basic().clickelement_id('8-6')
        Assertions().assertEqual_xpath('类型', '/html/body/div[4]/div/table/thead/tr/th[2]')
        Function().exit_HT()
    # 系统维护
    def test_0028(self):
        # 机构管理
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[9]')
        Basic().clickelement_id('9-1')
        Assertions().assertEqual_xpath('机构名称', '/html/body/div[5]/div/table/thead/tr/th[2]/a')
        # 学员管理
        Basic().clickelement_id('9-2')
        Assertions().assertEqual_xpath('学员账号', '/html/body/div[3]/div/table/thead/tr/th[2]')
    def test_0030(self):
        # 账号管理
        Basic().clickelement_id('9-3')
        Assertions().assertEqual_xpath('账号', '/html/body/div[6]/div[3]/form/table/thead/tr/th[2]')
    def test_0031(self):
        # 角色管理
        Basic().clickelement_id('9-4')
        Assertions().assertEqual_xpath('角色名称', '/html/body/div[4]/div/table/thead/tr/th[2]')
    def test_0032(self):
        # 菜单管理
        Basic().clickelement_id('9-5')
        Assertions().assertEqual_xpath('系统名称', '/html/body/div[6]/div/table/thead/tr/th[2]')
    def test_0033(self):
        # 其他设置
        Basic().clickelement_id('9-6')
        Assertions().assertEqual_xpath('系统维护>其他设置', '/html/body/div[2]/h3')
        Function().exit_HT()

    # def test_0034(self):
    #     # 审查日志
    #     Basic().clickelement_id('9-7')
    # def test_0035(self):
    #     # 区县管理员
    #     Basic().clickelement_id('9-8')

    # 数据统计
    def test_0036(self):
        # 面授项目统计
        Function().login_HT('admin', '123456')
        Basic().ActionChains_xpath('/html/body/span/div[1]/div[1]/div[2]/ul/li[10]')
        Basic().clickelement_id('10-1')
        Assertions().assertEqual_xpath('面授项目数据统计', '/html/body/div[3]/h2')
    def test_0037(self):
        # 临床实践统计
        Basic().clickelement_id('10-2')
        time.sleep(5)
        Assertions().assertEqual_xpath('临床实践数据统计', '/html/body/div[3]/h2')
    def test_0038(self):
        # 远程项目统计
        Basic().clickelement_id('10-3')
        time.sleep(5)
        Assertions().assertEqual_xpath('远程项目数据统计', '/html/body/div[3]/h2')
        # 退出系统
        Function().exit_HT()
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.dr.quit()
        pass

if __name__ == '__main__':
    unittest.main()

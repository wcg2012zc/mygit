import unittest
import time
from Utils.DriverHandle import DriverHandle
from Utils.readxmlData import xmlfile
from ElementLayout.Basiclibrary import Basic, Assertions
from ElementLayout.Functionlibrary import Function
from selenium.webdriver.common.action_chains import *
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
class Testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = DriverHandle().driver
        cls.dr.get("http://dev.ncme.org.cn/qiantai/")
        time.sleep(5)

    def setUp(self):
        # self.dr = DriverHandle().driver
        # self.dr.get('http://dev.ncme.org.cn/qiantai/')
        time.sleep(3)

    # 个人中心-我的胜任力
    def test_0001(self):
        Function().login_QT('18633949113', 'Aa123456')
        Basic().ActionChains_class('login_link')
        Basic().clickelement_link_text('我的胜任力')
        Assertions().assertEqual_xpath('北京凯尔医院', '//*[@id="myYiyuan"]')
        time.sleep(1)
        Function().exit_QT()

    # 个人中心-我的学习
    def test_0002(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            time.sleep(3)
            Basic().ActionChains_link_text('个人中心')
            Basic().clickelement_link_text('我的学习')
        except:
            Basic().ActionChains_link_text('个人中心')
            Basic().clickelement_link_text('我的学习')
        Assertions().assertEqual_xpath('抗精神病药的合理应用', '\
        /html/body/div[1]/div[4]/form/div/div/div/ul/li[13]/div[3]/div/div[1]/h2')
        Function().exit_QT()

    # 个人中心-我的学分/证书
    def test_0003(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            time.sleep(3)
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('我的学分/证书')
        except:
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('我的学分/证书')
        # 断言
        Assertions().assertEqual_xpath('无学分申请或证书领取记录！', '\
        /html/body/div[1]/div[4]/form/div/div/center')
        # 退出
        Function().exit_QT()

    # 个人中心-我的收藏
    def test_0004(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            time.sleep(3)
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('我的收藏')
        except:
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('我的收藏')
        # 断言
        Assertions().assertEqual_xpath('没有收藏的内容！', '\
        /html/body/form/div/div[5]/div[2]/div/div[1]/center')
        time.sleep(3)
        # 退出
        Basic().ActionChains_link_text('个人中心')
        Function().exit_QT()

    # 个人中心-学习卡管理
    def test_0005(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            time.sleep(3)
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('学习卡管理')
        except:
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('学习卡管理')
        # 断言
        Assertions().assertEqual_id('添加学习卡', 'addcard')
        time.sleep(3)
        # 退出
        Function().exit_QT()

    # 个人中心-我的学科
    def test_0006(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            time.sleep(3)
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('我的学科')
        except:
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('我的学科')
        # 断言
        Assertions().assertEqual_class('新生儿科学护理', 'main_title_2')
        time.sleep(3)
        # 退出
        Function().exit_QT()

    # 个人中心-消息管理
    def test_0007(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            time.sleep(3)
            Basic().ActionChains_class('login_link')
            Basic().clickelement_link_text('消息管理')
        except:
            Basic().ActionChains_class('login_link')
            Basic().clickelement_link_text('消息管理')
        # 断言
        Assertions().assertEqual_id('全部设为已读', 'readAll')
        # 退出
        Function().exit_QT()

    # 个人中心-学习报告
    def test_0008(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            time.sleep(3)
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('学习报告')
        except:
            Basic().ActionChains_class('login_link')
            time.sleep(1)
            Basic().clickelement_link_text('学习报告')
        # 断言
        Assertions().assertEqual_id('项目学习报告', 'tab1')
        # 退出
        Function().exit_QT()

    # 个人中心-账号管理
    def test_0009(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            Basic().ActionChains_class('login_link')
            Basic().clickelement_link_text('账号管理')
        except:
            Basic().ActionChains_class('login_link')
            Basic().clickelement_link_text('账号管理')
        Basic().cleartextbox_id('account_name')
        Basic().inputtext_id('account_name', '18633949113')
        Basic().select_id_value('sex', '2')
        Basic().select_id_value('region1', '111000001')
        Basic().select_id_value('region2', '111000032')
        Basic().select_id_value('rspropid', '111000372')
        Basic().cleartextbox_id('tt')
        time.sleep(1)
        Basic().inputtext_id('tt', '北京凯尔医院')
        Basic().clickelement_id('1134')
        Basic().select_id_value('work_type', '2')
        Basic().select_id_value('work_unit', '610010664')
        Basic().select_id_value('xueke1', '580001')
        Basic().select_id_value('xueke2', '580005')
        Basic().select_id_value('xueke3', '580007')
        # 点击确定
        Basic().clickelement_name('submit2')
        time.sleep(3)
        # 修改手机号
        Basic().clickelement_id('tab2')
        Basic().clickelement_xpath('/html/body/form/div/div[4]/div[2]/div/div[2]/ul/li[2]/span[1]')
        Basic().cleartextbox_id('newmobile')
        Basic().inputtext_id('newmobile', '18633949113')
        Basic().inputtext_id('verify_code', '195753')
        Basic().clickelement_xpath('/html/body/form/div/div[6]/div[2]/div[2]/button')
        time.sleep(2)
        # 获取网页上的警告信息
        Function().alert()
        time.sleep(2)
        Function().alert()
        time.sleep(3)
        # 修改密码
        Basic().clickelement_xpath('/html/body/form/div/div[4]/div[2]/div/div[2]/ul/li[1]/span')
        Basic().inputtext_id('curpassword', 'Aa123456')
        Basic().inputtext_id('newpassword', 'Aa123456')
        Basic().inputtext_id('retypassword', 'Aa123456')
        Basic().clickelement_xpath('/html/body/form/div/div[5]/div[2]/div[2]/button')
        time.sleep(2)
        # 获取网页上的警告信息
        Function().alert()
        time.sleep(2)
        Function().alert()
        time.sleep(5)
        # 修改邮箱
        Basic().clickelement_xpath('/html/body/form/div/div[4]/div[2]/div/div[2]/ul/li[3]/span[1]')
        Basic().inputtext_id('newemail', '12345678@qq.com')
        Basic().clickelement_xpath('/html/body/form/div/div[7]/div[2]/div[2]/button')
        time.sleep(2)
        # 获取网页上的警告信息
        Function().alert()
        time.sleep(2)
        Function().alert()
        time.sleep(5)
        Basic().wait_xpath(6000, '/html/body/form/div/div[1]/div/div/div[2]/span/a[1]')
        # 退出
        Function().exit_QT()

    # 注册
    def test_0010(self):
        Basic().clickelement_link_text('注册')
        Basic().clickelement_id('certificate_type')
        Basic().select_id_text('certificate_type', '军官证')
        Basic().inputtext_id('certificate_no', '1231231061')
        Basic().inputtext_id('real_name', '张四')
        Basic().select_id_value('region1', '111000001')
        Basic().select_id_value('region2', '111000032')
        Basic().select_id_value('rspropid', '111000375')
        Basic().inputtext_id('tt', '北京大学医院')
        time.sleep(1)
        Basic().clickelement_id('5338')
        Basic().select_id_value('work_type', '1')
        Basic().select_id_value('work_unit', '610010659')
        Basic().select_id_value('xueke1', '510001')
        Basic().select_id_value('xueke2', '510002')
        Basic().select_id_value('xueke3', '510019')
        Basic().select_id_value('grassroot', '1')
        Basic().clickelement_id('tab_btn1')
        # 账号验证
        Basic().inputtext_id('mobile_phone', '15000001261')
        Basic().inputtext_id('verify_code', '195753')
        Basic().inputtext_id('account_password', 'Aa123456')
        Basic().inputtext_id('confirmpassword', 'Aa123456')
        Basic().clickelement_id('register_btn')
        time.sleep(7)
        # 断言
        Assertions().assertEqual_xpath('用户登录', '/html/body/form/div/div[3]/h2[2]')

    # 登录
    def test_0011(self):
        Function().login_QT('18633949113', 'Aa123456')
        # 断言
        Assertions().assertEqual_class('个人中心', 'login_link')
        # 退出
        Function().exit_QT()

    # 证书查询
    def test_0012(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
            Basic().clickelement_link_text('证书查询')
        except:
            Basic().clickelement_link_text('证书查询')
        # 远程继教学分查询
        Basic().inputtext_id('idcard', '130634198108150919')
        Basic().select_id_value('begintime', '2015')
        Basic().select_id_value('endtime', '2018')
        Basic().clickelement_name('comment_submit')
        # 断言
        Assertions().assertEqual_xpath('未搜索到该学员', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div/span')

        # 学员培训证书查询
        Basic().inputtext_id('idcard1', '130634198108150919')
        Basic().clickelement_names('comment_submit', 1)
        # 断言
        Assertions().assertEqual_xpath('未搜索到该学员', '/html/body/div[1]/div[4]/div[1]/div[2]/div/div/span')

    # 首页-帮助
    def test_0013(self):
        Basic().clickelement_class('help')
        # 注册与登录
        Assertions().assertIn_xpath('如何注册', '/html/body/div[1]/div[3]/div/div[1]/div/ol/li[1]')
        # 试用学习卡
        Basic().clickelement_id('tab2')
        Assertions().assertIn_xpath('为什么在个人中心点击添加学习卡后无反应', '\
        /html/body/div[1]/div[3]/div/div[2]/div/ol/li[1]')
        # 项目学习
        Basic().clickelement_id('tab3')
        Assertions().assertIn_xpath('为什么学习项目前要登录', '/html/body/div[1]/div[3]/div/div[3]/div/ol/li[1]')
        # 直播学习
        Basic().clickelement_id('tab4')
        Assertions().assertIn_xpath('如何学习直播课程', '/html/body/div[1]/div[3]/div/div[4]/div/ol/li[1]')
        # 申请学分
        Basic().clickelement_id('tab5')
        Assertions().assertIn_xpath('完成项目学习后', '/html/body/div[1]/div[3]/div/div[5]/div/ol/li[1]')
        Function().homepage_text()
    # 首页-全科医学-图片信息验证
    def test_0014(self):
        try:
            Basic().clickelement_xpath('/html/body/form/div/div[1]/div[2]/div/ul/li[1]/a')
        except:
            Function().homepage_text()
            Basic().clickelement_xpath('/html/body/form/div/div[1]/div[2]/div/ul/li[1]/a')
        time.sleep(2)
    # 页面标题栏
        # 学科
        Assertions().assertEqual_xpath('学科：', '/html/body/form/div/div[3]/ul[1]/li[1]')
        # 类型
        Assertions().assertEqual_xpath('类型：', '/html/body/form/div/div[3]/ul[2]/li[1]')
        # 级别
        Assertions().assertEqual_xpath('级别：', '/html/body/form/div/div[3]/ul[3]/li[1]')
        # 授课形式
        Assertions().assertEqual_xpath('授课形式:', '/html/body/form/div/div[3]/ul[4]/li[1]')
    # 项目图片信息验证
        Basic().ActionChains_xpath('/html/body/form/div/div[4]/ul[2]/li[2]/span')
        # 项目名称
        Assertions().assertIn_xpath('全科医学和社区居民健康管理', '/html/body/form/div/div[4]/ul[2]/li[2]/div/h2')
        # 项目简介
        Assertions().assertIn_xpath('本项目结合当今社区医疗管理发展趋势', '\
        /html/body/form/div/div[4]/ul[2]/li[2]/div/p[1]')
        # 学分
        Assertions().assertEqual_xpath('0.0 分', '/html/body/form/div/div[4]/ul[2]/li[2]/div/p[2]')
        # 价格
        Assertions().assertEqual_xpath('免费', '/html/body/form/div/div[4]/ul[2]/li[2]/div/div[2]/span[1]')

    # 开始学习
    def test_0015(self):
        Basic().clickelement_xpath('/html/body/form/div/div[4]/ul[2]/li[2]/div')
        time.sleep(2)
        Basic().clickelement_name('study_begin')
        time.sleep(1)
        Assertions().assertEqual_xpath('全科医学和社区居民健康管理', '/html/body/div[3]/div[2]/div/h2')
        Assertions().assertIn_xpath('项目负责人', '/html/body/div[3]/div[2]/div/h3[1]')
        Assertions().assertIn_xpath('来源', '/html/body/div[3]/div[2]/div/h3[2]')
        Assertions().assertEqual_id('目录', 'tab1')
        Assertions().assertEqual_id('讨论', 'tab2')
        Assertions().assertEqual_id('笔记', 'tab3')
    # 讨论
    def test_0016(self):
        Basic().clickelement_id('tab2')
        Basic().inputtext_id('talk', '讨论讨论讨论讨论讨论讨论讨论讨论')
        Basic().clickelement_name('comment_submit')
    # 笔记
    def test_0017(self):
        Basic().clickelement_id('tab3')
        Basic().inputtext_id('notice', '笔记笔记笔记笔记笔记笔记')
        Basic().clickelement_name('comment_submit')
    def test_0018(self):
        # 点击返回
        Basic().clickelement_class('go_back')
        Assertions().assertEqual_xpath('项目简介', '/html/body/div[2]/div[5]/div[1]/div[3]/h4/span')
        # 返回首页
        Function().homepage_text()

    # 首页-学科-“更多”
    def test_0019(self):
        Basic().clickelement_link_text('更多')
        time.sleep(2)
        Assertions().assertEqual_xpath('学科：', '/html/body/form/div/div[3]/ul[1]/li[1]')
        Assertions().assertEqual_xpath('类型：', '/html/body/form/div/div[3]/ul[2]/li[1]')
        Assertions().assertEqual_xpath('级别：', '/html/body/form/div/div[3]/ul[3]/li[1]')
        Assertions().assertEqual_xpath('授课形式:', '/html/body/form/div/div[3]/ul[4]/li[1]')
        # 点击心胸外科学
        Basic().clickelement_xpath('/html/body/form/div/div[3]/ul[1]/li[2]/span[39]')
        # 图片信息验证
        Basic().ActionChains_xpath('/html/body/form/div/div[4]/ul[2]/li[1]/span')
        # 项目名称
        Assertions().assertIn_xpath('胸腺疾病的手术治疗', '/html/body/form/div/div[4]/ul[2]/li[1]/div/h2')
        # 项目简介
        Assertions().assertIn_xpath('本项目主要针对胸腺疾病', '/html/body/form/div/div[4]/ul[2]/li[1]/div/p[1]')
        # 项目负责人
        Assertions().assertIn_xpath('项目负责人', '/html/body/form/div/div[4]/ul[2]/li[1]/div/div[1]/span')
        # 学分
        Assertions().assertEqual_xpath('0.0 分', '/html/body/form/div/div[4]/ul[2]/li[1]/div/p[2]')
        # 价格
        Assertions().assertEqual_xpath('免费', '/html/body/form/div/div[4]/ul[2]/li[1]/div/div[2]/span[1]')
        # 返回首页
        Function().homepage_text()

    # 首页-搜索
    def test_0020(self):
        Basic().inputtext_id('search_input', '耳鼻喉')
        Basic().clickelement_id('search_button')
        # 断言
        Assertions().assertIn_xpath('耳鼻喉经典手术示教与讲座', '/html/body/div[1]/div[3]/div[2]/div[1]/ul[1]/li/div/h2')
        # 返回首页
        Function().homepage_text()

    # 意见反馈
    def test_0021(self):
        Basic().clickelement_id('feedback')
        Basic().inputtext_id('content', '意见反馈意见反馈意见反馈意见反馈')
        time.sleep(2)
        Basic().inputtext_xpath('/html/body/div[1]/div[3]/div[1]/form/div[3]/div/div[2]/input', 'D:\\001.jpg')
        code = Basic().getvalue_id('yzmCode', 'value')
        Basic().inputtext_id('yzmInput', code)
        Basic().inputtext_id('qq', '123456@qq.com')
        Basic().clickelement_xpath('/html/body/div[1]/div[3]/div[1]/form/div[7]/a')
        # 获取网页上的警告信息
        Function().alert()
        # 返回首页
        Function().homepage_text()

    # 继续医学教育项目
    def test_0022(self):
        try:
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[1]/a/span')
        except:
            Function().homepage_text()
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[1]/a/span')
        # 优质慕课
        Assertions().assertEqual_xpath('优质慕课', '//*[@id="biao"]')
        Function().homepage_text()
    # 专项能力
    def test_0023(self):
        try:
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[2]/a/span')
        except:
            Function().homepage_text()
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[2]/a/span')
        Assertions().assertEqual_xpath('专项能力', '/html/body/div[1]/div[4]/h1')
        Function().homepage_text()
    # 胜任力模型
    def test_0024(self):
        try:
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[3]/a/span')
        except:
            Function().homepage_text()
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[3]/a/span')
        Assertions().assertEqual_xpath('胜任力模型', '/html/body/form/div/div[3]/h1')
        Function().homepage_text()
    # 基层卫生能力建设平台
    def test_0025(self):
        try:
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[4]/a/span')
        except:
            Function().homepage_text()
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[4]/a/span')
        Assertions().assertEqual_xpath('基层卫生能力建设平台', '/html/body/div[2]/div[2]/div/p/b')
        DriverHandle().driver.get("http://dev.ncme.org.cn/qiantai/")
    # 县级医院骨干专科医师培训项目
    def test_0026(self):
        try:
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[5]/a/span')
        except:
            DriverHandle().driver.get("http://dev.ncme.org.cn/qiantai/")
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[5]/a/span')
        Assertions().assertEqual_xpath('县级医院骨干专科医师培训', '/html/body/div[4]/div[8]/div/p/span[2]')
        Function().homepage_text()
    # 紧缺人才培训项目
    def test_0027(self):
        try:
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[6]/a/span')
        except:
            Function().homepage_text()
            Basic().clickelement_xpath('/html/body/form/div/div[3]/div[1]/div[6]/a/span')
        # 基层卫生能力建设平台
        Assertions().assertEqual_xpath('紧缺人才培训项目', '/html/body/div[4]/div[8]/p/span[2]')
        Basic().clickelement_xpath('/html/body/div[4]/div[1]/div/div/ul/li[1]/a')
    # 轮播图—糖尿病专项培训
    def test_0028(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[2]/div[1]/div[1]/ul/li[2]/a/img')
        Assertions().assertIn_xpath('抱歉，糖尿病专项培训仅对指定人员开放', '/html/body/div[4]/div[8]/div[2]/div')
        Function().homepage_text()
    # 轮播图—县级医院骨干专科医师培训
    def test_0029(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[2]/div[1]/div[1]/ul/li[4]/a/img')
        Assertions().assertEqual_xpath('县级医院骨干专科医师培训', '/html/body/div[4]/div[7]/div/p/span[2]')
        DriverHandle().driver.get("http://dev.ncme.org.cn/qiantai/")
    # 轮播图—紧缺人才培训项目
    def test_0030(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[2]/div[1]/div[1]/ul/li[5]/a/img')
        Assertions().assertEqual_xpath('紧缺人才培训项目', '/html/body/div[4]/div[7]/p/span[2]')
        DriverHandle().driver.get("http://dev.ncme.org.cn/qiantai/")
    # 轮播图—基层卫生能力建设平台
    def test_0031(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[2]/div[1]/div[1]/ul/li[6]/a/img')
        Assertions().assertEqual_xpath('基层卫生能力建设平台', '/html/body/div[2]/div[2]/div/p/b')
        DriverHandle().driver.get("http://dev.ncme.org.cn/qiantai/")

    # 专委会
    def test_0032(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[4]/ul/li[1]/span/i')
        Assertions().assertEqual_id('传染病学专家委员会', '356')
        Assertions().assertEqual_xpath('主任委员', '/html/body/form/div/div[3]/div/div[3]/ul[1]/li[1]/a/div[2]/span[1]')
        Assertions().assertEqual_xpath('李兰娟', '/html/body/form/div/div[3]/div/div[3]/ul[1]/li[1]/a/div[2]/h2')
        Assertions().assertEqual_xpath('浙江大学医学院附属第一医院', '/html/body/form/div/div[3]/div/div[3]/ul[1]/li[1]/a/div[2]/h3')
        Assertions().assertEqual_id('骨外科学专家委员会', '359')
        Assertions().assertEqual_id('妇产科学专家委员会', '358')
        Function().homepage_text()

    # 合作机构
    def test_0033(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[4]/ul/li[2]/span/i')
        Assertions().assertEqual_xpath('复旦大学附属儿科医院', '/html/body/div[1]/div[3]/div[2]/div[2]/h2')
        Function().homepage_text()
    # 名师
    def test_0034(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[4]/ul/li[3]/span/i')
        Assertions().assertIn_xpath('按姓名拼音顺序排序', '/html/body/form/div/div[3]/p')
        Function().homepage_text()

    # 海外视野
    def test_0035(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[4]/ul/li[4]/span/i')
        Assertions().assertIn_xpath('肾细胞癌概述', '/html/body/form/div/div[4]/ul[2]/li[1]/div/h2')
        Function().homepage_text()

    # 首页-分类导航
    def test_0036(self):
        try:
            Function().login_QT('18633949113', 'Aa123456')
        except:
            Function().homepage_text()
        time.sleep(2)
        # 断言
        Assertions().assertIn_class_s('继续医学教育项目', 'main_title', 0)
        Assertions().assertIn_class_s('名师课程', 'main_title', 1)
        Assertions().assertIn_class_s('专委会', 'main_title', 2)
        Assertions().assertIn_class_s('合作机构', 'main_title', 3)
        Assertions().assertIn_class_s('典型病例', 'main_title', 4)
        Assertions().assertIn_class_s('精彩直播', 'main_title', 5)
        Assertions().assertIn_class_s('指南解读', 'main_title', 6)

    # 首页—分类—继续医学教育项目
    def test_0037(self):
        # 图片信息验证
        ####### 滑动滚动条向下
        js = "var action=document.documentElement.scrollTop=500"
        self.dr.execute_script(js)
        time.sleep(2)
        Basic().ActionChains_xpath('/html/body/form/div/div[3]/div[5]/ul/li[1]/span')
        # 项目名称
        Assertions().assertEqual_xpath('艾滋病诊治进展', '\
        /html/body/form/div/div[3]/div[5]/ul/li[1]/div/h2')
        # 项目简介
        Assertions().assertIn_xpath('本项目邀请国内顶尖的艾滋病专家对近年艾滋病的最新进展进行了介绍', '\
                /html/body/form/div/div[3]/div[5]/ul/li[1]/div/p[1]')
        # 项目负责人
        Assertions().assertIn_xpath('项目负责人', '/html/body/form/div/div[3]/div[5]/ul/li[1]/div/div/span')
        # 学分
        Assertions().assertIn_xpath('0分', '/html/body/form/div/div[3]/div[5]/ul/li[1]/div/p[2]')
        # 价格
        Assertions().assertIn_xpath('免费', '/html/body/form/div/div[3]/div[5]/ul/li[1]/div/h3/span[1]')
    # 学习页面验证
    def test_0038(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[5]/ul/li[3]/div')
        Basic().clickelement_xpath('/html/body/div[2]/ul[2]/li/div/div[4]/p/button')
        time.sleep(3)
        Assertions().assertIn_xpath('作业治疗技术在职业康复中的规范化应用', '/html/body/div[3]/div[2]/div/h2')
        Assertions().assertIn_xpath('项目负责人', '/html/body/div[3]/div[2]/div/h3[1]')
        Assertions().assertIn_xpath('来源', '/html/body/div[3]/div[2]/div/h3[2]')
        Assertions().assertEqual_id('目录', 'tab1')
        Assertions().assertEqual_id('讨论', 'tab2')
        Assertions().assertEqual_id('笔记', 'tab3')
        # 点击返回
        Basic().clickelement_class('go_back')
        Assertions().assertEqual_xpath('项目简介', '/html/body/div[2]/div[5]/div[1]/div[3]/h4/span')
        Function().homepage_text()

    # 直播回放
    def test_0039(self):
        Basic().clickelement_xpath('/html/body/form/div/div[3]/div[10]/ul/li[1]/span[1]')
        Basic().clickelement_xpath('/html/body/div[2]/ul[2]/li/div[2]/h3[2]/button')
        time.sleep(3)
        Assertions().assertIn_xpath('2018树兰国际器官移植论坛', '/html/body/div[3]/div[2]/div/h2')
        Assertions().assertIn_xpath('项目负责人', '/html/body/div[3]/div[2]/div/h3[1]')
        Assertions().assertIn_xpath('来源', '/html/body/div[3]/div[2]/div/h3[2]')
        Assertions().assertEqual_id('目录', 'tab1')
        Assertions().assertEqual_id('讨论', 'tab2')
        Assertions().assertEqual_id('笔记', 'tab3')
        # 点击返回
        Basic().clickelement_class('go_back')
        Assertions().assertEqual_xpath('项目简介', '/html/body/div[2]/div[5]/div[1]/div[3]/h4/span')
        Function().homepage_text()

    def tearDown(self):
        # self.dr.quit()
        #time.sleep(2)
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.dr.quit()
        pass

if __name__ == '__main__':
        unittest.main()
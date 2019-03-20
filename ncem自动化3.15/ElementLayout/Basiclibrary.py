
import unittest
from selenium import webdriver
from Utils.singleton import singleton
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.common import exceptions
import selenium.webdriver.support.ui as ui
from Utils.DriverHandle import DriverHandle
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.wait import WebDriverWait

class Basic:
    def __init__(self):
        self.driver = DriverHandle().driver
# 单击按钮
    #根据id定位对象并单击
    def clickelement_id(self,i):
        try:
            a = self.driver.find_element_by_id(i).click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # id重复时定位对象并单击
    def clickelement_ids(self, i, j):
        try:
            a = self.driver.find_elements_by_id(i)[j].click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # 根据class定位对象并单击
    def clickelement_class(self, i):
        try:
            a = self.driver.find_element_by_class_name(i).click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # class重复时定位对象并单击
    def clickelement_class_s(self, i, j):
        try:
            a = self.driver.find_elements_by_class_name(i)[j].click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # 根据name定位对象并单击
    def clickelement_name(self, i):
        try:
            a = self.driver.find_element_by_name(i).click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # name重复时定位对象并单击
    def clickelement_names(self, i, j):
        try:
            a = self.driver.find_elements_by_name(i)[j].click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    #根据xpath定位对象并单击
    def clickelement_xpath(self,i):
        try:
            a = self.driver.find_element_by_xpath(i).click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # 根据link_text定位对象并单击
    def clickelement_link_text(self, i):
        try:
            a = self.driver.find_element_by_link_text(i).click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # link_text重复时定位对象并单击
    def clickelement_link_text_s(self, i, j):
        try:
            a = self.driver.find_elements_by_link_text(i)[j].click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # 根据partial_link_text查找对象并单击
    def clickelement_P_link_text(self, i):
        try:
            a = self.driver.find_element_by_partial_link_text(i).click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')
    # partial_link_text重复时查找对象并单击
    def clickelement_P_link_text_s(self, i, j):
        try:
            a = self.driver.find_elements_by__link_text(i)[j].click()
            return a
        except Exception as e:
            print(e, '未找到点击对象')

# 清除文本框内容
    # 根据id定位文本框并清除内容
    def cleartextbox_id(self, id):
        try:
            a = self.driver.find_element_by_id(id).clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # id重复时定位对象并清除内容
    def cleartextbox_ids(self, i, j):
        try:
            a = self.driver.find_elements_by_id(i)[j].clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # 根据class定位对象并清除内容
    def cleartestbox_class(self, i):
        try:
            a = self.driver.find_element_by_class_name(i).clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # class重复时定位对象并清除内容
    def cleartestbox_class_s(self, i,j):
        try:
            a = self.driver.find_elements_by_class_name(i)[j].clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # 根据name定位对象并清除内容
    def cleartextbox_name(self, i):
        try:
            a = self.driver.find_element_by_name(i).clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # name重复时查找对象并清除内容
    def cleartextbox_names(self, i, j):
        try:
            a = self.driver.find_elements_by_name(i)[j].clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # 根据xpath定位对象并清除内容
    def cleartextbox_xpath(self, i):
        try:
            a = self.driver.find_element_by_xpath(i).clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # 根据link_text定位对象并清除内容
    def cleartextbox_link_text(self, i):
        try:
            a = self.driver.find_element_by_link_text(i).clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # link_text定位对象并清除内容
    def cleartextbox_link_text_s(self, i, j):
        try:
            a = self.driver.find_elements_by_link_text(i)[j].clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # 根据partial_link_text查找对象并清除内容
    def cleartextbox_P_link_text(self, i):
        try:
            a = self.driver.find_element_by_partial_link_text(i).clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')
    # partial_link_text重复时定位对象并清除内容
    def cleartextbox_P_link_text_s(self, i, j):
        try:
            a = self.driver.find_elements_by_partial_link_text(i)[j].clear()
            return a
        except Exception as e:
            print(e, '未找到文本框')

# 定位文本框并输入内容
    # 根据id定位文本框并输入内容
    def inputtext_id(self, id, keys):
        try:
            a = self.driver.find_element_by_id(id).send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # id重复时对象并输入内容
    def inputtext_ids(self, i,j, keys):
        try:
            a = self.driver.find_element_by_id(i)[j].send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # 根据class定位对象并输入内容
    def inputtext_class(self, i, keys):
        try:
            a = self.driver.find_element_by_class_name(i).send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # class重复时定位对象并输入内容
    def inputtext_class_s(self, i,j, keys):
        try:
            a = self.driver.find_elements_by_class_name(i)[j].send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # 根据name定位时对象并输入内容
    def inputtext_name(self, i, keys):
        try:
            a = self.driver.find_element_by_name(i).send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # name重复时定位对象并输入内容
    def inputtext_names(self, i, j, keys):
        try:
            a = self.driver.find_elements_by_name(i)[j].send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # 根据xpath查找对象并输入内容
    def inputtext_xpath(self, i , keys):
        try:
            a = self.driver.find_element_by_xpath(i).send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # 根据link_text查找对象并输入内容
    def inputtext_link_text(self, i, keys):
        try:
            a = self.driver.find_element_by_link_text(i).send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # link_text重复时定位对象并输入内容
    def inputtext_link_text_s(self, i, j, keys):
        try:
            a = self.driver.find_elements_by_link_text(i)[j].send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # 根据partial_link_text对定位象并输入内容
    def inputtext_P_link_text(self, i, keys):
        try:
            a = self.driver.find_element_by_partial_link_text(i).send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')
    # partial_link_text重复时定位对象并输入内容
    def inputtext_P_link_text_s(self, i, j, keys):
        try:
            a = self.driver.find_elements_by_partial_link_text(i)[j].send_keys(keys)
            return a
        except Exception as e:
            print(e, '未找到文本框或输入内容错误')

# 获取对象的文本信息
    # 根据id查找对象并获取文本
    def gettext_id(self, id,):
        try:
            a = self.driver.find_element_by_id(id).text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # id重复时定位对象并获取文本
    def gettext_ids(self, i,j):
        try:
            a = self.driver.find_element_by_id(i)[j].text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # 根据class查找对象并获取文本
    def gettext_class(self, i,):
        try:
            a = self.driver.find_element_by_class_name(i).text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # class重复时定位对象并获取文本
    def gettext_class_s(self, i,j):
        try:
            a = self.driver.find_elements_by_class_name(i)[j].text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # 根据name查找对象并获取文本
    def gettext_name(self, i, ):
        try:
            a = self.driver.find_element_by_name(i).text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # name重复时定位对象并输入获取文本
    def gettext_names(self, i, j):
        try:
            a = self.driver.find_elements_by_name(i)[j].text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # 根据xpath定位对象并获取文本
    def gettext_xpath(self, i,):
        try:
            a = self.driver.find_element_by_xpath(i).text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # 根据link_text定位对象并获取文本
    def gettext_link_text(self, i, ):
        try:
            a = self.driver.find_element_by_link_text(i).text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # link_text重复时定位对象并获取文本
    def gettext_link_text_s(self, i, j):
        try:
            a = self.driver.find_element_by_link_text(i)[j].text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # 根据partial_link_text定位对象并获取文本
    def gettext_P_link_text(self, i, ):
        try:
            a = self.driver.find_element_by_partial_link_text(i).text
            return a
        except Exception as e:
            print(e, '获取文本失败')
    # partial_link_text重复时定位对象并获取文本
    def gettext_P_link_text_s(self, i, j):
        try:
            a = self.driver.find_elements_by_partial_link_text(i)[j].text
            return a
        except Exception as e:
            print(e, '获取文本失败')

# 获取对象的value（目前用于获取验证码）
    # 根据id定位对象并获取value
    def getvalue_id(self, id, value):
        try:
            a = self.driver.find_element_by_id(id).get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # id重复时定位对象并获取value
    def getvalue_ids(self, i,j, value):
        try:
            a = self.driver.find_element_by_id(i)[j].get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # 根据class查找对象并获取value
    def getvalue_class(self, i, value):
        try:
            a = self.driver.find_element_by_class_name(i).get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # class重复时定位对象并获取value
    def getvalue_class_s(self, i,j, value):
        try:
            a = self.driver.find_elements_by_class_name(i)[j].get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # 根据name查找对象并获取value
    def getvalue_name(self, i, value):
        try:
            a = self.driver.find_element_by_name(i).get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # name重复时定位对象并获取value
    def getvalue_names(self, i, j, value):
        try:
            a = self.driver.find_elements_by_name(i)[j].get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # 根据xpath查找对象并获取value
    def getvalue_xpath(self, i, value):
        try:
            a = self.driver.find_element_by_xpath(i).get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # 根据link_text查找对象并获取value
    def getvalue_link_text(self, i, value):
        try:
            a = self.driver.find_element_by_link_text(i).get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # link_text重复时定位对象并获取value
    def getvalue_link_text_s(self, i, j, value):
        try:
            a = self.driver.find_elements_by_link_text(i)[j].get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # 根据partial_link_text查找对象并获取value
    def getvalue_P_link_text(self, i, value):
        try:
            a = self.driver.find_element_by_partial_link_text(i).get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')
    # partial_link_text重复时定位对象并获取value
    def getvalue_P_link_text_s(self, i, j, value):
        try:
            a = self.driver.find_elements_by_partial_link_text(i)[j].get_attribute(value)
            return a
        except Exception as e:
            print(e, '获取验证码失败')

# 鼠标悬停
    # 通过id定位对象并执行鼠标悬停
    def ActionChains_id(self, i):
        try:
            a = ActionChains(self.driver).move_to_element(self.driver.find_element_by_id(i)).perform()
            return a
        except Exception as e:
            print(e, '鼠标悬浮操作失败')
    # 通过class定位对象并执行鼠标悬停
    def ActionChains_class(self,i):
        try:
            a = ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name(i)).perform()
            return a
        except Exception as e:
            print(e, '鼠标悬浮操作失败')
    # 通过name定位对象并执行鼠标悬停
    def ActionChains_name(self,i):
        try:
            a = ActionChains(self.driver).move_to_element(self.driver.find_element_by_name(i)).perform()
            return a
        except Exception as e:
            print(e, '鼠标悬浮操作失败')
    # 通过id定位对象并执行鼠标悬停
    def ActionChains_link_text(self,i):
        try:
            a = ActionChains(self.driver).move_to_element(self.driver.find_element_by_link_text(i)).perform()
            return a
        except Exception as e:
            print(e, '鼠标悬浮操作失败')
    # 通过id定位对象并执行鼠标悬停
    def ActionChains_xpath(self,i):
        try:
            a = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(i)).perform()
            return a
        except Exception as e:
            print(e, '鼠标悬浮操作失败')

# 切入ifram操作
    # 通过id定位ifram并切入
    def iframe_id(self, i):
        try:
            a = self.driver.switch_to.frame(self.driver.find_element_by_id(i))
            return a
        except Exception as e:
            print(e, '切入iframe悬浮框失败')
    # 通过class定位ifram并切入
    def iframe_class(self, i):
        try:
            a = self.driver.switch_to.frame(self.driver.find_element_by_class_name(i))
            return a
        except Exception as e:
            print(e, '切入iframe悬浮框失败')
    # 通过name定位ifram并切入
    def iframe_name(self, i):
        try:
            a = self.driver.switch_to.frame(self.driver.find_element_by_name(i))
            return a
        except Exception as e:
            print(e, '切入iframe悬浮框失败')
    # 通过link_text定位ifram并切入
    def iframe_link_text(self, i):
        try:
            a = self.driver.switch_to.frame(self.driver.find_element_by_link_text(i))
            return a
        except Exception as e:
            print(e, '切入iframe悬浮框失败')
    # 通过id定位ifram并切入
    def iframe_xpath(self, i):
        try:
            a = self.driver.switch_to.frame(self.driver.find_element_by_xpath(i))
            return a
        except Exception as e:
            print(e, '切入iframe悬浮框失败')
# 切出ifram的操作
    def iframe_out(self):
        try:
            DriverHandle().driver.switch_to.default_content()
        except Exception as e:
            print(e, '切出iframe操作失败')

# 执行下一步的等待时间（等待时间为毫秒）
    def wait_id(self,i,j):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_element_by_id(j))
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_ids(self,i, j, x):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_elements_by_id(j)[x])
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_class(self,i,j):
        wait = ui.WebDriverWait(DriverHandle().driver, i)
        wait.until(lambda driver: self.driver.find_element_by_class_name(j))
    def wait_class_s(self,i,j, x):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_elements_by_class_name(j)[x])
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_name(self,i,j):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_element_by_name(j))
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_name_s(self,i,j, x):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_elements_by_name(j)[x])
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_link_text(self,i,j):
        try:
            wait = ui.WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_element_by_link_text(j))
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_link_text_s(self,i,j):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_elements_by_link_text(j))
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_P_link_text(self,i,j):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_element_by_partial_link_text(j))
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_P_link_text_s(self,i,j, x):
        try:
            wait = WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_element_by_partial_link_text(j)[x])
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
    def wait_xpath(self,i,j):
        try:
            wait = ui.WebDriverWait(DriverHandle().driver, i)
            wait.until(lambda driver: self.driver.find_element_by_xpath(j))
        except Exception as e:
            print(e, '网络异常或未找到定位对象')
# 跳转网页操作(一般在第一个和第二个窗口之间操作)
    def Switch(self, i):
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[i])
        except Exception as e:
            print(e, '切换网页操作失败')

# 下拉框选择
    # 通过ID定位select，通过value选择对象
    def select_id_value(self, i, j):
        try:
            a = Select(self.driver.find_element_by_id(i)).select_by_value(j)
            return a
        except Exception as e:
            print(e, '未找到下拉框内对象 ')
    # 通过ID定位select，通过选项的顺序选择，第一个为 0
    def select_id_index(self, i, j):
        try:
            a = Select(self.driver.find_element_by_id(i)).select_by_value(j)
            return a
        except Exception as e:
            print(e, '未找到下拉框内对象 ')
    # 通过ID定位select，通过text选择对象
    def select_id_text(self, i, j):
        try:
            a = Select(self.driver.find_element_by_id(i)).select_by_visible_text(j)
            return a
        except Exception as e:
            print(e, '未找到下拉框内对象 ')
# 复选框全选
    def checkbox(self, i):
        try:
            a = self.driver.find_elements_by_xpath(i)
            for i in a:
                i.click()

        except Exception as e:
            print(e)
# 滑动滚动条向下500
    def scroll_down(self):
        js = "var action=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)

# 找到iframe          （输入视频时长用两个方法）             ########################
    def iframe(self, iframe):
        try:
            a = self.driver.switch_to.frame(iframe)
            return a
        except:
            print('没有找到%s这个元素' % (iframe))
    def id(self,id):
        try:
            a = self.driver.find_element_by_id(id)
            return a
        except:
            print('没有找到%s这个元素' % (id))            #####################

class Assertions(unittest.TestCase):
# 验证（输入预期结果，输入xpath（预期结果完全等于实际结果））
    def assertEqual_id(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_id(实际结果)
        print(Actual_result)
        self.assertEqual(Expected_result, Actual_result)     # 预期结果等于实际结果
    def assertEqual_class(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_class(实际结果)
        print(Actual_result)
        self.assertEqual(Expected_result, Actual_result)     # 预期结果等于实际结果
    def assertEqual_class_s(self, 预期结果, 实际结果, j):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_class_s(实际结果, j)
        print(Actual_result)
        self.assertEqual(Expected_result, Actual_result)     # 预期结果等于实际结果
    def assertEqual_name(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_name(实际结果)
        print(Actual_result)
        self.assertEqual(Expected_result, Actual_result)     # 预期结果等于实际结果
    def assertEqual_link_text(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_link_text(实际结果)
        print(Actual_result)
        self.assertEqual(Expected_result, Actual_result)     # 预期结果等于实际结果
    def assertEqual_P_link_text(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_P_link_text(实际结果)
        print(Actual_result)
        self.assertEqual(Expected_result, Actual_result)     # 预期结果等于实际结果
    def assertEqual_xpath(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_xpath(实际结果)
        print(Actual_result)
        self.assertEqual(Expected_result, Actual_result)     # 预期结果等于实际结果

# 验证（输入预期结果，输入xpath（预期结果包含于实际结果））
    def assertIn_id(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_id(实际结果)
        print(Actual_result)
        self.assertIn(Expected_result, Actual_result)  # 预期结果包含于实际结果
    def assertIn_class(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_class(实际结果)
        print(Actual_result)
        self.assertIn(Expected_result, Actual_result)  # 预期结果包含于实际结果
    def assertIn_class_s(self, 预期结果, 实际结果, j):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_class_s(实际结果, j)
        print(Actual_result)
        self.assertIn(Expected_result, Actual_result)     # 预期结果等于实际结果
    def assertIn_name(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_name(实际结果)
        print(Actual_result)
        self.assertIn(Expected_result, Actual_result)  # 预期结果包含于实际结果
    def assertIn_link_text(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_link_text(实际结果)
        print(Actual_result)
        self.assertIn(Expected_result, Actual_result)  # 预期结果包含于实际结果
    def assertInl_P_link_text(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_P_link_text(实际结果)
        print(Actual_result)
        self.assertIn(Expected_result, Actual_result)  # 预期结果包含于实际结果
    def assertIn_xpath(self, 预期结果, 实际结果):
        Expected_result = 预期结果
        Actual_result = Basic().gettext_xpath(实际结果)
        print(Actual_result)
        self.assertIn(Expected_result, Actual_result)  # 预期结果包含于实际结果




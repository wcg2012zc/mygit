#!/usr/bin/python
#encoding:utf-8

import xml
from xml.dom import minidom
import xml.dom.minidom
class xmlfile(object):
    #def xmlfile(self,xmlfilename,labelname,labelindex):
    def logindata(self,paraname,index):
        dom = xml.dom.minidom.parse('../TestData/loginData.xml')
        root = dom.documentElement
        login = root.getElementsByTagName(paraname)
        loginlist1 = login[index]
        return loginlist1.firstChild.data

    def setupcourse(self,paraname,index):
        dom = xml.dom.minidom.parse('../TestData/loginData.xml')    # 打开xml文件
        root = dom.documentElement        # 得到文档元素对象
        course = root.getElementsByTagName(paraname)            # 按标签名称查找，返回标签结点数组
        course1 = course[index]
        return course1.firstChild.data

    def len(self,paraname):
        dom = xml.dom.minidom.parse('../TestData/loginData.xml')
        root = dom.documentElement
        course = root.getElementsByTagName(paraname)
        len1 = len(course)
        return len1



    def xmlfile(self, xmlfilename, contentname, contentindex):
        dom = xml.dom.minidom.parse('../TestData/' + xmlfilename)
        #root = dom.documentElement
        root = dom.getElementsByTagName("logindata")
        courses = root.getElementsByTagName("Courses")
        lessons = courses.getElementsByTagName("lesson")
        length = lessons.length
        print(length)
        for mylesson in lessons:
            print(mylesson.attributes["Name"].value)
            print(mylesson.getElementsByTagName("coursename")[0].nodeValue)
            print(mylesson.getElementsByTagName("courseinstr")[0].nodeValue)
            print(mylesson.getElementsByTagName("coursepic")[0].nodeValue)
            print(mylesson.getElementsByTagName("surname")[0].nodeValue)
            print(mylesson.getElementsByTagName("unitname")[0].nodeValue)
            print(mylesson.getElementsByTagName("videoname")[0].nodeValue)
            print(mylesson.getElementsByTagName("unitname")[0].nodeValue)
            print(mylesson.getElementsByTagName("progress")[0].nodeValue)
            return mylesson.getElementsByTagName("progress")


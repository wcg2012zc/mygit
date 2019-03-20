#/usr/bin/python
#encoding:utf-8
import time,unittest,sys
from selenium import webdriver
class screenshot(object):
    def screenshot(self):
        curtime = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        screenshotname = curtime + ".png"
        picturepath = "//D:\resultpicture//" + screenshotname
        return picturepath

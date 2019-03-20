#!/usr/bin/python3
#encoding:utf-8

from selenium import webdriver
from Utils.singleton import singleton

@singleton
class DriverHandle(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

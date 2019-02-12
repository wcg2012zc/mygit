#!/usr/bin/pyhthon3
#coding:utf-8

from unittest import TestCase
from Test_Api_Project.base_api.register_api import RegisterApi
from Test_Api_Project.base_api.send_sms_code_api import SendSmsCaptcha
from Test_Api_Project.utilities import user
import json
from Test_Api_Project import settings

class TestRegisterApi(TestCase):
    new_mobile = '13011009944'
    password = '123abc'
    nick_name = 'XiangXi'

    def test_register_success(self):
        #调用发送短信验证码接口
        send_sms_code_api = SendSmsCaptcha()
        send_sms_code_api.post({'type':'register','phone':self.new_mobile})

        #校验发送短信验证码接口HTTP状态码为200
        self.assertEqual(send_sms_code_api.get_status_code(),200)

        #校验发送短信验证码接口反参中code值为0，代表成功（不同项目该字段值不一定为0）
        self.assertEqual(send_sms_code_api.get_code(),0)

        #通过数据库数据库获取短信验证码
        sms_code = user.get_sms_captcha(self.new_mobile)

        #调用注册接口
        pass

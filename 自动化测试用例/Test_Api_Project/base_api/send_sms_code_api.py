#!/usr/bin/python3
#coding:utf-8

from base_api.base_api import BaseApi
from Test_Api_Project import settings

class SendSmsCaptcha(BaseApi):
    url = '/user/sendsms'
    def build_custom_param(self, data):
        return {'type': data['type'], 'phone': data['phone']}

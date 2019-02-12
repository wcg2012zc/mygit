#!/usr/bin/python3
#coding:utf-8



from Test_Api_Project import settings
from base_api.base_api import BaseApi


class RegisterApi(BaseApi):
    url = '/home/register'
    # 对BaseApi类中build_custom_param方法重写
    def build_custom_param(self,data):
        return \
            {'login_name':data['login_name'],'password':data['password'],'code':data['code'],'nickname':data['nickname']}
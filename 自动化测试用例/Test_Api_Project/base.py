#!/usr/bin/python3
#coding:utf-8

import json
import requests
from Test_Api_Project import settings

class BaseApi(object):
    url = ''
    base_url = settings.API_TEST_BASE_URL

    def __init__(self,url_params=None):
        if not url_params:
            url_params = []
        self.url_params = url_params
        self.response = None
        self.base_url = self.base_url
    #拼接url
    def api_url(self):
        if not self.url:
             raise RuntimeError("no url been set")
        return self._get_url()

    def _get_url(self):
        format_url = self.url.format(self.url_params)
        return "{0}{1}".format(self.base_url,format_url)

    #封装post请求
    def post(self,data=None):
        if not data:
            data = {}
        base_param = self.build_base_param(data)
        custom_param = self.build_custom_param(data)
        data.update(base_param)
        data.update(custom_param)
        self.response = requests.post(url=self.api_url(),data=data,header = settings.HEADERS)
        return self.response


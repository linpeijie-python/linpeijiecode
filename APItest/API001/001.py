#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 8:12
# @Author  : Mark
# @File    : 001.py
# @Software: PyCharm


import requests
corpsecret="FMuZYyBAlTteSDZhsq0qxncu9mAfXpL_4cfwaHpvec0"
corpid="ww1756db8e44d7af76"
def test_token():
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r=requests.get(url).json()
    print(r)
    return r["access_token"]

def test_get():
    token=test_token()
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=LinPeiJie"
    print(requests.get(url).json())

def test_add():
    token=test_token()
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    data = {
        "userid": "linpeijie111",
        "name": "杰哥哥",
        "mobile": "18011892659",
        "department":[1]
    }
    print(requests.post(url,json=data).json())


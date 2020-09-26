#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 9:38
# @Author  : Mark
# @File    : department.py
# @Software: PyCharm
import pytest
import requests
import json

corpsecret="FMuZYyBAlTteSDZhsq0qxncu9mAfXpL_4cfwaHpvec0"
corpid="ww1756db8e44d7af76"
def test001_get_token():
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r=requests.get(url).json()
    print(r)
    return (r['errcode'])
    return r["access_token"]

#新建部门
#@pytest.mark.skip()
def test002_add():
    token = test001_get_token()
    url=f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
    data={
        "name": "广州研发中心",
        "name_en": "GZRD",
        "parentid": 1,
        "order": 1,
        "id": 2

    }
    r=requests.post(url,json=data).json()
    print(r)

#删除部门
#@pytest.mark.skip()
def test003_deleted():
    token = test001_get_token()
    url=f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id=2"
    r=requests.get(url).json()
    print(r)

#获取部门列表
def test004_get():
    token = test001_get_token()
    url=f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}"
    r=requests.get(url).json()
    print(r)

#更新部门
def test005_update():
    token = test001_get_token()
    url=f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
    data={
        'id': 1,
        'name': '小白羊',
        'order': 100000000
    }
    r=requests.post(url,json=data).json()
    print(r)



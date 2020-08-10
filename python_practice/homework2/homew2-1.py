#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 3:05
# @Author  : Mark
# @File    : homew2-1.py
# @Software: PyCharm
from python_practice.homework2.homework2 import TongLao
class XuZhu(TongLao):
    def __init__(self,name,HP,force,ememy_hp,ememy_force):
        super().__init__(name,HP,force,ememy_hp,ememy_force)
    def read(self,name):
        print("罪过罪过")
xuzhu=XuZhu("xuzhu",300,20,350,35)
xuzhu.read("虚竹")

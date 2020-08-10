#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 1:01
# @Author  : Mark
# @File    : homework1.py
# @Software: PyCharm
#python实战二--》#作业1
class star():
    def __init__(self,name,team,location,year):
        self.name=name
        self.team=team
        self.location=location
        self.year=year
    def stars(self):
        print(f"球星是名字：{self.name}",f"球队是：{self.team}",f"场上位置是：{self.location}",f"当前年龄是：{self.year}")

class superstar(star):
    def __init__(self,name,team,location,year):
        super().__init__(name,team,location,year)
    def young(self):
        if self.year>30:
            print(f"{self.name}老了")
        else:
            print(f"{self.name}还年轻")

Star=star("C罗","尤文图斯","前锋",30)
Star.stars()
youngstar=superstar("C罗","尤文图斯","前锋",30)
youngstar.young()


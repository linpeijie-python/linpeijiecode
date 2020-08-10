#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 10:01
# @Author  : Mark
# @File    : python_oo.py
# @Software: PyCharm
#面向对象
class House:
    #静态属性-》变量,类变量,在类之中，方法之外
    door = "red"
    floor = "white"
    #构造函数，是在类实例化的时候直接执行
    def __init__(self):
    #实例变量，类变量中，方法之内，以self.变量名的方式去定义，实例变量的作用域为这个类中的所有方法
        print(self.door)
        self.yangtai = "大"

    #动态属性-》方法（函数）
    def sleep(self):
        print(self.yangtai)
        #普通变量，在类之中，方法之中，并且不会以self.
        self.shuijiao = "房子是用来睡觉的"


    def cook(self):
        print(self.yangtai)
        print(self.shuijiao)
        print("房子可以做饭吃")
#实例化--》变量=类（）
north_house =House()
north_house.sleep()
north_house.cook()
china_house =House()
#调用类变量
print(House.door)
House.door = "yellow"
north_house.door="black"
print(north_house.door)
#图纸的door是什么颜色？
print(House.door)
#china_house的door是什么颜色？
print(china_house.door)
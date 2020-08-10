#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 23:25
# @Author  : Mark
# @File    : bicycle.py
# @Software: PyCharm

class Bicycle:
    def run(self,km):
        print(f"一共用脚骑了{km}公里,累死了")

#电动自行车类EBicycle继承自Bicycle
class EBicycle(Bicycle):
    #如果属性需要传参定义，可以使用构造函数
    def __init__(self,valume):
        self.valume=valume
    def fill_charge(self,vol):
        self.valume=self.valume+vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")

    def run(self,km):
        #1.获得目前电量所能电动骑行的最大里程数
        power_km=self.valume*10
        if power_km>=km:
            print(f"我使用电瓶电量起来{km}公里")
        else:
            print(f"我使用电瓶骑行了{power_km}")
            super().run(km-power_km)

ebike=EBicycle(10)
#ebike.valume(3)
#ebike.fill_charge(200)
ebike.run(500)



#bike = Bicycle()
#bike.run(10)
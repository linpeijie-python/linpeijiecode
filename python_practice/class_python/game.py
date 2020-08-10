#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 0:07
# @Author  : Mark
# @File    : game.py
# @Software: PyCharm
class Game():
    # 初始化战斗回合
    def __init__(self,my_hp,your_hp):
        self.my_hp=my_hp
        self.my_power=200
        self.your_hp=your_hp
        self.your_power=199
        self.fight_round = 1
    def fight(self):
        while True:
            # 计算我的剩余血量
            self.my_hp = self.my_hp - self.your_power
            # 输出当前轮次我剩余血量值
            print("第", self.fight_round, "轮后，我的剩余血量是：", self.my_hp)

            # 计算敌人的剩余血量
            self.your_hp = self.your_hp - self.my_power
            # 输出当前轮次敌人剩余血量值
            print("第", self.fight_round, "轮后，敌人的剩余血量是：", self.your_hp)

            # 计算战斗汇合
            self.fight_round = self.fight_round + 1

            # 判断谁先输
            # 我的血量是否<=0
            if self.my_hp <= 0:
                # 如果我的血量<=0，输出我输了
                print("我输了!")
                # 成立则跳出循环并且结束
                break
            # 判断敌人血量是否<=0
            elif self.your_hp <= 0:
                # 如果敌人的血量<=0，输出我赢了
                print("我赢了！")
                # 成立则跳出循环并且结束
                break

class Houyi(Game):
    #如果重名的话，子类的属性会覆盖掉父类的属性
    def __init__(self,my_hp,your_hp):
        self.defense=100
        #继承父类的构造方法，如果父类的构造方法有形参，需要传递参数
        super().__init__(my_hp,your_hp)
    def fight(self):
        while True:
            # 计算我的剩余血量
            self.my_hp = self.my_hp +self.defense- self.your_power
            # 输出当前轮次我剩余血量值
            print("第", self.fight_round, "轮后，我的剩余血量是：", self.my_hp)

            # 计算敌人的剩余血量
            self.your_hp = self.your_hp - self.my_power
            # 输出当前轮次敌人剩余血量值
            print("第", self.fight_round, "轮后，敌人的剩余血量是：", self.your_hp)

            # 计算战斗汇合
            self.fight_round = self.fight_round + 1

            # 判断谁先输
            # 我的血量是否<=0
            if self.my_hp <= 0:
                # 如果我的血量<=0，输出我输了
                print("我输了!")
                # 成立则跳出循环并且结束
                break
            # 判断敌人血量是否<=0
            elif self.your_hp <= 0:
                # 如果敌人的血量<=0，输出我赢了
                print("我赢了！")
                # 成立则跳出循环并且结束
                break


houyi=Houyi(1000,1300)
#demo2=Houyi
houyi.fight()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 1:01
# @Author  : Mark
# @File    : homework2.py
# @Software: PyCharm
class TongLao():
    def __init__(self,name,HP,force,ememy_hp,ememy_force):
        self.HP=HP
        self.force=force
        self.name=name
        self.ememy_hp = ememy_hp
        self.ememy_force = ememy_force
    def see_people(name):
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("路过，我不认识你")
    def fight_zms(self):
        self.force=self.force*10
        self.HP=self.HP/2
        print(f"{self.name}使用天山天山折梅手",f"当前武力值为{self.force}", f"当前血量是{self.HP}")
    def fight(self):
        while True:
            self.HP=self.HP-self.ememy_force
            self.ememy_hp=self.ememy_hp-self.force
            if self.HP>self.ememy_hp:
                print("敌人输了")
                break
            else:
                print("我输了")
                break
if __name__ == '__main__':
    winner=TongLao("无崖子",300,20,350,35)
    winner.see_people()
    winner.fight()






"""
题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = my_hp - enemy_power
enemy_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

"""
思路：
1、自定义一个关键字函数，后续调用关键字函数可以输入对应的角色血量值和角色的攻击力
2、定义方法fight，游戏规则：
    初始化回合数
    角色血量=初始血量-对方攻击力
    每一轮攻击完成后使用while（true）进行比较，判断是否有角色血量为0
    如果有角色血量为0，则break输出对应结果
"""

#自定义关键字函数
def fight(my_hp,enemy_hp,my_power,enemy_power):
    # 初始化战斗回合
    fight_round = 1

    while True:
        # 计算我的剩余血量
        my_hp = my_hp - enemy_power
        #输出当前轮次我剩余血量值
        print("第", fight_round, "轮后，我的剩余血量是：", my_hp)

        # 计算敌人的剩余血量
        enemy_hp = enemy_hp - my_power
        #输出当前轮次敌人剩余血量值
        print("第", fight_round, "轮后，敌人的剩余血量是：", enemy_hp)

        # 计算战斗汇合
        fight_round = fight_round + 1

        # 判断谁先输
        # 我的血量是否<=0
        if my_hp <= 0:
            #如果我的血量<=0，输出我输了
            print("我输了!")
            #成立则跳出循环并且结束
            break
        #判断敌人血量是否<=0
        elif enemy_hp <= 0:
            # 如果敌人的血量<=0，输出我赢了
            print("我赢了！")
            # 成立则跳出循环并且结束
            break

# 调用自定义函数
fight(1000,800,200,200)
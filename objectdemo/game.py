#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
一个回合制游戏，每个角色都有hp（血量） 和 power（攻击力），hp初始值1000,power初始值200
定义一个fight 方法
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
2个hp 进行对比，血量剩余多的人获胜
'''

def game():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1200
    enemy_power = 199


    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(my_hp)
        print(enemy_hp)

        # if my_final_hp > enemy_final_hp:
        #     print("我赢了")
        # else:
        #     print("我输了")
#三木表达式
        # print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")
        if my_hp <= 0:
            print("我输了")
            break
        if enemy_hp <= 0:
            print("我赢了")
            break


game()

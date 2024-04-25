#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
代码优化--继承
后裔，后裔继承了Game 的 hp ,power,并多了护甲属性
重新定义另一个defense 属性：
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp -power
2个人的Hp 进行对比，血量先为零的输掉比赛
'''

class Game:
    # my_hp = 1000
    my_power = 200
    # enemy_hp = 1200
    enemy_power = 199

    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)
            print(self.enemy_hp)

            # if my_final_hp > enemy_final_hp:
            #     print("我赢了")
            # else:
            #     print("我输了")
            # 三木表达式
            # print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break

    def back_home(self):
        print("回城")


class HouYi(Game):
    def __init__(self, defense, my_hp, enemy_hp):
        self.defense = defense
        super().__init__(my_hp, enemy_hp)

    def fight(self):

        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)
            print(self.enemy_hp)

            # if my_final_hp > enemy_final_hp:
            #     print("我赢了")
            # else:
            #     print("我输了")
            # 三木表达式
            # print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break

houyi = HouYi(200,1000,1500)
houyi.fight()
houyi.back_home()

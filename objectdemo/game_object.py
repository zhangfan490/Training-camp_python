#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
设计一个回合制游戏（面向对象），每个角色都有hp（血量） 和 power（攻击力），hp初始值1000,power初始值200
定义一个fight 方法
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
2个hp 进行对比，血量剩余多的人获胜
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


class HouYi(Game):

        def __init__(self, defense, my_hp, enemy_hp):
            self.defense = defense
            #子类的构造方法中调用父类的构造方法（_init_方法），
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


houyi = HouYi(200, 1000, 1500)
houyi.fight()

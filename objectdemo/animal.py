#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
1.写一个面向对象的例子：
创建一个类（Animal）[动物类]，类属性（名称，颜色，年龄，性别），类方法（叫，跑）
创建子类[猫]，继承[动物类]
复写父类_init_方法，继承父类的属性
增加一个新的属性，毛发=短毛
增加一个新的方法，会桌老鼠
复写父类的【会叫】的方法，改成【喵喵叫】

创建子类[狗]，继承[动物类]
复写父类_init_方法，继承父类的属性
增加一个新的属性，毛发=长毛
增加一个新的方法，会看家
复写父类的【会叫】的方法，改成【汪汪叫】

调用_name_ == “_main_”: 创建一个猫的实例，调用会捉老鼠的方法，打印【猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
创建一个狗的实例，调用会看家的方法，打印【狗的姓名，颜色，年龄，性别，毛发】

2.将数据配置到yaml文件里
'''
import yaml


class Animal:
    name: str = None
    color: str = 'black'
    age: int = 1
    gender: str = '公'

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def cray(self):
        print(f"{self.name} is craying")

    def run(self):
        print(f"{self.name} is running")


class Cat(Animal):
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name} 会捉老鼠")

    def cray(self):
        print(f"{self.name}喵喵叫")


class Dog(Animal):
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name} 会看家")

    def cray(self):
        print(f"{self.name}汪汪叫")


if __name__ == '__main__':
    with open("animal.yml") as f:
        datas = yaml.safe_load(f)
    # print(datas)
    hair = datas['default']['hair']
    name = datas['default']['name']
    color = datas['default']['color']
    age = datas['default']['age']
    gender = datas['default']['gender']

    cat = Cat(hair, name, color, age, gender)
    print(cat.name)
    print(f"他的名字: {name},颜色: {color},年龄: {age},性别: {gender},毛发: {hair}")

    cat.skill()
    cat.cray()





    # mm = Cat()
    # mm.skill()



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
类
1.属性：姓名，性别，年龄，存款金额....
2.方法：吃，睡觉，跑....
'''


class Person:
    #类变量：name,age,gender,money
    name: str = None
    age: int = 18
    gender: str = '男'
    __money: float = 0

    #构造函数 方法；  self类方法,类方法调用传参，self代表实例本身
    def __init__(self,name,age,gender,money):
        print("构造函数")
        #self.变量  实例化变量（实例变量赋值）
        self.name = name
        self.age = age
        self.gender = gender
        #私有属性的定义加 __
        self.__money = money

    def eat(self):
        print(f"{self.name} is eating")

    # 类不能直接调用方法，如果想使用，需要在方法前面加 @classmethod
    @classmethod
    def sleep(self):
        print("sleeping")

    def run(self):
        print(f"{self.name} is running")


class FunnyMan(Person):
    skill: str = ""

    def __init__(self,skill,name,age,gender,money):
        self.skill = skill
        #通过super这个方法来访问父类的对象（子类继承父类init方法）
        super().__init__(name,age,gender,money)


    def fun(self):
        print(f"{self.name} is funny,his skill is {self.skill}")

st = FunnyMan("单口相声","ST", 30,"男",1000)

print(st.name)
st.run()
st.fun()




# p_ls = Person("李四","18","女","2000")
# print(p_ls.name)

# #实例化对象
# p_zs = Person()
# print(p_zs.name)
# p_zs.run()
#
# print(Person.age)
# #类不能直接调用方法，如果想使用，需要在方法前面加 @classmethod
# Person.sleep()

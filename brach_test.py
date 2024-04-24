#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
# a = 3
# if a == 0:
#     print('a = 0')
# else:
#     print('a != 0')

'''
求和：1~100
分支结构实现：求和：1~100 之间的偶数
使用Python实现：求和：1~100 之间的偶数
猜数字

生成一个平方列表，如[1,4,9...]，使用for 循环怎么写，使用列表推导式怎么写

A >= 90
80 <= B <90
60 <= C <80
D < 60
'''

'''
member = ['小甲鱼', 88, '黑夜', 90, '米兔', 85, '已经', 90, '斜阳', 88] 利用for循环打印member 列表中的每一个内容
小甲鱼
88
黑夜
90
米兔
85
已经
90
斜阳
88

讲上述内容打印成
小甲鱼 88
黑夜 90
米兔 85
已经 90
斜阳 88

用2种方法打印 0到9 各个数的平方，然后放在列表里
'''


'''
# list1 = ['1.Just do it','2.一切皆有可能','3.让变成改变世界','4.Impossible is nothing']
# list2 = ['4.阿迪达斯','2.李宁','3.鱼c工作室','1.耐克']
# list3 = [xxxx]
# '''
str1 = '<a href = "http://www.fishc.com/dvd" target = "_blank">'
print(str1[16:29])








# member = ['小甲鱼', 88, '黑夜', 90, '米兔', 85, '已经', 90, '斜阳', 88]
# print(member[0])
# print(member[1])

# for i in member:
#     print(i)
#
# #(len(member)函数返回的是列表中元素的数量
# for i in range(len(member)):
#     # print(i)
#     if i % 2 == 0:
#     #member[i]列表索引
#         print(member[i],member[i + 1])



#
# list1 = ['1.Just do it', '2.一切皆有可能', '3.让变成改变世界', '4.Impossible is nothing']
# list2 = ['4.阿迪达斯', '2.李宁', '3.鱼c工作室', '1.耐克']
# list3 = []
#
# for slogan in list1:
#     # print(slogan)
#     print(slogan[0])
#
# for name in list2:
#     print(name[0])
#
#
#
# for slogan in list1:
#     for name in list2:
#         #判断前面的数字是否是一一对应的；0可以让list1和list2中数字相同的一一对应
#         if slogan[0] == name[0]:
#             #slogan[2:]分割出slogan中的1.2.3.4.
#             list3.append((name + ':' + slogan[2:]))
# for each in list3:
#     print(each)









# f = open('C:\\test.txt', 'wb')
# f.write('I love FishC.com \n')
# f.close()

# def my_fun1():
#     x = 5
#     def my_func2():
#         x *= x
#         return x
#     return my_func2()
#
# my_fun1()

# list = [5,1,3,4,2]
# list1 = list.sort()
# print(list1)
# class MyException(Exception):
#     def __int__(self,msg):
#         print(f"这是一个异常：{msg}")
#
# def set_age(num):
#     if num <= 0 or num > 200:
#         raise MyException(f"值错误:{num}")
#
#     else:
#         print(f"设置的年龄为：{num}")
# set_age(-10)
# for n
# list1 = []
# for i in range(0,10):
#     list1.append(i **2)
# print(list1)
#
# #列表推导式
# list1 = [i ** 2 for i in range(10)]
# print(list1)


# member = ['小甲鱼', 88, '黑夜', 90, '米兔', 85, '已经', 90, '斜阳', 88]

# for i in member:
#     print(i)

# for i in range(len(member)):
#     if i % 2 == 0:
#         print(member[i],member[i + 1])


# namelist = ['lili', 'tom', 'coco']
# print(f'my list is {namelist}')
# # print('our name :{},{} and {}'.format(*namelist))









#
# while True:
#     score = int(input("请输入一个分数："))
#     if score >= 90:
#         print('A')
#     elif 80 <= score < 90:
#         print('B')
#     elif 60 <= score < 80:
#         print('C')
#     elif 0 <= score < 60:
#         print('D')
#     else:
#         print('输入错误！')








# for i in range(1,101,2):
#     print(i)
# from baidu import search
#
# search()
#
# print(dir())

# list1 = []
# for i in range(1,4):
#     list1.append(i ** 2)
# print(list1)
#
# #列表推导式
# list2 = [i ** 2 for i in range(1,4)]
# print('list2',list2)

# list3 = []
# for i in range(1,4):
#     if i != 1:
#         list3.append(i ** 2)
# print(list3)

# list3 = [i ** 2 for i in range(1,4) if i != 1]
# print(list3)
# list_h = [1,3,2,9,0]
# # list_h.sort(reverse=True)
# list_h.reverse()
# print(list_h)




# def func2(a=1):
#     print("这是一个参数a",a)
#
# func2(3)



#定义函数

# def func1(a,b,c):
#     print("这是一个参数a:",a)
#     print("这是一个参数b:",b)
#     print("这是一个参数c:",c)
#
# #函数的调用
# func1(4,5,6)




# import random
# # personal_num = 0
# comuter_num = random.randint(1,101)
# # print(comuter_num)
# while True:
#     personal_num = int(input("请输入一个数："))
#     if personal_num > comuter_num:
#         print("小一点")
#     elif personal_num < comuter_num:
#         print("大一点")
#     elif personal_num == comuter_num:
#         print("猜对了")
#         break
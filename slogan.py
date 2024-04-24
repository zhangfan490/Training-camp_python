#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
list1 = ['1.Just do it', '2.一切皆有可能', '3.让变成改变世界', '4.Impossible is nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼c工作室', '1.耐克']
list3 = []
最终实现：
1.耐克:Just do it
2.李宁:一切皆有可能
3.鱼c工作室:让变成改变世界
4.阿迪达斯:Impossible is nothing
'''


list1 = ['1.Just do it', '2.一切皆有可能', '3.让变成改变世界', '4.Impossible is nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼c工作室', '1.耐克']
list3 = []

for slogan in list1:
    # print(slogan)
    print(slogan[2:])




for slogan in list1:
    for name in list2:
        #判断前面的数字是否是一一对应的；0可以让list1和list2中数字相同的一一对应
        if slogan[0] == name[0]:
            #slogan[2:]分割出slogan中的1.2.3.4.
            list3.append((name + ':' + slogan[2:]))
for each in list3:
    print(each)
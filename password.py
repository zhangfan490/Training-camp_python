#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
设计验证密码程序_小甲鱼——分支和循环,用户只有3次机会输入错误，不过如果用户输入的内容中包含“*”则不计算在内。
'''

count = 3
password = "FishC.com"

while count:
    passwd = input("请输入密码：")
    if passwd == password:
        print("密码正确，进入程序...")
        break
    else:
        print("密码输入错误")
        if "*" in passwd:
            print(f"密码中不能含有'*'号！您还有{count}次机会！")
            continue
        else:
            print(f"输入错误，您还有{count-1}次机会！")

    count -= 1
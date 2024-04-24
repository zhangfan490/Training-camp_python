#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco

'''
1.拥有礼物的标识
2.定义发礼物的方法
3.定义展示礼物的方法
4.启动方法
'''

# 1.拥有礼物的标识

have_gift = False


# 2.定义发礼物的方法

def send():
    print("发礼物了")
    global have_gift
    have_gift = True


# 3.定义展示礼物的方法

def show():
    if have_gift == True:
        print("收到礼物，好开心")
    else:

        print("没有礼物")


# 4.启动方法
if __name__ == '__main__':
    send()
    show()
print(locals())
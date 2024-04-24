#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco

'''
原有存款 1000元，发工资后存款变为2000元：定义模块
1.money.py save_money = 1000
2.定义发工资模块send_money,用来增加收入计算
3.定义工资查询模块select_monkey，展示工资数额
4.定义一个start.py启动文件展示最终存款金额
'''

# 原有存款
save_money = 1000


# 定义发工资模块

def send_money():
    send_money = 1000
    global save_money
    print(f"发工资前，有存款为{save_money}")
    save_money = save_money + send_money


# 定义查询模块

def select_money():
    if save_money == 2000:
        print(f"发工资啦，现有存款为{save_money}")
    else:
        print('没有发工资')


if __name__ == '__main__':
    send_money()
    select_money()

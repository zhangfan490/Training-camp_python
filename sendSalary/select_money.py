#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco

#工资查询模块
import money


def select_money():
    if money.save_money == 2000:
        print(f"发工资后，现有存款{money.save_money}")
    else:
        print("没有发工资")
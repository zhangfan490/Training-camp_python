#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco

# 3.定义展示礼物的方法
import gift


def show():
    have_gift = gift.have_gift
    if have_gift == True:
        print("收到礼物，好开心")
    else:

        print("没有礼物")

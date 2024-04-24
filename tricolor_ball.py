#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配
'''

#8个球中红球可能出现的个数
for red in range(0, 4):
    for yellow in range(0, 4):
        #range(2,7)产生[2,3,4,5,6],如果绿球是1个，红球+黄球需要有7个才能符合要求，所以绿球不能是1个
        for green in range(2, 7):
            if red + yellow + green == 8:

                #  \t是制表符的含义
                print(red, '\t', yellow, '\t', green)


# for red in range(0, 4):
#     for yellow in range(0, 4):
#         for green in range(2, 7):
#             if red + yellow + green == 8:
#                 print('red'*red, end="")
#                 print('yellow'*yellow, end="")
#                 print('green'*green, end="")

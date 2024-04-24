#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
请写一个进制转换程序，程序演示如下：
请输入一个整数（输入Q结束程序）:108
十进制 -> 十六进制：108 -> 0x6c
十进制 -> 八进制：108 -> 0o154
八进制 -> 二进制：108 ->  0b1101100
请输入一个整数（输入Q结束程序）:Q
'''

q = True
while q:
    num = input('请输入一个整数（输入Q结束程序）:')
    if num != 'Q':
        num = int(num)
        print('十进制 -> 十六进制：%d -> 0x%x' % (num, num))
        print('十进制 -> 八进制：%d -> 0o%o' % (num, num))
        # bin()返回一个整数int或者长整数 long int 的二进制表示
        print('八进制 -> 二进制：%d -> ' % num, bin(num))
    else:
        q = False

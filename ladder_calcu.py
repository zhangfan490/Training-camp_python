#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
有一个长阶梯，若每step上2节，最后剩余1节；若每step上3节，最后剩余2节；若每step上5节，最后剩余4节；若每step上6节，最后剩余5节；只有每部上7节，最后刚好不剩。
该台阶至少有多少节？
'''

def step_num(n):
    print("在1 - %d之间的阶梯数为：" %n)
    sum = 0
    for i in range(7, n+1):
        #阶梯数满足的条件
        if (i %7 == 0) and (i %6 == 5) and (i %5 == 4) and (i %3 == 2):
            sum += 1
            print("%d" %i)
    print("在1- %d之间，有%d个数可以满足爱因斯坦对阶梯的要求" %(n, sum))

if __name__ == "__main__":
    while True:
        n = int(input("请输入n值："))
        print(f"输入的n值是：{n}")
        step_num(n)
        break
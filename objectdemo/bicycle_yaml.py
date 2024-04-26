#!/usr/bin/env python
# -*- coding: utf-8 -*-
# creat by Pycharm
# @python-version 3.8.10
# @author coco
'''
写一个Bicycle(自行车)类，有 run方法，调用时显示骑行里程km(骑行里程为传入的数字)
在写一个电动自行车类EBicycle 继承Bicycle，添加电池电量battery_level 属性通过传参传入，同时有2个方法：
1.fill_charge(vol)用来充电， vol 为电量
2.run(km)方法用于骑行，每骑行10Km 消耗1度电，当电量耗尽调用Bicycle 的 run方法骑行
通过传入骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑行里程数）
'''
import yaml


class Bicycle:
    def run(self, km):
        print(f"骑行里程数为：{km}km")


class EBicycle(Bicycle):
    def __init__(self, battery_level):
        # 初始化电量
        self.battery_level = battery_level

    def fill_charge(self, vol):
        # 充电
        self.battery_level = self.battery_level + vol

    def run(self, km):
        # 用电骑行，用脚蹬
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f"已经使用电骑行:{self.battery_level * 10}km")
            #调用父类方法，用脚蹬的里程数
            bicycle = Bicycle()
            bicycle.run(miles)
            # super().run(miles)

        else:
            print(f"已经使用电骑行:{km}km")


if __name__ == '__main__':
    with open("bicycle_config.yml") as f:
        # yaml.safe_load(f) 中的 f 和上面的 with open () as f 对应，属于常规写法
        datas = yaml.safe_load(f)

    print(datas)
    # 打印'e1_level'的数据
    # print(datas['e1_level'])

    # 'e1_level'中的'battery_level'和 'run_km'
    battery_level = datas['default']['battery_level']
    run_km = datas['default']['run_km']

    #实例化
    eb = EBicycle(battery_level)
    eb.run(run_km)

    # eb = EBicycle(10)
    # eb.run(101)
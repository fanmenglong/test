#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-12 16:48
# @Author  : Lone
# @File    : averager.py


class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

# 闭包
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

# 闭包 使用自由变量 nonlocal
def make_averager_v2():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager


if __name__ == '__main__':

    avg = make_averager_v2()
    print(avg(10))
    print(avg(11))
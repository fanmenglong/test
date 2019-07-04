#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-28 20:05
# @Author  : Lone
# @File    : coroaverager0.py

from coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        count += 1
        total += term
        average = total/count

coro_avg = averager()
next(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(20))
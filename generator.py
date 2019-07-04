#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-07-02 14:29
# @Author  : Lone
# @File    : generator.py

def generator(n):
    i = 1
    while True:
        yield i**n
        i += 1

gen_1 = generator(1)
gen_3 = generator(3)

def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {} next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1*sum_1, sum_3)

get_sum(8)
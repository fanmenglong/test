#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-12 14:55
# @Author  : Lone
# @File    : deco_test.py

promos = []

def promition(func):
    promos.append(func)
    return func

@promition
def fun1():
    pass
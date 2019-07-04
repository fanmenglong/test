#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-10 21:15
# @Author  : Lone
# @File    : dict_test.py

from functools import partial
from operator import mul

triple = partial(mul, 3)

print(list(map(triple, range(5))))
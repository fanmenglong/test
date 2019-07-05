#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-07-01 11:03
# @Author  : Lone
# @File    : text.py
import time
from threading import Thread

import time
from tqdm import tqdm

for i in tqdm(range(1000)):
    time.sleep(.01)
    print('')
    print("work in dev branch")
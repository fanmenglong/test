#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-27 17:24
# @Author  : Lone
# @File    : sentence.py

import re
import abc
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = Sentence('"I love you forever", the Lone said')
it = iter(s)

while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


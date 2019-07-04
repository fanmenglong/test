#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-06 15:04
# @Author  : Lone
# @File    : card.py

from collections import namedtuple
from random import choice
import array
import os

Card = namedtuple("Card", ["suit", "rank"])


class MyCard:

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "♠️ ♥️ ♣️ ♦️".split()

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __repr__(self):
        return "MyCard"

card = MyCard()
print(card)
print(len(card))
print(card[12::13])
# for c in card:
#     print(c)
# cnt = 0
# while True:
#     one_card = choice(card)
#     if one_card.suit == "♠️" and one_card.rank == "A":
#         print("You got ♠️A")
#         break
#     cnt += 1
#
# print(cnt)

_, filename = os.path.split("./txt.txt")
print(filename)

a, b, *rest = range(2)

print(b)
print(rest)
print("{:<30}".format("Center"))
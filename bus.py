#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-12 21:21
# @Author  : Lone
# @File    : bus.py
class TwilightBus:
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def print(self):
        print(self.passengers)


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']

bus = TwilightBus(basketball_team)

bus.drop('Tina')
bus.pick('Lone')
bus.print()

print(basketball_team)

print('I love {Lone:.2f}'.format(Lone=0.1234))
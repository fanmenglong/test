#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2019-06-27 21:30
# @Author  : Lone
# @File    : aritprog_gen.py
import itertools
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step*index

print(list(aritprog_gen(1, .5, 3)))

def fun(target):
    n, a, b = 0, 0, 1
    while n < target:
        yield b
        a, b = b, a+b
        n += 1

f = fun(6)
print(list(f))

print(len(list(itertools.product('abc', repeat=3))))
print(list(itertools.permutations('abc', 3)))

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss or len(ss)==0:
            return ss

        res = list(itertools.permutations(ss, 3))
        ans = []
        for i in res:
            ans.append(''.join(i))

        return ans

s = Solution()


print(s.Permutation('abc'))
print(all(f))
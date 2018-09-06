#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:46:17 2018
@author: sabbir

"""

from math import gcd

def lcm(a, b):
     return a * b // gcd(a, b)

res = 1
for i in range(2, 21):
     res = lcm(res, i)
print('The result is = ', res)
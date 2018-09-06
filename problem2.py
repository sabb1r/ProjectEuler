#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 12:13:14 2018
@author: sabbir

"""

first = second = 1
res = 0
while first < 4000000:
    if not first % 2:
        res = res + first
    first, second = second, first + second
print("The result is = ", res)
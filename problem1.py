#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 12:07:44 2018
@author: sabbir

"""

i, res = 1, 0
while i < 1000:
    if i%3 == 0 or i%5 == 0:
        res += i
    i += 1
print('The result is = ', res)
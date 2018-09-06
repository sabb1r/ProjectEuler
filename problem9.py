#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:13:58 2018
@author: sabbir

"""

n = 1000 // 2
m = 1000 // 3

for num1 in range(n-1, m+1, -1):
     for num2 in range(num1-1, m-1, -1):
          num3 = 1000 - num1 - num2
          if num1 ** 2 == num2 ** 2 + num3 ** 2:
               print('The result is = ', num1 * num2 * num3)
               break
     else:
          continue
     break

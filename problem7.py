#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:04:26 2018
@author: sabbir

"""
from math import sqrt
def is_prime(num):
     if num < 2:
          return False
     elif num == 2:
          return True 
     elif num % 2 == 0:
          return False
     for i in range(3, int(sqrt(num))+1, 2):
          if num % i == 0:
               return False
     else:
          return True
     
start = 1    # 2 is already counted
i = 3
while start != 10001:
    if is_prime(i):
        start += 1
    i = i + 2
print('The answer is = ', i-2)
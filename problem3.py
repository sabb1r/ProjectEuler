#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 12:24:44 2018
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

dividend = 600851475143
res = 0
for divisor in range(2, int(sqrt(dividend))+1):
     quotient, rem = dividend // divisor, dividend % divisor
     if rem == 0:
          if is_prime(quotient):
               print('The result is = ', quotient)
               break
          elif is_prime(divisor) and divisor > res:
               res = divisor
else:
     print('The result is = ', res)
               
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:18:08 2018
@author: sabbir

"""
# %% Assisting Functions

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
     
# %% Main Code
          
res = 2 # Prime number 2 is added initially
i = 3
while i < 2000000:
    if is_prime(i):
        res = res + i
    i = i + 2
print('The answer is =', res)
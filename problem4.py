#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:04:01 2018
@author: sabbir

"""

def is_palindrome(num):
     if str(num) == str(num)[::-1]:
          return True
     else:
          return False

res = []
num1 = 999
while num1 >= 100:
     num2 = num1
     while num2 >= 100:
          prod = num1 * num2
          if is_palindrome(prod):
               res.append(prod)
          num2 -= 1
     num1 -= 1

print('The result is = ', max(res))

          
          
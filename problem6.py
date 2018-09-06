#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:01:53 2018
@author: sabbir

"""

n = 100
sqr_sum = n*(n+1)*(2*n+1)//6
sum_sqr = (n*(n+1)//2)**2
print('The result is = ',abs(sqr_sum-sum_sqr))
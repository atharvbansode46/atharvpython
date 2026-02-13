# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 15:42:43 2026

@author: User
"""

year=int(input("enter year:"))
if(year % 400 ==0) or (year % 4== 0 and year % 100 !=0):
    print("leap year")
else:
    print("not a leap year")
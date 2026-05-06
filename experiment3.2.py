# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:23:36 2026

@author: Atharv Bansode
"""

def simple_interest(principal, rate, time):
  si = (principal * rate * time) / 100
  return si
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
interest = simple_interest(p, r, t)
print("Simple Interest is:", interest)
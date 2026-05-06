# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:11:54 2026

@author: Atharv Bansode
"""

purchases = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for item in purchases:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Item frequency:", frequency)
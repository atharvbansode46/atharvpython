# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:07:23 2026

@author: Atharv Bansode
"""

# Taking prices from user

prices = []

n = int(input("Enter number of products: "))

for i in range(n):
    price = int(input("Enter price: "))
    prices.append(price)

total_bill = sum(prices)

print("Total bill amount:", total_bill)
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:16:54 2026

@author: Atharv Bansode
"""

try:
    with open("complaints.txt", "r") as file:
        print("List of Complaints:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Complaint file not found.")
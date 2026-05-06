# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:05:41 2026

@author: Atharv Bansode
"""

marks = [78, 85, 90, 67, 88]
total = sum(marks)

#length of students
count = len(marks)

# Calculating average
average = total / count

# Finding topper marks (maximum marks)
topper = max(marks)

# Displaying the results
print("Marks of students:", marks)
print("Average marks:", average)
print("Topper marks:", topper)
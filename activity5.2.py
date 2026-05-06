# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:11:15 2026

@author: Atharv Bansode
"""

# Roll numbers of students in two classes
class_A = {101, 102, 103, 104, 105}
class_B = {104, 105, 106, 107}

# Find students present in both classes
common_students = class_A.intersection(class_B)

# Output
print("Students present in both classes:", common_students)
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:15:44 2026

@author: Atharv Bansode
"""

with open("attendance.txt", "a") as f:
    for i in range(3):
        name = input("Enter student name: ")
        status = input("Present/Absent: ")
        f.write(name + " - " + status + "\n")

print("Attendance recorded successfully.")
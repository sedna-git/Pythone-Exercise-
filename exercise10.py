# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 00:53:04 2026

@author: Sam-Tech
"""

#تمرین دهم

with open("text.txt", "w", encoding="utf-8") as file:
    file.write("Python Programming")


count = 0

with open("text.txt", "r", encoding="utf-8") as file:
    while True:
        ch = file.read(1) 
        if ch == "":      
            break
        print(ch)          
        count += 1   

print("تعداد کاراکترها:", count)

#چالش
count = 0

with open("text.txt", "r", encoding="utf-8") as file:
    while True:
        ch = file.read(1)
        if ch == "":
            break
     
        if ch.isalpha() and ch.isascii():
            print(ch)
            count += 1

print("تعداد حروف انگلیسی:", count)
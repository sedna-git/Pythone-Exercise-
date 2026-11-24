# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:58:04 2026

@author: Sam-Tech
"""

#تمرین نهم

with open("students.txt","w",encoding="utf-8") as file:
    file.write("سارا\n")
    file.write("ستایش\n")
    file.write("یاسمن\n")
    
with open("students.txt","r",encoding="utf-8") as file:
    print(file.read())
    
name=input("نام را وارد نمایید")
with open("students.txt","a",encoding="utf-8") as file:
    file.write(name+"\n")

with open("students.txt","r",encoding="utf-8") as file:
    print(file.read())    
    
    #چالش
count=0
with open("students.txt","r",encoding="utf-8") as file:
    for line in file.readlines():
         count=count+1
         print(count,"_",line)
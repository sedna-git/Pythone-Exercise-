# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:46:22 2026

@author: Sam-Tech
"""

import tkinter as tk
from tkinter import messagebox,ttk
import os


datafile='task.txt'

#------------عملیات دکمه ها------------

def add_task():
    
    task=enter_task.get()
    if task:
          list_box.insert(tk.END, task)
          enter_task.delete(0, tk.END)
      
      
def del_task():
    selected= list_box.curselection()
    if selected:
        list_box.delete(selected)
        
def del_all():
    list_box.delete(0, tk.END)
    
    
def save_task():
    tasks=list_box.get(0,tk.END)
    with open(datafile,'w',encoding='utf-8') as f:
        for task in tasks:
            f.write(task+"\n")
            
            
            
def lod_task():
    if os.path.exists(datafile):
        with open(datafile,'r',encoding='utf-8') as f:
            for line in f:
                task = line.strip()
                if task:
                    list_box.insert(tk.END, task)
            
            
#--------ساختن پنجره اصلی-----

window=tk.Tk() 
window.title("مدیریت وظایف-TO DO LIST")
window.geometry("600x650")
window.resizable(False,False)

#----------بخش بالایی----------

frame_top=tk.Frame(window).pack(pady=15)
tk.Label(frame_top,text="NEW PLAN:",font=("vazir",13,"bold")).pack()
enter_task=tk.Entry(frame_top,width=35,font=("vazir",11))
enter_task.pack()
btn_add=tk.Button(frame_top,text="Add",font=("vazir",11),bg="green",fg="white",command=add_task)
btn_add.pack()


#----------بخش میانی----------


frame_middle=tk.Frame(window)
frame_middle.pack(fill=tk.BOTH,expand=True,padx=15,pady=5)

list_box=tk.Listbox(frame_middle,height=15,font=("vazir",11) ,selectbackground="#a6a6a6")
list_box.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

scroll=tk.Scrollbar(frame_middle,orient=tk.VERTICAL,command=list_box.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)

list_box.config(yscrollcommand=scroll.set)


#-------بخش دکمه های پایین-------

frame_btn=tk.Frame(window)
frame_btn.pack(pady=15)

btn_del=tk.Button(frame_btn,text="DELET",bg="red",fg="white",width=20,command=del_task)
btn_del.pack(side=tk.LEFT,padx=10)

btn_clear=tk.Button(frame_btn,text="DELET ALL",bg="#ff9800",fg="white",width=20,command=del_all)
btn_clear.pack(side=tk.LEFT,padx=10)

lod_task()


window.protocol('WM_DELETE_WINDOW',lambda:(save_task(),window.destroy()))


window.mainloop()
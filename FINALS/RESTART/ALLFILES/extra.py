from tkinter import *
import tkinter as ttk
import  datetime
import time
import linecache as lc


second_page=Tk()
second_page.geometry("450x450")
second_page.title("ROUTINE ITEMS")
second_page.configure(bg="#FFDE59")

#item naming box
nameitem_frame = LabelFrame(second_page, text="Name Your Item", background="#FFDE59")
nameitem_frame.place(relx=0.5, rely=0.2, anchor=CENTER)

new_item = Label(nameitem_frame, text="Enter Item Name: ", background="#FFDE59")
new_item.grid(row=0, column=0)

item_entry = Entry(nameitem_frame, background="#FFDE59")
item_entry.grid(row=0, column=1)

def checkbitem_name():
    v = open("practicewriting.txt", "w")
    v.write(item_entry.get())
    v.close()
    first_page.destroy()

def gotolist():
    second_page.destroy()

nextpg = Button(second_page, text="Confirm", command=gotolist)
nextpg.place(relx=0.5, rely=0.7, anchor=CENTER)

second_page.mainloop()

from tkinter import *
import tkinter as ttk
import  datetime
import time

fourth = Tk()
fourth.geometry("500x850")

fourth.title("TOTALS")
fourth.configure(bg="#FFDE59")
#for item1-10 if checked = 1, +1 to total score


def close():
    fourth.destroy()


button = Button(fourth, text="Confirm", command=close)
button.place(relx=0.5, rely=0.8, anchor=CENTER)

fourth.mainloop()
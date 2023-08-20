from tkinter import *
import tkinter as ttk
import  datetime
import time
import linecache as lc

#configure window
third=Tk()
third.geometry("500x850")
third.title("HOMESCREEN")
third.configure(bg="#FFDE59")

#logo
img = PhotoImage(file="/Users/andzilem/code 1/EXPERIMENTAL Andzile's DDT Project - Code copy/RESTART/img/gday 250.png")

logo_frame = Frame(third)
logo_frame.place(relx=0.2, rely=0.12, anchor=CENTER)

bg_img = Label(logo_frame, image=img, border=0, borderwidth=0)
bg_img.grid()

d = datetime.datetime.now()
day = d.strftime("%A")

dayoftheweek = ttk.Frame(third)
dayoftheweek.place(relx=0.65, rely=0.1, anchor=CENTER)



name = "andy"

weekday = ttk.Label(dayoftheweek, text="Good Morning " + name + "\nToday is " + day + ". Let's get ready for the day!", background="#FFDE59")
weekday.grid(row=0, column=0)

routines = ttk.Frame(third)
routines.place(relx=0.5, rely=0.3, anchor=CENTER)

routine = ttk.Label(routines, text="Today's Routine", background="#FFDE59")
routine.grid(row=0, column=0)

get_list = open(file="/Users/andzilem/code 1/EXPERIMENTAL Andzile's DDT Project - Code copy/RESTART/DB_list.txt")

item1 = 1
getfile = [next(get_list)for x in range(item1)]
check = Checkbutton(routines, text=getfile, onvalue=1, offvalue=0)
check.grid(row=2, column=0)

file = lc.getline(filename="r.txt",lineno=2)
check = Checkbutton(routines, text=getfile, onvalue=1, offvalue=0 )
check.grid(row=3, column=0)


def gotolastpg():
    third.destroy()
    import GUIxfinish

butto = Button(third, text="Confirm", command=gotolastpg)
butto.place(relx=0.5, rely=0.8, anchor=CENTER)




third.mainloop()
from tkinter import *
import tkinter as ttk
import  datetime
import time
import linecache as lc

first = Tk()
first.geometry("500x850")

first.title("WELCOME")
first.configure(bg="#FFDE59")

img = PhotoImage(file="/Users/andzilem/2023CODE/Final G'DAY project files/RESTART/img/GDAY_logo500.png")  

logo_frame = Frame(first)
logo_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

bg_img = Label(logo_frame, image=img, border=0, borderwidth=0)
bg_img.grid()

rego_frame = Frame(first, background="#FFDE59")
rego_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

welcome = Label(rego_frame, text="Good Morning! \nWelcome to \"G\'DAY\" your morning routine app.", background="#FFDE59")
welcome.grid(row=0, column=0)

name_frame = Frame(rego_frame)
name_frame.grid(row = 1, column=0,columnspan=2)

name_label = Label(name_frame, text="Please enter your name:", background="#FFDE59")
name_label.grid(row=1, rowspan=1, column=0)


name_entry = Entry(name_frame, background="#FFDE59")
name_entry.grid(row=1, column=1)

def users_name():
    name = name_entry.get()
    first.destroy()
    import SECOND_

name_button = Button(rego_frame, text="Confirm", command=users_name)
name_button.grid(row=2, column=0, columnspan=2)


first.mainloop()

#connfigure window
second=Tk()
second.geometry("400x250")
second.title("ROUTINE ITEMS")
second.configure(bg="#FFDE59")

#item naming box
nameitem = LabelFrame(second, text="Name Your Item", background="#FFDE59")
nameitem.place(relx=0.5, rely=0.2, anchor=CENTER)

new_item = Label(nameitem, text="Enter Item Name: ", background="#FFDE59")
new_item.grid(row=0, column=0)

item_entry = Entry(nameitem, background="#FFDE59")
item_entry.grid(row=0, column=1)
#item = item_entry.get()

item_frame = LabelFrame(second, text=("Your Routine Items"), background="#FFDE59")
item_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#routine funtions 
def getroutineitems():
    printing.config(text=item_entry.get())

def error():
    print("not hello")

#maybe a while loop to say under __ amount of charatcers
#or an if loop chsrters no <<< max character numbers

if item_entry.get() == "hello":
    print(item_entry.get()) 
    new = Button(nameitem, text="Add New Item", command=getroutineitems)
    new.grid(row=1, column=0, columnspan=2)
else:
    new = Button(nameitem, text="Add New Item", command=error)
    new.grid(row=1, column=0, columnspan=2)


#I JSUT REMEBERED THAT I HAVE TO MAKE THEM CHECKBTTONS

printing = Checkbutton(item_frame, text=item_entry.get())
printing.grid(row=4, column=1)

def gotolist():
    second.destroy()
    import GUItoday2

nextpg = Button(second, text="Confirm", command=gotolist)
nextpg.place(relx=0.5, rely=0.7, anchor=CENTER)

second.mainloop()


#configure window
third=Tk()
third.geometry("500x850")
third.title("HOMESCREEN")
third.configure(bg="#FFDE59")

#logo
img = PhotoImage(file="/Users/andzilem/2023CODE/Final G'DAY project files/RESTART/img/GDAY_logo250.png")

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

#this is a lot
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

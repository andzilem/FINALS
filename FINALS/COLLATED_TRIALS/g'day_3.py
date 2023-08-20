from tkinter import *
import tkinter as ttk
import  datetime
import time
import linecache as lc

first_page = Tk()
first_page.geometry("450x500")

first_page.title("WELCOME")
first_page.configure(bg="#FFDE59")

logo = PhotoImage(file="/Users/andzilem/2023CODE/Final G'DAY project files/RESTART/img/GDAY_logo500.png")  

logo_frame = Frame(first_page)
logo_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

bg_logo = Label(logo_frame, image=logo, border=0, borderwidth=0)
bg_logo.grid()

rego_frame = Frame(first_page, background="#FFDE59")
rego_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

welcome = Label(rego_frame, text="Good Morning! \nWelcome to \"G\'DAY\" your morning routine app.", background="#FFDE59")
welcome.grid(row=0, column=0)

name_frame = Frame(rego_frame)
name_frame.grid(row = 1, column=0,columnspan=2)

name_label = Label(name_frame, text="Please enter your name:", background="#FFDE59")
name_label.grid(row=1, rowspan=1, column=0)


name_entry = Entry(name_frame, background="#FFDE59")
name_entry.grid(row=1, column=1)


#user name function
def users_names():
    f = open("practicereading.txt", "w")
    f.write(name_entry.get())
    f.close()
    first_page.destroy()


name_button = Button(rego_frame, text="Confirm", command=users_names)
name_button.grid(row=2, column=0, columnspan=2)


first_page.mainloop()

#connfigure window
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

#def checkbitem_name():
    written = open("practicewriting.txt", "w")
    written.write(item_entry.get())
    written.close()
    first_page.destroy()



def gotolist():
    second_page.destroy()

nextpg = Button(second_page, text="Confirm", command=gotolist)
nextpg.place(relx=0.5, rely=0.7, anchor=CENTER)

second_page.mainloop()


#configure window
third_page=Tk()
third_page.geometry("450x600")
third_page.title("HOMESCREEN")
third_page.configure(bg="#FFDE59")

#logo
logo = PhotoImage(file="/Users/andzilem/2023CODE/Final G'DAY project files/RESTART/img/GDAY_logo250.png")

logo_frame = Frame(third_page)
logo_frame.place(relx=0.2, rely=0.12, anchor=CENTER)

bg_logo = Label(logo_frame, image=logo, border=0, borderwidth=0)
bg_logo.grid()

d = datetime.datetime.now()
day = d.strftime("%A")

dayoftheweek = ttk.Frame(third_page)
dayoftheweek.place(relx=0.65, rely=0.1, anchor=CENTER)

f = open("practicereading.txt", "r")

weekday = ttk.Label(dayoftheweek, text="Good Morning " + f.read() + "\nToday is " + day + ".\n Let's get ready for the day!", background="#FFDE59")
weekday.grid(row=0, column=0)
#maybe change good morning good after noon good night depending on the time of day

routines = ttk.Frame(third_page)
routines.place(relx=0.5, rely=0.3, anchor=CENTER)

routine = ttk.Label(routines, text="Today's Routine", background="#FFDE59")
routine.grid(row=0, column=0)

get_list = open(file="/Users/andzilem/2023CODE/Final G'DAY project files/RESTART/DB_list.txt")



check = Checkbutton(routines, text= "yo", onvalue=1, offvalue=0)
check.grid(row=2, column=0)

file = lc.getline(filename="read.txt",lineno=1)
check = Checkbutton(routines, text=file, onvalue=1, offvalue=0 )
check.grid(row=3, column=0)

#from tutorial

C2 = Checkbutton(routines, text = "wake up", onvalue = 1, offvalue = 0, height=5,  width = 20)
C2.grid(row=5, column=0)

def gotolastpg():
    third_page.destroy()

butto = Button(third_page, text="Confirm", command=gotolastpg)
butto.place(relx=0.5, rely=0.8, anchor=CENTER)

third_page.mainloop()



extra fourth = Tk()
fourth.geometry("450x350")

fourth.title("TOTALS")
fourth.configure(bg="#FFDE59")

total = (check_values1 +
check_values2 +
check_values3 +
check_values4 +
check_values5 +
check_values6 +
check_values7 +
check_values8 +
check_values9 +
check_values10 +)

def close():
    fourth.destroy()


button = Button(fourth, text="Confirm", command=close)
button.place(relx=0.5, rely=0.8, anchor=CENTER)

fourth.mainloop()

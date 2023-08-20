from tkinter import *
import tkinter as ttk
import  datetime
import time

#configure first window
first_page = Tk()
first_page.geometry("450x750")

first_page.title("WELCOME")
first_page.configure(bg="#FFDE59")

#setting logo on page
logo = PhotoImage(file="/Users/andzilem/2023CODE/FINALS/img/GDAY_logo500.png")

logo_frame = Frame(first_page)
logo_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

background_logo = Label(logo_frame, image=logo, border=0, borderwidth=0)
background_logo.grid()

#frame that holds name input and welcome message
register_frame = Frame(first_page, background="#FFDE59")
register_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

welcome = Label(register_frame, text="Good Morning! \nWelcome to \"G\'DAY\" your morning routine app.", background="#FFDE59")
welcome.grid(row=0, column=0)

name_frame = Frame(register_frame)
name_frame.grid(row = 1, column=0,columnspan=2)

name_label = Label(name_frame, text="Please enter your name:", background="#FFDE59")
name_label.grid(row=1, rowspan=1, column=0)

name_entry = Entry(name_frame, background="#FFDE59")
name_entry.grid(row=1, column=1)

#function that writes users name in file
def record_name():
    write_name = open("/Users/andzilem/2023CODE/FINALS/TEXT FILES/writing_name.txt", "w")
    write_name.write(name_entry.get())
    write_name.close()
    first_page.destroy()

#button to destroy page and go to the next page
nextpage_button = Button(register_frame, text="Confirm", command=record_name)
nextpage_button.grid(row=2, column=0, columnspan=2)

first_page.mainloop()

#configure second window
second_page=Tk()
second_page.geometry("450x750")
second_page.title("ROUTINE ITEMS")
second_page.configure(bg="#FFDE59")

#frame that holds the item naming entrybox
nameitem_frame = LabelFrame(second_page, text="Name Your Item", background="#FFDE59")
nameitem_frame.place(relx=0.5, rely=0.2, anchor=CENTER)

list_items = Label(nameitem_frame, text="Enter Item Name: ", background="#FFDE59")
list_items.grid(row=0, column=0)

item_list = Entry(nameitem_frame, background="#FFDE59")
item_list.grid(row=0, column=1, rowspan=3, columnspan=3)

#frame with notes on the structure to enter inputs
limit_frame = LabelFrame(second_page, text="Note", background="#FFDE59")
limit_frame.place(relx=0.5, rely=0.3, anchor=CENTER)

info = Label(limit_frame, text="Enter item names seperated by commas. \n Must input exaclty 10 routine items.", background="#FFDE59")
info.grid(row=0, column=0)

#function to write the users routine list
def record_list():
    w = open("/Users/andzilem/2023CODE/FINALS/TEXT FILES/writing_list.txt", "w")
    w.write(item_list.get())
    w.close()
    second_page.destroy()

#button to destroy page and go to the next page
nextpage_button = Button(second_page, text="Confirm", command=record_list)
nextpage_button.place(relx=0.5, rely=0.7, anchor=CENTER)

second_page.mainloop()


#configure third and last window
third_page=Tk()
third_page.geometry("450x750")
third_page.title("HOMESCREEN")
third_page.configure(bg="#FFDE59")

#setting logo on page
logo = PhotoImage(file="/Users/andzilem/2023CODE/FINALS/img/GDAY_logo250.png")

logo_frame = Frame(third_page)
logo_frame.place(relx=0.2, rely=0.12, anchor=CENTER)

background_logo = Label(logo_frame, image=logo, border=0, borderwidth=0)
background_logo.grid()

#retrieving current day of the week
current = datetime.datetime.now()
today = current.strftime("%A")

day = ttk.Frame(third_page)
day.place(relx=0.65, rely=0.1, anchor=CENTER)

#reading file for users name
r = open("/Users/andzilem/2023CODE/FINALS/TEXT FILES/writing_name.txt", "r")

weekday = ttk.Label(day, text="G'Day to you " + r.read() + "\nToday is " + today + ".\n Let's get ready for the day!", background="#FFDE59")
weekday.grid(row=0, column=0)

routine = ttk.Label(third_page, text="Today's Routine", background="#FFDE59")
routine.place(relx=0.2, rely=0.34, anchor=W)

#reading file for routine items
get_list = open(file="/Users/andzilem/2023CODE/FINALS/TEXT FILES/writing_list.txt", mode = "r")

#hold list into a list variable and split using commas for seperating into checkbuttons
list =get_list.read().split(",")

#users final routine as checkbuttons
check1 = Checkbutton(third_page, text= list[0], onvalue=1, offvalue=0, background="#FFDE59")
check1.place(relx=0.2, rely=0.4, anchor=W)

check2 = Checkbutton(third_page, text=list[1], onvalue=1, offvalue=0, background="#FFDE59" )
check2.place(relx=0.2, rely=0.43, anchor=W)

check3 = Checkbutton(third_page, text = list[2], onvalue = 1, offvalue = 0, background="#FFDE59")
check3.place(relx=0.2, rely=0.46, anchor=W)

check4 = Checkbutton(third_page, text=list[3], onvalue=1, offvalue=0, background="#FFDE59" )
check4.place(relx=0.2, rely=0.49, anchor=W)

check5 = Checkbutton(third_page, text = list[4], onvalue = 1, offvalue = 0,background="#FFDE59")
check5.place(relx=0.2, rely=0.52, anchor=W)

check6 = Checkbutton(third_page, text= list[5], onvalue=1, offvalue=0, background="#FFDE59")
check6.place(relx=0.2, rely=0.55, anchor=W)

check7 = Checkbutton(third_page, text=list[6], onvalue=1, offvalue=0, background="#FFDE59")
check7.place(relx=0.2, rely=0.58, anchor=W)

check8 = Checkbutton(third_page, text = list[7], onvalue = 1, offvalue = 0, background="#FFDE59")
check8.place(relx=0.2, rely=0.61, anchor=W)

check9 = Checkbutton(third_page, text=list[8], onvalue=1, offvalue=0, background="#FFDE59")
check9.place(relx=0.2, rely=0.64, anchor=W)

check10 = Checkbutton(third_page, text = list[9], onvalue = 1, offvalue = 0, background="#FFDE59")
check10.place(relx=0.2, rely=0.67, anchor=W)

def destroy():
    get_list.close()
    third_page.destroy()

#button to destroy page
close_button = Button(third_page, text="Confirm",command= destroy)
close_button.place(relx=0.5, rely=0.8, anchor=CENTER)

third_page.mainloop()


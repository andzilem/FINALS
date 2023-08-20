from tkinter import *

first = Tk()
first.geometry("500x850")

first.title("WELCOME")
first.configure(bg="#FFDE59")

img = PhotoImage(
    file="/Users/andzilem/code 1/EXPERIMENTAL Andzile's DDT Project - Code copy/RESTART/img/my_G'DAY_logo.png")

logo_frame = Frame(first)
logo_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

bg_img = Label(logo_frame, image=img, border=0, borderwidth=0)
bg_img.grid()

rego_frame = Frame(first, background="#FFDE59")
rego_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

welcome = Label(
    rego_frame, text="Good Morning! \nWelcome to \"G\'DAY\" your morning routine app.", background="#FFDE59")
welcome.grid(row=0, column=0)

name_frame = Frame(rego_frame)
name_frame.grid(row=1, column=0, columnspan=2)

name_label = Label(
    name_frame, text="Please enter your name:", background="#FFDE59")
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

# still need to change fonts

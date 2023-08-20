from tkinter import *

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

#this s dont work,, up into txt file and read it,,, or somm like that

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

#poopoo i wan it to like print the list items i have under hte buttons but it just does ".!entry" instead of the actuall text, and i dont think it works for inputingn predsing submut and doing it a again with a diff word. might have ti loop :(
# Import Needed Modules
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")


def time():
    time_string = strftime(" %H:%M:%S %p ")
    label.config(text=time_string)
    label.after(1000, time)


label = Label(root, font=("ds_digital", 100), background="black", foreground="Purple")
label.pack(anchor="center")

time()
mainloop()

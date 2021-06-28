# Import Needed Modules
from tkinter import *
from tkinter.ttk import *
from time import strftime
# Create The MAin Window
root = Tk()
# set title
root.title("Digital Clock")


# Time Function
def time():
    time_string = strftime(" %H:%M:%S %p ")
    label.config(text=time_string)
    label.after(1000, time)


# Add To Screen
label = Label(root, font=("ds_digital", 100), background="black", foreground="Purple")
label.pack(anchor="center")
# Call The Function
time()
# Close The Loop
mainloop()

# Import Needed Modules
import tkinter as tk
from tkinter.ttk import *
from time import strftime
# Create The MAin Window
root = tk.Tk()
# Var
WIDTH = 700
HEIGHT = 400
# set title
root.title("Digital Clock")
# set icon
root.iconphoto(False, tk.PhotoImage(file="logo.png"))
# set Back
root.configure(bg="Black")
# set size
root.geometry(f"{WIDTH}x{HEIGHT}")


# Time Function
def time():
    time_string = strftime(" %H:%M:%S %p ")
    label.config(text=time_string)
    label.after(1000, time)


# Add To Screen
label = Label(root, font=("DS-Digital", 100), background="black", foreground="#25ee00")
label.place(x=30, y=120)
# Call The Function
time()
# Close The Loop
tk.mainloop()

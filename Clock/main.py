from tkinter import *
from tkinter import Tk
from tkinter.ttk import  *
from time import strftime
root: Tk = Tk()
root.title("clock")
def time():
    string =strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = Label(root, font =("ds_digital",90), background= "black", foreground = "white")
label.pack(anchor='center')
time()
mainloop()

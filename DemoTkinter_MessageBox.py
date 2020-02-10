import tkinter as tk
from  tkinter import *
from tkinter import messagebox

m = tk.Tk()
m.geometry("300x400")

def ShowData():
    messagebox.showinfo("Congratulations, your demo is running ")

Showbtn = tk.Button(m,text = "click here" ,bg = "Black",fg = "White",command =ShowData)
Showbtn.pack()



m.mainloop()
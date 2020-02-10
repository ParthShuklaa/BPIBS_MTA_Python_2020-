import tkinter

m = tkinter.Tk()
m.title("My First GUI in python")
m.geometry("400x300")
clickBtn = tkinter.Button(m,activebackground ='Yellow' ,bg = "Black" ,fg="White",text="Click here")
#clickBtn.grid(row = '0',column ='0')
clickBtn.place(height = "100",  width ="60")
submitBtn = tkinter.Button(m,bg = "red",fg ="Black",text = "Submit")
#submitBtn.grid(row='1',column='1')
submitBtn.place(height ="150" ,width ="120")
mySpinBox = tkinter.Spinbox(m,from_=0, to =10)
#mySpinBox.grid(row='1',column='0')
mySpinBox.place(height ="60", width = "50")

m.mainloop()
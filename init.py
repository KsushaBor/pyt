from tkinter import *
root = Tk()
root.title("Welcome to GeekForGeeks")
root.geometry('500x300')
ldl = Label(root, text = "Камень,ножницы, бумага")
ldl.grid()
def clicked():
    ldl.configure(text= "Раз")
btn = Button(root, text = "Камень" ,
         fg = "red", command=clicked)
btn.grid(column=2, row=0)
def cliked():
    ldl.configure(text= "ЕУк")
btn = Button(root, text = "Click me" ,
         fg = "blue", command=cliked)
btn.grid(column=1, row=1)
def cliked():
    ldl.configure(text= "з")
btn = Button(root, text = "Click me" ,
         fg = "red", command=cliked)
btn.grid(column=3, row=2)
root.mainloop()
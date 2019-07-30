from tkinter import *
import threading

a = 0
n = 6

top = Tk()
top.resizable(0, 0)
top.title("Traffic Light")
f = Frame(top, width = "190", height = "300")
j = Label(text = "10", fg = "yellow", font = "Helvetica 30 bold")
j.place(x = 140, y = 10)
p = PhotoImage(file = "yellow.png")
l = Label(image = p)
l.place(x = 4, y = 50)
l.photo = p
l.pack()
j.pack()
def change():
    global a
    global n

    l.place(x = 4, y = 50)
    if a == 0:
        if n == 0:
            a = 1
            n = 10
            p2 = PhotoImage(file = "red.png")
            l.configure(image = p2)
            l.image = p2
            j.config(fg = "red")
            j.config(text = "10")
        else:
            n = n - 1
            j.config(text = n)

    elif a == 1:
        if n == 0:
            a = 2
            n = 10
            p3 = PhotoImage(file = "green.jpg")
            l.configure(image = p3)
            l.image = p3
            j.config(fg = "green")
            j.config(text = "10")
        else:
            n = n - 1
            j.config(text = n)
    elif a == 2:
        if n == 0:
            a = 0
            n = 5
            p4 = PhotoImage(file = "yellow.png")
            l.configure(image = p4)
            l.image = p4
            j.config(fg = "yellow")
            j.config(text = "5")
        else:
            n = n - 1
            j.config(text = n)
    t = threading.Timer(1, change).start()
change()
f.pack()
f.mainloop()

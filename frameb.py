from tkinter import *
import threading

le = int(input("Enter Time For Red Light: "))
le1 = int(input("Enter Time For Green Light: "))
speed = float(input("Enter Speed Of Traffic Light: "))
a = 0
n = 6
d = 0
s = 0
st = 0
gz = 0
top = Tk()
top.resizable(0, 0)
top.title("Traffic Light")
f = Frame(top, width = "190", height = "275")
j = Label(text = "10", fg = "yellow", font = "Helvetica 30 bold")
j.place(x = 140, y = 10)
p = PhotoImage(file = "yellow.gif")
l = Label(image = p)
l.place(x = 4, y = 50)
l.photo = p
b = Button(top, text = "STOP TRAFFIC LIGHT", fg = "blue", bg = "orange", font = "Helvetica 10 bold")
def action():
    global d
    global s
    global st
    if d == 0:
        d = 1
        b.config(text = "START TRAFFIC LIGHT")
    elif d == 1:
        d = 0
        if a == 0:
            p9 = PhotoImage(file = "yellow.gif")
            l.configure(image = p9)
            l.image = p9
            j.config(fg = "yellow")
        elif a == 1:
            p10 = PhotoImage(file = "red.gif")
            l.configure(image = p10)
            l.image = p10
            j.config(fg = "red")
        elif a == 2:
            p11 = PhotoImage(file = "green.jpg")
            l.configure(image = p11)
            l.image = p11
            j.config(fg = "green")
        b.config(text = "STOP TRAFFIC LIGHT")
b.config(command = action)
b.place(x = 17, y = 270)
l.pack()
j.pack()
def change():
    global a
    global n
    global d
    global s
    global speed
    global st
    global gz
    global le
    
    l.place(x = 4, y = 50)
    if d == 0:
        if a == 0:
            if n == 0:
                a = 1
                n = le
                p2 = PhotoImage(file = "red.gif")
                l.configure(image = p2)
                l.image = p2
                j.config(fg = "red")
                j.config(text = le)
            else:
                n = n - 1
                j.config(text = n)

        elif a == 1:
            if n == 0:
                gz = 0
                a = 2
                n = le1
                p3 = PhotoImage(file = "green.jpg")
                l.configure(image = p3)
                l.image = p3
                j.config(fg = "green")
                j.config(text = le1)
            else:
                if n < 7:
                                if gz == 0:
                                                gz = 1
                                                n = n - 1
                                                j.config(text = n)
                                elif gz == 1:
                                                gz = 0
                                                j.config(text = "")
                else:
                                n = n - 1
                                j.config(text = n)
        elif a == 2:
            if n == 0:
                a = 0
                n = 5
                p4 = PhotoImage(file = "yellow.gif")
                l.configure(image = p4)
                l.image = p4
                j.config(fg = "yellow")
                j.config(text = "5")
            else:
                if n < 7:
                                if gz == 0:
                                                gz = 1
                                                n = n - 1
                                                j.config(text = n)
                                elif gz == 1:
                                                gz = 0
                                                j.config(text = "")
                else:
                                n = n - 1
                                j.config(text = n)
    elif d == 1:
        if s == 0:
            s = 1
            p5 = PhotoImage(file = "yellow.gif")
            l.configure(image = p5)
            l.image = p5
            j.config(fg = "yellow")
            j.config(text = "--")
        elif s == 1:
            s = 0
            p6 = PhotoImage(file = "shut.gif")
            l.configure(image = p6)
            l.image = p6
            j.config(fg = "yellow")
            j.config(text = "")
    t = threading.Timer(speed, change).start()
change()
f.pack()
f.mainloop()

#Abhay Tripathi XI - J 2019 - 2020

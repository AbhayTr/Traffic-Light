from tkinter import *
import threading
import datetime

slot = input("Enter Slot: ")
sub = input("Enter Subject Name: ")
st = input("Enter Start Time: ")
sm = 0
if st[1] != ":":
    sh = int(st[0] + st[1])
    sm = int(st[3] + st[4])
else:
    sh = int(st[0])
    sm = int(st[2] + st[3])
et = input("Enter End Time: ")
em = 0
if et[1] != ":":
    eh = int(et[0] + et[1])
    em = int(et[3] + et[4])
else:
    eh = int(et[0])
    em = int(et[2] + et[3])
let = (60 - sm) + em
root = Tk()
f = Frame(root, width = "1000", height = "1000")
l = Label(root, font = "bold 50", fg = "blue", bg = "yellow")
def tim():
    x = str(datetime.datetime.now())
    hr = int(x[11] + x[12])
    hr1 = x[11] + x[12]
    mn = "AM"
    if hr > 12:
        hr2 = hr - 12
        if hr2 < 10:
            hr1 = "0" + str(hr2)
        else:
            hr1 = str(hr2)
    
    if hr >= 12:
        mn = "PM"
        
    mi = int(x[14] + x[15])
    mi1 = x[14] + x[15]
    sec = int(x[17] + x[18])
    sec1 = x[17] + x[18]
    if sh != eh:
        if mi > sm:
            rem = (let - (mi - sm)) - 1
            se = 60 - sec
            m = "Minutes"
            s = "Seconds"
            if rem == 1:
                m = "Minute"
            if se == 1:
                s = "Second"
        
            l.config(text = "SCHEDULE FOR XI - J FOR" + " " + slot + " SLOT:" + "\n \n" + sub + ":- " + st+ " " + "-"+ " " + et + "\n \n" + "CURRENT TIME: \n" + hr1 + ":" + mi1 + ":" + sec1+ " " + mn + "\n \n" + "REMAINING TIME: \n" + str(rem)+ " " + m+ " " + str(60 - sec)+ " " + s)
        else:
            rem = (em - mi) - 1
            se = 60 - sec
            m = "Minutes"
            s = "Seconds"
            if rem == 1:
                m = "Minute"
            if se == 1:
                s = "Second"
            
            if rem < 0:
                l.config(text = "SCHEDULE FOR XI - J FOR" + " " +slot + " SLOT:" + "\n \n" + sub + ":- " + st+ " " + "-"+ " " + et + "\n \n" + "CURRENT TIME: \n" + hr1 + ":" + mi1 + ":" + sec1+ " " + mn + "\n \n" + "REMAINING TIME: \n SLOT OVER!!!")
            else:
                l.config(text = "SCHEDULE FOR XI - J FOR" + " " +slot + " SLOT:" + "\n \n" + sub + ":- " + st+ " " + "-"+ " " + et + "\n \n" + "CURRENT TIME: \n" + hr1 + ":" + mi1 + ":" + sec1+ " " + mn + "\n \n" + "REMAINING TIME: \n" + str(rem)+ " " + m+ " " + str(60 - sec)+ " " + s)
    else:
        rem = (em - mi) - 1
        se = 60 - sec
        m = "Minutes"
        s = "Seconds"
        if rem == 1:
            m = "Minute"
        if se == 1:
            s = "Second"
            
        if rem < 0:
            l.config(text = "SCHEDULE FOR XI - J FOR" + " " +slot + " SLOT:" + "\n \n" + sub + ":- " + st+ " " + "-"+ " " + et + "\n \n" + "CURRENT TIME: \n" + hr1 + ":" + mi1 + ":" + sec1+ " " + mn + "\n \n" + "REMAINING TIME: \n SLOT OVER!!!")
        else:
            l.config(text = "SCHEDULE FOR XI - J FOR" + " " +slot + " SLOT:" + "\n \n" + sub + ":- " + st+ " " + "-"+ " " + et + "\n \n" + "CURRENT TIME: \n" + hr1 + ":" + mi1 + ":" + sec1+ " " + mn + "\n \n" + "REMAINING TIME: \n" + str(rem)+ " " + m+ " " + str(60 - sec)+ " " + s)
    
    threading.Timer(1, tim).start()
tim()
l.pack()
root.title("DPS GURGAON SECTOR - 45 XI - J 2019 - 20")
root.resizable(0, 0)
f.mainloop()

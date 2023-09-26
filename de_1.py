# de 1 mon ngon ngu lap trinh Python
import tkinter as tk
class tugiac():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def chuvi(self):
        return self.a+self.b+self.c+self.d
    def canhlon(self):
        m = self.a
        if m < self.b:
            m = self.b
        if m < self.c:
            m = self.c
        if m < self.d:
            m = self.d
        return m
'''obj = tugiac(2,4,4,6)
print('chu vi = ',obj.chuvi())
print('canh lon nhat:',obj.canhlon())'''
def nhapdulieu():
    c1 = canh1.get()
    c2 = canh2.get()
    c3 = canh3.get()
    c4 = canh4.get()
    obj = tugiac(c1,c2,c3,c4)
    ds.append(obj)
def tinhtoan():
    s = []
    cv = []
    for i in range(0,len(ds)):
        stam =  'chu vi hinh ' +str(i) + ':' + str(ds[i].chuvi()) + 'do dai canh lon = ' + str(ds[i].canhlon())
        s.append(stam)
        cv.append(ds[i].chuvi())
    label2.config(text = s[0])
    label2.pack()
    label3.config(text = s[1])
    label3.pack()
    label4.config(text = s[2])
    label4.pack()
    s2 = 'Chu vi nho nhat ' + str(min(cv))
    label5.config(text = s2)
    label5.pack()
from tkinter import *
ds = []
w = Tk()
w.geometry('300x400')
w.title('Bai tap so 1')
label1 = Label(w,text ='Hay nhap 4 canh :').pack()
canh1= DoubleVar()
canh2= DoubleVar()
canh3= DoubleVar()
canh4= DoubleVar()
E1 = Entry(w,textvariable = canh1).pack()
E2 = Entry(w,textvariable = canh2).pack()
E3 = Entry(w,textvariable = canh3).pack()
E4 = Entry(w,textvariable = canh4).pack()
b1 = Button(w,text = 'Them du lieu',command = nhapdulieu).pack()
b2 = Button(w,text = 'Tinh toan', command = tinhtoan).pack()
label2  = Label(w)
label3 = Label(w)
label4 = Label(w)
label5 = Label(w)
                  



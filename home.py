#pyinstaller --onefile configuration.py
from   tkinter import *
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from datamain import *
from datamain import createdatabase
def homes():
    createdatabase()
    def shree():
        fo = open("studentdata.tsv", "w")
        cursor.execute("select * from student")
        n = cursor.fetchall()
        for i in n:
            u = str(i)
            fo.write(u)
            fo.write('\n')
        fo.close()
        fo = open("staffdata.tsv", "w")
        cursor.execute("select * from datastaff")
        n = cursor.fetchall()
        for i in n:
            u = str(i)
            fo.write(u)
            fo.write('\n')
        fo.close()
        fo = open("enterddata.tsv", "w")
        cursor.execute("select * from teacher")
        n = cursor.fetchall()
        for i in n:
            u = str(i)
            fo.write(u)
            fo.write('\n')
        fo.close()
        from tkinter import messagebox
        messagebox.showinfo("IMPORTANT", "$UCCESSFULLY RESET THE DATABASE")
        from datamain import deletedatabasedata
        deletedatabasedata()

    def REG():
        R.destroy()
        from registion import registations
        registations()

    def RES():
        R.destroy()
        from REGTEACHER import regteachers
        regteachers()

    def login():
        R.destroy()
        from loginstudent import logstudent
        logstudent()

    def loginS():
        R.destroy()
        from login import logins
        logins()

    def exits():
        cursor.close()
        R.destroy()

    R = tk.Tk()

    R.title('HOME PAGE')
    R.geometry("600x720")
    R.configure(background='LIGHTBLUE')

    l = Label(R, text="SARASWATI COLLEGE OF ENGINEERING , KHARGHAR ,NAVI MUMBAI")
    l.config(bg='lightblue', fg='purple')
    l.place(x=100, y=20)

    l1 = Label(R, text="STUDENT EVENT ATTENDENCE MANAGEMENT")
    l1.config(bg='lightblue', fg='purple')
    l1.place(x=150, y=50)

    l2 = Label(R, text="REGISTOR FOR EVENT")
    l2.config(bg='lightblue', fg='purple')
    l2.place(x=50, y=200)

    l3 = Label(R, text="LOGIN FOR STUDENT")
    l3.config(bg='lightblue', fg='purple')
    l3.place(x=50, y=300)

    l4 = Label(R, text="REGISTOR FOR FACULTY")
    l4.config(bg='lightblue', fg='purple')
    l4.place(x=50, y=400)

    l5 = Label(R, text="LOGIN FOR FACULTY")
    l5.config(bg='lightblue', fg='purple')
    l5.place(x=50, y=500)

    b1 = Button(R, text='REGISTION', command=REG, width='20', height='1')
    b1.place(x=300, y=200)

    b2 = Button(R, text='LOGIN FOR STUDENT', command=login, width='20', height='1')
    b2.place(x=300, y=300)

    b3 = Button(R, text='REGISTION', command=RES, width='20', height='1')
    b3.place(x=300, y=400)

    b4 = Button(R, text='LOGIN', command=loginS, width='20', height='1')
    b4.place(x=300, y=500)

    b5 = Button(R, text='EXIT', command=exits, width='20', height='1')
    b5.place(x=150, y=600)

    b6 = Button(R, text='RESET', command=shree, width='15', height='1')
    b6.place(x=480, y=650)

    R.mainloop()

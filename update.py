from tkinter import *
import tkinter.ttk as ttk
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from datamain import *

def updates():
    def back_home():
        rose.destroy()
        from home import homes
        homes()

    def getreg(b, e, d, R):
        if b == 'COMPUTER ENGINEERING':
            STR = 'COMP'
        elif b == 'INFORMATION TECHNOLOGY':
            STR = 'IT'
        elif b == 'ELEC.& TELECOMMUNICATION':
            STR = 'EXTC'
        elif b == 'CIVIL ENGINEEING':
            STR = 'CIVL'
        elif b == 'MECHANICAL ENGINEERIN':
            STR = 'MECH'

        if e == 'NURTURE MANGEMENT':
            STR = STR + 'NU'
        elif e == 'CESA':
            STR = STR + 'CE'
        elif e == 'SPORTS':
            STR = STR + 'SP'
        elif e == 'ACE':
            STR = STR + 'AC'
        elif e == 'ROTRACT CLUB':
            STR = STR + 'RC'
        elif e == 'STUDENT SECTION':
            STR = STR + 'SS'

        if d == 'FE':
            STR = STR + 'FE'
        elif d == 'SE':
            STR = STR + 'SE'
        elif d == 'TE':
            STR = STR + 'TE'
        elif d == 'BE':
            STR = STR + 'BE'
        elif d == 'ME':
            STR = STR + 'ME'
        STR = STR + str(R)
        return (STR)

    def setreg(n):
        if n[0] == 'COMPUTER ENGINEERING':
            cb.set('COMPUTER ENGINEERING')
        elif n[0] == 'INFORMATION TECHNOLOGY':
            cb.set('INFORMATION TECHNOLOGY')
        elif n[0] == 'ELEC.& TELECOMMUNICATION':
            cb.set('ELEC.& TELECOMMUNICATION')
        elif n[0] == 'CIVIL ENGINEEING':
            cb.set('CIVIL ENGINEEING')
        elif n[0] == 'MECHANICAL ENGINEERING':
            cb.set('MECHANICAL ENGINEERING')

        if n[1] == 'NURTURE MANGEMENT':
            cb1.set('NURTURE MANGEMENT')
        elif n[1] == 'CESA':
            cb1.set('CESA')
        elif n[1] == 'SPORTS':
            cb1.set('SPORTS')
        elif n[1] == 'ACE':
            cb1.set('ACE')
        elif n[1] == 'ROTRACT CLUB':
            cb1.set('ROTRACT CLUB')
        elif n[1] == 'STUDENT SECTION':
            cb1.set('STUDENT SECTION')

        if n[2] == 'FE':
            cb2.set('FE')
        elif n[2] == 'SE':
            cb2.set('SE')
        elif n[2] == 'TE':
            cb2.set('TE')
        elif n[2] == 'BE':
            cb2.set('EE')
        elif n[2] == 'ME':
            cb2.set('ME')
        T.insert(END, n[3])
        T1.insert(END, n[4])
        T2.insert(END, n[5])

    def delete(username):
        cursor.execute("delete from student where reg='" + username + "'")

    def SUBMIT():
        username = T0.get("1.0", "end-1c")
        cursor.execute("select * from student where reg='" + username + "'")
        n = cursor.fetchone()
        setreg(n)
        delete(username)

    def UPDATE():
        T3.delete("1.0", END)
        b = cb.get()
        e = cb1.get()
        d = cb2.get()
        PASS = T2.get("1.0", "end-1c")
        n = T.get("1.0", "end-1c")
        R = int(T1.get("1.0", "end-1c"))
        reg = getreg(b, e, d, R)
        T3.insert(END, reg)
        val = (b, e, d, n, R, PASS, reg)
        cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s,%s)", val)
        cnx.commit()

    def exits():
        rose.destroy()

    rose = tk.Tk()

    rose.title('REGISTION FOR STUDENTS')
    rose.geometry("600x720")
    rose.configure(background='LIGHTBLUE')

    l = Label(rose, text="SARASWATI COLLEGE OF ENGINEERING , KHARGHAR ,NAVI MUMBAI")
    l.config(bg='lightblue', fg='purple')
    l.place(x=100, y=20)

    l1 = Label(rose, text="STUDENT EVENT REGISTATION")
    l1.config(bg='lightblue', fg='purple')
    l1.place(x=200, y=50)

    l0 = Label(rose, text="ENTER YOUR OLD REGISTION NO.")
    l0.config(bg='lightblue', fg='purple')
    l0.place(x=50, y=150)

    l2 = Label(rose, text="BRANCH")
    l2.config(bg='lightblue', fg='purple')
    l2.place(x=50, y=200)

    l3 = Label(rose, text="EVENT")
    l3.config(bg='lightblue', fg='purple')
    l3.place(x=50, y=250)

    l4 = Label(rose, text="YEAR")
    l4.config(bg='lightblue', fg='purple')
    l4.place(x=50, y=300)

    l7 = Label(rose, text="ROLL NUMBER")
    l7.config(bg='lightblue', fg='purple')
    l7.place(x=50, y=350)

    l5 = Label(rose, text="NAME")
    l5.config(bg='lightblue', fg='purple')
    l5.place(x=50, y=400)

    l8 = Label(rose, text="PASSWORD")
    l8.config(bg='lightblue', fg='purple')
    l8.place(x=50, y=450)

    l6 = Label(rose, text="YOUR REGISTION NO.")
    l6.config(bg='lightblue', fg='purple')
    l6.place(x=50, y=550)

    cb = ttk.Combobox(rose, values=(
    "COMPUTER ENGINEERING", "INFORMATION TECHNOLOGY", "ELEC.& TELECOMMUNICATION", "CIVIL ENGINEEING",
    "MECHANICAL ENGINEERING"))
    cb.set('BRANCH')
    cb.place(x=300, y=200)

    cb1 = ttk.Combobox(rose, values=("NURTURE MANGEMENT", "CESA", "SPORTS", "ACE", "ROTRACT CLUB", "STUDENT SECTION"))
    cb1.set('EVENTS')
    cb1.place(x=300, y=250)

    cb2 = ttk.Combobox(rose, values=("FE", "SE", "TE", "BE", "ME"))
    cb2.set('YEAR')
    cb2.place(x=300, y=300)

    T = Text(rose, width="25", height="1", background='lightblue')
    T.place(x=300, y=400)

    T1 = Text(rose, width="25", height="1", background='lightblue')
    T1.place(x=300, y=350)

    T2 = Text(rose, width="25", height="1", background='lightblue')
    T2.place(x=300, y=450)

    T3 = Text(rose, width="25", height="1", background='lightblue')
    T3.place(x=300, y=550)

    T0 = Text(rose, width="15", height="1", background='lightblue')
    T0.place(x=300, y=150)

    b1 = Button(rose, text='SUBMIT', command=SUBMIT, width='6', height='1')
    b1.place(x=500, y=150)

    b1 = Button(rose, text='UPDATE', command=UPDATE, width='6', height='1')
    b1.place(x=400, y=500)

    b2 = Button(rose, text='EXIT', command=exits, width='6', height='1')
    b2.place(x=350, y=600)

    b2 = Button(rose, text='BACK', command=back_home, width='6', height='1')
    b2.place(x=250, y=600)

    rose.mainloop()

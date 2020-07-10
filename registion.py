from tkinter import *
import tkinter.ttk as ttk
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from datamain import *

def registations():
    def back_home():
        r.destroy()
        from home import homes
        homes()

    def getreg(b, e, Y, R):
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

        if Y == 'FE':
            STR = STR + 'FE'
        elif Y == 'SE':
            STR = STR + 'SE'
        elif Y == 'TE':
            STR = STR + 'TE'
        elif Y == 'BE':
            STR = STR + 'BE'
        elif Y == 'ME':
            STR = STR + 'ME'

        STR = STR + str(R)
        return (STR)

    def submit():
        T3.delete("1.0", END)
        b = cb.get()
        e = cb1.get()
        Y = cb2.get()
        PASS = T2.get("1.0", "end-1c")
        n = T.get("1.0", "end-1c")
        R = int(T1.get("1.0", "end-1c"))
        reg = getreg(b, e, Y, R)
        T3.insert(END, reg)
        val = (b, e, Y, n, R, PASS, reg)
        cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s,%s)", val)
        cnx.commit()

    def exits():
        r.destroy()

    r = tk.Tk()

    r.title('REGISTION FOR STUDENTS')
    r.geometry("600x720")
    r.configure(background='LIGHTBLUE')

    l = Label(r, text="SARASWATI COLLEGE OF ENGINEERING , KHARGHAR ,NAVI MUMBAI")
    l.config(bg='lightblue', fg='purple')
    l.place(x=100, y=20)

    l1 = Label(r, text="STUDENT EVENT REGISTATION")
    l1.config(bg='lightblue', fg='purple')
    l1.place(x=200, y=50)

    l2 = Label(r, text="BRANCH")
    l2.config(bg='lightblue', fg='purple')
    l2.place(x=50, y=150)

    l3 = Label(r, text="EVENT")
    l3.config(bg='lightblue', fg='purple')
    l3.place(x=50, y=200)

    l4 = Label(r, text="YEAR")
    l4.config(bg='lightblue', fg='purple')
    l4.place(x=50, y=250)

    l7 = Label(r, text="ROLL NUMBER")
    l7.config(bg='lightblue', fg='purple')
    l7.place(x=50, y=300)

    l5 = Label(r, text="NAME")
    l5.config(bg='lightblue', fg='purple')
    l5.place(x=50, y=350)

    l8 = Label(r, text="PASSWORD")
    l8.config(bg='lightblue', fg='purple')
    l8.place(x=50, y=400)

    l6 = Label(r, text="YOUR REGISTION NO.")
    l6.config(bg='lightblue', fg='purple')
    l6.place(x=50, y=500)

    cb = ttk.Combobox(r, values=(
    "COMPUTER ENGINEERING", "INFORMATION TECHNOLOGY", "ELEC.& TELECOMMUNICATION", "CIVIL ENGINEEING",
    "MECHANICAL ENGINEERIN"))
    cb.set('BRANCH')
    cb.place(x=300, y=150)

    cb1 = ttk.Combobox(r, values=("NURTURE MANGEMENT", "CESA", "SPORTS", "ACE", "ROTRACT CLUB", "STUDENT SECTION"))
    cb1.set('EVENTS')
    cb1.place(x=300, y=200)

    cb2 = ttk.Combobox(r, values=("FE", "SE", "TE", "BE", "ME"))
    cb2.set('YEAR')
    cb2.place(x=300, y=250)

    T = Text(r, width="25", height="1", background='lightblue')
    T.place(x=300, y=350)

    T1 = Text(r, width="25", height="1", background='lightblue')
    T1.place(x=300, y=300)

    T2 = Text(r, width="25", height="1", background='lightblue')
    T2.place(x=300, y=400)

    T3 = Text(r, width="25", height="1", background='lightblue')
    T3.place(x=300, y=500)

    b1 = Button(r, text='SUBMIT', command=submit, width='6', height='1')
    b1.place(x=400, y=450)

    b2 = Button(r, text='EXIT', command=exits, width='6', height='1')
    b2.place(x=350, y=550)

    b3 = Button(r, text='BACK', command=back_home, width='6', height='1')
    b3.place(x=250, y=550)

    r.mainloop()
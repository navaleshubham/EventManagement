from   tkinter import *
import warnings
from datamain import *
warnings.filterwarnings("ignore")
import tkinter as tkk

def logins():
    ro = tkk.Tk()

    def log():
        username = T.get("1.0", "end-1c")
        password = T1.get("1.0", "end-1c")
        cursor.execute("select password from datastaff where reg='" + username + "'")
        n = cursor.fetchone()

        if (n == None):
            from tkinter import messagebox
            messagebox.showerror("error", "USER IS NOT REGISTOR")

        elif (n[0] == password):
            ro.destroy()
            from gui import guis
            guis()

        else:
            from tkinter import messagebox
            messagebox.showerror("error", "username and password don't mathces")

    def exits():
        try:
            ro.destroy()
            from home import homes
            homes()
        except:
            ro.quit()

    ro.title('LOGIN')
    ro.geometry("600x720")
    ro.configure(background='LIGHTBLUE')

    l = Label(ro, text="SARASWATI COLLEGE OF ENGINEERING , KHARGHAR ,NAVI MUMBAI")
    l.config(bg='lightblue', fg='purple')
    l.place(x=100, y=20)

    l1 = Label(ro, text="LOGIN FOR FACULTY")
    l1.config(bg='lightblue', fg='purple')
    l1.place(x=250, y=50)

    l2 = Label(ro, text="USERNAME:-")
    l2.config(bg='lightblue', fg='purple')
    l2.place(x=50, y=200)

    l3 = Label(ro, text="PASSWORD:-")
    l3.config(bg='lightblue', fg='purple')
    l3.place(x=50, y=300)

    T = Text(ro, width="25", height="1", background='lightblue')
    T.place(x=200, y=200)

    T1 = Text(ro, width="25", height="1", background='lightblue')
    T1.place(x=200, y=300)

    b1 = Button(ro, text='LOGIN', command=log, width='15', height='1')
    b1.place(x=100, y=500)

    b2 = Button(ro, text='EXIT', command=exits, width='15', height='1')
    b2.place(x=300, y=500)

    ro.mainloop()
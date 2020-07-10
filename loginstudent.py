from   tkinter import *
import warnings
warnings.filterwarnings("ignore")
import tkinter as tkk
from datamain import *

def logstudent():
    ros = tkk.Tk()

    def log():
        username = T.get("1.0", "end-1c")
        password = T1.get("1.0", "end-1c")
        cursor.execute("select pass from student where reg='" + username + "'")
        n = cursor.fetchone()

        if (n == None):
            from tkinter import messagebox
            messagebox.showerror("error", "USER IS NOT REGISTOR")

        elif (n[0] == password):
            ros.destroy()
            from update import updates
            updates()

        else:
            from tkinter import messagebox
            messagebox.showerror("error", "username and password don't mathces")

    def exits():
        ros.destroy()
        from home import homes
        homes()

    ros.title('LOGIN FOR STUDENT')
    ros.geometry("600x720")
    ros.configure(background='LIGHTBLUE')

    l = Label(ros, text="SARASWATI COLLEGE OF ENGINEERING , KHARGHAR ,NAVI MUMBAI")
    l.config(bg='lightblue', fg='purple')
    l.place(x=100, y=20)

    l1 = Label(ros, text="LOGIN FOR STUDENT")
    l1.config(bg='lightblue', fg='purple')
    l1.place(x=250, y=50)

    l2 = Label(ros, text="USERNAME:-")
    l2.config(bg='lightblue', fg='purple')
    l2.place(x=50, y=200)

    l3 = Label(ros, text="PASSWORD:-")
    l3.config(bg='lightblue', fg='purple')
    l3.place(x=50, y=300)

    T = Text(ros, width="25", height="1", background='lightblue')
    T.place(x=200, y=200)

    T1 = Text(ros, width="25", height="1", background='lightblue')
    T1.place(x=200, y=300)

    b1 = Button(ros, text='LOGIN', command=log, width='15', height='1')
    b1.place(x=100, y=500)

    b2 = Button(ros, text='EXIT', command=exits, width='15', height='1')
    b2.place(x=300, y=500)

    ros.mainloop()
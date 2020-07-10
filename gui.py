from tkinter import *
import tkinter.ttk as ttk
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from datamain import *
def guis():
    createdatabase()
    root = tk.Tk()

    def getdataS():
        fo = open("studentshistory.tsv", "w")
        cursor.execute("select * from student")
        n = cursor.fetchall()
        for i in n:
            u = str(i)
            fo.write(u)
            fo.write('\n')
        fo.close()

    def getdataE():
        fo = open("attendencesubmitted.tsv", "w")
        cursor.execute("select * from teacher")
        n = cursor.fetchall()
        for i in n:
            u = str(i)
            fo.write(u)
            fo.write('\n')
        fo.close()

    def getdataD():
        fo = open("staffdata.tsv", "w")
        cursor.execute("select * from datastaff")
        n = cursor.fetchall()
        for i in n:
            u = str(i)
            fo.write(u)
            fo.write('\n')
        fo.close()

    def add():
        branch = cb.get()
        event = cb1.get()
        regno = T3.get("1.0", "end-1c")
        date = T1.get("1.0", "end-1c")
        time = T4.get("1.0", "end-1c")
        name = T.get("1.0", "end-1c")
        val = (branch, event, date, time, name, regno)
        getstatus(regno, val)
        T3.delete("1.0", END)

    def getstatus(regno, val):
        res = ("select reg field from student where reg='" + regno + "'")
        cursor.execute(res)
        n = cursor.fetchall()
        if (n == []):
            from tkinter import messagebox
            messagebox.showerror("INPUTERROR", "THE REGISTATION NUMBER IS NOT VALID")
        else:
            store(val, regno)

    def store(val, regno):
        res = ("select regno field from teacher where regno='" + regno + "'")
        cursor.execute(res)
        n = cursor.fetchall()
        if (n != []):
            from tkinter import messagebox
            messagebox.showinfo("INPUTERROR", "THE REGISTATION NUMBER IS PERIOUSLY ADDED")
        else:
            cursor.execute("INSERT INTO teacher VALUES (%s, %s, %s, %s, %s, %s)", val)
            cnx.commit()

    def search():
        def byname():
            from tkinter import messagebox
            messagebox.showinfo("SEARCH BY USING NAME", "PLEASE ENTER NAME OF STUDENT")

        def byreg():
            from tkinter import messagebox
            messagebox.showinfo("SEARCH BY USING REGISTATION NUMBER", "PLEASE ENTER REGISTATION NUMBER OF STUDENT")

        def bybranch():
            from tkinter import messagebox
            messagebox.showinfo("SEARCH BY USING BRANCH", "PLEASE ENTER BRANCH OF STUDENTS")

        def find():
            t = Text(root, height=15, width=72)
            t.place(x=600, y=250)
            if (rb1.select):
                E = En.get()
                sql = ("select * from student where name like'" + E + "'")
                cursor.execute(sql)
                n = cursor.fetchall()
                for x in n:
                    t.insert(END, x)
                    t.insert(END, ' \n')
                cnx.commit()
            if (rb2.select):
                E = En.get()
                sql = ("select * from student where reg like '" + E + "'")
                cursor.execute(sql)
                n = cursor.fetchall()
                for x in n:
                    t.insert(END, x)
                    t.insert(END,'\n')
                cnx.commit()
            if (rb3.select):
                E = En.get()
                sql = ("select * from student where branch like '" + E + "'")
                cursor.execute(sql)
                n = cursor.fetchall()
                for x in n:
                    t.insert(END, x)
                    t.insert(END, '\n')
                cnx.commit()

        var = tk.IntVar()
        lbe = Label(root, text="search in the database")
        lbe.configure(bg='lightblue')
        lbe.place(x=600, y=70)
        rb1 = Radiobutton(root, text="SEARCH BY USING NAME", value=1, variable=var, command=byname)
        rb2 = Radiobutton(root, text="SEARCH BY USING REGISTATION  NUMBER", value=2, variable=var, command=byreg)
        rb3 = Radiobutton(root, text="SEARCH BY USING BRANCH", value=3, variable=var, command=bybranch)
        rb1.configure(bg='lightblue')
        rb2.configure(bg='lightblue')
        rb3.configure(bg='lightblue')
        rb1.grid(row=1, sticky=W)
        rb2.grid(row=2, sticky=W)
        rb3.grid(row=3, sticky=W)
        rb1.place(x=600, y=100)
        rb2.place(x=600, y=130)
        rb3.place(x=600, y=160)
        En = Entry(root, width=25)
        En.place(x=600, y=190)
        b = Button(root, text='search', height=1, width=6, command=find)
        b.place(x=600, y=230)

    def home():
        root.destroy()
        from home import homes
        homes()

    def submit():
        from tkinter import messagebox
        messagebox.showinfo("SUCESS", "DATA SUBMISSION IS SUCESSFUL")

    def exits():
        root.destroy()
        from home import homes
        home()

    root.title('ATTENDENCE MANAGEMENT')
    root.geometry("1200x800")
    root.configure(background='lightblue')

    l = Label(root, text="SARASWATI COLLEGE OF ENGINEERING , KHARGHAR ,NAVI MUMBAI")
    l.config(bg='lightblue', fg='purple')
    l.place(x=100, y=20)

    l1 = Label(root, text="EVENT ATTENDENCE MANAGEMENT SYSTEM")
    l1.config(bg='lightblue', fg='purple')
    l1.place(x=150, y=50)

    l2 = Label(root, text="BRANCH")
    l2.config(bg='lightblue', fg='purple')
    l2.place(x=50, y=150)

    l3 = Label(root, text="EVENT")
    l3.config(bg='lightblue', fg='purple')
    l3.place(x=50, y=200)

    l5 = Label(root, text="DATE")
    l5.config(bg='lightblue', fg='purple')
    l5.place(x=50, y=250)

    l8 = Label(root, text="TIME")
    l8.config(bg='lightblue', fg='purple')
    l8.place(x=50, y=300)

    l6 = Label(root, text="FACULTY REGISTATION NUMBER")
    l6.config(bg='lightblue', fg='purple')
    l6.place(x=50, y=350)

    l7 = Label(root, text="REGISTION NUMBERS")
    l7.config(bg='lightblue', fg='purple')
    l7.place(x=50, y=400)

    cb = ttk.Combobox(root, values=(
    "COMPUTER ENGINEERING", "INFORMATION TECHNOLOGY", "ELEC.& TELECOMMUNICATION", "CIVIL ENGINEERING",
    "MECHANICAL ENGINEERIN"))
    cb.set('BRANCH')
    cb.place(x=300, y=150)

    cb1 = ttk.Combobox(root, values=("NURTURE MANGEMENT", "CESA", "SPORTS", "ACE", "ROTRACT CLUB", "STUDENT SECTION"))
    cb1.set('EVENTS')
    cb1.place(x=300, y=200)

    T = Text(root, width="25", height="1", background='lightblue')
    T.place(x=300, y=350)

    T1 = Text(root, width="25", height="1", background='lightblue')
    T1.place(x=300, y=250)
    ls = Label(root, text='enter date informat dd/mm/yyyy')
    ls.config(bg='lightblue', fg='purple')
    ls.place(x=310, y=270)

    T4 = Text(root, width="25", height="1", background='lightblue')
    T4.place(x=300, y=300)
    lp = Label(root, text='enter the time slots')
    lp.config(bg='lightblue', fg='purple')
    lp.place(x=320, y=320)

    T3 = Text(root, width="25", height="1", background='lightblue')
    T3.place(x=300, y=400)

    b = Button(root, text='ADD', command=add, width='6', height='1')
    b.place(x=50, y=500)

    b1 = Button(root, text='SUBMIT', command=submit, width='6', height='1')
    b1.place(x=150, y=500)

    b2 = Button(root, text='SEARCH', command=search, width='6', height='1')
    b2.place(x=250, y=500)

    b3 = Button(root, text='BACK', command=exits, width='6', height='1')
    b3.place(x=350, y=500)

    b4 = Button(root, text='GET STUDENT DATA', command=getdataS, width='20', height='1')
    b4.place(x=1000, y=50)

    b5 = Button(root, text='GET STAFF DATA', command=getdataD, width='20', height='1')
    b5.place(x=1000, y=100)

    b6 = Button(root, text='GET ENTERED DATA', command=getdataE, width='20', height='1')
    b6.place(x=1000, y=150)

    root.mainloop()


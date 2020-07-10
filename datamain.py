import mysql
from mysql.connector import connection
from mysql.connector import (connection)
#cnx = connection.MySQLConnection(user='shubham', passwd='shubham', host='127.0.0.1')
#cursor = cnx.cursor()


try:
    fo=open("donottouch.txt","r")
    n=int(fo.read(1))
    username=fo.read(n)
    m=int(fo.read(1))
    password=fo.read(n)
    fo.close()
    #print("U:",username,'\n',"P:",password)
    cnx = connection.MySQLConnection(user=username, password=password, host='127.0.0.1')
    cursor = cnx.cursor()


except:
    from tkinter import messagebox
    messagebox.showerror("ERROR", "DATABASE CONNECTION UNSUCESSFULL")


def createdatabase():
    try:
        cursor.execute("use computer")

    except:
        cursor.execute("create database computer")
        cursor.execute("use computer")
        cursor.execute("create table student(branch varchar(30) not null,event  varchar(20) not null,year   varchar(5)  not null,name   varchar(30) not null,rollno int not null,pass   varchar(10) null,reg    varchar(20) not null)")
        cursor.execute("create table teacher(branch varchar(30) not null,event  varchar(20) not null,date   varchar(10) not null,time   varchar(20) not null,REG    varchar(30) null,regno  varchar(20) not null)")
        cursor.execute("create table datastaff(branch   varchar(30) not null,event    varchar(20) null,year     varchar(5)  null,name     varchar(30) null,password varchar(10) null,reg      varchar(20) null)")
        #cursor.execute(" create table output(regno    varchar(20) not null,name     varchar(30) not null,branch   varchar(30) null,year     varchar(10) null,rollno   int         not null,event    varchar(20) not null,date     varchar(10) null,timeslot varchar(10) not null)")


def deletedatabasedata():
    cursor.execute("use computer")
    cursor.execute("truncate table teacher")
    cursor.execute("truncate table student")
    cursor.execute("truncate table datastaff")
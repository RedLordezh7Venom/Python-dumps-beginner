import mysql.connector

import datetime

con = mysql.connector.connect(host='localhost',user='root',password='root',database='slave',auth_plugin='mysql_native_password')

myc=con.cursor()

def add():
    E=int(input("Enter Admission no"))
    N=input("Enter the name ")
    S=input("Enter Gender")
    D=input("Enter Class")
    L=input("Enter contact number")
    DOB=input("Enter date of birth")
    ch=input("save the record? Y/N ")
    if ch=='Y' or ch=='y':
        myc.execute("insert into student_management values(%s,%s,%s,%s,%s,%s)",(E,N,D,S,L,DOB))
        con.commit()
        print(myc)
    else:
        pass

def display():
 myc.execute("select * from student_management")
 for d in myc:
     print(d)
     
def search():
    G=int(input("Enter the Admission number to search"))
    E=[]
    E.append(G)
    myc.execute("select * from student_management where Admissionno=%s",(E))
    data=myc.fetchall()
    if data==[]:
        print("No student with given admission number found")
    else:
        print(data)

def delete():
    E=int(input("Enter the Admission number to delete "))
    myc.execute("delete from student_management where Admissionno=%s",(E,))
    ch=input("save the record? Y/N ")
    if ch=='Y' or ch=='y':
        con.commit()
    else:
        pass

def modify():
    E=int(input("Enter Admission number "))
    N=input("Enter the name ")
    D=input("Enter the Class")
    S=input("Enter the Gender ")
    L=input("Enter contact number")
    DOB=input("Enter date of birth")
    myc.execute("update student_management set Name=%s, Class=%s, Gender=%s,DOB=%s,contact=%s where Admissionno=%s",(N,D,S,DOB,L,E))
    con.commit()


while True:

    c=int(input("1.Add \n2.Display \n3.Search \n4.Modify \n5.Delete \n6.Exit \nEnter your choice"))
    if c==1:
        add()
    elif c==2:
        display()
    elif c==3:
        search()
    elif c==4:
        modify()
    elif c==5:
        delete()
    elif c==6:
        break
    else:
     print("Enter a valid choice")
     

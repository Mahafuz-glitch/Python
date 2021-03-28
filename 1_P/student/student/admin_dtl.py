import sqlite3
from tkinter import *


#Fetch all data one by one    
def u_view():
    root=Tk()
    root.title("OLD BOOK STALL")
    root.geometry("700x400+400+150")
    #root.resizable(0,0)
    con=sqlite3.connect('book.db')
    cur=con.cursor()

#############################################################################  
    cur.execute("select * from signup")
    f=cur.fetchall()
    k=3
    l1=Label(root,font=(10),width=70,anchor='w')
    l1['text']="\tu_id\tu_name\t\tu_phone\t\tu_add\tu_password"
    l1.grid(row=2,column=0,padx=0,rowspan=1)#,sticky=E)
    a=0
    for i in f:
        l1=Label(root,font=(10),justify='left',anchor='e')
        if(a==0):
            l1['bg']='red'
            a=1
        else:
            l1['bg']='yellow'
            a=0
        l1['text']="{}\t {}\t {}\t {}\t {}".format(i[0],i[1],i[2],i[3],i[4])
        
        l1.grid(row=k,column=0)
        k=k+1
    root.mainloop()

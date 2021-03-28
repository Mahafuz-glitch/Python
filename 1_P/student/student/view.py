import sqlite3
from tkinter import *
from db_buy import *
#CREATE TABLE FOR SALEING BOOK
#def b_create_table():
 #   cur.execute("CREATE TABLE IF NOT EXISTS sale(b_ib INTEGER PRIMARY KEY AUTOINCREMENT , u_b_id INTEGER, b_name TEXT, b_edition TEXT, b_author TEXT, b_helth TEXT, b_price INTEGER, b_date TEXT)")
  #  con.commit()

  
#Fetch all data one by one    
def b_view():
    root=Tk()
    root.title("OLD BOOK STALL")
    root.geometry("700x400+400+150")
    #root.resizable(0,0)
    con=sqlite3.connect('book.db')
    cur=con.cursor()

##############################################################################
#CALL b_buy FUNCTION AND SEND DATE THROUGH THIS FUNCTION  
    def bk_buy():
        e=int(e1.get())
        #print(type(e))
        b_buy(e)
    
  

##############################################################################  
    cur.execute("select * from sale where status='available'")
    f=cur.fetchall()
    k=3
    l1=Label(root,text='Enter book id:',font=(10))
    l1.grid(row=0,column=0,padx=240,ipadx=0,sticky=W)
    e1=Entry(root,font=(10))
    e1.grid(row=0,column=0,padx=50,sticky=NW,ipadx=0,columnspan=1)
    b1=Button(root,text="buy",font=(10),command=bk_buy)
    b1.grid(row=0,column=0,padx=0,sticky=NW,ipadx=0,columnspan=1)

    l1=Label(root,font=(10),width=70,anchor='w')
    l1['text']="b_id\tu_id\tb_name\tedition\t author\t health\t price\t date"
    l1.grid(row=2,column=0,padx=0,rowspan=1)
    a=0
    for i in f:
        l1=Label(root,font=(10),justify='left')
        if(a==0):
            l1['bg']='red'
            a=1
        else:
            l1['bg']='yellow'
            a=0
        l1['text']="{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        
        l1.grid(row=k,column=0)
       # b1=Button(root,text="buy",font=(10))#,command=b_buy)
        #b1.grid(row=k,column=1)
        k=k+1
    root.mainloop()

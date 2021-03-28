from tkinter import *
import sqlite3
from db_sale import *
#####################################################################################################

# THIS IS SIGN UP PAGE THERE ARE 4 ENTRY YOU HAVE TO FILL UP ABOUT USE TO GET AN USER ID 1-NAME 2-PHONE NUMBER 3-ADDRESS 4-PASSWORD
def a_sale():
    root=Tk()
    root.configure(background='#ccffdd',relief=RAISED)
    root.title("OLD BOOK STALL")
    root.geometry("600x400+400+150")
    root.resizable(0,0)
#GLOBAL VARIABLE
    #u_id=IntVar
    #name=StringVar
    #edition=StringVar
    #author=StringVar
    #helth=StringVar
    #price=IntVar
    #date=StringVar

    def pre_sale():
        
        b_create_table()
    
        b_insert_data(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get())
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
    

    l0=Label(root,text="BOOK DETAILS",bg="#00331a",fg="White",font=("impact",15),width="60",height='1',justify="right")
    l0.grid(row=0,column=0,columnspan=2)

    l1=Label(root,text="USER ID",bg="#006633",fg="White",font=("impact",12),width="15",height='1',anchor='w')
    l1.grid(row=1,column=0)
    e1=Entry(root,bg="#66ffb3",fg="black",font=("impact",12),width="37")#,textvariable=u_id)
    e1.grid(row=1,column=1,pady=10,padx=0)

    l2=Label(root,text="BOOK NAME",bg="#006633",fg="White",font=("impact",12),width="15",height='1',anchor='w')
    l2.grid(row=2,column=0,)
    e2=Entry(root,bg="#66ffb3",fg="black",font=("impact",12),width="37")#,textvariable=name)
    e2.grid(row=2,column=1,pady=10,padx=0)

    l3=Label(root,text="BOOK EDITION",bg="#006633",fg="White",font=("impact",12),width="15",height='1',anchor='w')
    l3.grid(row=3,column=0,)
    e3=Entry(root,bg="#66ffb3",fg="black",font=("impact",12),width="37")#,textvariable=edition)
    e3.grid(row=3,column=1,pady=10,padx=0)

    l4=Label(root,text="AUTHOR NAME",bg="#006633",fg="White",font=("impact",12),width="15",height='1',anchor='w')
    l4.grid(row=4,column=0,)
    e4=Entry(root,bg="#66ffb3",fg="black",font=("impact",12),width="37")#,textvariable=author)
    e4.grid(row=4,column=1,pady=10,padx=50)

    l5=Label(root,text="BOOK HELTH",bg="#006633",fg="White",font=("impact",12),width="15",height='1',anchor='w')
    l5.grid(row=5,column=0,)
    e5=Entry(root,bg="#66ffb3",fg="black",font=("impact",12),width="37")#,textvariable=helth)
    e5.grid(row=5,column=1,pady=10,padx=50)

    l6=Label(root,text="BOOK PRICE",bg="#006633",fg="White",font=("impact",12),width="15",height='1',anchor='w')
    l6.grid(row=6,column=0,)
    e6=Entry(root,bg="#66ffb3",fg="black",font=("impact",12),width="37")#,textvariable=price)
    e6.grid(row=6,column=1,pady=10,padx=50)

    l7=Label(root,text="ISSUE DATE",bg="#006633",fg="White",font=("impact",12),width="15",height='1',anchor='w')
    l7.grid(row=7,column=0,)
    e7=Entry(root,bg="#66ffb3",fg="black",font=("impact",12),width="37")#,textvariable=date)
    e7.grid(row=7,column=1,pady=10,padx=120)


    b1=Button(root,text="SUBMITE",bg="#00331a",fg="White",font=("impact",12),width="20",command=pre_sale)
    b1.grid(row=8,column=0,pady=10,padx=0,columnspan=4)
    
########################################################################################################

    root.mainloop()

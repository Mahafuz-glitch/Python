import sqlite3
con=sqlite3.connect('book.db')
cur=con.cursor()

def acc_del(d):
    cur.execute("delete from signup where u_ib=?",(d,))
    con.commit()


def bk_del(d):
    cur.execute("delete from sale where b_ib=?",(d,))
    con.commit()

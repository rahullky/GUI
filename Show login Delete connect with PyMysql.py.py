from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql as sql
import os


top = Tk()
top.geometry('1500x600')
top.config(bg='#D3D3D3')


tv = ttk.Treeview(top)
tv['columns'] = ('Name', 'lastname', 'Age')                
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=200)
tv.column('lastname', anchor=CENTER, width=200)                     #..........Data ko show karne..with Treeview.....................................
tv.column('Age', anchor=CENTER, width=200)
tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('lastname', text='Lastname', anchor=CENTER)
tv.heading('Age', text='Age', anchor=CENTER)
tv.place(x=700, y=100)



l = Label(top, text='REGISTRATION', bg='#D3D3D3', fg='black', font=('Arial 20 bold'))
l.place(x=400, y=50)

l2 = Label(top, text='Name', bg='#D3D3D3', fg='black', font=('Arial 15 bold'))
l2.place(x=300, y=150)

el = Entry(top, font=('Arial 15 bold'))
el.place(x=400, y=150)

l3 = Label(top, text='Lastname', bg='#D3D3D3', fg='black', font=('Arial 15 bold'))
l3.place(x=300, y=200)

e2 = Entry(top, font=('Arial 15 bold'))
e2.place(x=400, y=200)

l5 = Label(top, text='age', bg='#D3D3D3', fg='black', font=('Arial 15 bold'))
l5.place(x=300, y=250)

e3 = Entry(top, font=('Arial 15 bold'))
e3.place(x=400, y=250)



"""...Conecttion part """
def ins():
    k = el.get()
    k2 = e2.get()
    k3 = int(e3.get())
    print(k, k2, k3)
    db = sql.connect(host='127.0.0.1', user="root", password="Arun@7838@83", db="amitt")
    cur = db.cursor()
    s = "insert into test values(%s, %s, %s)"
    result = cur.execute(s, (k, k2, k3))
    if result > 0:
        messagebox.showinfo("Result", "Record insert successful")
    else:
        messagebox.showinfo("Result", "Record insert failed")
    db.commit()

def delete():
    k = el.get()
    db = sql.connect(host='127.0.0.1', user="root", password="Arun@7838@83", db="amitt")
    cur = db.cursor()
    s = "delete from test where name=%s"
    result = cur.execute(s, k)
    if result > 0:
        messagebox.showinfo("Result", "Record Delete successful")
    else:
        messagebox.showinfo("Result", "Record not Delete ")
    db.commit()

def show():
    tv.delete(*tv.get_children())  
    db = sql.connect(host='127.0.0.1', user="root", password="Arun@7838@83", db="amitt")
    cur = db.cursor()
    s = "Select * from test"
    cur.execute(s)
    result = cur.fetchall()
    for i in result:
        Name = i[0]
        lastname = i[1]
        age = i[2]
        tv.insert("", 'end', values=(Name, lastname, age))

def login():
    import pymysql as sql
    db = sql.connect(host='127.0.0.1', user="root", password="Arun@7838@83", db="amitt")
    cur= db.cursor()
    cur.execute("select * from  test where name =%s and lastname = %s",(el.get(),e2.get()))
    result = cur.fetchone()

    if result is None:
        messagebox.showinfo("Error", "Invalid User name and password")
    else:
        top.destroy()
        import kkk

b1 = Button(top, text='Submit', font=('Arial 15 '), command=ins)
b1.place(x=400, y=350)

b2 = Button(top, text='Delete', font=('Arial 15 '), command=delete)
b2.place(x=500, y=350)

b3 = Button(top, text='Show', font=('Arial 15 '), command=show)
b3.place(x=600, y=350)

b4 = Button(top, text='Login', font=('Arial 15 '), command=login)
b4.place(x=700, y=350)

top.mainloop()









#.part 1     importing
#start................................................................

#top = Tk()
#top.geometry('1500x600')
#top.config(bg='#D3D3D3')





# part 2   data ko show karna  with TreeView 
# part 3   Lable (name?) 
# part 4   Entry (input) dene 


"""...Conecttion part """
# part    Insert function with pymysql
# part    Delete function
# part    show  and login function connect with pymysql 

"""....Button part .."""

#...top.mainloop()
#endig................................................................    
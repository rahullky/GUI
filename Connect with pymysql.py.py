from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry('1000x600')
top.config(bg='#D3D3D3')       #..Light gray: #D3D3D3

def ins():
    k = el.get()
    k2 = e2.get()
    k3 = int(e3.get())
    print(k, k2, k3)
    import pymysql as sql
    db = sql.connect(host='127.0.0.1', user="root", password="Arun@7838@83", db="amitt")
    cur = db.cursor()
    s = "insert into test values('%s', '%s', '%s')" % (k, k2, k3)
    result = cur.execute(s)

    if result > 0:
        messagebox.showinfo("Result", "Record insert successful")
    else:
        messagebox.showinfo("Result", "Record insert failed")

    db.commit()


l = Label(top, text='REGISTRATION', bg='#D3D3D3', fg='black', font=('Arial 20 bold'))  
l.place(x=400, y=50)

l2 = Label(top, text='First', bg='#D3D3D3', fg='black', font=('Arial 15 bold')) 
l2.place(x=300, y=150)

el = Entry(top, font=('Arial 15 bold'))
el.place(x=400, y=150)

l3 = Label(top, text='Lastname', bg='#D3D3D3', fg='black', font=('Arial 15 bold'))  
l3.place(x=300, y=200)

l4 = Label(top, text='Result', bg='#D3D3D3', fg='black', font=('Arial 15 bold'))  
l4.place(x=300, y=450)

e2 = Entry(top, font=('Arial 15 bold'))
e2.place(x=400, y=200)

l5 = Label(top, text='age', bg='#D3D3D3', fg='black', font=('Arial 15 bold'))  
l5.place(x=300, y=250)

e3 = Entry(top, font=('Arial 15 bold'))
e3.place(x=400, y=250)

b = Button(top, text='Submit', font=('Arial 15 '), command=ins)
b.place(x=400, y=350)

top.mainloop()

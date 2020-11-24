from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.geometry('300x300')
window.title('Login Form')

name_ent = Entry(window)
surname_ent= Entry(window)
age_ent = Entry(window)

name_ent.place(x=90, y=50)
surname_ent.place(x=90, y=100)
age_ent.place(x=90, y=150)

lbl_1 = Label(window, text='Name: ')
lbl_2 = Label(window, text='Surname: ')
lbl_3 = Label(window, text='Age: ')

lbl_1.place(x=20, y=55)
lbl_2.place(x=20, y=105)
lbl_3.place(x=20, y=155)


def login():
    age = int(age_ent.get())
    ages = (age)
    if ages <18:
        messagebox.showerror('Error', 'You must be over 18')
        window.withdraw()
    elif ages >=18:
        messagebox.showinfo('Welcome', 'play responsibly ' + name_ent.get())
        window.withdraw()
        logged_in()


btn1 = Button(window, text='Login', bg='green', width='17', height='2', command=login)
btn1.place(x=90, y=200)

def logged_in():
    root = Tk()
    root.geometry('700x400')
    root.title('Lotto Ticket Generator')

    lbl1 = Label(root, text='Lotto Generator', font=["Arial",20])
    lbl1.pack()

    ent1 = Entry(root)
    ent1.place(x=10, y=100)

    ent2 = Entry(root)
    ent2.pack()

    root.mainloop()






window.mainloop()



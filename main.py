from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.geometry('350x350')
window.title('Login Form')

full_nm = Entry(window)
age_ent = Entry(window)

full_nm.place(x=90, y=50)
age_ent.place(x=90, y=120)

lbl_1 = Label(window, text='Full name: ')
lbl_2 = Label(window, text='Age: ')

lbl_1.place(x=10, y=55)
lbl_2.place(x=10, y=125)


def login():
    age = int(age_ent.get())
    ages = (age)
    if ages <18:
        messagebox.showerror('Error', 'You must be over 18')
        window.withdraw()
    elif ages >=18:
        messagebox.showinfo('Welcome', 'Are you ready to be a Millionare ' + full_nm.get())
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



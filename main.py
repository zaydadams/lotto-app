from tkinter import *
from random import sample
from tkinter import messagebox
# Login GUI
window = Tk()
window.geometry('350x350')
window.title('Login Form')

full_nm = Entry(window)
age_ent = Entry(window)

full_nm.place(x=90, y=50)
age_ent.place(x=90, y=120)

lbl_1 = Label(window, text='Full name ')
lbl_2 = Label(window, text='Age ')

lbl_1.place(x=10, y=55)
lbl_2.place(x=30, y=125)


# functions for the first GUI
def login():
    age = int(age_ent.get())
    ages = (age)
    if ages < 18:
        messagebox.showerror('Error', 'You must be over 18')
        window.withdraw()
    elif ages >= 18:
        messagebox.showinfo('Welcome Particapant', 'Are you ready to be a Millionare ' + full_nm.get())
        window.withdraw()
        logged_in()


btn1 = Button(window, text='Login', bg='green', width='17', height='2', command=login)
btn1.place(x=90, y=200)


def logged_in():
    root = Tk()
    root.geometry('700x400')
    root.title('Lotto Ticket Generator')
    lbl1 = Label(root, text='Lotto Generator', font=["Arial", 20])
    lbl1.pack()


    ent1 = Entry(root, width='2')
    ent2 = Entry(root, width='2')
    ent3 = Entry(root, width='2')
    ent4 = Entry(root, width='2')
    ent5 = Entry(root, width='2')
    ent6 = Entry(root, width='2')

    ent1.place(x=180, y=80)
    ent2.place(x=210, y=80)
    ent3.place(x=240, y=80)
    ent4.place(x=270, y=80)
    ent5.place(x=300, y=80)
    ent6.place(x=330, y=80)

    def user():
        num1=int(ent1.get())
        num2=int(ent2.get())
        num3=int(ent3.get())
        num4=int(ent4.get())
        num5=int(ent5.get())
        num6=int(ent6.get())

        list=[num1,num2,num3,num4,num5,num6]
        return list

    label1=Label(root,text="", bg='blue',fg='white')
    label1.place(x = 100, y= 120)

    def generate():
        r = sample(range(1, 50), 6)
        r.sort()

        label1.configure(text=r)

        counter = 0

        for number in user():
            if number in r:
                counter += 1

        if counter <= 1:
            messagebox.showinfo("attention", "you a unlucky poes")

        elif counter <= 2:
            messagebox.showinfo("attention", "you Won a R10 go buy you R10 mtn")

        elif counter <= 3:
            messagebox.showinfo("attention", "you Won Something")

        elif counter <= 4:
            messagebox.showinfo("attention", "you Won Something")

        elif counter <= 5:
            messagebox.showinfo("attention", "you Won Something")

        elif counter <= 6:
            messagebox.showinfo("attention", "you Won Something")


    btn = Button(root, text="generate", command=generate)
    btn.place(x=120, y=150)

    def clear():
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)
        label1.delete(0, END)


    btn2 =Button(root, text='clear', command=clear)
    btn2.pack()
    root.mainloop()


window.mainloop()

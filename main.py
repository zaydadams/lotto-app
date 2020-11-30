from tkinter import *
from random import sample
from tkinter import messagebox
from datetime import *

# Login GUI
window = Tk()
window.geometry('350x350')
window.title('Login Form')
window.config(bg='grey')

full_nm = Entry(window)
age_ent = Entry(window)

full_nm.place(x=90, y=50)
age_ent.place(x=90, y=120)

lbl_1 = Label(window, text='Full name ', bg='black', fg='white')
lbl_2 = Label(window, text='Age ', bg='black', fg='white')

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


btn1 = Button(window, text='Login', bg='black', fg='white', width='17', height='2', command=login)
btn1.place(x=90, y=200)

#second GUI
def logged_in():
    root = Tk()
    root.geometry('700x400')
    root.title('Lotto Ticket Generator')
    root.config(bg='grey')
    lbl1 = Label(root, text='Lotto Generator', font=["Arial", 20], bg='black', fg='white')
    lbl1.pack()

    ent1 = Entry(root, border='3', width='2')
    ent2 = Entry(root, border='3', width='2')
    ent3 = Entry(root, border='3', width='2')
    ent4 = Entry(root, border='3', width='2')
    ent5 = Entry(root, border='3', width='2')
    ent6 = Entry(root, border='3', width='2')

    ent1.place(x=350, y=120)
    ent2.place(x=400, y=120)
    ent3.place(x=450, y=120)
    ent4.place(x=500, y=120)
    ent5.place(x=550, y=120)
    ent6.place(x=600, y=120)

    def user():
        num1 = int(ent1.get())
        num2 = int(ent2.get())
        num3 = int(ent3.get())
        num4 = int(ent4.get())
        num5 = int(ent5.get())
        num6 = int(ent6.get())

        list=[num1,num2,num3,num4,num5,num6]
        return list

    label1= Label(root, text="", bg='black', fg='white')
    label1.place(x=500, y=200)

    label2= Label(root, text="Winning Numbers: ", bg='black', fg='white')
    label2.place(x=350, y=200)


    def generate():
        r = sample(range(1, 50), 6)
        r.sort()

        label1.configure(text=r)

        a= open("lottery.txt","a+")
        txt = "The lucky numbers are: " +str(r)
        txt1 = "The Users entries: " +str(user())
        today = datetime.now()
        day = today.strftime("%d %B %Y")
        time = today.strftime("%H:%M %p")
        data = "Name: "+full_nm.get() +"\n"+txt+"\n"+txt1+"\nDate: "+str(day)+"\nTime: "+str(time)+"\n="+"\n"
        a.write(data)

        counter = 0

        for number in user():
            if number in r:
                counter += 1

        if counter <= 1:
            messagebox.showerror("", "unlucky try again")

        elif counter == 2:
            messagebox.showerror("", "unlucky try again")

        elif counter == 3:
            messagebox.showerror("", "Unlucky try again")

        elif counter == 4:
            messagebox.showerror("", "Unlucky try again")

        elif counter == 5:
            messagebox.showerror("", "Unlucky try again")

        elif counter == 6:
            messagebox.showinfo("", "You Won")



    btn = Button(root, text="generate", bg='black', fg='white', command=generate)
    btn.place(x=120, y=122)

    def clear():
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)

    def exit():
        root.destroy()

    ext_btn = Button(root, text='exit', bg='black', fg='white', command=exit)
    ext_btn.place(x=180, y=200)

    btn2 =Button(root, text='clear', bg='black', fg='white', command=clear)
    btn2.place(x=100, y=200)

    def generate():
        text = open("lottery.txt","a+")
        text.write("Lotto numbers"+str(generate()))

    root.mainloop()


window.mainloop()

# function
from random import sample


r_num= sample(range(0, 50), 6)
print(r_num)

def victory():
    correct_num =[]
    for i in mylist:
        if i in r_num:
            correct_num.append(i)
    num_right = len(correct_num)
    if num_right == 1:
        print("you have won")

    if num_right == 2:
        print("you have won")

    if num_right == 3:
        print("you have won")

    if num_right == 4:
        print("you have won")


    if num_right == 5:
        print("you have won")


    if num_right == 6:
        print("you have won")

    else:
            print("you lose")
mylist=[]
for i in range(6):
    num = int(input("Enter number "+str(i+1)+": "))
    mylist.append(num)


victory()

# Gui
from tkinter import *
import random

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

shw_num = LabelFrame(root)
shw_num.pack()



def generate():
    random.randint(0, 49)



shw_btn = Button(root, text='generate', command=generate)
shw_btn.pack()

root.mainloop()



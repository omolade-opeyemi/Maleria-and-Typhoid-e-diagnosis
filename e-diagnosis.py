import tkinter
from tkinter import*
import itertools
win = Tk()
win.resizable(width=False, height=False)
win.title('E-diagnosis for maleria and typhoid')
win.configure(width = 430, height = 500, bg = 'skyblue')
l1 = Label(text = 'FOLLOW THE STEPS BELOW TO DIAGNOSE YOURSELF \nFOR MALERIA  OR TYPHOID',fg = 'black',bg = 'skyblue')
l1.place(x= 70,y=10)
t1 = Listbox(width = 65,height = 10)
t1.place(x=18, y=50)
list=['please select yes or no \n to take diagnosis.yes or no','FEVER','HEADACHE','MUSCLE PAIN AND FATIGUE','SWEATING','DRY COUGH','ABDOMINAL PAIN','DIARRHEA OR CONSTIPATION','NAUSEA AND VOMITING','SHIVERING','RASH']

yes = []
no = []



def true():
    return True
def false():
    return False

b1 = Button(text='YES', bd = 5, padx = 10, pady = 5, command = lambda :rb3.select())
b1.place(x=40,y=250)
b2 = Button(text='NO', bd = 5,padx = 10, pady = 5, command = lambda :rb4.select())
b2.place(x=300,y=250)
r2 = IntVar()
rb3 = Radiobutton(win, text = 'yes', variable = r2, value = 1)
rb3.place(x=40, y = 400)
rb4 = Radiobutton(win, text = 'no', variable = r2, value = 2)
rb4.place(x=300,y=400)
selection = r2.get()
n=0
def show(j):
    t1.delete(END,0)
    t1.insert(END,list[j])
for r in range(10,400,40):
    n+=1
    be =Button(text = n, padx = 13, command = lambda j=n :show(j) )
    be.place(x =r,y=300)

t1.insert(END , list[0])
if selection == 1:
    for i in range(1, 11):
        t1.delete(0, END)
        t1.insert(END , list[i])
        if  selection == 1:
            yes.append(list[i])
        elif selection == 2:
            no.append(list[i])
    else:
        t1.insert(END,'Thank you for banking with us')

win.mainloop()
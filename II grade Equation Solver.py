##############################
# IMPORT LIBRARIES
##############################
import numpy as np
from tkinter import *


##############################
# FUNCTION DEFINITION
##############################
def calcola():
    a = float(insert1.get())
    b = float(insert2.get())
    c = float(insert3.get())
    delta = b**2 - 4*a*c
    if insert4.get() == '=':
        if delta > 0:
            x1 = (- b + np.sqrt(delta))/(2*a)
            x2 = (- b - np.sqrt(delta))/(2*a)
            if x1 < x2:
                x = x1, ' V ', x2
            else:
                x = x2, ' V ', x1
        elif delta == 0:
            x = -b/(2*a)
        else:
            x = 'Equazione impossibile'
    elif insert4.get() == '>':
        if delta > 0:
            if a > 0: # Concordi esterni
                x1 = (- b + np.sqrt(delta))/(2*a)
                x2 = (- b - np.sqrt(delta))/(2*a)
                if x1 < x2:
                    x = 'x < ', x1, ' V x > ', x2
                else:
                    x = 'x < -', x2, ' V x > ', x1
            elif a < 0: # Discordi interni
                x1 = (- b + np.sqrt(delta))/(2*a)
                x2 = (- b - np.sqrt(delta))/(2*a)
                if x1 < x2:
                    x = x1, ' < x < ', x2
                else:
                    x = x2, ' < x < ', x1
        elif delta == 0: # Quadrato di binomio
            if b > 0:
                coef = - np.sqrt(c)
            elif b < 0:
                coef = np.sqrt(c)
            x = 'R - {', coef, '}'
        else:
            if a > 0:
                x = 'R'
            elif a < 0:
                x = 'Equazione impossibile'
    elif insert4.get() == '<':
        if delta > 0:
            if a < 0: # Concordi esterni
                x1 = (- b + np.sqrt(delta))/(2*a)
                x2 = (- b - np.sqrt(delta))/(2*a)
                if x1 < x2:
                    x = 'x < ', x1, ' V x > ', x2
                else:
                    x = 'x < ', x2, ' V x > ', x1
            elif a > 0: # Discordi interni
                x1 = (- b + np.sqrt(delta))/(2*a)
                x2 = (- b - np.sqrt(delta))/(2*a)
                if x1 < x2:
                    x = x1, ' < x < ', x2
                else:
                    x = x2, ' < x < ', x1
        elif delta == 0: # Quadrato di binomio
            if b > 0:
                coef = - np.sqrt(c)
            elif b < 0:
                coef = np.sqrt(c)
            x = 'R - {', coef, '}'
        else:
            if a < 0:
                x = 'R'
            else:
                x = 'Disequazione impossibile'
    output.configure(text=x)
            
def pulisci():
    insert1.delete(0, END)
    insert1.configure(text='')
    insert2.delete(0, END)
    insert2.configure(text='')
    insert3.delete(0, END)
    insert3.configure(text='')
    insert4.delete(0, END)
    insert4.configure(text='')
    output.configure(text='')


##############################
# MAIN BODY
##############################
f = Tk()
f.title('Risolutore di II grado')
f.geometry('400x400')

alta = Frame(f)
alta.pack()
title = Label(alta, text='Risolutore di II grado', font='arial 14')
title.grid(column=0, row=0, columnspan=2, padx=5, pady=5)
text1 = Label(alta, text='Inserisci il coefficiente a', font='arail 11')
text1.grid(column=0, row=1, padx=5, pady=5)
insert1 = Entry(alta)
insert1.grid(column=1, row=1, padx=5, pady=5)
text2 = Label(alta, text='Inserisci il coefficiente b', font='arial 11')
text2.grid(column=0, row=2, padx=5, pady=5)
insert2 = Entry(alta)
insert2.grid(column=1, row=2, padx=5, pady=5)
text3 = Label(alta, text='Inserisci il coefficiente c', font='arial 11')
text3.grid(column=0, row=3, padx=5, pady=5)
insert3 = Entry(alta)
insert3.grid(column=1, row=3, padx=5, pady=5)
text4 = Label(alta, text='Inserisci il segno', font='arial 11')
text4.grid(column=0, row=4, padx=5, pady=5)
insert4 = Entry(alta)
insert4.grid(column=1, row=4, padx=5, pady=5)

medium = Frame(f)
medium.pack()
output = Label(medium, text='')
output.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

bassa = Frame(f)
bassa.pack()
Solve = Button(bassa, text='Solve', font='arial 11', command=calcola)
Solve.grid(column=0, row=0, padx=5, pady=5)
Clean = Button(bassa, text='Clean', font='arial 11', command=pulisci)
Clean.grid(column=1, row=0, padx=5, pady=5)
Exit = Button(bassa, text='Exit', font='arial 11', command=f.destroy)
Exit.grid(column=2, row=0, padx=5, pady=5)

f.mainloop()

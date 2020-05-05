import tkinter
from tkinter import messagebox


raiz = tkinter.Tk()
raiz.title('messagebox')


def resetW():
    tkinter.messagebox.showinfo('WARNING','Reseteando el mundo')


rstbtn = tkinter.Button(raiz, text='Reset the world', command=resetW)
rstbtn.pack()




raiz.mainloop()

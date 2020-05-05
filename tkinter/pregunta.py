import tkinter
from tkinter import messagebox


raiz = tkinter.Tk()
raiz.title('pregunta')


def resetW():
    resultado = tkinter.messagebox.askquestion('WARNING','Resetear el mundo????')
    if (resultado == 'yes'):
        print('Reseteando el mundo')
    else:
        print('cagueta')

rstbtn = tkinter.Button(raiz, text='Reset the world', command=resetW)
rstbtn.pack()




raiz.mainloop()

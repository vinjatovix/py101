import tkinter

raiz = tkinter.Tk()
raiz.title('botón')


def accion():
    print('Reseteando el mundo')

boton = tkinter.Button(raiz,text='Reset the world', command=accion)

boton.pack()


raiz.mainloop()

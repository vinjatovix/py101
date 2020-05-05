import tkinter

raiz = tkinter.Tk()
raiz.title('radio')


def seleccionar():
    print('La opcion seleccionada es {}'.format(opcion.get()))


opcion = tkinter.IntVar()

rb1 = tkinter.Radiobutton(
    raiz, text='op1', variable=opcion, value=1, command=seleccionar)
rb1.pack()
rb2 = tkinter.Radiobutton(
    raiz, text='op2', variable=opcion, value=2, command=seleccionar)
rb2.pack()
rb3 = tkinter.Radiobutton(
    raiz, text='op3', variable=opcion, value=3, command=seleccionar)
rb3.pack()


raiz.mainloop()

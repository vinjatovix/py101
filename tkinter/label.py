import tkinter

raiz = tkinter.Tk()
raiz.title('label')



texto = 'Hola Mundo'
etiqueta = tkinter.Label(raiz,text=texto)
etiqueta.config(fg='yellow',bg='lightblue',font=('Cortana',30))

etiqueta.pack()





raiz.mainloop()
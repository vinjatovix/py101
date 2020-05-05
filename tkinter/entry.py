import tkinter

raiz = tkinter.Tk()
raiz.title('entry')




entrada = tkinter.Entry(raiz)
entrada.config(justify='center')
entrada.pack()



entrada2 = tkinter.Entry(raiz)
entrada2.config(justify='center',show='*')
entrada2.pack()





raiz.mainloop()
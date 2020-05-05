import tkinter

raiz = tkinter.Tk()
raiz.title('checkbutton')


def verificar():
    v = ck1.get()
    if ( v == 1):
        print('Eres un humano')
    else:
        print('Erec un robot')



ck1 = tkinter.IntVar()

ckbtn = tkinter.Checkbutton(raiz, text='Eres un humano?',
                            variable=ck1, onvalue=1, offvalue=0,
                            command=verificar)
ckbtn.pack()


raiz.mainloop()

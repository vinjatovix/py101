import tkinter
from tkinter import  filedialog


raiz = tkinter.Tk()
raiz.title('pregunta')


def loadFile():
    filePath = filedialog.askopenfilename(title='¿Qué quieres cargar?')
    print(filePath)
   


rstbtn = tkinter.Button(raiz, text='Cargar', command=loadFile)
rstbtn.pack()




raiz.mainloop()
 
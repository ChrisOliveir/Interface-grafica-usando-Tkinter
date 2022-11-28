import tkinter as tk
from tkinter import Tk



'''def valores():
    janela = tk.Tk()
    janela.title("Pegar numeros")
    janela.rowconfigure(0, weight=1)
    janela.columnconfigure([0,1], weight=1)
    rss = 45
    state = True
    tsl = 10
    a = tk.Entry()
    a.grid(row=1, column=1)
    b = a.get()
    if state == True:
        if tsl > b:
            if rss < 50:
                 print("ok")
            else:
                print("n ok")
        if tsl < b:
            if rss > 50:
                print("n ok")
            else:
                print("n ok")
                
    
    botao = tk.Button(text="Adicionar numero", command=b)
    botao.grid(row=2, column=1)

    janela.mainloop() # visualizar a janela que ele esta construindo

valores()'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def busca(b):
    tdd = 5
    rss = 5
    if tdd > b:
        print("ok") 
    else:
        print("n ok")   


ttk.Button(root, text='Selecione 4', command=lambda: busca(4)).pack()
ttk.Button(root, text='Selecione 6', command=lambda: busca(6)).pack()


root.mainloop()
   


             
'''janela = tk.Tk()
janela.title("Pegar numeros")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)
tes = tk.Entry() # campo de entrada de informações
tes.grid(row=1, column=1)

botao = tk.Button(text="Adicionar numero", command=val)
botao.grid(row=2, column=1)

janela.mainloop() # visualizar a janela que ele esta construindo-   '''     

       
           
                 


    


    


'''def numeros(a):
    b = 45
    if b > a :
        print('ok')
    else:
        print("n ok")

numeros(46)'''
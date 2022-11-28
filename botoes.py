import tkinter as tk
from tkinter import Tk

janela = tk.Tk()
janela.title("teste 1")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)

mensagem = tk.Label(text="Teste", foreground='white', background="black", width=35, height=5)  # criar objeto, foreground = cor da letra, background= cor da caixa da letra
# as cores eu posso procurar o numero hexadecimal 
mensagem.grid(row=0,column=0, columnspan=2, sticky="NSEW") # permite que coloque as mensagens em linhas e colunas como se fosse o excel, columnspan = quantas colunas ocupa.
#sticky = preenche para leste/oeste/norte/sul colocando as respectivas iniciais em ingles NSEW

mensagem2 = tk.Label(text="selecione o valor")
mensagem2.grid(row=1, column=0)

tes = tk.Entry() # campo de entrada de informações
tes.grid(row=1, column=1)


def busca(b):
    a = tk.Entry()
    b = a
    tdd = 5
    rss = 5
    if tdd > b:
        print("ok")    



botao = tk.Button(text="Adicionar numero", command=lambda: busca(4))
botao.grid(row=2, column=1)
print(botao)

janela.mainloop() # visualizar a janela que ele esta construindo

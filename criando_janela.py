# cria-se essencialmente uma janela vazia e vai colocando os objetos que deseja.
import tkinter as tk
from tkinter import Tk # tkinter ja esta instalado automaticamente no python

janela = tk.Tk()
janela.title("teste 1")

mensagem = tk.Label(text="Teste", foreground='white', background="black", width=35, height=5)  # criar objeto, foreground = cor da letra, background= cor da caixa da letra
# as cores eu posso procurar o numero hexadecimal 
mensagem.pack() # pega a mensagem e coloca dentro do tkinter

mensagem2 = tk.Label(text="selecione o valor")
mensagem2.pack()

tes = tk.Entry() # campo de entrada de informações
tes.pack()

janela.mainloop() # visualizar a janela que ele esta construindo

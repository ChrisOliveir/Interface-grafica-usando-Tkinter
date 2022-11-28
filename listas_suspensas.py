import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Pegar numeros")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)

mensagem = tk.Label(text="Teste", foreground='white', background="black", width=35, height=5)  # criar objeto, foreground = cor da letra, background= cor da caixa da letra
# as cores eu posso procurar o numero hexadecimal 
mensagem.grid(row=0,column=0, columnspan=2, sticky="NSEW") # permite que coloque as mensagens em linhas e colunas como se fosse o excel, columnspan = quantas colunas ocupa.
#sticky = preenche para leste/oeste/norte/sul colocando as respectivas iniciais em ingles NSEW

mensagem2 = tk.Label(text="selecione o valor")
mensagem2.grid(row=1, column=0)

'''tes = tk.Entry() # campo de entrada de informações
tes.grid(row=1, column=1)
'''


dicionario_numeros = {
    'a': 8,
    'b': 9,
}

num = list(dicionario_numeros.keys())
nums = ttk.Combobox(janela, values = num)
nums.grid(row=1, column=1)

def buscar_numeros():
    numero_preenchido = nums.get()
    numero_disponivel = dicionario_numeros.get(numero_preenchido)
    mensagem = tk.Label(text="Numero não disponivel")
    mensagem.grid(row=3, column=0)
    if numero_disponivel:
        mensagem["text"] = f'numero do {numero_preenchido} é {numero_disponivel}'
        pass 
    else:
        pass 

botao = tk.Button(text="Adicionar numero", command=buscar_numeros)
botao.grid(row=2, column=1)

janela.mainloop() # visualizar a janela que ele esta construindo

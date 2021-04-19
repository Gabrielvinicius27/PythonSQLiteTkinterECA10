import tkinter as tk 
from tkinter import ttk 

import sqlite3


def fnNome(*args):
    print("Nome {}".format(enNome.get()))
def fnRa(*args):
    print("Ra {}".format(enRa.get())) 
def fnCracha(*args):
    print("Cracha {}".format(enCracha.get())) 
def fnChamada(*args):
    print("Chamada {}".format(enChamada.get())) 


def montaCamposPesquisa(frame, campos):
    index = 0
    for campo in campos:
        globals()["lb"+str(campo)] = ttk.Label(frame, text="{}:".format(campo))
        globals()["en"+str(campo)] = ttk.Entry(frame)
        globals()["en"+str(campo)].bind('<Return>', globals()["fn"+str(campo)])
        globals()["bt"+str(campo)] = ttk.Button(frame, text="Pesquisar", command = globals()["fn"+str(campo)])
        
        globals()["lb"+str(campo)].grid(row=0, column=index, sticky='w') 
        globals()["en"+str(campo)].grid(row=0, column=index+1, padx=2) # padx é o espaçamento de 2 pixels na vertical
        globals()["bt"+str(campo)].grid(row=0, column=index+2, padx=2)
        index += 3

janela = tk.Tk()

# Frame Campos de Pesquisa
frEntradas = ttk.LabelFrame(janela, text = "Campos de Pesquisa")
# Função que cria e posiciona campos de pesquisa
# Informar quais campos deseja criar e em qual frame colocar
# Serão criados entradas que se chamaram (en + nomeCampo) Ex enRa
# Serão criados botões que se chamatam (bt + nomeCampo) Ex btCracha
campos = ['Nome', 'Ra', 'Cracha', 'Chamada']
montaCamposPesquisa(frEntradas, campos)

frEntradas.grid(row=0, column=0)

janela.geometry("1200x500+0+0")
janela.title("Consulta de Alunos - Integração SQLite e GUI")
janela.mainloop()

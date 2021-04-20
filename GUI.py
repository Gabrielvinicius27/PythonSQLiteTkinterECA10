import tkinter as tk 
from tkinter import ttk 

import sqlite3


def fnNome(*args):
    print("Nome {}".format(enNome.get()))
    Consulta("nome", enNome.get())
def fnRa(*args):
    print("Ra {}".format(enRa.get())) 
    Consulta("ra", enRa.get())
def fnCracha(*args):
    print("Cracha {}".format(enCracha.get())) 
    Consulta("cracha", enCracha.get())
def fnChamada(*args):
    print("Chamada {}".format(enChamada.get())) 
    Consulta("chamada", enChamada.get())

def Consulta(campo, valor):
    tree.delete(*tree.get_children())
    conn = sqlite3.connect('eca10_2021_1.db')
    cur =  conn.cursor()
    registro = 'SELECT * FROM alunos WHERE {0} LIKE "%{1}%"'.format(campo, valor)
    cur.execute(registro)
    result = cur.fetchall()
    
    count = 1
    for item in result:
        tree.insert('', 'end', count, text=count)
        tree.set(count, 'RA', item[0])
        tree.set(count, 'Nome', item[1])
        tree.set(count, 'Cracha', item[2])
        tree.set(count, 'Chamada', item[3])
        count+=1
    countResults.set("Quantidade de linhas encontradas: {}".format(count - 1))

def montaCamposPesquisa(frame, campos, photo):
    index = 0
    for campo in campos:
        globals()["lb"+str(campo)] = ttk.Label(frame, text="{}:".format(campo))
        globals()["en"+str(campo)] = ttk.Entry(frame)
        globals()["en"+str(campo)].bind('<Return>', globals()["fn"+str(campo)])
        globals()["bt"+str(campo)] = ttk.Button(frame, image=photo, command = globals()["fn"+str(campo)])
        
        globals()["lb"+str(campo)].grid(row=0, column=index, sticky='w') 
        globals()["en"+str(campo)].grid(row=0, column=index+1, padx=2) # padx é o espaçamento de 2 pixels na vertical
        globals()["bt"+str(campo)].grid(row=0, column=index+2, padx=2)
        index += 3
    
janela = tk.Tk()

# Frame Campos de Pesquisa
frEntradas = ttk.LabelFrame(janela, text = "Campos de Pesquisa")

# Função que cria e posiciona campos de pesquisa
# Informar quais campos deseja criar, em qual frame colocar e imagem para os botões 
# Serão criados entradas que se chamaram (en + nomeCampo) Ex enRa
# Serão criados botões que se chamatam (bt + nomeCampo) Ex btCracha
campos = ['Nome', 'Ra', 'Cracha', 'Chamada']
photo = tk.PhotoImage(file = './iconePesquisa.png', height=20, width=20)
montaCamposPesquisa(frEntradas, campos, photo)

frTree = ttk.LabelFrame(janela, text="Resultados da Pesquisa")
tree = ttk.Treeview(frTree)
tree['columns'] = ['Nome', 'RA', 'Cracha', 'Chamada']
for column in tree['columns']:
    tree.heading(column, text=column)

countResults = tk.StringVar()
lbCountResults = ttk.Label(frTree, textvariable=countResults)

frEntradas.grid(row=0, column=0)
frTree.grid(row=1)
tree.grid(row=0, columnspan=2)
lbCountResults.grid(row=1, column=0, sticky='w')

janela.geometry("1200x500+0+0")
janela.title("Consulta de Alunos - Integração SQLite e GUI")
janela.mainloop()

import tkinter as tk 
from tkinter import ttk 

import sqlite3

# Funções para passar parâmetros de consulta
def fnNome(*args):
    Consulta("nome", str(enNome.get()))
def fnRa(*args):
    Consulta("ra", str(enRa.get()))
def fnCracha(*args):
    Consulta("cracha", str(enCracha.get()))
def fnChamada(*args):
    Consulta("chamada", str(enChamada.get()))

# Função para fazer consulta
def Consulta(campo, valor):
    # Limpa o widget Treeview
    tree.delete(*tree.get_children())
    # Conecta a base de dados
    conn = sqlite3.connect('eca10_2021_1.db')
    cur =  conn.cursor()
    # Faz o SELECT usando os parâmetros passados para a função
    registro = 'SELECT * FROM alunos WHERE {0} LIKE "%{1}%"'.format(campo, valor)
    cur.execute(registro)
    result = cur.fetchall()
    # Fecha a conexão
    cur.close()
    conn.close()
    # Preenche o widget Treeview
    count = 1
    for item in result:
        tree.insert('', 'end', count, text=count)
        tree.set(count, 'RA', item[0])
        tree.set(count, 'Nome', item[1])
        tree.set(count, 'Cracha', item[2])
        tree.set(count, 'Chamada', item[3])
        count+=1
    # Mostra quantos resultados foram encontrados
    countResults.set("Quantidade de linhas encontradas: {}".format(count - 1))

# Função para montar os campos de pesquisa
def montaCamposPesquisa(frame, campos, photo):
    index = 0
    for campo in campos:
        # globals()[] será usado para criar o nome do objeto
        globals()["lb"+str(campo)] = ttk.Label(frame, text="{}:".format(campo))
        globals()["en"+str(campo)] = ttk.Entry(frame)
        globals()["en"+str(campo)].bind('<Return>', globals()["fn"+str(campo)])
        globals()["bt"+str(campo)] = ttk.Button(frame, image=photo, command = globals()["fn"+str(campo)])
        
        # Posiciona widgets na tela
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

# Cria widget Treeview e seu Frame
frTree = ttk.LabelFrame(janela, text="Resultados da Pesquisa")
tree = ttk.Treeview(frTree)
# Colunas do Treeview
tree['columns'] = ['Nome', 'RA', 'Cracha', 'Chamada']
for column in tree['columns']:
    tree.heading(column, text=column)
# Label para mostrar quantos resultados foram encontrados
countResults = tk.StringVar()
lbCountResults = ttk.Label(frTree, textvariable=countResults)
# Monta alguns widgets na tela
frEntradas.grid(row=0, column=0)
frTree.grid(row=1)
tree.grid(row=0, columnspan=2)
lbCountResults.grid(row=1, column=0, sticky='w')
# Configura janela
janela.geometry("1200x500+0+0")
janela.title("Consulta de Alunos - Integração SQLite e GUI")
janela.mainloop()

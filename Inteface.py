"""
Tkinter == TK interface
TK interface é a biblioteca
Tkinter é a biblioteca gráfica nativa do python  que te permite criar interface com Python, vem junto ao python;
A biblioteca não faz parte do Python mas o Python faz uso dela
Elas é multiplataforma nos principais sistemas unix e microsoft windows
tkinter pertence a biblioteca TclTK que nos permite fazer o uso dos principais recursos da biblioteca
GUI--- Grafic User Interface == Inteface gráfica de usuário
"""
"""
#############################################Algumas palavras usadas####################################################
Widget: é todo componente que compõe uma interface. ex: Botões, janelas, entre outros.
Container: é um widget ou componente que pode conter outros componentes. Todo container também está contido num outro container.
Window: Uma area retangular que é capaz de receber os nossos componentes. Uma janela.
Top-level-widindow: é uma janela independente que se sobre põe a janela que estamos trabalhando e é usada por outras janelas.
Frame: é a unidade básica de organização de layout complexos.
Chil-parent: é o nome da relação entre componentes e seu container. Um campo adicionado a nossa janela é uma relação parent-child,na qual a janela é o parente e o campo é o child


#Estamos importando tudo da biblioteca tkinter
from tkinter import *
#Atribuindo a instância Tk a nossa varíavel janela
janela = Tk()

#Nossa label
Label(janela, text = "Olá mundo").pack()

janela.mainloop()
############################################################
import tkinter as tk

window = tk.Tk()

#Alterando o titulo da janela
window.title("AngoCoder")
#Aterando a cor de fundo
window["bg"] = "white"
#Alterando a altura, largura e a posição por chamar a Dinstância Geometry.
#Segue-se essa ordem LxA+E+T Largura, Altura + para definir a instância Esqueda do video e + para definir a instância do Topo do vídeo
#Definindo a largura, altura, Disntância esquertda e do Topo do vídeo.
#wxh+l+t
# 1300x800+100+100
window.geometry("1300x800+100+100")#Propriedades da nosaa janela
window.mainloop()

##Gerenciador de layoute é um widget que gerencia o posicionamento dos layoutes dentro do container

Os três Pilares da Iterface Gráfica
1 - Greanciadores de Layout == Place, pack e grid.
2 - Widget (Componentes)
3 - eventos
"""
#Desenvolvimento de interface
#Trabalhando com Python 3.4
#Conjunto de carectere: UTF8

#Estamos chamando a nossa biblioteca tkinter por tk
from functools import partial
from tkinter import *
window = Tk()
window.title("AngoCoder")
#Criando eventos de click

def btn_click_nome():
    print(ed1.get())
    print(ed2.get())
    ##lb["text"] = ed1.get() mostrando a senha a partir do albel

"""
#########Calculos de adição#### mine calculadora
from tkinter import *
janela = Tk()
    def btn2():
      numero1 = int(edt1.get())
      numero2 = int(edt2.get())   
      if(numero1 == '' and numero2 == ''):
            lb["text"] = "Digite os dois valores"
        else:
          soma = nuemro1 + numero2
      lb["text"] = soma  
      

edit1 = Entery(janela)
edit1.place(x=100, y=100)

edit2 = Entery(janela)
edit2.place(x=100, y=120)
btn = Button(janela, text="Soma", width=20, command=btn2)
lb = Label(janela, text="Resultado")

janela.geometry
janela.mainloop("300x300+200+200")
"""
#Entrada de dados
#ed1
ed1 = Entry(window)
ed1.place(x=100, y=110)
#Label
lb = Label(window, text="Digita seu email ou telemóvel")
#Posicionando o nosso label
lb.place(x = 100, y = 97)
#ed2
ed2 = Entry(window)
ed2.place(x=100, y=188)
#Label
lb = Label(window, text="Digite sua senha de usuario")
#Posicionando o nosso label
lb.place(x = 100, y = 160)
#Botão
btn = Button(window, width=20, text="Entrar ", command=btn_click_nome)
#Posicionando o nosso botão
btn.place(x=100, y=220)
btn["bg"] = "green"

#Botão2
btn2 = Button(window, width=20, text="Cadstrar ")
#Posicionando o nosso botão
btn2.place(x=100, y=250)
btn2["bg"] = "Blue"

#Label
lb = Label(window, text="Seja Bem-Vindo de volta à AngoCoder")
#Posicionando o nosso label
lb.place(x = 50, y = 20)

window.geometry("300x300+200+200")
window.mainloop()
"""
#Gerenciador de layout Pack
from tkinter import *
janela = Tk()
lb1 = Labael(janela, text="1", bg="red")
lb2 = Labael(janela, text="2", bg="green")
lb3 = Labael(janela, text="3", bg="blue")
lb4 = Labael(janela, text="4", bg="yellow")
lb6 = Labael(janela, text="6", bg="white")
##O pack() define a ordem em que os componentes serão apresentados
lb3.pack(side=Left)# Posicionado na parte esquerda
lb1.pack(side=Rigth)#Posicionado na parte direita
lb2.pack(side=BOTTOM)#Posicionado na parte inferior
lb4.pack(side=Top)#Posicionado na parte superior
lb5.pack(sid=RIGTH, fill=y)#Alinahdo a esquarda na vertical
lb6.pack(sid=TOP, fill=BOTH, expand=1 )#Estará alinahdo no topo, em todas as direções
"""

"""
Gerenciador de layout Grid
O mais usado
#Para entendermos sobre grid temos que entender o conceito de linhas e colunas

from tkinter import *
janela = Tk()

lb = Labael(janela, text="6", bg="blue")
lb.grid(row=1, column=1)#O nosso componente estará na primeira linha e na primeira coluna

lb1 = Labael(janela, text="5", bg="red")
lb1.grid(row=1, column=2)#O nosso componente estará na primeira linha e na segunda coluna


janela.geometry(300x200+100+100)
janela.mainloop()
"""



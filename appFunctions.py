from consts import *
import numpy as np
import time as t
import tkinter as tk


#Limpa os dados da TreeView:
def clearData(tv):
    tv.delete(*tv.get_children())


#Função que plota a curva de carga:
def FunBotaoPlotar(ax, canva):
    ax.clear()
    ax.plot(np.arange(0,24,1),cc, color='red', label='Curva de carga', linewidth=4)
    ax.set_ylabel('Porcentagem de carga')
    ax.set_xticks(range(24))
    ax.set_yticks(np.arange(0,1.25,0.25))
    ax.grid(True)
    canva.draw()
    
    print('plotarCC')

    
    
#Função que roda o algoritmo genético: 
def FunBotaoRoda(tv, pma, pmc, pmb, ax, canva):
    t1 = t.time()
    pms = [pma, pmc, pmb]
    
    #==Verifica se algum dos valores está vazio==#
    if '' in pms:
        tk.messagebox.showerror("Informativo", "Insira valores para Pma, Pmb e Pmc")
        return None
    clearData(tv)
    
    pms = [int(pm) for pm in pms]
    
    for valCC in cc:
        ...
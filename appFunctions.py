from consts import *
import numpy as np
import time as t
import tkinter as tk
from funAG import FunAG as AG
import pandas as pd


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
    
    
#Função que roda o algoritmo genético: 
def FunBotaoRoda(tv, pma, pmc, pmb):
    #Contador de tempo:
    t1 = t.time()
    #Lista com os valores máximos de potência:
    pms = [pma.get(), pmb.get(), pmc.get()]
    
    #Verifica se algum dos valores de potência está vazio:
    if '' in pms:
        pms = [1000, 1000, 1000]
    
    #Limpa os dados da TreeView:
    clearData(tv)
    
    #Passa os valores de potência para inteiros:
    pms = [int(pm) for pm in pms]
    
    #Cria o dicionario com as potencias em cada fase, barramento e valor da fob:
    dicResultadoAg = {'% Carga':[], 'Pot A':[], 'Pot B':[], 'Pot C':[], 'FOB':[]}
    
    #Rodando o algoritmo genético:
    for valCC in cc:
        #Variável q representa a hora do dia:
        i=0
        
        #Objeto do algoritmo genético:
        ag = AG(valCC)
        #Chama o método de execução do algoritmo genético:
        results, log, dicMelhoresIndiv = ag.execAg(pms=pms, 
                                                   numRep=1)
        
        #Adiciona os valores no dicionário:
        listaPotsBus = dicMelhoresIndiv['cromossomos']
        listaFobs = dicMelhoresIndiv['fobs']
        dicResultadoAg['% Carga'].append(i)
        dicResultadoAg['Pot A'].append([listaPotsBus[idx][0] for idx in range(len(listaPotsBus))])
        dicResultadoAg['Pot B'].append([listaPotsBus[idx][1] for idx in range(len(listaPotsBus))])
        dicResultadoAg['Pot C'].append([(-listaPotsBus[idx][0]-listaPotsBus[idx][1]) for idx in range(len(listaPotsBus))])
        dicResultadoAg['FOB'].append(listaFobs)
        
        i+=1
    
    #Printa o dicionário com os resultados:  
    print(dicResultadoAg)
    
    #Cria um DataFrame com os resultados:
    dfResultadoAg = pd.DataFrame(dicResultadoAg)
    
    #Cria uma TreeView com os melhores indivíduos:
    tv["column"] = list(dfResultadoAg)
    tv["show"] = "headings"
    for column in tv["columns"]:
        tv.heading(column, text=column) 
    df_rows = dfResultadoAg.to_numpy().tolist()
    for row in df_rows:
        tv.insert("", "end", values=row)
    t2 = t.time()
    print(t2-t1)
    
    return None
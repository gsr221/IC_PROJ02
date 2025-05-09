from curvaCarga import curva_carga as cc
import numpy as np

def plotar(y, ax, canva):
    ax.clear()
    ax.plot(np.arange(0,24,1),y)
    canva.draw()

def FunBotaoPlotar(ax, canva):
    plotar(cc, ax, canva)
    
def FunBotaoRoda():
    ...
    
def plotar():
    ...
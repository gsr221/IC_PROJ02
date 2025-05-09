import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
from appFunctions import *

class App (tk.Tk):
    def __init__(self):
        #Setup inicial:
        super().__init__()
        self.title('Aplicativo IC02')
        self.geometry('1280x720')
        
        #Frames:
        self.frame_top = FrameTop(self)
        self.frame_mid = FrameMid(self)
        self.frame_bot = FrameBot(self)
        
        #Loop da janela:
        self.mainloop()
        
class FrameTop(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.creat_widgets()
        self.creat_layout()
        
    def creat_widgets(self):
        self.figCC, self.axCC = plt.subplots()
        self.axCC.set_ylabel('Porcentagem de carga')
        self.axCC.set_xticks(range(24))
        self.axCC.grid(True)
        self.canvasCC = FigureCanvasTkAgg(self.figCC, master=self)
        
    def creat_layout(self):
        self.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.39)
        self.canvasCC.get_tk_widget().place(relx=0, rely=0, relheight=1, relwidth=1)
        
        
class FrameMid(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.creat_widgets()
        self.creat_layout() 
        
    def creat_widgets(self):
        self.potMaLabel = tk.Label(self, text = 'Pma =')
        self.potMbLabel = tk.Label(self, text = 'Pmb =')
        self.potMcLabel = tk.Label(self, text = 'Pmc =')
        
        self.potMaEntry = tk.Entry(self)
        self.potMbEntry = tk.Entry(self)
        self.potMcEntry = tk.Entry(self)
        
    def creat_layout(self):
        self.place(relx=0, rely=0.43, relwidth=1, relheight=0.03)
        
        self.potMaLabel.place(relx=0, rely=0, relwidth=0.1, relheight=1)
        self.potMbLabel.place(relx=0.15, rely=0, relwidth=0.1, relheight=1)
        self.potMcLabel.place(relx=0.3, rely=0, relwidth=0.1, relheight=1)
        
        self.potMaEntry.place(relx=0.07, rely=0, relwidth=0.1, relheight=1)
        self.potMbEntry.place(relx=0.22, rely=0, relwidth=0.1, relheight=1)
        self.potMcEntry.place(relx=0.37, rely=0, relwidth=0.1, relheight=1)
        
class FrameBot(ttk.Frame, FrameTop):
    def __init__(self, parent):
        ttk.Frame.__init__(parent)
        FrameTop.__init__()
        self.creat_widgets()
        self.creat_layout()
        
    def creat_widgets(self):
        #Subframes:
        self.frameResults = ttk.Frame(self)
        self.frameGraficoDeseq = ttk.Frame(self)
        self.frameBotoes = ttk.Frame(self)
        
        #Gráfico:
        self.figDeseq, self.axDeseq = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figDeseq, master=self.frameGraficoDeseq)
        self.axDeseq.set_ylabel('Desequilíbrio Máximo')
        self.axDeseq.set_xticks(range(24))
        self.axDeseq.set_yticks(np.arange(0,2.5,0.5))
        self.axDeseq.grid(True)
        self.toolbarDeseq = NavigationToolbar2Tk(self.canvas, self.frameGraficoDeseq)
        self.toolbarDeseq.update()
        
        #Treeview:
        self.tree = ttk.Treeview(self.frameResults)
        self.treescrolly = ttk.Scrollbar(self.frameResults, orient="vertical", command=self.tree.yview)
        self.treescrollx = ttk.Scrollbar(self.frameResults, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.treescrolly.set, xscrollcommand=self.treescrollx.set)
        
        #Botoes:
        self.botaoRodar = ttk.Button(self.frameBotoes, text = 'Rodar')
        self.botaoPlot = ttk.Button(self.frameBotoes, text = 'Curva de Carga', command = lambda: FunBotaoPlotar(FrameTop.axCC, FrameTop.canvaCC))
        
    def creat_layout(self):
        self.place(relx=0.02, rely=0.48, relwidth=0.96, relheight=0.5)
        
        self.frameResults.place(relx=0, rely=0, relwidth=0.5, relheight=0.92)
        self.frameGraficoDeseq.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.92)
        self.frameBotoes.place(relx=0, rely=0.92, relwidth=1, relheight=0.08)
        
        self.botaoRodar.place(relx=0.8, rely=0, relwidth=0.1, relheight=1)
        self.botaoPlot.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        
        self.canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=0.9)
        self.toolbar.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        
        self.tree.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.treescrolly.pack(side="right", fill='y')
        self.treescrollx.pack(side="bottom", fill='x')
        
App()
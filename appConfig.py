import tkinter as tk
from tkinter import ttk

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
        
    def creat_widget(self):
        ...
        #Criar o widget para plotar o gráfico
        
class FrameMid(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def creat_widget(self):
        potMaLabel = tk.Label(self, text = 'Pma =')
        potMbLabel = tk.Label(self, text = 'Pmb =')
        potMcLabel = tk.Label(self, text = 'Pmc =')
        
        potMaEntry = tk.Entry(self)
        potMbEntry = tk.Entry(self)
        potMcEntry = tk.Entry(self)
        
class FrameBot(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def creat_widgets(self):
        botaoRodar = ttk.Button(self, text = 'Rodar')
        botaoPlot = ttk.Button(self, text = 'Plotar Curva')
        #===========
        #Criar o lugar para mostrar os resultados, pensar ainda como serão exibidos
        #===========
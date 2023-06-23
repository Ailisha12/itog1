import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *

class Logg(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.style = ttk.Style(theme='morph')
        self.title('Логи')
        self.geometry("500x600")
        self.resizable(False,False)
        self.exc = ttk.Entry() 
        self.exc.pack(pady=10) 
        
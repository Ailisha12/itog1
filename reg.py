import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
import sqlite3


class Registration(tk.Toplevel):

    def __init__(self,parent):
        super().__init__(parent)
        self.style = ttk.Style(theme='morph')
        self.title('Регистрация')
        self.geometry("500x600")
        self.resizable(False,False)
        
        self.RegLabelEntry = ttk.Label(self,text='Регистрация', font=("Helvetica",34,'bold'),bootstyle="morph")
        self.RegLabelEntry.pack(pady=30)

        self.RegLoginHint = ttk.Label(self,text='Логин', font=("Helvetica",15,'bold'),bootstyle="morph")
        self.RegLogin = ttk.Entry(self,bootstyle="morph",width=30,font=("Helvetica",20,'bold'))
        self.RegPasswordHint = ttk.Label(self,text='Пароль', font=("Helvetica",15,'bold'),bootstyle="morph")
        self.RegPassword = ttk.Entry(self,bootstyle="morph",width=30,show="*",font=("Helvetica",20,'bold'))

        self.RegLoginHint.pack(pady=5)
        self.RegLogin.pack(pady=30)
        self.RegPasswordHint.pack(pady=5)
        self.RegPassword.pack(pady=30)

        def InsertIntoDb():
            conn = sqlite3.connect("Users.db")
            cur = conn.cursor()
            log = self.RegLogin.get()
            reg = self.RegPassword.get()
            cur.execute(f"Select Login,Password from Users WHERE Login = '{log}' AND Password = '{reg}'")
            if cur.fetchone() is None:
                cur.execute("INSERT INTO Users VALUES (?,?)",(log,reg))
                conn.commit()
                self.RegLabelEntry.config(text="Регистрация прошла успешна")
            else:
                self.RegLabelEntry.config(text="Пользователь уже есть в сисмете")


        ButtonReg = ttk.Button(self,text='Регистрация',bootstyle="success outline", command=InsertIntoDb)
        ButtonReg.pack(pady=10)
        self.mainloop()


import tkinter as tk
import ttkbootstrap as ttk
import sqlite3
from tkinter import *
from reg import Registration
from Log import Logg

class login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = ttk.Style(theme='morph')
        self.title("Login")
        self.geometry("500x600")
        self.resizable(False,False)
        self.LabelEntry = ttk.Label(text='Войти в аккаунт', font=("Helvetica",34,'bold'),bootstyle="morph")
        self.LabelEntry.pack(pady=30)

        self.LoginHint = ttk.Label(text='Логин', font=("Helvetica",15,'bold'),bootstyle="morph")
        self.Login = ttk.Entry(bootstyle="morph",width=30,font=("Helvetica",20,'bold'))
        self.PasswordHint = ttk.Label(text='Пароль', font=("Helvetica",15,'bold'),bootstyle="morph")
        self.Password = ttk.Entry(bootstyle="morph",width=30,show="*",font=("Helvetica",20,'bold'))

        self.LoginHint.pack(pady=5)
        self.Login.pack(pady=30)
        self.PasswordHint.pack(pady=5)
        self.Password.pack(pady=30)
        self.button = ttk.Button(text='Войти',bootstyle="success outline", command=self.LogIn)
        self.button.pack(pady=10)
        def Reg():
            Regist = Registration(self)
            Regist.grab_set()
        self.ButtonReg = ttk.Button(text='Регистрация',bootstyle="success outline",command=Reg)
        self.ButtonReg.pack(pady=10)
        self.mainloop()
    def LogIn(self):
        conn = sqlite3.connect("Users.db")
        cur = conn.cursor()
        userLogin = self.Login.get()
        userPassword = self.Password.get()
        cur.execute(f"Select Login,Password from Users WHERE Login = '{userLogin}' AND Password = '{userPassword}' ")
        if not cur.fetchall():
            self.LabelEntry.config(text="Пользователя не существует")
        else:
            self.LabelEntry.config(text="Вы вошли")
            log = logo(self)
            log.grab_set()
            
        self.mainloop()
        
        

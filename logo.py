import requests
import sqlite3
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *


class logo(tk.Toplevel):
    
    def __init__(self,parent):
        super().__init__(parent)

        self.style = ttk.Style(theme='morph')
        self.title('title')
        self.geometry("1000x600")
        self.resizable(False,False)
    #подключение к базе с логами
        conn = sqlite3.connect('Logi.db')
        cur=conn.cursor()
        cur.execute("DELETE FROM files")
        conn.commit()
        
        response = requests.get(f'http://127.0.0.1:5000/logs')
        file = response.json()

        ip = []
        time = []
        method=[]
        status=[]
        host=[]

        for i in file:
            ip.append(i['ip_address'])
            time.append(i['request_time'])
            method.append(i['method'])
            status.append(i['status'])
            host.append(i['host'])


        for i in range(len(ip)):
            cur.execute('INSERT INTO files (ip, time, method, status, host) VALUES (?, ?, ?, ?, ?)', (ip[i], time[i], method[i], status[i], host[i]))

        conn.commit()

        
        notebook = ttk.Notebook(self, bootstyle='success')
        notebook.pack(expand=True, fill=BOTH)

        window = ttk.Frame(notebook)
        window1 = ttk.Frame(notebook)
        window2 = ttk.Frame(notebook)
        window3 = ttk.Frame(notebook)

        window.pack(fill=BOTH, expand=True)
        window1.pack(fill=BOTH, expand=True)
        window2.pack(fill=BOTH, expand=True)
        window3.pack(fill=BOTH, expand=True)


        columns = ('IP','Время','Метод','Статус','Host')

        treeview = ttk.Treeview(window, bootstyle="success",columns=columns,show='headings')
        treeview.pack(pady=10)

        for c in columns:
            treeview.heading(c, text=c)

        # заполняем treeview данными
        cur.execute("""SELECT ip, time, method, status, host FROM files""")
        values = cur.fetchall()

        for value in values:
            treeview.insert('', END, values=value)

        # обновляем таблицу в случае загрузки файла
        def update():
            cur.execute("DELETE FROM files")
            conn.commit()

            response = requests.get(f'http://127.0.0.1:5000/logs')
            file = response.json()

            ip = []
            time = []
            method=[]
            status=[]
            host=[]

            for i in file:
                ip.append(i['ip_address'])
                time.append(i['request_time'])
                method.append(i['method'])
                status.append(i['status'])
                host.append(i['host'])



            for i in range(len(ip)):
                cur.execute('INSERT INTO files (ip, time, method, status, host) VALUES (?, ?, ?, ?, ?)', (ip[i], time[i], method[i], status[i], host[i]))
            
            treeview.delete(*treeview.get_children()) 

            cur.execute("""SELECT ip, time, method, status, host FROM files""")
            values = cur.fetchall()

            for value in values:
                treeview.insert('',END,values=value)

            status_label.config(text="запрос выполнен")

            conn.commit()
    # Фильтр по всем пунктам
        def filter():

            day2 = day.get()
            months2 = months.get()
            years2 = years.get()

            end_days2 = end_days.get()
            end_months2 = end_months.get()
            end_years2 = end_years.get()

            ips2 = ips.get()

            if not all([day2, months2, years2, end_days2, end_months2, end_years2, ips2]):
                info3.config(text="Заполните все поля")
                return


            try:
                response = requests.get(f'http://127.0.0.1:5000/logs?start_date={day2}/{months2}/{years2}&end_date={end_days2}/{end_months2}/{end_years2}&ip={ips2}')
                file = response.json()
            except ValueError as error:
                info3.config(text="error")
                print(error)
                return
            
            cur.execute("DELETE FROM files")
            conn.commit()

            ip = []
            time = []
            method=[]
            status=[]
            host=[]

            for i in file:
                ip.append(i['ip_address'])
                time.append(i['request_time'])
                method.append(i['method'])
                status.append(i['status'])
                host.append(i['host'])

            for i in range(len(ip)):
                cur.execute('INSERT INTO files (ip, time, method, status, host) VALUES (?, ?, ?, ?, ?)', (ip[i], time[i], method[i], status[i], host[i]))

            treeview.delete(*treeview.get_children()) 

            cur.execute("""SELECT ip, time, method, status, host FROM files""")
            values = cur.fetchall()

            for value in values:
                treeview.insert('',END,values=value)

            info3.config(text="запрос выполнен")

            conn.commit()
        # Фильтруем по ip
        def filter_ip():

            ip = ip_entry.get()

            if not ip:
                ip_status_label.config(text="IP-адрес не указан")
                return
            try:
                response = requests.get(f'http://127.0.0.1:5000/logs?ip={ip}')
                response.raise_for_status() 
                file = response.json()
            except ValueError as error:
                print(error)
                return

            cur.execute("DELETE FROM files")
            conn.commit()

            ip = []
            time = []
            method=[]
            status=[]
            host=[]

            for i in file:
                ip.append(i['ip_address'])
                time.append(i['request_time'])
                method.append(i['method'])
                status.append(i['status'])
                host.append(i['host'])

            for i in range(len(ip)):
                cur.execute('INSERT INTO files (ip, time, method, status, host) VALUES (?, ?, ?, ?, ?)', (ip[i], time[i], method[i], status[i], host[i]))

            treeview.delete(*treeview.get_children()) 

            cur.execute("""SELECT ip, time, method, status, host FROM files""")
            values = cur.fetchall()

            for value in values:
                treeview.insert('',END,values=value)

            ip_status_label.config(text="запрос выполнен")

            conn.commit()

        # Фильтр по промежутку даты
        def filter_date():

            day1 = day.get()
            month1 = month.get()
            year1 = year.get()

            end_day1 = end_day.get()
            end_month1 = end_month.get()
            end_year1 = end_year.get()

            if not all([day1, month1, year1, end_day1, end_month1, end_year1]):
                info2.config(text="Заполните все поля")
                return


            try:
                response = requests.get(f'http://127.0.0.1:5000/logs?start_date={day1}/{month1}/{year1}&end_date={end_day1}/{end_month1}/{end_year1}')
                response.raise_for_status()
                file = response.json()
            except ValueError as error:
                info2.config(text="error")
                print(error)
                return

            cur.execute("DELETE FROM files")
            conn.commit()

            ip = []
            time = []
            method=[]
            status=[]
            host=[]

            for i in file:
                ip.append(i['ip_address'])
                time.append(i['request_time'])
                method.append(i['method'])
                status.append(i['status'])
                host.append(i['host'])

            for i in range(len(ip)):
                cur.execute('INSERT INTO files (ip, time, method, status, host) VALUES (?, ?, ?, ?, ?)', (ip[i], time[i], method[i], status[i], host[i]))

            treeview.delete(*treeview.get_children()) 

            cur.execute("""SELECT ip, time, method, status, host FROM files""")
            values = cur.fetchall()

            for value in values:
                treeview.insert('',END,values=value)

            info2.config(text="запрос выполнен")

            conn.commit()

        

       
        but = Button(window , text="Обновить", font=('arial', 15), width=30, command=update)
        but.pack(pady=10)

        status_label = tk.Label(window, text='')
        status_label.pack(pady=10)

        
        label_ip = Label(window1 , text="Напишите IP", font=('arial', 25), bd=18)
        label_ip.pack(pady=10)

        ip_entry = Entry(window1 , font=('arial', 20), width=15)
        ip_entry.pack(pady=10)

        btn1 = Button(window1 , text="Выполнить", font=('arial', 15), width=30, command=filter_ip)
        btn1.pack(pady=10)

        ip_status_label = tk.Label(window1, text='')
        ip_status_label.pack(pady=10)

       

        label_start = Label(window2 , text="От", font=('arial', 25), bd=18)
        label_start.pack(pady=10)
        label_start.place(x=80, y=60)

        label_day = Label(window2 , text="Напишите день", font=('arial', 25), bd=18)
        label_day.pack(pady=10)
        label_day.place(x=80, y=120)

        day = Entry(window2 , font=('arial', 20), width=15)
        day.pack(pady=10)
        day.place(x=100, y=180)

        label_month = Label(window2 , text="Выберите месяц", font=('arial', 25), bd=18)
        label_month.pack(pady=10)
        label_month.place(x=80, y=240)

        monthID = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = ttk.Combobox(window2, font=('arial', 15), values=monthID)
        month.pack(pady=10)
        month.place(x=100, y=300)

        label_year = Label(window2 , text="Напишите год", font=('arial', 25), bd=18)
        label_year.pack(pady=10)
        label_year.place(x=80, y=340)

        year = Entry(window2 , font=('arial', 20), width=15)
        year.pack(pady=10)
        year.place(x=100, y=420)

       
        label_end = Label(window2 , text="До", font=('arial', 25), bd=18)
        label_end.pack(pady=10)
        label_end.place(x=680, y=60)

        label_day_end = Label(window2 , text="Напишите день", font=('arial', 25), bd=18)
        label_day_end.pack(pady=10)
        label_day_end.place(x=680, y=120)

        end_day = Entry(window2 , font=('arial', 20), width=15)
        end_day.pack(pady=10)
        end_day.place(x=700, y=180)

        label_month_end = Label(window2 , text="Выберите месяц", font=('arial', 25), bd=18)
        label_month_end.pack(pady=10)
        label_month_end.place(x=680, y=240)

        monthID_end = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        end_month = ttk.Combobox(window2, font=('arial', 15), values=monthID_end)
        end_month.pack(pady=10)
        end_month.place(x=700, y=300)

        label_year_end = Label(window2 , text="Напишите год", font=('arial', 25), bd=18)
        label_year_end.pack(pady=10)
        label_year_end.place(x=680, y=340)

        end_year = Entry(window2 , font=('arial', 20), width=15)
        end_year.pack(pady=10)
        end_year.place(x=700, y=420)

        btn2 = Button(window2 , text="Выполнить", font=('arial', 18), width=30, command=filter_date)
        btn2.pack(pady=10)
        btn2.place(x=300, y=500)

        
        info2 = tk.Label(window2, text='')
        info2.pack(pady=10)
        info2.place(x=420, y=580)

        

        label_ip2 = Label(window3 , text="Напишите IP", font=('arial', 25), bd=18)
        label_ip2.pack(pady=10)
        label_ip2.place(x=400, y=240)

        ips = Entry(window3 , font=('arial', 20), width=15)
        ips.pack(pady=10)
        ips.place(x=400, y=300)

        

        label_start2 = Label(window3 , text="От", font=('arial', 25), bd=18)
        label_start2.pack(pady=10)
        label_start2.place(x=80, y=60)

        label_day2 = Label(window3 , text="Напишите день", font=('arial', 25), bd=18)
        label_day2.pack(pady=10)
        label_day2.place(x=80, y=120)

        days = Entry(window3 , font=('arial', 20), width=15)
        days.pack(pady=10)
        days.place(x=100, y=180)

        label_month2 = Label(window3 , text="Выберите месяц", font=('arial', 25), bd=18)
        label_month2.pack(pady=10)
        label_month2.place(x=80, y=240)

        monthID2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        months = ttk.Combobox(window3, font=('arial', 15), values=monthID2)
        months.pack(pady=10)
        months.place(x=100, y=300)

        label_year2 = Label(window3 , text="Напишите год", font=('arial', 25), bd=18)
        label_year2.pack(pady=10)
        label_year2.place(x=80, y=340)

        years = Entry(window3 , font=('arial', 20), width=15)
        years.pack(pady=10)
        years.place(x=100, y=420)

        

        label_end2 = Label(window3 , text="До", font=('arial', 25), bd=18)
        label_end2.pack(pady=10)
        label_end2.place(x=680, y=60)

        label_day_end2 = Label(window3 , text="Напишите день", font=('arial', 25), bd=18)
        label_day_end2.pack(pady=10)
        label_day_end2.place(x=680, y=120)

        end_days = Entry(window3 , font=('arial', 20), width=15)
        end_days.pack(pady=10)
        end_days.place(x=700, y=180)

        label_month_end2 = Label(window3 , text="Выберите месяц", font=('arial', 25), bd=18)
        label_month_end2.pack(pady=10)
        label_month_end2.place(x=680, y=240)

        monthID_end2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        end_months = ttk.Combobox(window3, font=('arial', 15), values=monthID_end2)
        end_months.pack(pady=10)
        end_months.place(x=700, y=300)

        label_year_end2 = Label(window3 , text="Напишите год", font=('arial', 25), bd=18)
        label_year_end2.pack(pady=10)
        label_year_end2.place(x=680, y=340)

        end_years= Entry(window3 , font=('arial', 20), width=15)
        end_years.pack(pady=10)
        end_years.place(x=700, y=420)

        btn3 = Button(window3 , text="Выполнить", font=('arial', 18), width=30, command=filter)
        btn3.pack(pady=10)
        btn3.place(x=300, y=500)

        info3 = tk.Label(window3, text='')
        info3.pack(pady=10)
        info3.place(x=420, y=580)

        
        notebook.add(window,text='База данных')
        notebook.add(window1,text='Фильтр по ip')
        notebook.add(window2,text='Фильтр по дате')
        notebook.add(window3,text='Фильтр по ip с датой')
import sqlite3
conn = sqlite3.connect('Logi.db')
cur=conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS files
         (ip TEXT NOT NULL,
         time TEXT NOT NULL,
         method TEXT NOT NULL,
         status TEXT NOT NULL,
         host TEXT NOT NULL);''')
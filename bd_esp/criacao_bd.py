import sqlite3


#criação do BD

conn = sqlite3.connect("banco.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS ESP (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , DIA_HORA TEXT NOT NULL,DADO_LIDO TEXT NOT NULL,DESCRICAO TEXT, STATE BOOL NOT NULL)")

conn.commit()

conn.close()

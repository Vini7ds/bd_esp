import pandas as pd
import sqlite3

conn = sqlite3.connect("banco.db")

cur = conn.cursor()

df = pd.read_sql_query("SELECT * FROM ESP",conn)

conn.close()

print(df)






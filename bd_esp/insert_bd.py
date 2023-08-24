import datetime
import sqlite3


def insert(banco_db, tabela, dado_lido, descrip):
    hora = datetime.datetime.now()
    conn = sqlite3.connect(banco_db)
    cur = conn.cursor()
    comando = "INSERT INTO " + tabela + " (DIA_HORA, DADO_LIDO, DESCRICAO, STATE) VALUES (?,?,?,1)"
    cur.execute(comando, (hora, dado_lido, descrip))
    conn.commit()
    conn.close()


def update_state(banco_db, tabela, item):
    conn = sqlite3.connect(banco_db)
    cur = conn.cursor()

    comando = ("UPDATE " + tabela + " SET STATE = not STATE where DADO_LIDO = ?")
    cur.execute(comando, (item,))

    conn.commit()
    conn.close()


def check_exi(banco_db, tabela, coluna, item):
    conn = sqlite3.connect(banco_db)
    cur = conn.cursor()

    comando = ("SELECT 1 FROM " + tabela + " WHERE " + coluna + " = ?")
    cur.execute(comando, (item,))

    result = bool(cur.fetchone())

    conn.close()

    return result

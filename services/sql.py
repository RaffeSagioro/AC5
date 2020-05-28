import sqlite3
from contextlib import closing

sql_create = ''' CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente VARCHAR(50) NOT NULL,
    login VARCHAR(20) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    cep VARCHAR(9) NOT NULL
);
'''

def conectar():
    return sqlite3.connect('rrg_games.db')

def criar_bd():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.executescript(sql_create)
        con.commit()

def criar_cliente(nome_cliente, login, senha, cpf, cep):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("INSERT INTO cliente (nome_cliente, login, senha, cpf, cep) VALUES (?, ?, ?, ?, ?)", (nome_cliente, login, senha, cpf))
        id_cliente = cur.lastrowid
        con.commit()
        return id_cliente        
   
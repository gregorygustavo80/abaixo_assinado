# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect("abaixo_assinado.db")
cursor = conn.cursor()

# Cria tabela de assinaturas
cursor.execute("""
CREATE TABLE IF NOT EXISTS assinaturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    bairro TEXT NOT NULL,
    pet TEXT
)
""")

# Cria tabela de comentários com autor
cursor.execute("""
CREATE TABLE IF NOT EXISTS comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    autor TEXT
)
""")

conn.commit()
conn.close()
print("✅ Banco de dados inicializado com sucesso.")
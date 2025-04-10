import sqlite3

conn = sqlite3.connect("abaixo_assinado.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM assinaturas")
cursor.execute("DELETE FROM comentarios")

conn.commit()
conn.close()

print("Banco de dados limpo com sucesso!")

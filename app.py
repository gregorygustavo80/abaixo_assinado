from flask import Flask, request, jsonify, render_template
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()

    # Busca as assinaturas
    cursor.execute("SELECT nome, bairro, pet FROM assinaturas")
    assinaturas = cursor.fetchall()

    # Busca os comentários com autor
    cursor.execute("SELECT texto, autor FROM comentarios")
    comentarios = cursor.fetchall()

    conn.close()
    return render_template("index.html", assinaturas=assinaturas, comentarios=comentarios)

@app.route("/assinar", methods=["POST"])
def assinar():
    data = request.json
    nome = data.get("nome")
    bairro = data.get("bairro")
    pet = data.get("pet")

    conn = sqlite3.connect("abaixo_assinado.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO assinaturas (nome, bairro, pet) VALUES (?, ?, ?)", (nome, bairro, pet))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Assinatura registrada com sucesso!"})

@app.route("/comentario", methods=["POST"])
def comentar():
    data = request.json
    texto = data.get("comentario")
    autor = data.get("autor")

    conn = sqlite3.connect("abaixo_assinado.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comentarios (texto, autor) VALUES (?, ?)", (texto, autor))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Comentário enviado com sucesso!"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa a porta fornecida pelo Render
    app.run(debug=True, host="0.0.0.0", port=port)

from flask import Flask, request, jsonify, render_template
import psycopg2
import os

def get_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

app = Flask(__name__)

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
    nome = data.get("nome", "").strip()
    bairro = data.get("bairro", "").strip()
    pet = data.get("pet", "").strip()

    # Validação dos campos
    if not nome or not bairro or not pet:
        return jsonify({"erro": "Todos os campos são obrigatórios!"}), 400
    
    if len(nome) < 3 or len(bairro) < 3 or len(pet) < 2:
        return jsonify({"erro": "Por favor, preencha os campos corretamente!"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO assinaturas (nome, bairro, pet) VALUES (%s, %s, %s)", (nome, bairro, pet))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Assinatura registrada com sucesso!"})

@app.route("/comentario", methods=["POST"])
def comentar():
    data = request.json
    texto = data.get("comentario", "").strip()
    autor = data.get("autor", "").strip()

    # Validação dos campos
    if not texto or not autor:
        return jsonify({"erro": "Todos os campos são obrigatórios!"}), 400
    
    if len(autor) < 3 or len(texto) < 10:
        return jsonify({"erro": "O nome deve ter pelo menos 3 caracteres e o comentário 10 caracteres!"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comentarios (texto, autor) VALUES (%s, %s)", (texto, autor))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Comentário enviado com sucesso!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

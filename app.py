from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Necessário para usar flash()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assinar', methods=['POST'])
def assinar():
    nome = request.form['nome']
    comentario = request.form['comentario']
    
    # Verificar se o comentário está vazio
    if not comentario.strip():
        flash("O campo de comentário não pode estar em branco.", "error")
        return redirect(url_for('index'))  # Redireciona de volta para a página inicial
    
    # Simulação de sucesso
    flash("Assinatura registrada com sucesso!", "success")
    return redirect(url_for('index'))  # Redireciona após salvar a assinatura

if __name__ == '__main__':
    app.run(debug=True)

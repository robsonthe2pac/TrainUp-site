from flask import Flask, request, jsonify
import random, string

app = Flask(__name__)

# Base de dados simulada
USUARIOS = {}  # email ou telefone como chave, valor: {nome, codigo}

# Função para gerar código de acesso
def gerar_codigo():
    return 'TU-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Sign Up
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    telefone = data.get('telefone')
    chave = email if email else telefone

    if chave in USUARIOS:
        return jsonify({"status":"erro","mensagem":"Usuário já registrado."})

    codigo = gerar_codigo()
    USUARIOS[chave] = {"nome": nome, "codigo": codigo}

    # Aqui você pode implementar envio do código via email ou WhatsApp
    print(f"Código de acesso para {nome}: {codigo}")

    return jsonify({"status":"sucesso","mensagem": f"Registrado com sucesso! Seu código: {codigo}"})

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    chave = data.get("email") or data.get("telefone")
    codigo = data.get("codigo")

    user = USUARIOS.get(chave)
    if user and user['codigo'] == codigo:
        return jsonify({"status":"sucesso","mensagem":"Login realizado com sucesso!"})
    return jsonify({"status":"erro","mensagem":"Email/Telefone ou código inválido."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
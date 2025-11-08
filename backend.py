from flask import Flask, request, render_template_string
from flask_mail import Mail, Message

app = Flask(__name__, static_folder=".")

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'infolearn8441@gmail.com'  # seu email
app.config['MAIL_PASSWORD'] = 'SUA_SENHA_AQUI'          # senha ou App Password
mail = Mail(app)

# Rotas principais
@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/index.html')
def index():
    return app.send_static_file('index.html')

@app.route('/cursos.html')
def cursos():
    return app.send_static_file('cursos.html')

@app.route('/servicos.html')
def servicos():
    return app.send_static_file('servicos.html')

@app.route('/contactos.html')
def contactos():
    return app.send_static_file('contactos.html')

@app.route('/sobre.html')
def sobre():
    return app.send_static_file('sobre.html')

@app.route('/style.css')
def css():
    return app.send_static_file('style.css')

@app.route('/<image_name>.jpg')
def images(image_name):
    return app.send_static_file(f'{image_name}.jpg')

# Formulário de inscrição
@app.route('/inscrever', methods=['GET', 'POST'])
def inscrever():
    curso_selecionado = request.args.get('curso', '')

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        curso = request.form.get('curso')

        # Enviar email para o InfoLearn
        msg = Message(
            subject=f"Nova inscrição: {curso}",
            sender=app.config['MAIL_USERNAME'],
            recipients=['infolearn8441@gmail.com'],
            body=f"Nome: {nome}\nEmail: {email}\nCurso: {curso}"
        )
        mail.send(msg)
        return render_template_string("""
            <h2>Inscrição recebida com sucesso!</h2>
            <p>Você também pode entrar em contato via <a href="https://wa.me/258878080213">WhatsApp</a>.</p>
            <a href="/index.html">Voltar para Início</a>
        """)

    # Formulário HTML com curso pré-selecionado
    return render_template_string(f"""
        <h2>Inscrição em Curso</h2>
        <form method="POST">
            <label>Nome:</label><br>
            <input type="text" name="nome" required><br><br>
            <label>Email:</label><br>
            <input type="email" name="email" required><br><br>
            <label>Curso:</label><br>
            <input type="text" name="curso" value="{curso_selecionado}" readonly style="background:#f0f0f0;"><br><br>
            <button type="submit">Inscrever-se</button>
        </form>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
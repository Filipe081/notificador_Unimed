from flask import Flask, render_template, request, redirect, url_for, flash
from services.notificacao import ServicoDeNotificacao
import os

app = Flask(__name__)
app.secret_key = 'supersecreto'
servico = ServicoDeNotificacao()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['GET', 'POST'])
def enviar_notificacao():
    if request.method == 'POST':
        usuario = request.form['usuario']
        canal = request.form['canal']
        mensagem = request.form['mensagem']
        try:
            servico.enviar(usuario, canal, mensagem)
            flash('Notificação enviada com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Erro: {str(e)}', 'danger')
    return render_template('enviar.html')

@app.route('/logs')
def ver_logs():
    return render_template('log.html', logs=servico.logs)

if __name__ == '__main__':
    app.run(debug=True)

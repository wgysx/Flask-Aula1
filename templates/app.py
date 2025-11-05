from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá, Mundo!"

@app.route('/info')
def info():
    modulo = "Flask"
    aula = 1
    return f"<h1>Módulo: {modulo} — Aula {aula}</h1>"

@app.route('/bemvindo/<usuario>')
def bemvindo(usuario):

    return f"<h1>Bem-vindo, {usuario.capitalize()}!</h1>"

@app.route('/home')
def home():
    return redirect("/")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

if __name__ == '__main__':

    app.run(debug=True)

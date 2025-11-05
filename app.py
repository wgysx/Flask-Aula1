from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo!'
@app.route('/sobre')
def sobre():
    return "<h1>pagina info<h1>"
@app.route('/info')
def info():
    modulo = "css"
    aula = '7'
    return f"<h1>Modulo: {modulo}</h1><h1>Aula: {aula}</h1>"

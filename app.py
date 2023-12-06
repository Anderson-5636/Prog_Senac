import pessoa   
from flask import Flask

app = Flask(__name__)


# url statica

@app.route("/")
def Index():
    return "TIRAAAAAAA"

@app.route("/portadosfundos")
def portadosfundos():
    return "asdasdasd BOY, SITE ERRADO"

# url dinamica

@app.route("/Incluir/<nome>/<idade>/<email>")
def Incluir(nome, idade, email):
    pessoa_teste = pessoa.Pessoa(nome)
    pessoa_teste.idade = int(idade)
    pessoa_teste.email = email
    pessoa_teste.Incluir()
    return f'a pessoa cujo email {email} foi incluida'

@app.route("/Excluir/<email>")
def Excluir(email):
    pessoa_teste = pessoa.email = email
    pessoa_teste.Excluir()
    return 'a pessoa foi excluida {}'

@app.route("/Listar")
def Listar():
    pessoa_teste = pessoa.Pessoa('')
    return pessoa_teste.Listar()


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=80, debug=True)
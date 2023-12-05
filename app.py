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

@app.route("/incluir/<nome>/<idade>/<email>")
def incluir(nome, idade, email):
    pessoa_teste = pessoa.Pessoa(nome)
    pessoa_teste.idade = int(idade)
    pessoa_teste.email = email
    pessoa_teste.incluir()
    return 'a pessoa foi incluida'

@app.route("/Excluir/<email>")
def Excluir(email):
    pessoa_teste = pessoa.email = email
    pessoa_teste.excluir()
    return 'a pessoa foi excluida {}'.format(Excluir)

@app.route("/Listar")
def Listar():
    pessoa_teste = pessoa.Pessoa('')
    return pessoa_teste.Listar()


if __name__ == '__main__': 
    app.run()
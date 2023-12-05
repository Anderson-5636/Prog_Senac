import principal
from flask import Flask

app = Flask(_name_)

'''
# url statica

@app.route("/")
def Index():
    return "TIRAAAAAAA"

@app.route("/portadosfundos")
def portadosfundos():
    return "ERROU BOY, SITE ERRADO"
'''
# url dinamica

@app.route("/adicionar/<nome>/<idade>/<email>")
def adicionar(nome, idade, emai):
    pessoa_teste = pessoa.Pessoa (nome)
    pessoa_teste.idade = int(idade)
    pessoa_teste.email = email
    pessoa_teste.incluir;
    return f'a pessoa {nome} foi adicionada com o {email}'.format(adicionar)

@app.route("/excluir/<email>")
def excluir(email):
    pessoa_teste.email = email
    pessoa_teste.excluir;
    return 'a pessoa foi excluida {}'.format(excluir)

@app.route("/listar/<todos>")
def listar(todos):
    return 'a pessoa foi adicionada {}'.format(listar)


if _name_ == '_main_': 
    app.run()
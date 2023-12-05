import sqlite3

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
        self.email = ''
 
    def Incluir(self):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"insert into pessoa values('{self.nome}', '{self.idade}', '{self.email}')")
        banco.commit()
    
    def Excluir(self):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"delete from pessoa where nome = '{self.nome}'")
        banco.commit()

    def Alterar(self, nome):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"update pessoa set nome = '{novo_nome}', idate = {self.idade}, email = '{self.email}' where nome = '{self.nome}' ")
        banco.commit()

    def Listar(self):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"Select * from nome")
        print(cursor.fetchall())

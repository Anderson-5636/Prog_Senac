import sqlite3

class Pessoa:
    Connection = sqlite3.connect('primeiro_banco.db')
    Cursor = Connection.cursor()
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
        self.email = ''
        
    def Incluir(self):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"insert into pessoa values('{self.nome}', '{self.idade}', '{self.email}')")
        banco.commit()

    def Alterar(self, novo_nome):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"update pessoa set nome = '{novo_nome}' where nome = '{novo_nome}' ")
        banco.commit()
    
    '''
    # Alterar feito pelo professor
    def Alterar(self, novo_nome):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"update pessoa set nome = '{novo_nome}', idate = '{self.idade}', email = '{self.email}' where nome = '{novo_nome}' ")
        banco.commit()
    '''
    
    def Excluir(self, nome):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"delete from pessoa where nome = '{nome}'")
        banco.commit()
    
    def Listar(self):
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute(f"select * from pessoa")
        return cursor.fetchall()
  
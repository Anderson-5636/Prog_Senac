import pessoa

while True:
    print('1) incluir pessoa')
    print('2) alterar pessoa')
    print('3) excluir pessoa')
    print('4) Listar pessoas')
    print('5) Criar a tabela pessoa')
    print('0) sair do sistema')
    print()
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        pessoa_teste = pessoa.Pessoa(input('Nome: '))
        pessoa_teste.idade = int(input('Idade: '))
        pessoa_teste.email = input('Email: ')
        pessoa_teste.Incluir;
    elif opcao == 2:
        pessoa_teste = pessoa.Pessoa(input('Nome: '))
        pessoa_teste.alterar
        
    elif opcao == 3:
        pessoa_teste = pessoa.Pessoa(input('Nome: '))
        pessoa_teste.Excluir
        
    elif opcao == 4:
        pessoa_teste = pessoa.Pessoa('')
        pessoa_teste.Listar
        
    elif opcao == 5:
        pessoa_teste = pessoa.Pessoa(input('Nome: '))
        pessoa_teste.Criar_tabela
        
    elif opcao == 0:
        break
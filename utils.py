from model import Pessoas, Usuarios

## Insere dados na tabela Pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Tudão', idade=80)
    print(pessoa)
    pessoa.save()

## Consulta dados na tabela Pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Tidão').first()
    #print(pessoa.nome, pessoa.idade)
    print(pessoas)

## Altera dados na tabela Pessoas
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Tudão').first()
    pessoa.idade = 18
    pessoa.nome = 'Tidão'
    pessoa.save()
    print(pessoa.nome, pessoa.idade)

## Exclui dados na tabela Pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    #exclui_pessoa()
    #consulta_pessoas()
    insere_usuario('Mira', '999')
    insere_usuario('Jade', '888')
    consulta_todos_usuarios()

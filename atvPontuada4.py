import os
os.system ("clear || cls")
from dataclasses import dataclass
from time import sleep
Lista_funcionario = []

@dataclass   # Adicionando classes.
class Funcionario:
    nome: str
    data_admissao: str
    cpf: str
    area: str

nome_arquivo = 'funcionarios.csv' # Nomeando o arquivo .csv

def Cadastrar_Funcionario(lista):  # Função para adicionar funcionário a lista e ao arquivo.
    funcionario = Funcionario(
        nome = input('Diigte o nome do seu funcionario: '),
        data_admissao = input('Digite a data que entrou na empressa: '),
        cpf = input('Digite o seu CPF: '),
        area = input('Em qual area dentro da empresa você esta atuando: ')
    )
    Lista_funcionario.append(funcionario)
    os.system('cls || clear')
    with open (nome_arquivo, 'a') as arquivo_funcionario:
        arquivo_funcionario.write(f'Nome: {funcionario.nome}\n Data de admissão: {funcionario.data_admissao}\n CPF: {funcionario.cpf}\n Areá de atuação: {funcionario.area}\n')

def Mostrar_dados(lista): # Função para printar dados do Funcionário
    if not lista:
        print('A lista esta vazia')
        return
    os.system('clear || cls')
    print('Funcionarios Cadastrados DENDÊ TECH')
    try:
        for print_funcionario in Lista_funcionario:
            print(f'{print_funcionario.nome}\n{print_funcionario.data_admissao}\n{print_funcionario.cpf}\n{print_funcionario.area}') # metodo para mostrar na tela de forma mas organizada.
            print('-' * 30)
    except ValueError:
        print('Lista vazia')

def Atualizar_dados(lista): # Função para atualizar dados do funcionario.
    if not lista:
        print('Lista vazia')
        return
    Mostrar_dados(lista)
    funcionario_antigo = input('Digite o nome do funcionario que deseja atualizar as informações: ')
    os.system("clear || cls")
    try:
        indice = [funcionario.nome for funcionario in lista].index(funcionario_antigo) # Comando para identificar a posição do funcionário
        funcionario = lista[indice]
        funcionario.nome = input('Digite o novo nome do funcionario: ') # Trocar ou não nome
        funcionario.data_admissao = input('Digite o nome da data de admissão do funcionario: ') # Trocar ou não data de adimissão
        funcionario.cpf = input('Digite o CPF: ')  # Trocar ou não cpf
        funcionario.area = input('Digite a area do funcionario: ') # Trocar ou não a Area
        print(f'As informaçoes do {funcionario.nome} foram salvas')
    except ValueError:
        print(f'O fucionario {funcionario_antigo} não foi encontrado')

def Excluir_funcionario(lista): # função para excluir dados do funcionario.
    if not lista:
        print('Lista vazia')
        return
    Mostrar_dados(lista)
    funcionario_excluir = input('Digite o nome do funcionario que deseja excluir: ') 
    os.system("clear || cls")
    for funcionario in Lista_funcionario:
        if funcionario.nome == funcionario_excluir:
            lista.remove(funcionario) # Removendo Funcionario.
            print(f'Funcionario {funcionario.nome} Excluido com sucesso! ')
            return
    print(f'Funcionario com o nome {funcionario_excluir} Não encontrado!')

def Menu(): # Mostrar Menu com as opções para o usuario.
    while True: # while true para continuar pedindo e não encerrar com apenas 1 funcionario.
        print('''
1 | Adicionar
2 | Mostrar dados
3 | Atualizar Dados
4 | Excluir
5 | Encerrar
    ''')
        opcao = str(input('Digite o codigo para executar uma ação: '))
        os.system('cls || clear')

        match opcao: # chamar as funçoes organizadamente para cada caso.
            case "1":
                Cadastrar_Funcionario(Lista_funcionario)
            case "2":
                Mostrar_dados(Lista_funcionario)
            case "3":
                Atualizar_dados(Lista_funcionario)
            case "4":
                Excluir_funcionario(Lista_funcionario)
            case "5":
                print("Encerrando...")
                sleep(2)
                break
            case _:
                print('Opção invalida')
Menu() # chamando a função "Menu".
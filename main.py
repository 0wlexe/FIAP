from datetime import date
import os


# Cadastrar usuários
def preencherDados(lista):

    valida_nomered = []

    newCad = 'S'
    while newCad == 'S':
        nomered = input("\nDigite seu nome reduzido: ")
        nomered.lower()

        if nomered in valida_nomered:
            print("\nEsse nome reduzido já está sendo utilizado! Tente novamente.")

        elif nomered not in valida_nomered:

            valida_nomered.append(nomered)

            dados = [
                nomered,
                input("\nDigite seu nome completo: "),
                input("\nDigite seu cargo: "),
                input('''\n Escolha seu nível de acesso:
                [1] Visitante 
                [2] Usuário
                [3] Administrativo 
                [4] Técnico
                [5] Super-Usuário
                    
                '''),
                input("Digite a data: ")
                ]

            lista.append(dados)

        resp = input("\nDeseja continuar? \"S\" ou \"N\" ").upper()
            
        if resp == "S":
            print("\nUsuário Cadastrado com sucesso!")
            break
        else:
            print("Processo encerrado.")
            break
    

# Procurar por nome reduzido
def procuranomeRed(lista):
    busca = input("\nDigite o nome reduzido que deseja buscar: ")
    busca.lower()

    for elemento in lista:
        if busca == elemento[0]:
            print("\nResultados para {}:\n".format(elemento[0]))
            print("\nNome completo: {}".format(elemento[1])),
            print("\nCargo: {}".format(elemento[2])),
        
        else:
            print("\nNome não cadastrado.")
                

# Retornar usuários de acordo com o nível de acesso
def exibirDados(lista):
    nivel = input("\nInforme o nível de acesso: ")
    
    for elemento in lista:
        if nivel == elemento[3]:
            print("Nome completo: {}".format(elemento[1]))
            print("Cargo: {}".format(elemento[2]))

        else:
            print("\nNível invalido!")
            exibirDados(lista)


# Buscar usuário por data

def filtrarData(lista):
    data = []

    for elemento in lista:
        if elemento[4] not in data:
            data.append(elemento[4])
            print("Datas disponíveis: {}".format(str(data)))
    
    buscaData = input("\nDigite a data que deseja buscar: ")
            
    for elemento in lista:
        if elemento[4] == buscaData:
            print("O usuário {} acessou o sistema nesta data.".format(elemento[0]))
        
        else:
            print("Nenhum acesso encontrado nesta data.")

# Super Usuários
def superUser(lista):
    count = 0

    for elemento in lista:
        if elemento[3] == elemento[3]:
            print("\nO nível de acesso do usuário {} é {}".format(elemento[0], elemento[3]))
            count = count + 1
    
    print("\nNúmero total de super-usuários: " + str(count))

# Excluir por nome reduzido 
def excluirnomeRed(lista):

    excluir = input("\nDigite o nome reduzido que deseja excluir: ")
    excluir.lower()

    for elemento in lista:
        if excluir == elemento[0]:
            lista.remove(elemento[0])
            print("\nUsuário excluído.")

        else:
            print("\nUsuário não encontrado.")



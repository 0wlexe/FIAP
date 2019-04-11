from main import *
import os

os.system('cls' if os== 'nt' else 'clear') 

elementos = []
escolha = 0

try:
    while escolha <= 6: 

        print("\n(1) Cadastrar novo usuário")
        print("(2) Procurar por nome reduzido")
        print("(3) Procurar por nível de acesso")
        print("(4) Procurar acessos por data")
        print("(5) Listar quantidade de usuários")
        print("(6) Excluir usuário")

        escolha = int(input("\nEscolha que deseja fazer: "))
            
        if escolha == 1:
            preencherDados(elementos)

        elif escolha == 2:
            procuranomeRed(elementos)

        elif escolha == 3:
            exibirDados(elementos)

        elif escolha == 4:
            filtrarData(elementos)

        elif escolha == 5:
            superUser(elementos)

        elif escolha == 6:
            excluirnomeRed(elementos)

except KeyboardInterrupt:
    print("\nProcesso encerrado...{finale}")
exit()
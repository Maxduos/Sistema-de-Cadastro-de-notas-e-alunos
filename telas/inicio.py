from telas.cadastro import abrir_cadastro
from telas.lista import abrir_lista

def abrir_inicio():

    while True:

        print("\n---  S I S T E M A   P A R A   C A D A S T R O   D E   N O T A S  ---\n")

        print("[1] Cadastro de Notas e Aluno")
        print("[2] Lista de notas e alunos")
        print("[3] Sair do Sistema\n")

        opcao = int(input("Digite a opção desejada:"))

        if opcao == 1:
            abrir_cadastro()
        elif opcao == 2:
            abrir_lista()
        elif opcao == 3:
            print("Saindo do sistema...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

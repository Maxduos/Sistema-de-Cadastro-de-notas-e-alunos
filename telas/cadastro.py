from telas.dados import alunos

def abrir_cadastro():

    print("---  C A D A S T R O   D E   N O T A S   E   A L U N O   ---\n")

    nome = input("Digite o nome do aluno:")

    notas_aluno = []
    
    while True:

        materia = input("Digite a matéria: ")
        nota = float(input("Digite a nota: "))

        notas_aluno.append({
            "materia": materia,
            "nota": nota
        })

        continuar = input("Deseja cadastrar outra matéria? (s/n): ")

        if continuar.strip().lower() == "n":
            break

        print("\nContinuando...")
        

        aluno = {
            "nome": nome,
            "notas": notas_aluno
        }

        alunos.append(aluno)

        print("Cadastro e notas realizados com sucesso!\n")

   

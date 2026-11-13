from telas.dados import alunos

def abrir_cadastro():

    print("---  C A D A S T R O   D E   N O T A S   E   A L U N O   ---\n")

    nome = input("Digite o nome do aluno:")

    notas_aluno = []
    
    for i in range(7):
        materia = input(f"Digite a matéria {i+1}:")
        nota = float(input(f"Digite a nota da matéria {i+1}:"))

        notas_aluno.append({
            "materia": materia,
            "nota": nota
        })


        voltar = input("\nDeseja voltar ao menu inicial? (s/n): ")

        if voltar.strip().lower() == "s":
            break 
    

    aluno = {
        "nome": nome,
        "notas": notas_aluno
    }

    alunos.append(aluno)

    print("Cadastro e notas realizados com sucesso!\n")

   

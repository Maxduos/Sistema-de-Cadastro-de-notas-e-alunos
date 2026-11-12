from telas.dados import alunos
def abrir_cadastro():

    print("---  C A D A S T R O   D E   N O T A S   E   A L U N O   ---\n")

    nome = input("Digite o nome do aluno:")
    materia = input("Digite a matéria:")
    nota = float(input("Digite a nota do aluno:"))
    

    aluno = {
        "nome": nome,
        "nota": nota,
        
}

    alunos.append(aluno)

    print("Cadastro e notas realizados com sucesso!\n")


    from telas.inicio import abrir_inicio
    abrir_inicio()

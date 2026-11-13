from telas .dados import alunos
def abrir_lista():
    
    print("---   L I S T A   D E   N O T A S   E   A L U N O S   ---\n")

    for aluno in alunos:
        print(f"Nome: {aluno["nome"]}")
        print(f"Matéria: {aluno["materia"]}")
        print(f"Nota: {aluno["nota"]}\n")
         

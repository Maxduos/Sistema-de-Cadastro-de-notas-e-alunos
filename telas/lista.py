from telas.dados import alunos

def abrir_lista():

    print("--- LISTA DE NOTAS E ALUNOS ---\n")

    for aluno in alunos:

        print(f"Nome: {aluno['nome']}")

        for nota in aluno["notas"]:

            print(f"Matéria: {nota['materia']}")
            print(f"Nota: {nota['nota']}")

        print()
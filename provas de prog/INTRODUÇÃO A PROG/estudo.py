# Créditos: aprender-python.blogspot.com.br

bool = True

alunos = []

while bool:
    print('''
    1 - Cadastrar Aluno
    2 - Remover Aluno
    3 - Listar Alunos
    4 - Encerrar Programa

    Digite o número da operação desejada:
    ''')
   

    n = int(input("> "))

    if n == 1:
        nome = input("\nDigite o nome do aluno que deseja adicionar: ")
        alunos.append(nome)

    elif n == 2:
        nome = input("\nDigite o nome do aluno que deseja deletar: ")

        if nome in alunos:
            alunos.remove(nome)
            print(nome, "deletado da lista.")
        else:
            print("\nAluno não está cadastrado na lista.")

    elif n == 3:
        print("\nAlunos cadastrados:\n")
        alunos.sort()
        for x, y in enumerate(alunos):  # Enumerate é uma função que serve para enumerar os itens da lista.
            print("\t", x, "-", y)

    elif n == 4:
        bool = False
    else:
        print("\nOpção inválida.")
    print('=-='*10)

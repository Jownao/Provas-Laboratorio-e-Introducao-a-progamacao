peso1 = 3
peso2 = 3
peso3 = 4
faltas= 20
aluno=0
aprovados=0
provaFinal=0
reprovadoMedia=0
reprovadoFalta=0
alunos = int(input("Digite quantidade de alunos:"))
while aluno<alunos:
    al1 = (input("Nome do aluno:"))
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    n3 = float(input("Nota 3:"))
    falta1 = input("Numero de faltas:")

    media1 = (n1*peso1+n2*peso2+n3*peso3)/(peso1+peso2+peso3)

    if media1 >=6:
        print("Aprovado")
        aprovados=aprovados+1
    elif media1 >=4:
        print("Prova final")
        provaFinal=provaFinal+1
    else:
        print("Reprovado")
        reprovadoMedia=reprovadoMedia+1
    aluno=aluno+1

porAprovados=(aprovados*100)/alunos
porReprovados=(reprovadoMedia*100)/alunos


print("Alunos de aprovados:",aprovados,"Alunos de prova final:",provaFinal)
print(reprovadoMedia,"Reprovados por média")
print(porAprovados,"Por cento de aprovados",porReprovados,"Por cento de reprovados")
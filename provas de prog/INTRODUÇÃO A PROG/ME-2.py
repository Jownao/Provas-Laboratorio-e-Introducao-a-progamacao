participantes=[]
cod=[]
questao=[]
parBin=0
codBin=0
queBin=0
#numero_participantes=sum(participantes)

print(f'Digite o nome e o código do participante')
for i in range(1, 4):
    participantes.append(str(input('Nome: ')))
    cod.append(int(input('Código: ')))
    for j in range(1, 4):
        questao.append(float(input(f'Para questão {j} digite um número escolhido. ')))


print('{}Número de participantes é {}'.format(participantes,bin(parBin)))
print(codBin)
print(queBin)


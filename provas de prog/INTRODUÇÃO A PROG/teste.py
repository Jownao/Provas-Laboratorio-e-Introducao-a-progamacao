numero=0
divisores=[]
#NÚMERO
print('Digite um número inteiro positivo')
ativador=1
while ativador==1:
    try:
        numero=int(input('Número: '))
        ativador=0
        if numero<0:
            print('O número digitado é inválido')
            ativador=1
    except:
        print('O número digitado é inválido')
        ativador=1

#DIVISORES
for i in range(numero):
    if numero%(i+1)==0:
        divisores.append(i+1)

#PRINT DO RESULTADO
if sum(divisores)==numero:
    print('Número lido: {}  Resultado: {}(divisores) {}(soma dos divisores (é perfeito)'.format(numero,divisores, sum(divisores)))
else:
    print('o numero não é perfeito')
array = []
print('digite 20 numeros: ')

for i in range(0,4):
    numero = int(input("Numero: "))
    array.append(numero)
    if i == 0:
        menor = numero
    elif numero < menor:
        menor = numero

lugar = array.index(menor)

print("O menor elemento de N e", menor, "e sua posicao dentro do vetor e:", lugar)

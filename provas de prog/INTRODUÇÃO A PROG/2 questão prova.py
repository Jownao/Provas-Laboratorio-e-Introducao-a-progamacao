
salarioMenor=0
familias=0
hab=0
casa=0
casas=int(input("Digite quantas casas você visitou:"))
while casa<casas:
    sal1=float(input("Soma dos salarios da família:"))
    hab1=float(input("Quantas pessoas vivem na casa:"))
    sal1=sal1+sal1
    hab1=hab1+hab1
    casa=casa+1
    if sal1<998:
        salarioMenor=salarioMenor+1

mediaHab=hab1/casas
mediaSal=sal1/casas
porSalMenor=(salarioMenor*100)/casas

print(mediaHab,"Media de habitantes por residencia")
print(mediaSal,"Media de salario por casa")
print(porSalMenor,"Por cento das casas tem o salário menor que R$998,00")

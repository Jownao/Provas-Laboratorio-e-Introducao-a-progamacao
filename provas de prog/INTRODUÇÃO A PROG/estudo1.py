numVoo=[]
origem=[]
destino=[]
assentos=[]
qtdPassageiros=[]
nomePassageiro=[]
qtdVoos=0

#IMFORMAÇÕES DO VOO
#QUANTIDADE DE VOOS
print('Digite a quantidade de voos que estaram disponiveis')
ativador=1
while ativador==1:
    try:
        qtdVoos=int(input('Quantidade: '))
        ativador=0
    except:
        print('Erro')
        ativador=1

#NUMERO DO VOO
print('Digite o numero do voo')
for i in range(qtdVoos):
    print('Voo {}'.format(i+1))
    ativador=1
    while ativador==1:
        try:
            numVoo.append(int(input('Numero: ')))
            ativador=0
        except:
            print('Erro')
            ativador=1

#ORIGEM
print('Digite a origem do voo')
for i in range(qtdVoos):
    print('Voo {}'.format(i+1))
    print('Numero {}'.format(numVoo[i]))
    ativador=1
    while ativador==1:
        try:
            origem.append(str(input('Origem: ')))
            ativador=0
        except:
            print('Erro')
            ativador=1

#DESTINO
print('Digite o destino do voo')
for i in range(qtdVoos):
    print('Voo {}'.format(i+1))
    print('Numero {}'.format(numVoo[i]))
    print('Origem {}'.format(origem[i]))
    ativador=1
    while ativador==1:
        try:
            destino.append(str(input('Destino: ')))
            ativador=0
        except:
            print('Erro')
            ativador=1

#QUANTIDADE DE ASSENTOS DISPONIVEIS
print('Digite a quantidade de assentos disponiveis por voo')
for i in range(qtdVoos):
    print('Voo {}'.format(i+1))
    print('Numero {}'.format(numVoo[i]))
    print('Origem {}'.format(origem[i]))
    print('Destino {}'.format(destino[i]))
    ativador=1
    while ativador==1:
        try:
            assentos.append(int(input('Assentos: ')))
            ativador=0
        except:
            print('Erro')
            ativador=1
#LISTAS EXTRAS
for i in range(qtdVoos):
    qtdPassageiros.append(0)
    nomePassageiro.append(0)

#MENU
menu=0
while menu==0:
    print('''
    1. Consultar Voo
    2. Efetura Reserva
    3. Listar Voos
    4. Sair
    ''')
    print('Digite o numero da opção desejada')
    ativador=1
    while ativador==1:
        try:
            resposta=int(input('Opção escolhida: '))
            ativador=0
        except:
            print('Erro')
            ativador=1

    #RESPOSTA 1 CONSULTA DE VOO
    if resposta==1:
        ativador=1
        print('Digite o numero do voo que deseja consultar')
        while ativador==1:
            try:
                consulta=int(input('Numero do voo: '))
                ativador=0
            except:
                print('Erro')
                ativador=1
        if consulta in numVoo:
            index=numVoo.index(consulta)
            print('Numero do voo: {}'.format(numVoo[index]))
            print('Origem do voo: {}'.format(origem[index]))
            print('Destino do voo: {}'.format(destino[index]))
            print('Qauntidade de assentos disponiveis: {}'.format(assentos[index]))
            print('Passageiros: {}'.format(qtdPassageiros[index]))
        else:
            print('Voo Inexistente')

    #RESPOSTA 2 EFETUAR RESERVAS
    elif resposta==2:
        ativador=1
        print('Digite o numero do voo que deseja fazer a reserva')
        while ativador==1:
            try:
                reserva=int(input('Numero do voo: '))
                ativador=0
            except:
                print('Erro')
                ativador=1
        ativador=1
        print('Digite o seu nome para fazer a reserva')
        while ativador==1:
            try:
                nome=str(input('Nome: '))
                ativador=0
            except:
                print('Erro')
                ativador=1
        if reserva in numVoo:
            index=numVoo.index(reserva)
            if qtdPassageiros[index] == assentos[index]:
                print('Voo Lotado')
            else:
                nomePassageiro.append(nome)
                #add passageiro
                valor=qtdPassageiros[index]
                valor=valor+1
                qtdPassageiros[index]=valor
                #retirar assento usado
                valor2=assentos[index]
                valor2=valor2-1
                assentos[index]=valor2
                print('Reserva efetuada com sucesso')
        else:
            print('Voo Inexistente')

    #RESPOSTA 3 LISTAR VOOS
    elif resposta==3:
        print('Lista de voos e suas informações:')
        for i in range(qtdVoos):
            print('Numero do voo: {}'.format(numVoo[i]))
            print('Origem: {}'.format(origem[i]))
            print('Destino: {}'.format(destino[i]))
            print('Assentos Disponiveis: {}'.format(assentos[i]))
            print('Quantidade de passageiros: {}'.format(qtdPassageiros[i]))

    #RESPOSTA 4 SAIR
    elif resposta==4:
        menu=1
    else:
        print('opção invalida')

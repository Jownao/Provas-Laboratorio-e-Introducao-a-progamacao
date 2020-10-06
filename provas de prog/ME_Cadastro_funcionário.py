import os

lista_cadastro = []
lista_setor = []
lista_salario = []
grupo_setor = []
total_setor = []

if os.path.exists('funcionarios.txt'):
    arquivo = open('funcionarios.txt', 'a')
else:
    arquivo = open('funcionarios.txt', 'w')
    arquivo.write('Matrícula - Nome - E-mail - Telefone - Celular - Endereço - Número - Complemento - Bairro - Cidade - UF - Cargo - Setor - Salário - INSS - IRPF - Salário Liquido')
    arquivo.write('\n')
arquivo.close()


def cadastro_matricula():
    matricula = input('Digite a mátricula, SOMENTE NÚMEROS:\n').strip()
    return matricula


def cadastro_nome():
    entrada = input('Digite o nome:\n').strip()
    nome = []
    for i in entrada.split():
        nome.append(i.capitalize())
    return ' '.join(nome)


def cadastro_email():
    while True:
        email = input('Digite o e-mail:\n').strip()
        if "@" in email:
            break
        else:
            print('E-mail inválido, por favor, tente novamente!')
    return email


def cadastro_telefone():
    while True:
        telefone = input('Digite o telefone, SOMENTE NÚMEROs:\n').strip()
        if len(telefone) >= 8:
            break
        else:
            print('O telefone deve ter no mínimo 8 digitos, por favor, tente novamente!')
    return telefone


def cadastro_celular():
    while True:
        celular = input('Digite o celular, SOMENTE NÚMEROS:\n').strip()
        if len(celular) >= 8:
            break
        else:
            print('O celular deve ter no mínimo 8 digitos, por favos, tente novamente!')
    return celular


def cadastro_endereco():
    entrada = input('Digite o nome da rua:\n').strip()
    endereco = []
    for i in entrada.split():
        endereco.append(i.capitalize())
    return ' '.join(endereco)


def cadastro_numero():
    return input('Digite o número:\n').strip()


def cadastro_bairro():
    entrada = input('Digite o nome do bairro:\n').strip()
    bairro = []
    for i in entrada.split():
        bairro.append(i.capitalize())
    return ' '.join(bairro)


def cadastro_cidade():
    entrada = input('Digite o nome da cidade:\n').strip()
    cidade = []
    for i in entrada.split():
        cidade.append(i.capitalize())
    return ' '.join(cidade)


def cadastro_uf():
    return input('Digite o UF:\n').strip().upper()


def cadastro_complemento():
    return input('Digite o complemento:\n').strip()


def cadastro_cargo():
    return input('Digite o cargo:\n').strip().upper()


def cadastro_setor():
    return input('Digite o setor:\n').strip().upper()


def cadastro_salario():
    return input('Digite o salário, CENTAVOS SEPARADOS POR PONTO:\n').strip()


def calcular_inss(salario):
    inss = 0
    if salario <= 1045:
        inss = salario * 0.075
    elif salario > 1045 and salario <= 2089.60:
        inss = salario * 0.09
    elif salario > 2089.60 and salario <= 3314.40:
        inss = salario * 0.12
    elif salario > 3314.40 and salario <= 6101.06:
        inss = salario * 0.14
    else:
        inss = 713.10
    return inss


def calcular_irpf(salario):
    if salario <= 1903.98:
        irpf = 0
    elif salario >= 1903.99 and salario <= 2826.65:
        irpf = (salario * 0.075) + 142.80
    elif salario >= 2826.66 and salario <= 3751.05:
        irpf = (salario * 0.15) + 354.80
    elif salario >= 3751.06 and salario <= 4664.68:
        irpf = (salario * 0.225) + 636.13
    else:
        irpf = (salario * 0.275) + 869.36
    return irpf


def calcular_salario_liquido(salario, inss, irpf):
    return salario - (inss + irpf)


while True:
    print('_' * 50)
    print('OPÇÕES:\n1 - Cadastrar Funcionário.\n2 - Listar Cadastros.\n3 - Listar Custo por Setor.\n0 - Encerar o Programa.')
    print('_' * 50)
    opcao = int(input('Digite a opção:\n'))
    if opcao == 0 or opcao == 1 or opcao == 2 or opcao == 3:
        if opcao == 1:
            lista_cadastro.clear()
            print('_' * 50)
            print('Cadastro de Funcionário.')
            print('Dados Pessoais.')
            matricula = cadastro_matricula()
            lista_cadastro.append(matricula)
            nome = cadastro_nome()
            lista_cadastro.append(nome)
            print('_' * 50)
            print('Dados de Contato.')
            email = cadastro_email()
            lista_cadastro.append(email)
            telefone = cadastro_telefone()
            lista_cadastro.append(telefone)
            celular = cadastro_celular()
            lista_cadastro.append(celular)
            print('_' * 50)
            print('Dados de Endereço.')
            endereco = cadastro_endereco()
            lista_cadastro.append(endereco)
            numero = cadastro_numero()
            lista_cadastro.append(numero)
            while True:
                opcao_complemento = input('Possui complemento? Digite: S para SIM ou N para NÃO:\n').upper().strip()
                if opcao_complemento == 'S' or opcao_complemento == 'N':
                    if opcao_complemento == 'S':
                        complemento = cadastro_complemento()
                        break
                    else:
                        complemento = None
                        break
                else:
                    print('Opção inválida, por favor, tente novamente!')
            lista_cadastro.append(complemento)
            bairro = cadastro_bairro()
            lista_cadastro.append(bairro)
            cidade = cadastro_cidade()
            lista_cadastro.append(cidade)
            uf = cadastro_uf()
            lista_cadastro.append(uf)
            print('_' * 50)
            print('Dados da Função.')
            cargo = cadastro_cargo()
            lista_cadastro.append(cargo)
            setor = cadastro_setor()
            lista_cadastro.append(setor)
            salario = float(cadastro_salario())
            lista_cadastro.append(salario)
            inss = float(calcular_inss(salario))
            lista_cadastro.append(inss)
            irpf = float(calcular_irpf(salario))
            lista_cadastro.append(irpf)
            salario_liquido = calcular_salario_liquido(salario, inss, irpf)
            lista_cadastro.append(salario_liquido)
            arquivo = open('funcionarios.txt', 'a')
            for i in range(17):
                arquivo.write(str(lista_cadastro[i]))
                if i < 16:
                    arquivo.write(' - ')
            arquivo.write('\n')
            arquivo.close()
        elif opcao == 2:
            print('_'*50)
            print('Funcionários Cadastrados.')
            print('_' * 225)
            arquivo = open('funcionarios.txt', 'r')
            for l in arquivo:
                linha = l.strip()
                itens = linha.split(' - ')
                for i in range(len(itens)):
                    print(f'{itens[i]:<10} - ', end='')
                    if i == 16:
                        print('\n')
            print('_' * 225)
            arquivo.close()
        elif opcao == 3:
            print('_'*50)
            print('Custo por Setor.')
            arquivo = open('funcionarios.txt', 'r')
            for l in arquivo:
                linha = l.strip().split(' - ')
                lista_setor.append(linha[12])
                lista_salario.append(linha[13])
            arquivo.close()
            lista_setor.pop(0)
            lista_salario.pop(0)
            for s in range(len(lista_setor)):
                if lista_setor[s] not in grupo_setor:
                    grupo_setor.append(lista_setor[s])
                    total_setor.append(0)
                posicao = grupo_setor.index(lista_setor[s])
                total_setor[posicao] += float(lista_salario[s])
            print('_' * 50)
            print('Setor     -     Total Gasto')
            for i in range(len(grupo_setor)):
                print(f'{grupo_setor[i]:<10}-     R${total_setor[i]:<10}')
        else:
            break
    else:
        print('Opção inválida, por favor, digite novamente!')

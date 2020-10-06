import os
import cadastar_agenda as ca

if os.path.exists('agenda.txt'):
    arquivo = open('agenda.txt', 'a')
else:
    arquivo = open('agenda.txt', 'w')
    arquivo.write('Agenda'.center(50, '-'))
    arquivo.write('\n')
    arquivo.write('_' * 50)
    arquivo.write('\n')
arquivo.close()

while True:
    print('Sistema de agenda!'.center(50, '-'))
    print('Escolha uma opção!')
    print('1 - Cadastrar novo contado.\n2 - Listar contatos.\n0 - Encerrar o sistema.')
    opcao = int(input('Digite a opção: '))
    if opcao == 0 or opcao == 1 or opcao == 2:
        if opcao == 0:
            break
        if opcao == 1:
            print('_'*50)
            print('Cadastro de contato!'.center(50, '*'))
            nome = ca.nome()
            telefone = ca.telefone()
            email = ca.email()
            facebook = ca.facebook()
            linkedin = ca.linkedin()
            data_nasciemnto = ca.data_nascimento()
            with open('agenda.txt', 'a') as arquivo:
                arquivo.write(f'Nome: {nome}'.ljust(50))
                arquivo.write('\n')
                arquivo.write(f'Telefone: {telefone}'.ljust(50))
                arquivo.write('\n')
                arquivo.write(f'E-mail: {email}'.ljust(50))
                arquivo.write('\n')
                arquivo.write(f'Facebook: {facebook}'.ljust(50))
                arquivo.write('\n')
                arquivo.write(f'Linkedin: {linkedin}'.ljust(50))
                arquivo.write('\n')
                arquivo.write(f'Data de Nascimento: {data_nasciemnto}'.ljust(50))
                arquivo.write('\n')
                arquivo.write('_' * 50)
                arquivo.write('\n')
        else:
            print('_' * 50)
            print('Contatos cadastrados!'.center(50, '*'))
            arquivo = open('agenda.txt', 'r')
            for l in arquivo:
                linha = l.strip()
                itens = linha.split(' - ')
                for i in range(len(itens)):
                    print(f'{itens[i]}')
            arquivo.close()
    else:
        print('*' * 50)
        print('Opção inválida, por favor, tente novamente!')

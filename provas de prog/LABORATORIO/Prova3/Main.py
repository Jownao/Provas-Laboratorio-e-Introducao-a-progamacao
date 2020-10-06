import Docente as doc
import Secretaria as sec
import Protocolo as pro
import Funcionario as fun
loop = 1
while loop != 0:
    print('========================\n'+
          '       Protocolo        \n'+
        '========================\n'+
        '[1] Cadastro de Funcionários\n'+
        '[2] Cadastrar Protocolo\n'+
        '[0] Sair\n')
    opcao = int(input('Digite uma opção do menu: '))
    while True:
        if opcao >= 1 and opcao <= 2:
            if opcao == 1:
                print('[1]Cadastrar Docente\n[2]Cadastrar Secretária\n')
                while True:
                    escolha = int(input('Digite uma opção: '))
                    if escolha == 1 or escolha == 2:
                        if escolha == 1:
                            print('Cadastro Docente'.center(50, '-'))
                            docente = doc.docente()
                            funcionario = fun.funcionario()
                            docente.cadastrar()
                            escolha2 = int(input('Gostaria de exibir ?\n[1]Sim\n[0]Não\n'))
                            if escolha2 == 1:
                                funcionario.exibir()
                                docente.exibir()
                        else:
                            print('Cadastro Secretária'.center(50, '-'))
                            secretaria = sec.secretaria()
                            secretaria.cadastrar()
                            escolha2 = int(input('Gostaria de exibir ?\n[1]Sim\n[0]Não\n'))
                            if escolha2 == 1:
                                funcionario.exibir()
                                secretaria.exibir()
            elif opcao == 2:
                print('Cadastro do Protocolo'.center(50, '-'))
                protocolo = pro.protocolo()
                protocolo.emitir()
                escolha = int(input('Gostaria de exibir ?\n[1]Sim\n[0]Não\n'))
                if escolha == 1:
                    protocolo.exibir()
                print('Enviando para o Parecerista...')
                protocolo.emitirParecer()
                parecer = int(input('Digite para Aprovar ou Reprovar:\n[1]Aprovar\n[0]Reprovar\n'))
                if parecer == 1:
                    print('Parecer Aprovado!')
                else:
                    print('Parecer Reprovado!')
                escolha = int(input('Gostaria de exibir o parecer ?\n[1]Sim\n[0]Não\n'))
                if escolha == 1:
                    protocolo.exibirParecer()
                else:
                    pass
                break
        else:
            print('Opção inválida, por favor, tente novamente!')
            opcao = int(input('Digite uma opção do menu: '))

    loop = int(input('Digite 0 para sair, ou 1 para continuar: '))
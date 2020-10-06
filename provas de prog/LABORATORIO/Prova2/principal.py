import ParticipanteInterno as pin
import ParticipanteExterno as pex
import Ata as ata
import Sugestao as sug
import os
participantes_externos = []
participantes_internos = []
gerar_ata = ata.ata()

continuar = 1
while continuar != 0:
    print('MENU\n'
          '1 - Cadastrar Participantes\n'
          '2 - Gerar Ata\n'
          '3 - Sugerir Edição na Ata\n'
          '4 - Salvar Ata')
    opcao = int(input('Digite uma opção do menu: '))
    while True:
        if opcao >= 1 and opcao <= 4:
            if opcao == 1:
                print('1 - Participante Interno\n2 - Participante Externo')
                while True:
                    selecao = int(input('Digite uma opção entre 1 e 2: '))
                    if selecao == 1 or selecao == 2:
                        if selecao == 1:
                            interno = pin.participate_interno()
                            interno.incluir()
                            participantes_internos.append(interno.nome)
                        else:
                            externo = pex.participante_externo()
                            externo.incluir()
                            participantes_externos.append(externo.nome)
                        break
                    else:
                        print('Opção inválida, por favor, tente novamente!')
            elif opcao == 2:
                if (len(participantes_externos) + len(participantes_internos)) >= 2:
                    emissor = input('Digite o nome do emissor')
                    if emissor in participantes_internos:
                        gerar_ata.emitir(emissor)
                    else:
                        print('Pessoa não cadastrada.')

                else:
                    print('Menos de dois participantes cadastrados!')
            elif opcao == 3:
                sugestao = sug.sugestao()
                sugestao.emitir()
            else:
                gerar_ata.salvar()
            break
        else:
            print('Opção inválida, por favor, tente novamente!')

    continuar = int(input('Digite 0 para sair, ou 1 para continuar: '))

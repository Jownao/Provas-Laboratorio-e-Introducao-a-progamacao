from datetime import datetime
import os


class ata:

    def __init__(self):
        self.titulo = ''
        self.data_emissao = ('{}/{}/{}'.format(datetime.now().day, datetime.now().month, datetime.now().year))
        self.inicio = ('{}:{}'.format(datetime.now().hour, datetime.now().minute))
        self.termino = ''
        self.pauta = ''
        self.descricao = ''
        self.palavra_chave = ''
        self.tipo = ''
        self.status = ''
        self.emissor = ''

    def emitir(self, emissor):
        print('Ata'.center(50, '.'))
        self.titulo = input('Digite o titulo da ata: ')
        self.termino = input('Digite a hora do termino da reunião: ')
        self.pauta = input('Digite a Pauta: ')
        self.descricao = input('Digite uma decrição: ')
        self.palavra_chave = input('Digite a palavra chave: ')
        self.tipo = input('Digite o tipo da ata: ')
        self.status = input('Digite o status: ')
        self.emissor = emissor

    def exibir(self):
        print('Ata'.center(50, '.'))
        print(f'Titulo: {self.titulo}')
        print(f'Data: {self.data_emissao}')
        print(f'Inicio: {self.inicio}')
        print(f'Termino: {self.termino}')
        print(f'Pauta: {self.pauta}')
        print(f'Descrição: {self.descricao}')
        print(f'Palavra chave: {self.palavra_chave}')
        print(f'Tipo: {self.tipo}')
        print(f'Status: {self.status}')

    def concluir(self):
        pass

    def enviar_revisao(self):
        pass

    def salvar(self):
        if os.path.exists('ata.txt'):
            ata = open('ata.txt', 'a')
            ata.write('\n')
        else:
            ata = open('ata.txt', 'w')
            ata.write('\n')
        ata.write('Título: ')
        ata.write(self.titulo)
        ata.write('\n')
        ata.write('Data de emissão: ')
        ata.write(self.data_emissao)
        ata.write('\n')
        ata.write('Inicio: ')
        ata.write(self.inicio)
        ata.write('\n')
        ata.write('Termino: ')
        ata.write(self.termino)
        ata.write('\n')
        ata.write('Pauta: ')
        ata.write(self.pauta)
        ata.write('\n')
        ata.write('Descrição: ')
        ata.write(self.descricao)
        ata.write('\n')
        ata.write('Palavra Chave: ')
        ata.write(self.palavra_chave)
        ata.write('\n')
        ata.write('Tipo: ')
        ata.write(self.tipo)
        ata.write('\n')
        ata.write('Status: ')
        ata.write(self.status)
        ata.write('\n')
        ata.write('Emissor: ')
        ata.write(self.emissor)
        ata.write('\n')
        ata.close()

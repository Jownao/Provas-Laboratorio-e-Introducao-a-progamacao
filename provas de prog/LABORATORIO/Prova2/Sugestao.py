class sugestao:

    def __init__(self):
        self.data = ''
        self.descricao = ''

    def emitir(self):
        print('Sugestão'.center(50, '.'))
        self.data = input('Digite a data: ')
        self.descricao = input('Digite a descrição: ')

    def selecionar(self):
        pass
        '''print('Sugestão'.center(50, '.'))
        print(f'Data: {self.data}')
        print(f'Descrição: {self.descricao}')'''

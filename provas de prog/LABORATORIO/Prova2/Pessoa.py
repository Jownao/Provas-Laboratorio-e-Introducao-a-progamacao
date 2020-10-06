class pessoa:

    def __init__(self):
        self.nome = ''
        self.email = ''
        self.celular = ''

    def incluir(self):
        print('Dados Pessoais'.center(50, '.'))
        self.nome = input('Digite o nome: ')
        self.email = input('Digite o E-mail: ')
        self.celular = input('Digite o celular: ')

    def exibir(self):
        print('Dados Pessoais'.center(50, '.'))
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Celular: {self.celular}')

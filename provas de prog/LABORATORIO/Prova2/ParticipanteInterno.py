import Pessoa as pe


class participate_interno(pe.pessoa):

    def __init__(self):
        super().__init__()
        self.matricula = 0
        self.sexo = ''
        self.nascimento = ''
        self.telefone = ''
        self.setor = ''

    def incluir(self):
        super().incluir()
        print('Informaçoes Participante Interno'.center(50, '.'))
        self.matricula = input('Digite a matricula: ')
        self.sexo = input('Digite o genero: ')
        self.nascimento = input('Digite a data de nascimento: ')
        self.telefone = input('Digite o telefone: ')
        self.setor = input('Digite o setor: ')

    def exibir(self):
        super().exibir()
        print('Informaçoes Participante Interno'.center(50, '.'))
        print(f'Matricula: {self.matricula}')
        print(f'Genero: {self.sexo}')
        print(f'Data de nascimento: {self.nascimento}')
        print(f'Telefone: {self.telefone}')
        print(f'Setor: {self.setor}')

import Pessoa as pe


class participante_externo(pe.pessoa):

    def __init__(self):
        super().__init__()
        self.empresa = ''

    def incluir(self):
        super().incluir()
        print('Informaçoes do Perticipante Externo'.center(50, '.'))
        self.empresa = input('Digite o nome da empresa: ')

    def exibir(self):
        super().exibir()
        print('Informaçoes do Perticipante Externo'.center(50, '.'))
        print(f'Nome Empresa: {self.empresa}')

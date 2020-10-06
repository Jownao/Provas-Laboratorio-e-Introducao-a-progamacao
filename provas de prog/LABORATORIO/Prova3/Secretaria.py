import Funcionario as fu
class secretaria(fu.funcionario):
    def __init__(self):
        super().__init__()
        self.setor = ''
        self.salario = 0.0

    def cadastrar(self):
        super().cadastrar()
        print('Dados da Secretária'.center(50, '-'))
        self.setor = input('Entre com o setor: ')
        
    def exibir(self):
        super().exibir()
        print('Dados da Secretária'.center(50, '-'))
        print(self.setor)



        
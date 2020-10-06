import Funcionario as fu
class docente(fu.funcionario):
    def __init__(self):
        super().__init__()
        self.disciplina = ''
        self.salario = 0.0
        self.titulacao = ''
        
    def cadastrar(self):
        super().cadastrar()
        print('Dados do Docente'.center(50, '-'))
        self.disciplina = input('Entre com a disciplina: ')
        self.titulacao = input('Entre com a titulação: ')

    def exibir(self):
        super().exibir()
        print('Dados do Docente'.center(50, '-'))
        print(self.disciplina)
        print(self.titulacao)

        

import FolhaPagamento as fp
class funcionario():
    def __init__(self):
        self.matricula = 0
        self.nome = ''
        self.sexo = ''
        self.nascimento = ''
        self.salario = 0.0
        self.folha = fp.calculo_folha()
    def cadastrar(self):
        print('Dados do Funcionário'.center(50, '-'))
        self.matricula = int(input('Entre com a matricula: '))
        self.nome = input('Entre com o nome: ')
        self.sexo = input('Entre com o sexo: ')
        self.nascimento = input('Entre com a data de nascimento: ')
        self.salario = float(input("Entre com o salário:"))
        self.folha.entrar_salario(self.salario)
    def exibir(self):
        print('Dados do Funcionário'.center(50, '-'))
        print(self.matricula)
        print(self.nome)
        print(self.sexo)
        print(self.nascimento)
        print('Salário: ',self.salario)
        print('Folha de Pagamento'.center(50, '-'))
        self.folha.exibir_folha()
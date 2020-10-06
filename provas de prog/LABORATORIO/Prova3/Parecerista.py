
class Parecerista():
    def __init__(self):
        self.area = ''
    def cadastrar(self):
        print('Dados Parecerista'.center(50, '-'))
        self.area = input('Entre com a área: ')

    def exibir(self):
        print('Dados Parecerista'.center(50, '-'))
        print(self.area)

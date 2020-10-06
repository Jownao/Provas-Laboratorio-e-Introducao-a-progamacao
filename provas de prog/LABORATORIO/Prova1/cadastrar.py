import os
class cadastrar():
    def __init__(self):
        self.nome = ''
        self.telefone = ''
        self.email = ''
        self.facebook = ''
        self.linkedin = ''
        self.nascimento = ''
    def cadastro(self):
        self.nome = input('Entre com o nome:\n')
        self.telefone = input('Entre com o telefone:\n')
        self.email = input('Entre com o email:\n')
        self.facebook = input('Entre com o facebook:\n')
        self.linkedin = input('Entre com o linkedin:\n')
        self.nascimento = input('Entre com a data de nascimento:\n')
    def save(self):
        if os.path.exists('agenda.txt'):
            agenda = open('agenda.txt','a')
            agenda.write('\n')
        else:
            agenda = open('agenda.txt','w')
            agenda.write('\n')
        agenda.write('Nome',self.nome)
        agenda.write('\n')
        agenda.write(self.telefone)
        agenda.write('\n')
        agenda.write(self.email)
        agenda.write('\n')
        agenda.write(self.facebook)
        agenda.write('\n')
        agenda.write(self.linkedin)
        agenda.write('\n')
        agenda.write(self.nascimento)
        agenda.write('\n')

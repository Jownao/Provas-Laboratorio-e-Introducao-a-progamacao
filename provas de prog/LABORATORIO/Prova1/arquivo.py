import os
class salvar():
    def salvamento(self):
        if os.path.exists('agenda.txt'):
            agenda = open('agenda.txt','a')
            agenda.write(self)
            agenda.write('\n')
        else:
            agenda = open('agenda.txt','w')
        agenda.close()
    def exibir(self):
        agenda = open('agenda.txt','r')
        texto = agenda.read()
        print(texto)
        agenda.close()

from datetime import date

class protocolo():
    def __init__(self):
        data_atual = date.today()
        self.data_emissao = data_atual.strftime('%d/%m/%Y')
        self.data_inicio_experimento = ''
        self.justificativa_uso_animais = ''
        self.resumo_pt = ''
        self.resumo_en = ''
        self.data_envio_parecer = ''
        self.data_emissao_parecer = ''
        self.status_protocolo = ''
        self.especie = ''
        self.bioterio = ''
        self.parecer = ''

    def emitir(self):
        print('Dados do Protocolo'.center(50, '-'))
        print('Entre com as informações abaixo:\n ')        
        self.data_inicio_experimento = input('Data de ínicio do Experimento: ')
        self.justificativa_uso_animais = input('Justificativa de uso do animal: ')
        self.resumo_pt = input('Resumo em Português: ')
        self.resumo_en = input('Resumo em Inglês: ')
        self.data_envio_parecer = input('Data de envio ao Parecer: ')
        self.data_emissao_parecer = input('Data de emissão ao Parecer: ')
        self.status_protocolo = input('Status do protocolo: ')
        self.especie = input('Espécie: ')
        self.bioterio = input('Biotério: ')
        
    def emitirParecer(self):
        self.parecer = input('Insira o parecer: \n')

    def exibir(self):
        print('Dados do Protocolo'.center(50, '-'))
        print(self.data_emissao)
        print(self.data_inicio_experimento)
        print(self.justificativa_uso_animais)
        print(self.resumo_pt)
        print(self.resumo_en)
        print(self.data_envio_parecer)
        print(self.data_emissao_parecer)
        print(self.status_protocolo)
        print(self.especie)
        print(self.bioterio)

    def exibirParecer(self):
        print(self.parecer)
        


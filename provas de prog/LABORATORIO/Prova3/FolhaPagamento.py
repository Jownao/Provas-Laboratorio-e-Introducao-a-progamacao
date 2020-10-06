class calculo_folha():
    def __init__(self):
        self.salario_bruto = 0.0
        self.inss = 0.0
        self.irrf = 0.0
        self.salario_liquido = 0.0
        self.salario_sem_inss = 0.0

    def entrar_salario(self, salario=0.0):
        self.salario_bruto = salario
        
    def calcular_inss(self):
        if self.salario_bruto < 1751.82:
            self.inss = self.salario_bruto * 0.08
        elif self.salario_bruto > 1751.81 and self.salario_bruto < 2919.73:
            self.inss = self.salario_bruto * 0.09
        elif self.salario_bruto > 2919.72 and self.salario_bruto < 5839.46:
            self.inss = self.salario_bruto * 0.11
        elif self.salario_bruto > 5839.45:
            self.inss = 817.66

    def calcular_irrf(self):
        if self.salario_bruto < 1903.98:
            self.irrf = self.salario_bruto
        elif self.salario_bruto > 1903.98 and self.salario_bruto < 2836.66:
            self.irrf = self.salario_bruto * 0.075
        elif self.salario_bruto > 2836.65 and self.salario_bruto < 3751.05:
            self.irrf = self.salario_bruto * 0.15
        elif self.salario_bruto > 3751.04 and self.salario_bruto < 4664.68:
            self.irrf = self.salario_bruto * 0.225
        else:
            self.irrf = self.salario_bruto * 0.275

    def calcular_folha(self):
        self.calcular_inss()
        self.calcular_irrf()
        self.salario_liquido = self.salario_bruto - (self.irrf + self.inss)
    def exibir_folha(self):
        self.calcular_folha()
        print('Salário Bruto: R$ {}'.format(self.salario_bruto))
        print('Descontos')
        print('INSS: R$ {}'.format(self.inss))
        print('IRRF: R$ {}'.format(self.irrf))
        print('-------------------------------')
        print('Salário líquido: R$ {}'.format(self.salario_liquido))
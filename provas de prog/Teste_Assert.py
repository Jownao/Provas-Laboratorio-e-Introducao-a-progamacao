
def teste_email(email):
    assert '@' in email, 'Email inválido, "@" não digitado!'

def teste_telefone(telefone):
    assert len(telefone) >= 8, 'Número de telefone informado com menos de 8 caracteres numéricos!'

def teste_celular(celular):
    assert len(celular) >= 8, 'Número de celular informado com menos de 8 caracteres numéricos!'

def teste_inss(inss):
    assert inss == 180, 'Cálculo do INSS errado!'

def teste_irpf(irpf):
    assert irpf == 292.80, 'Cálculo do IRPF errado.'

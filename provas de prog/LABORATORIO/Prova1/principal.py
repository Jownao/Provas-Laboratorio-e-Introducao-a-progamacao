import cadastrar as c
import arquivo as a
print('========================\n'+
      '         AGENDA         \n'+
      '========================\n'+
      '[1] Novo cadastro\n'+
      '[2] Listar agenda\n')

res = int(input('Opção: '))

if res == 1:
    cd = c.cadastrar()
    cd.cadastro()
    cd.save()
elif res == 2:
    print()
    ag = a.salvar()
    ag.exibir()
else:
    print('Opção inválida!')

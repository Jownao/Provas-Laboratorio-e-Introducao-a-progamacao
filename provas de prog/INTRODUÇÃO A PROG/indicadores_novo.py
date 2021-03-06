# -*- coding: utf-8 -*-
"""indicadores_novo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c7cLuuPyCtx4yJp2hV1pV4AIbT3fqyEU
"""

import pandas as pd
import matplotlib.pyplot as plt

# Obtenção dos dados.
dados_indicadores = pd.read_excel('Ind030104-20120130.xlsx', sheet_name = 'Tabela')

linhas_colunas = dados_indicadores.shape

print(f'{linhas_colunas[0]} linhas e {linhas_colunas[1]} colunas.')
anos = (dados_indicadores.iloc[3:4, 0:10])

# Lista com os nomes das colunas.
lista_anos = anos.values.tolist()

# Renomeando as colunas.
dados_indicadores.columns = lista_anos

# Criação de um dataframe com os dados referente a regão nordeste.
nordeste = dados_indicadores.iloc[9:14, 0:10]

print(nordeste)

# Invertendo as linhas em colunas.
nordeste = nordeste.T
print(nordeste)

# Salvando um dataframe em um arquivo excel.
nordeste.to_excel('regiao_nordeste.xlsx')

# Dataframes com dados para as outras regiôes.
norte = dados_indicadores.iloc[4:9, 0:10]
norte = norte.T
print(norte)
sudeste = dados_indicadores.iloc[14:19, 0:10]
sudeste = sudeste.T
print(sudeste)
sul = dados_indicadores.iloc[19:24, 0:10]
sul = sul.T
print(sul)
centro_oeste = dados_indicadores.iloc[24:29, 0:10]
centro_oeste = centro_oeste.T
print(centro_oeste)
brasil = dados_indicadores.iloc[29:34, 0:10]
brasil = brasil.T
print(brasil)

# Dados Região Nordeste.
nordeste_municipal = nordeste[10]
nordeste_municipal = nordeste_municipal.values.tolist()
nordeste_estadual = nordeste[11]
nordeste_estadual = nordeste_estadual.values.tolist()
nordeste_federal = nordeste[12]
nordeste_federal = nordeste_federal.values.tolist()
nordeste_total = nordeste[13]
nordeste_total = nordeste_total.values.tolist()

# Dados Região Norte.
norte_municipal = norte[5]
norte_municipal = norte_municipal.values.tolist()
norte_estadual = norte[6]
norte_estadual = norte_estadual.values.tolist()
norte_federal = norte[7]
norte_federal = norte_federal.values.tolist()
norte_total = norte[8]
norte_total = norte_total.values.tolist()

# Dados Região Sudeste.
sudeste_municipal = sudeste[15]
sudeste_municipal = sudeste_municipal.values.tolist()
sudeste_estadual = sudeste[16]
sudeste_estadual = sudeste_estadual.values.tolist()
sudeste_federal = sudeste[17]
sudeste_federal = sudeste_federal.values.tolist()
sudeste_total = sudeste[18]
sudeste_total = sudeste_total.values.tolist()

# Dados Região Sul.
sul_municipal = sul[20]
sul_municipal = sul_municipal.values.tolist()
sul_estadual = sul[21]
sul_estadual = sul_estadual.values.tolist()
sul_federal = sul[22]
sul_federal = sul_federal.values.tolist()
sul_total = sul[23]
sul_total = sul_total.values.tolist()

# Dados Região Centro-Oeste.
centro_oeste_municipal = centro_oeste[25]
centro_oeste_municipal = centro_oeste_municipal.values.tolist()
centro_oeste_estadual = centro_oeste[26]
centro_oeste_estadual = centro_oeste_estadual.values.tolist()
centro_oeste_federal = centro_oeste[27]
centro_oeste_federal = centro_oeste_federal.values.tolist()
centro_oeste_total = centro_oeste[28]
centro_oeste_total = centro_oeste_total.values.tolist()

# Dados Brasil.
brasil_municipal = brasil[30]
brasil_municipal = brasil_municipal.values.tolist()
brasil_estadual = brasil[31]
brasil_estadual = brasil_estadual.values.tolist()
brasil_federal = brasil[32]
brasil_federal = brasil_federal.values.tolist()
brasil_total = brasil[33]
brasil_total = brasil_total.values.tolist()

anos = lista_anos[0][1:]

# Gráfico simples Região Nordeste.
plt.title('Região Nordeste.')
plt.plot(anos, nordeste_municipal[1:], label = 'Municipal')
plt.plot(anos, nordeste_estadual[1:], label = 'Estadual')
plt.plot(anos, nordeste_federal[1:], label = 'Federal')
plt.plot(anos, nordeste_total[1:], label = 'Total')
plt.legend()
plt.xlabel('Anos')
plt.ylabel('Valor')
plt.show()

# Gráfico simples Região Norte.
plt.title('Região Norte.')
plt.plot(anos, norte_municipal[1:], label = 'Municipal')
plt.plot(anos, norte_estadual[1:], label = 'Estadual')
plt.plot(anos, norte_federal[1:], label = 'Federal')
plt.plot(anos, norte_total[1:], label = 'Total')
plt.legend()
plt.xlabel('Anos')
plt.ylabel('Valor')
plt.show()

# Gráfico simples Região Sudeste.
plt.title('Região Sudeste.')
plt.plot(anos, sudeste_municipal[1:], label = 'Municipal')
plt.plot(anos, sudeste_estadual[1:], label = 'Estadual')
plt.plot(anos, sudeste_federal[1:], label = 'Federal')
plt.plot(anos, sudeste_total[1:], label = 'Total')
plt.legend()
plt.xlabel('Anos')
plt.ylabel('Valor')
plt.show()

# Gráfico simples Região Sul.
plt.title('Região Sul.')
plt.plot(anos, sul_municipal[1:], label = 'Municipal')
plt.plot(anos, sul_estadual[1:], label = 'Estadual')
plt.plot(anos, sul_federal[1:], label = 'Federal')
plt.plot(anos, sul_total[1:], label = 'Total')
plt.legend()
plt.xlabel('Anos')
plt.ylabel('Valor')
plt.show()

# Gráfico simples Região Centro-Oeste.
plt.title('Região Centro-Oeste.')
plt.plot(anos, centro_oeste_municipal[1:], label = 'Municipal')
plt.plot(anos, centro_oeste_estadual[1:], label = 'Estadual')
plt.plot(anos, centro_oeste_federal[1:], label = 'Federal')
plt.plot(anos, centro_oeste_total[1:], label = 'Total')
plt.legend()
plt.xlabel('Anos')
plt.ylabel('Valor')
plt.show()

# Gráfico simples Brasil.
plt.title('Brasil.')
plt.plot(anos, brasil_municipal[1:], label = 'Municipal')
plt.plot(anos, brasil_estadual[1:], label = 'Estadual')
plt.plot(anos, brasil_federal[1:], label = 'Federal')
plt.plot(anos, brasil_total[1:], label = 'Total')
plt.legend()
plt.xlabel('Anos')
plt.ylabel('Valor')
plt.show()

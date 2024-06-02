"""
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dado = np.loadtxt(url, delimiter = ',', usecols = np.arange(1,87 + 1,1))
dado_transposto = dado.T

#                      [escolhe quais linhas vai pegar, escolhe quais colunas vai pegar]
datas = dado_transposto[:,0] # salva somente os anos em datas, [pega todas a linhas, pega a coluna 0]
#                       [pega todas as linhas, pega da coluna 1 a coluna 6 ]
precos = dado_transposto[:,1:6] # salva todos os preços em preco

#datas = np.arange(1,88,1)

#plt.plot(datas, precos[:,0]) 
#plt.show() # mostra o grafico criado 

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

plt.plot(np.arange(1,13,1), Moscow_ano1)
plt.plot(np.arange(1,13,1), Moscow_ano2)
plt.plot(np.arange(1,13,1), Moscow_ano3)
plt.plot(np.arange(1,13,1), Moscow_ano4)
plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])

#plt.show()

np.array_equal(Moscow_ano3, Moscow_ano4) # array_equal compara se dois arrays são iguais, retorna false, porque os arrays não são iguais
np.allclose(Moscow_ano3, Moscow_ano4,10)# allclose compara se dois arrays são distantes dependendo do numero que passa, no caso passou 10 retorna True, porque a diferença entre eles é menor que 10 

# Lidando com NaNs
# NaNs são falhas nos dados ou dados faltando, exemplo [1,2, ,4] nesse array está faltando um dado no caso porlogica o 3

print(sum(np.isnan(Kaliningrad))) # isnan retorna false para todas as celulas que tiverem valor e true caso seja um nan, faz isso com todos os dados, o sum soma todos os dados posi true é 1 e false é 0 

# um jeito de substituir esse valor é fazendo a media do numero que vem antes e do numero que vem depois do nan

Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]]) # aqui vc substitui o valor nan deixando seus dados corretos, mean calcula a media de informações passadas

# calculandoa media dos prelos de maça por cidade 

print("Moscou: ",round(np.mean(Moscow), 2), "\nKalinigrad: ",round(np.mean(Kaliningrad), 2))
"""
# Exercicios

#Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas agora você deve selecionar parte dos dados. As colunas que iremos avaliar são as de diâmetro e peso. Crie arrays específicos para guardar o diâmetro e peso da laranja e toranja. O diâmetro está na coluna zero e o peso na coluna 1. Os dados referentes a laranja vão até a linha 4999 e os referentes à toranja iniciam na linha 5000 do arquivo. Após fazer a seleção de dados, importe a biblioteca matplotlib e crie um gráfico para a laranja e para a toranja do peso pelo diâmetro.

import numpy as np
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
oranges = np.loadtxt(url, delimiter = ',', usecols = np.arange(1,6,1), skiprows = 1)

diametro_laranja = oranges[:5000,0]
diametro_toranja = oranges[5000:,0]
peso_laranja = oranges[:5000,1]
peso_toranja = oranges[5000:,1]

plt.plot(diametro_laranja, peso_laranja)
plt.plot(diametro_toranja, peso_toranja)
plt.legend(['Laranja', 'Toranja'])

plt.show()
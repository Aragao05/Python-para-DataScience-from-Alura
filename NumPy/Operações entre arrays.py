import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dado = np.loadtxt(url, delimiter = ',', usecols = np.arange(1,87 + 1,1))
dado_transposto = dado.T

datas = dado_transposto[:,0]

precos = dado_transposto[:,1:6]
datas = np.arange(1,88,1)

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

plt.plot(datas, Moscow)
#plt.show()

# Diferença entre arrays

# Entender como eles estão crescendo conforme o tempo, Ajustar a reta para entender a taxa de crescimento do preço das maçãs

"""
y=ax+b   equação da reta

Y = preço das maças
x = Mês
a =  coeficiente angular
b = coeficiente linear, onde a linha corat o eixo y 
"""

# np.power(x, y) eleva o(s) valore(s) de x por y 

# np.sqrt(x) tira a raiz de x

# np.linalg.norm(Moscow - y) # faz o calculo da reta 

x = datas
y = 0.52*x+80 # calcula o valor de y, com valores chutados logo abaxi o calculo é fetio com os valores calculados esse é só um exemplo de como é feito um exboço com numeros chutados

np.linalg.norm(Moscow-y) # faz o calculo da reta 

#plt.plot(datas,Moscow)
#plt.plot(x,y)
#plt.show()

"""
np.copy(x) copia a array x para outra array ex
x = y     aqui caso y seja alterado x tambem vai pois x aponta para y
x = np.copy(y) # aqui o copy copia os valores de y para x  e caso os valores de y sejam alterados x não vai mudar poi é uma copia e não um ponteiro
"""

# Multiplicação

"""
â = coeficiente angular;
n = número de elementos;
Y = Moscow;
X = datas.
"""

Y = Moscow
X = datas
n = np.size(Moscow)

# calaculo do coeficiente angular 
a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2) # essa é a formula que stá na pasta formula, usadad para calcular o â coeficiente angular 

# calculo do coeficiente linear
b = np.mean(Y) - a*np.mean(X) # essa é a formula que stá na pasta formula, usadad para calcular o b coeficiente linear

# calculando o valor de y 
y = a*X+b

np.linalg.norm(Moscow-y) # fazendo o calculo da reta com os valores obtidos 

#plt.plot(datas,Moscow)
#plt.plot(X,y)
#plt.show()


# Motivo de Regressão
# Como podemos utilizqar os rsultados que nós obtivemos

#calcular o preço da maça no mes 100 (mes que não existe na planilha), fazer uma estimativa do valor que vai ser no mes 100

plt.plot(datas,Moscow)
plt.plot(X,y)
#plt.plot(41.5,41.5*a+b,'*r') # aqui voce faz um ponto vermelho no mes 41,5. o '* r' faz o ponto vermelho
plt.plot(100,100*a+b,'*b') # pome um  ponto azul no mes 100, a + b são os calculos da reta, coeficiente angula e linear
plt.plot()
plt.show()

#A regressão é muito utilizada em ciência de dados para a previsão e também a interpolação de valores


# Exercicios


url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
oranges = np.loadtxt(url, delimiter = ',', usecols = np.arange(1,6,1), skiprows = 1)

diametro_laranja = oranges[:5000,0]
diametro_toranja = oranges[5000:,0]
peso_laranja = oranges[:5000,1]
peso_toranja = oranges[5000:,1]

plt.plot(diametro_laranja, peso_laranja)
plt.plot(diametro_toranja, peso_toranja)
plt.legend(['Laranja', 'Toranja'])

Y = peso_laranja
X = diametro_laranja
n = np.size(X)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-np.sum(X)**2)
b = np.mean(Y) - a*np.mean(X)

plt.show()


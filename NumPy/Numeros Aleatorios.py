# Valores em um intervalo 

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

Y = Moscow
X = datas
n = np.size(Moscow)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2)
b = np.mean(Y) - a*np.mean(X)

#np.random.randint(low=40, high=100, size=100) # gera 100 numero inteiros com numeros entre 40 e 100

np.random.seed(84) # np.random.seed(x) gera numeros pseudo aleatorios baseados em x ou seja esses numeros pseudo aleatrios seram os mesmo toda vez que rodar o codigo com essa mesma seed, 

coef_angulares = np.random.uniform(low=0.10,high=0.90,size=100) # gera 100 numero floats com numeros entre 0.10 e 0.90

norma = np.array([]) # cria um array atraves e uma lista passada, no caso estaá endo passada uma lista vazzia pra criar um array vazio para adicionar os valores da conta que está fazedno no for abaixo
for i in range(100):
    norma = np.append(norma,np.linalg.norm(Moscow - (coef_angulares[i]* X + b))) # np.append adiciona valores em uma array, vc passa o nome da array e os valores a serem adicionados, no caso adima, ela vai adicionar os valores ed cada conta realizada 

#print(norma)

#print(coef_angulares)

dados = np.column_stack([norma, coef_angulares])  # np.column_stack une dois ou mais arrays, lado a lado, como colunas em uma matriz, aqui vai criar um arquico com 100 linhas e duas colunas 

np.savetxt('dados.csv', dados, delimiter=',') # salva um array em um arquivo de texto, primeiro passa o nome do arquivo, depois passa o array que vai ser salvo, depois o delimitador é qoue quer vai cepar os cados celula por celula






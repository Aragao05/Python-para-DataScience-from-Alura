# Conhecendo a Biblioteca de Dados

import numpy as np # importando a biblioteca numpy e apelidando ela como as

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'
# url é link do arquivo apples que está no git hub, vc consegue acessar ele dessa forma tambem, ai em vez de carregar o arquivo assi : 'NumPy/numpy_dados/apples_ts.csv' que está em alguma pasta do sistema, voce usa o url no lugar do path do arquivo

#apples = np.loadtxt('NumPy/numpy_dados/apples_ts.csv', delimiter = ',', usecols = np.arange(1,88,1))
dado = np.loadtxt(url, delimiter = ',', usecols = np.arange(1,87 + 1,1))
# loadtxt é uma função da biblioteca numpy que carrega arquivos para uso, delimiter passa a delimitaçãode um arquivo csv ou seja oque separa cada celula, cada informação
# delimiter = oque separa cada celula do arquivo csv
# usecols(1,88,1) ele fala que vai pegar os dados apartir da coluna 1 e vai até a coluna 87 pulando de 1 em 1, PS: arange pega só os valores entre os numeros começa na coluna 2 e vao até a coluna 87, por isso 87 + 1

#Cria array sequenciais 
np.arange(1,88,1) # vai começar em 1, 88 é quantidade de colunas que atabela tem mais + 1 no caso ele vai de 1 a 87, e vai contar de 1 em 1   

# A função ndim verifica a quantidade de dimensão do array
dado.ndim # tem 2 dimensãoes linha e coluna

# A função size verifica a quantidade de elementos(celulas) de um array
dado.size # tem 522 dados

# A função shape verifica o numero de elementos em cada dimensão
dado.shape # (6,8) tem 6 linhas e 87 colunas

# A função T realiza a transposição do array
dado_transposto = dado.T # Mostra a tabela seoara por linhas e colunas 
#print(dado_transposto)

# Exercicios

import numpy as np

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
oranges = np.loadtxt(url, delimiter = ',', usecols = np.arange(1,6,1), skiprows = 1)
# skiprows = pula uma quantodade de linhas x aprtir da primeira, acima ele pula a primeria linhab da tabela, se fosse 2 pulava a primeira e segunda linha 
#print(oranges)

print(oranges.T)
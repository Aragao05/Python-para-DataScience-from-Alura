# pip install matplotlib
#  Rodaar esse codigo no terminal instala a biblioteca matplotlib
# se quiser instlar uma versão especifica da biblioteca é só fazer assim:
# "bibliotecaxxx"==2.12.34
# iso vai instalar a bibliotecaxxx na versão 2.12.34
 
#import matplotlib   #importa a biblioteca pra uso 

#import matplotlib.pyplot as plt   #importa a biblioteca e para realizar 
# a chamada dela não precisa escrever o nome inteiro dela é só colocar plt que o compilador vai entender
#que está chamando essa biblioteca, o as é como se estivesse dando a bibliteca matplotlib.pyplot o 
#apelido de plt e podendo chamar ela dessa forma

#import random # importa biblioteca random, a principal usabilidade dela é te gerar numeros aletorios
#from random import choices # importa um meto especifico da biblioteca, fazer iso economiza memoria e não causa
#conflito de nomes entre outros metodos ou funções

#help(metodo)  te mostra como usar o metodo 

#print(matplotlib.__version__) #ver qual a versão da biblioteca

#estudantes = ["João","Maria","José"]
#notas = [8.5, 9, 6.5]

#plt.bar(x = estudantes, height = notas) # gera um grafico de barra com as notas e os alunos

#estudantes_2 = ["João","Maria","José", "Ana"]

#print(choices(estudantes_2)) # escolhe o nome de um estudante que contem na lista 


#
# Exercicios
#

# 2.Escreva um código para importar a biblioteca numpy com o alias np.

#import numpy as np


# 3.Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

#from random import choice
#lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
#print(choice(lista))


# 4.Crie um programa que sorteia, aleatoriamente, um número inteiro menor que 100.

#from random import randrange

#print(randrange(100))  # randrange pode receber até dois parametros o e escolhe um numero entre esses dois parametros ex randrange(10, 50)
# esse randrange vai mostrar os valores entre 10 e 50 aleatoriamente.


# 5.Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

#from math import pow # a função pow da biblioteca math recebe dois parametros e elva o primero numero pelo segundo Ex: pow(2,3) retorna: 8

#numero_1 = int(input("Insira um numero para ver sua potencia: "))
#numero_2 = int(input("Insira um numero para elevar o primerio numero: "))

#print(f"\nO numero {numero_1} elevado pelo numero {numero_2} retorna esse resultado: {pow(numero_1,numero_2)}\n")


# 6.Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é 
# numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer 
# o número de participantes do sorteio e devolva para ela o número sorteado.

#from random import randrange

#participantes = int(input("Insira o numero de participantes: "))

#print(f"O numero sorteado foi {randrange(0,participantes + 1)}") # a função randrange mostra até o ultimo numero, não mostra o ultimo numero
# por isso coloquei o + 1 no final para poder mostra o ultimo numero

# 7.Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 
#até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

#from random import randrange

#nome = input("Por favor insira o seu nome: ")
#token_gerado = randrange(1000, 9998 +1)

#print(f"\nOlá, {nome}, o seu token de acesso é {token_gerado}! Seja bem-vindo(a).\n")


# 8.Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa".
# Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que 
# faça essa seleção aleatória de acordo com a lista abaixo:

#from random import choice    # choice recebe uma lista como parametro e escolhe um item dessa lista

#frutas = ["maçã", "banana", "uva", "pêra", 
#          "manga", "coco", "melancia", "mamão",
#          "laranja", "abacaxi", "kiwi", "ameixa"]

#fruta_1 = choice(frutas)
#fruta_2 = choice(frutas)
#fruta_3 = choice(frutas)

#print(f"As tres frutas escolhidas são: {fruta_1}, {fruta_2}, {fruta_3}.")


# 9.Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. 
# A lista é a seguinte: No final, informe quais números possuem raízes inteiras e seus respectivos valores.

#from math import sqrt

#numeros = [2, 8, 15, 23, 91, 112, 256]

#for numero in numeros:
#    raiz = sqrt(numero)
#    if raiz.is_integer():
#        print(f"O numero {numero} é um numero com raiz inteira e sua raiz é: {raiz}")
#    else:
#        print(f"O numero {numero} não possui uma raiz inteira.")


# 10.Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado
# da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.



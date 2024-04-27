# Built in functions  são funções que estão dentro do python e podem ser chamadas a qualquer momento EX: print, type, list

#notas = {'1° Trimestre': 8.5, '2° Trimestre': 9.5, '3° trimestre': 7}

# calculandoa  soma do meto normal
#soma = 0
#for nota in notas.values():  # .values() pega todos os numeros do dicionario e trasnforma eles em uma lista iteravel
#    soma  += nota
#print(soma)

# calculando a soma usando uma Built in functions
#print(sum(notas.values()))  # sum() soma os numeros de uma lista


# calculando a media

#qtd_notas = len(notas) # len retona a quantidade de intens de algo 
#media = soma / qtd_notas
#print(round(media,2))


# fromato de uma função criada:
#def <nome>(<parametros>,<quantos quiser>):
#   <instruções>

# para utilizar a função voce precisa chamar ela passando os parametros que ela requer
#<nome>(<parametro_1>, <paremetro_2>)

# calcular a media de um estudante, sendo possivel aumentar e diminuir a quantidade de notas que ele tem

#notas = [8.5, 9.0, 6.0, 10.0]

#def media(lista):
#    calculo = sum(lista) / len(lista)
#    print(round(calculo,2))

#media(notas)


# Funçoes que retornam valores usam o return no final

#notas = [8.5, 9.0, 6.0, 10.0]

#def media(lista):
#    calculo = sum(lista) / len(lista)
#    return calculo  # return retorna um valor ao chamar a função e não mostra nado 
#print(f"O resultado da média é: {calulo})

#notas = [6.0, 7.0, 9.0, 5.0]

#def boletim(lista):
#    media = sum(lista) / len(lista)
    
#    if media >= 6:
#        situacao = "Aprovado(a)"
#    else:
#        situacao = "Reprovado(a)"
    
#   return (media, situacao)

#media, situacao = boletim(notas)
#print(f'O(a) estudante atingiu uma média de {media} e foi {situacao}.')


# Type hint

# a nossa função recebe uma lista do tipo list e retorna uma variável do tipo float
# caso não recebe nenhum valor de parâmetro será passada uma lista com um único
# elemento sendo ele zero

#def media(lista: list=[0]) -> float:
#   calculo = sum(lista) / len(lista)
#   return calculo


# Função Lambda

# é uma forma de criar funções anônimas, o que significa que elas não são declaradas 
#com um nome convencional usando a palavra-chave def. Em vez disso, você usa a palavra-chave lambda para criar uma função inline.

#nota = float(input("Digite a nota do(a) estudante: "))

#qualitativo = lambda x: x + 0.5

#qualitativo(nota)

# media ponderada usadno lambda

#N1 = float(input("Digite a 1ª nota do(a) estudante: "))
#N2 = float(input("Digite a 2ª nota do(a) estudante: "))
#N3 = float(input("Digite a 3ª nota do(a) estudante: "))

#media_ponderavel = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10
#media_estudante = media_ponderavel(N1, N2, N3)
#print(media_estudante)

# resumidamente ela recebe uma inserção de valores e faz algo usando eles

# Usando lambda atrelada ao map

# O map é uma _BUILT-IN FUNCTIONS que mapeia valores. Quando usado junto à lambda, conseguimos realizar funções 
# simples e rápidas que nos permitem alterar valores de variáveis, listas e até dicionários.

# problema: adiciona nota extra de 0.5 na media de alunos que ganharam uma gincana

#notas = [6.0, 7.0, 9.0, 5.5, 8.0]
#qualitativo = 0.5

#notas_atualizadas = map(lambda x: x + qualitativo, notas) # se não usar o map não é possivel acessar litas ou dicionarios
# nesse caso se não usar o map vai tentar somar 0.5 a lista como um todo e vai dar erro, usando o map vai somar 0.5 a cada 
# item da lista

#notas_atualizadas = list(notas_atualizadas) # se não trasnfdormar a saida da função lambda em uma lista quando for mostrar
# o resultado ela vai te mostar um endereço de memoria, transformando em lista ela te mostra a lista com os valores acrecisdos 0.5
#print(notas_atualizadas)


# Exercicios

# 1.Escreva um código que lê a lista abaixo e faça:A leitura do tamanho da lista, A leitura do maior e menor valor, A soma dos valores da lista

#lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

#tamanho = len(lista)
#soma = (sum(lista))
#maior_numero = max(lista)
#menor_numero = min(lista)

#print(f"A lista possui {tamanho} números em que o maior número é {maior_numero} e o menor número é {menor_numero}. A soma dos valores presentes nela é igual a {soma}")


# 2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, 
# para o número 7, a tabuada deve ser mostrada no seguinte formato:

#def tabuada(numero):
#    contador = 0
#    while contador <= 10:
#        multiplicacao = numero * contador
#        print(f"{numero} x {contador} = {multiplicacao}")
#        contador +=1

#numero = int(input("Escolha um numero para a sau tabuada de 0 a 10: "))
#tabuada(numero)


# 3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

#lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

#def multiplo(list):
#    resultado = []
#    for numero in list:
#        if numero % 3 == 0:
#            resultado.append(numero)
#    return resultado

#teste = multiplo(lista)
#print(teste)

# 4. Crie uma lista dos quadrados dos números da seguinte lista: 
# Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#calculo = list(map(lambda x: pow(x,2), lista))
#print(calculo)


# 5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas 
# competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 
# 5 notas digitadas pelas pessoas juradas.
# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 
# notas que sobraram. Retorne a média para apresentar o texto: "Nota da manobra: [media]"


#notas = []

#for i in range(1,6):
#  nota = float(input(f"Digite a {i}ª nota: "))
#  notas.append(nota)

#def media(lista):
#  lista.remove(max(lista))
#  lista.remove(min(lista))
#  return sum(lista) / len(lista)

#media = media(notas)
#print(f"Nota da manobra: {round(media, 1)}")


# 6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar 
# uma função que receba uma lista de 4 notas e retorne:
# maior nota
# menor nota
# média
# situação (Aprovado(a) ou Reprovado(a))
# Para testar o comportamento da função, os dados podem ser exibidos em um texto:
# "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"


#notas = []

#for i in range(1,5):
#  nota = float(input(f"Digite a {i}ª nota: "))
#  notas.append(nota)

#def cadastro(lista):
#  maior = max(lista)
#  menor = min(lista)
#  media = sum(lista) / len(lista)
#  if media >= 6:
#    situacao = "Aprovado(a)"
#  else:
#    situacao = "Reprovado(a)"
  
#  return (media, maior, menor, situacao)

#media, maior, menor, situacao = cadastro(notas)

#print(f"O(a) estudante obteve uma media de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")

# 7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus 
# nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: f"{nome.title()} {sobrenome.title()}", nomes, sobrenomes)

for n in nome_completo:
    print(f"nome completo: {n}")



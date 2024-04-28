# Lista de Lista

# Recebemos a demanda de transformar uma lista com o nome e as notas dos três trimestres de estudantes em uma lista simples com os 
# nomes separados das notas e uma lista de listas com as três notas de cada estudante separadas umas das outras.
# Os dados recebidos correspondem a uma lista com os nomes e as respectivas notas de cada estudante. Vamos resolver esse desafio? 
# Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.

""""
notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notas_juntas = []

for i in range(len(notas_turma)): # for de 0 a quantos intens tem na lista notas_turma
    if i % 4 == 0: # esse cara aqui ve quem é multiplo de 4 pois os nomes na lista aparecem em multiplos de 4, ex joao é 0 maria é 3, andou 4 
                   # casas então proximo nome vai estar na posição 7 pq andou 4 casas
        nomes.append(notas_turma[i])  # adiciona o nome da pessoa na lista nomes
    else:
        notas_juntas.append(notas_turma[i]) # adiciona a nota na lista notas_juntas

notas = []

for i in range(0, len(notas_juntas), 3): # esse for comça em 0 e vai até a quantidade de itens na lista notas_juntas, e pula de 3 em 3 casas
    notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]]) # adicona as notas por aluno em uma lista ex, as notas do joao são 
    # 8  9 10, poem essas tres notas em uma lista e poem essa lista dentro da lista notas, são tres porque cada aluno tem 3 notas, se tivessem
    # 4 notas seria 4 notas e pularia quantro casas

print(notas[0][2]) # em listas de listas para acessar uma lista dentro de outra lista usa se o [] para a posição da primeira lista e [] para a posição
# do item na lista, estrutura hierarquica se fossem 3 lisas para oque tem na terceira lista usaria [][][]
"""

# Listas de tuplas

# Nesta nova demanda, precisamos gerar uma lista de tuplas com os nomes dos estudantes e o código ID de cada um para a plataforma de análise dos dados. 
# A criação do código consiste em concatenar a primeira letra do nome do estudante a um número aleatório de 0 a 999. Os dados recebidos correspondem 
# a uma lista dos nomes de cada estudante.
"""
from random import randint # o randint escolhe do primero ao ultimo numero incluso

estudantes = ['João', 'Maria', 'José', 'Cláudia', 'Ana']

# gera um numero aleatorio de 0 a 999
def gera_codigo():
    return str(randint(0,999))

codigo_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo())) #adiciona uma tupla contendo nome e codigo do aluno a lista codigo_estudantes

print(codigo_estudantes)
"""

# List comprehension

# Forma simples de criar uma lista seguindo um padrão
# forma padrao [expressão for item in lista]

# Recebemos a demanda de criar uma lista com as médias dos estudantes da lista de listas que criamos na Situação 6. Lembrando que cada lista da 
# lista de listas possui as três notas de cada estudante.
"""
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float: # recebe como argumento uma lista, caso não passe nada e seja chama recebe como padrao uma lisat com 0, 
    #essa função vai retorna um valor em float
    ''' 
    Função para calcular a média de notas passadas por uma lista
    lista: list, default [0]
        Lista com as notas para calcular a média
    return = calculo: float
        Média calculada
    '''
    calculo = sum(lista) / len(lista)

    return calculo

        #[|     expressão     | for item in lista]
medias = [round(media(nota),1) for nota in notas]
print(medias)
"""

#Agora, precisamos utilizar as médias calculadas no exemplo anterior, pareando com o nome dos estudantes. Isto será necessário para 
#gerar uma lista que selecione aqueles estudantes que possuam uma média final maior ou igual a 8 para concorrer a uma bolsa para 
#o próximo ano letivo.
#Os dados recebidos correspondem a uma lista de tuplas com os nomes e códigos dos estudantes e a lista de médias calculadas logo acima.
"""
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# Gerando a lista de nomes (extraindoda tupla)
    #[expressão  for item in lista]
nomes = [nome[0] for nome in nomes] # gera uma lisat só com nomes

# 
estudantes = list(zip(nomes, medias)) # zip retorna um arquivo zip contedno cada elemento pareado das duas listas ou tuplas
# se não trasnformar em lista não é possivel ler o arquivo
# saida = [('João', 9.0), ('Maria', 7.3), ('José', 5.8), ('Cláudia', 6.7), ('Ana', 8.5)]

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
print(candidatos)
"""

# List comprehension com if-else









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
nomes = [nome[0] for nome in nomes] # gera uma lista só com nomes


estudantes = list(zip(nomes, medias)) # zip retorna um arquivo zip contedno cada elemento pareado das duas listas ou tuplas
# se não trasnformar em lista não é possivel ler o arquivo
# saida = [('João', 9.0), ('Maria', 7.3), ('José', 5.8), ('Cláudia', 6.7), ('Ana', 8.5)]

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
print(candidatos)
"""

# List comprehension com if-else

#Recebemos duas demandas a respeito desse projeto com as notas dos estudantes:
#Criar uma lista da situação dos estudantes em que caso sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso 
#contrário receberá o valor "Reprovado".
#Gerar uma lista de listas com:
#Lista de tuplas com o nome dos estudantes e seus códigos.
#Lista de listas com as notas de cada estudante.
#Lista com as médias de cada estudante.
#Lista da situação dos estudantes de acordo com as médias.
#Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (nomes, notas, medias).

#[resultado_if if cond else resultado_else for item in lista]
"""
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

#         resultado_if if    cond    else resultado_else for item in lista]
situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]

cadastro = [x for x in [nomes, notas, medias, situacao]] # coloca as listas passadas dentro da lista cadastro
lista_completa = [nomes, notas, medias, situacao] # faz a mesma coisa que cadastro faz só que mais simples
"""

#Dict comprehension

#Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos na Situação 10 para 
#passá-la à pessoa responsável por construir as tabelas, possibilitando a análise dos dados.
#As chaves do nosso dicionário serão as colunas identificando o tipo de dado.
#Os valores serão as listas com os dados correspondentes àquela chave.

#{chave: valor for item in lista}

"""
lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Media Final", "Situação"]

#          { chave   :       valor           for item in lista}
cadastro = {coluna[i]: lista_completa[i + 1] for i in range(len(coluna))}
# saida: retorna um dicionario com 3 item cadda chave contedno uma listas com as informações passadas, a chave notas vai ter a lista com as notas
# a chave media final contem um alisat com as medias e a chave situação contem uma lista com as situações

#                       [exp for item in lista]
cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
#cria uma chave estudante no dicionario cadastro e essa chave vai armazenar os nomes dos estudantes, que serão extraidos da lista_completa sendo selecionados 
# dessa forma lista_completa[0] escolhe a primeira lisat que é a lisat que contem os nomes em tuplas, [i] escolhe qual tupla vei ver por vez, [0] pega só o nome
# da tupla, resumidamente entra lista, entra na tulpa, pega só o nome [0][i][0]
"""


# Exercicios


# 1.  Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

"""
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

for lista in lista_de_listas:
    print(sum(lista))
"""

# 2.Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

"""
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista_peso = []

for tupla in lista_de_tuplas:
    lista_peso.append(tupla[2])

print(lista_peso)
"""

# 3.crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na 
# lista original e o segundo elemento sendo o próprio nome.
"""
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_de_tuplas = []

for posicao in range(len(lista)):
    lista_de_tuplas.append((posicao, lista[posicao]))

print(lista_de_tuplas)

"""

# 4.Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento 
# seja 'Apartamento', a partir da seguinte lista de tuplas:
"""
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

lista_de_apartamentos = []
#        tupla[1] indica qual elemento vai ser armazenado na lista, 
lista = [tupla[1] for tupla in aluguel if tupla[0]== 'Apartamento']

print(lista)
"""

# 5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista
"""
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

#                 {chave   : valor      for item in lista}
despesas_mensal = {meses[i]: despesa[i] for i in range(len(meses))}
print(despesas_mensal)
"""

# 6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente 
# os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores 
# de venda para que você ajude a realizar a filtragem dos dados a partir de um código:
"""
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), 
          ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

ano_2022 = [tupla[1] for tupla in vendas if tupla[0] == '2022' and tupla[1] > 6000]

print(ano_2022)
"""

# 7.Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da 
# seguinte maneira:
# Glicose igual ou inferior a 70: 'Hipoglicemia'
# Glicose entre 70 a 99: 'Normal'
# Glicose entre 100 e 125: 'Alterada'
# Glicose superior a 125: 'Diabetes'
# A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o 
# valor da glicemia em cada tupla.
"""
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

#                  resultado_if if    cond    else resultado_else e oque o else faz for item in lista
rotulos = [('Hipoglicemia', glicose) if glicose <= 70 
                else ('Normal', glicose) if glicose < 100 
                    else ('Alterada', glicose) if glicose < 125 
                        else ('Diabetes', glicose) 
            for glicose in glicemia]
print(rotulos)
"""

# 8.Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:
# O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a 
# quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 
# 'preco' e 'total'.
#Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.
"""
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

lista_de_tuplas = [('ID', 'QUANTIDADE','PREÇO', 'TOTAL')]
lista_de_tuplas += [(id[i], quantidade[i], preco[i], quantidade[i] * preco[i]) for i in range(len(id))]

for i in lista_de_tuplas:
    print(i)
"""

# 9.Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais 
# há uma coluna contendo a informação de qual é o Estado a que pertence:
# A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor 
# gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.
# A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome 
# de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 
           'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']



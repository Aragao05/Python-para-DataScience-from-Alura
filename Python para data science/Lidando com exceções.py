"""
Tipos de erros 

SyntaxError: ocorre quando por exemplo esquecemos de colocar um ')' ou um '"' ou ':'.

NameError: ocorre quando tentamos usar um nome que não foi criado tipo chamar a lista 'abelha'
sendo que não existe lista 'abelha'.

IndexError: aparece quando tentamos acessar um elento de uma lista que não existe ex
lista[1,2,3]  mostrar lista[4], vai dar erro porque lista na posição 4 não existe 

TypeError: aparece audno tentamos por exemplos somar uma string com inteiro

KeyError: aparece quando tentamos acessa ruma chave que não existe no dicionario 


Try:
    # codigo a ser executado. Caso uma exeçção seja lançada, pare imediatamente
exept <nome_da_exeção as e>:
    # Se uma exeção for lançada no try, rode esse codigo, senão pule essa etapa
"""

#Tratando exceções

# Situação
# Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de determinado(a) estudante. 
# Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) 
# na turma", e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante. Vamos trabalhar nesse exemplo com a exceção 
# Key Error que interromperá o processo desse pedaço do código. Vamos testar esse tratamento?
"""
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 
        'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try: # oque voce vai fazer
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError: # se oque fez deu o erro KeyError exibe ou faça isso
    print("Estudante não matriculado(a) na turma")
else: # se não deu erro faça isso
    print(resultado)
finally: # vai fazer sempre, se tiver erro ou não
    print("A consulta foi encerrada!")
"""


# Raise

# voce cria uma exeção para algum erro que não queira que aconteça
# raise ValueError("A lista de notas deve possuir dez elementos")

# Situação
# Você criou uma função para calcular a média de um estudante em uma dada matéria passando em uma lista as notas deste estudante. 
# Você pretende tratar 2 situações:
# Se a lista possuir um valor não numérico o cálculo de média não serà executado e uma mensagem de "Não foi possível calcular a média 
# do(a) estudante. Só são aceitos valores numéricos!" será exibida.
# Caso a lista tenha mais de 4 notas, será lançada uma exceção do tipo ValueError informando que "A lista não pode possuir mais de 4 notas."
# Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada. 
"""
def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas.")
    
    return calculo

try:
    #notas = [6, 7, 8, 9, 10]  # da o erro criado a lista tem mais de 4 valores 
    notas = [6, 7, 8, "9"]
    resultado = media(notas)
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")
"""

# Exercicios

# 1.


















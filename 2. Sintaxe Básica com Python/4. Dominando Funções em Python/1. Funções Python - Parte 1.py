"""
## Funções - Parte 1

É um bloco de código com parâmetros pré configurados e que podem ou não ter valores padrões.  
Possui um conjunto e entradas e outro conjunto de saídas.  
Normalmente utilizado em tarefas repetitivas, evitando reescrever o mesmo código várias vezes.
"""

"""
## Primeiras funções
"""

def ola_mundo():
    print('Olá, Mundo!')

def boas_vindas(nome):
    print(f"{nome}, bem-vindo ao Curso de Python!")

def saudacao(nome="Tiago"):
    print(f"Olá, {nome}!")
ola_mundo()
boas_vindas("Tiago")
saudacao()
saudacao("Fulano")
"""
## Retorno de valores
As funções def podem retornar diretamente os valores do parâmetros processados.
"""

def calcular_total(numeros):
    return sum(numeros)
print(calcular_total([10, 20, 30, 40, 50]))

def retorna_sucessor_antecessor(numero):
    return numero + 1, numero - 1

print(retorna_sucessor_antecessor(10))  # o retorno é uma tupla, pois o resultado é composto por mais de um valor

"""
## Argumentos Nomeados
São argumentos que devem ser passados para parâmetros da função.
"""

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido: Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Placa: {placa}\n\n")

salvar_carro("Fiat", "Uno", 2020, "ABC-1234")
salvar_carro(ano=2022, marca="Volkswagen", modelo="Chevrolet", placa="FEG-8768")

salvar_carro(marca=input("Marca: "), modelo=input("Modelo: "), ano=input("Ano: "), placa=input("Placa: "))

"""
## Args & Kwargs
Quando definidos (*args e **kwars), o método recebe os valores como tupla e dicionário, respectivamente.  
Arg e Kwargs são apenas uma convenção, podendo ser qualquer nomenclatura, desde que usados os sinais precedentes, * e **, respectivamente.
"""

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido: Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Placa: {placa}\n\n")

salvar_carro(**{"marca": "Ford", "modelo": "Ka", "ano": 2021, "placa": "XYZ-9876"})
def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Segunda-feira, 17 de Março de 2025",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.", 
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    author="Tim Peters",
    year=2004
)

"""
# ## Parâmetros somente por posição

Por padrão, os argumentos podem ser passados para um função Python tanto por posição quanto explicitamente pelo nome. 
No entanto, para manter legibilidade, faz sentido o dev visualizar apenas a definição da função para determinar os itens passados: 
por posição, posição e nome, ou por nome.
"""

"""
Posição apenas
"""
def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
        print(modelo, ano, placa, marca, motor, combustível)
criar_carro("Palio", 2019, "HFT-4782", marca="Fiat", motor="1.0", combustível="Gasolina")

criar_carro("Ka", 2020, "UOR-4234", "Ford", "1.0", "Alcool")

"""
# ## Objetos de primeira classe
# 
# 
"""

"""
# ## Escopo local e global
# 
# 
"""
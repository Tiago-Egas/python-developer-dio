"""
Old Style %

Formato antigo de interpolação de textos.  
As variáveis precisam estar em ordem e cada tipo de variável tem a sua nomenclatura de substituição.
"""

nome = "Tiago"
idade = 34
profissao = "Programador"
linguagem = "Python"

print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))

"""
Método format
Pouco semelhante ao método anterior devemos apenas informar {} e posteriormente informar a variável correspondente e ainda em ordem.  
"""

dados = {'nome': 'Tiago', 'idade': 34, 'profissao': 'Programador', 'linguagem': 'Python'}

## Evolução dos formatadores de strings

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.'.format(linguagem, profissao, idade, nome))

print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.'.format(linguagem, profissao, idade, nome))

print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(linguagem=linguagem, profissao=profissao, idade=idade, nome=nome))

print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(**dados))

"""
F-Strings
Interpolação mais utilizada e recomendada de se utilizar atualmente.
"""

PI = 3.14159265359

print(f'O valor de PI: {PI:0.2f}')
print(f'O valor de PI: {PI:14.8f}')

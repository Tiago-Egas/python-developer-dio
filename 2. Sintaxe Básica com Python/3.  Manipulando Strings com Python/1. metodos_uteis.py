"""
## Maiúsculo, minúsculo e título
Python, em comparação com outras linguagens, já possui funcionalidades de alterações caracteres.
"""

curso = "CuRso de PyThoN"
print("Maiúsculas:\t", end="")
print(curso.upper())
print("Minúsculas:\t", end="")
print(curso.lower())
print("Capitular:\t", end="")
print(curso.title())

"""
## Eliminando espaços em branco
Também possui limpeza do espaços informados durante digitação do usuário.
"""

curso = "       |Curso de Python|     "
print("Removendo espaços: ")
print("Esquerda:\t", end="")
print((curso.lstrip().center(30, "#")))
print("Direita:\t", end="")
print((curso.rstrip().center(30, "#")))
print("Ambos:\t\t", end="")
print((curso.strip().center(30, "#")))

"""
## Junções e centralizações
Centralização funciona para incluir caracteres no começo e final para alcançarem a quantidade de caracteres informada.  
Junções servem para incluir um caractere entre os caracteres existentes em uma string.
"""

curso = "Curso de Python"
print("Center: ", end="")
print((curso.center(30, "#")).upper())
print("Join: ", end="")
print("|".join(curso.upper()))

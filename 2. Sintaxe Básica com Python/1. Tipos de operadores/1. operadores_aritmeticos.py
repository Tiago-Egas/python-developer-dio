"""
Operadores Aritméticos
Esta aula temos os operadores de cálculos matemáticos básicos e como apresentar eles numa saída diretamente ou através do uso de outra variável.
"""

produto_1 = input("Informe o produto_1:\R= ")
produto_2 = input("Informe o produto_2:\nR= ")
prod1 = float(produto_1)
prod2 = float(produto_2)
print("")
print("Operações Básicas: ")
print(f"{prod1} + {prod2} = ", prod1 + prod2)
print(f"{prod1} - {prod2} = ", prod1 - prod2)
print(f"{prod1} / {prod2} = ", prod1 / prod2)
print(f"{prod1} // {prod2} = ", prod1 // prod2)
print(f"{prod1} * {prod2} = ", prod1 * prod2)
print(f"{prod1} % {prod2} = ", prod1 % prod2)
print(f"{prod1} ** {prod2} = ", prod1 ** prod2)

# Ordem das expressões, forçar com uso de parênteses

print("")
expressao_1 = (prod1 + prod1) * prod2
expressao_2 = (prod1 / prod2) + prod2 * ((prod1 - prod1) ** prod2)
print("Expressões: ")
print(f"(produto_1 + produto_1) * produto_2 = {expressao_1}")
print(f"(produto_1 / produto_2) + produto_2 * ((produto_1 - produto_1) ** produto_2) = {expressao_2}")

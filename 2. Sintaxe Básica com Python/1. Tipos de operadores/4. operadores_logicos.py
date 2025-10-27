"""
Operadores Lógicos
Nesta aula operamos os tipos de comparações entre textos e valores.
"""

print("Tabela verdade AND:")
print('Verdadeiro and Verdadeiro = ', True and True)
print('Verdadeiro and Falso = ', True and False)
print('Falso and Verdadeiro = ', False and True)
print('Falso and Falso = ', False and False)

print("Tabela verdade OR:")
print('Verdadeiro or Verdadeiro = ', True or True)
print('Verdadeiro or Falso = ', True or False)
print('Falso or Verdadeiro = ', False or True)
print('Falso or Falso = ', False or False)

print("Tabela verdade NOT:")
print('not (Verdadeiro or Verdadeiro) = ', not (True and True))
print('not (Verdadeiro or Falso) = ', not (True or False))
print('not (Falso or Verdadeiro) = ', not (False or True))
print('not (Falso or Falso) = ', not (False or False))

print("Tabela verdade XOR:")
print('Verdadeiro or Verdadeiro = ', True ^ True)
print('Verdadeiro ^ Falso = ', True ^ False)
print('Falso ^ Verdadeiro = ', False ^ True)
print('Falso ^ Falso = ', False ^ False)

saldo, saque, limite, conta_especial = (1000, 200, 100, True)
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
conta_especial_com_saldo_suficiente = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print("")
print("Conta normal com saldo = ", conta_normal_com_saldo_suficiente)
print("Conta especial com saldo = ", conta_especial_com_saldo_suficiente)

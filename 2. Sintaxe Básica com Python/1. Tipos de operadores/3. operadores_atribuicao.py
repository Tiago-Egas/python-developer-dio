"""
Operadores de atribuição
Nesta aula vimos como atribuir valores conforme os tipos de operadores.
Os mesmos operadores aritméticos podem ser usados aqui.
"""

print("\tExtrato bancário\t")
print("##################################\n")
saldo = 6000
print(f"Saldo inicial: \t...\t... {saldo}")
saldo += 400
print(f"Transferência: \t...\t... {saldo}")
saldo -= 100
print(f"Multa atraso: \t...\t... {saldo}")
saldo *= 2
print(f"Rend. Bitcoin: \t...\t... {saldo}")
saldo /= 1.2
print(f"Imp. de Renda: \t...\t... {saldo}")
saldo //= 2
print(f"Transferência: \t...\t... {saldo}")
saldo *= 2
print(f"Pagamento PIX: \t...\t... {saldo}")
saldo **= 1.2
print(f"Investimentos: \t...\t... {saldo}")
print("##################################\n")
print(f"Saldo Final: \t...\t... {saldo}")

# 'is' e 'is not' são verificadores de local

saldo, limite = (1000, 500)
print(saldo is limite)
print(saldo is not limite)
saldo, limite = (1000, 1000)
print(saldo is limite)
print(saldo is not limite)

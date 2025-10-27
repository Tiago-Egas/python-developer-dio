"""
Indentação e Blocos
Nesta aula nós vimos uma melhor forma de como o Python interpreta o código escrito e como ele afeta a execução.
"""

valor = float(input("Informe o valor: "))
saldo = float(input("Informe o saldo: "))
def sacar(valor):
    valor_saque = valor
    saldo_saque = saldo
    if saldo_saque >= valor_saque:
        print("Saldo maior que o valor.\nSaque liberado!")
    if saldo_saque < valor_saque:
        print("Saldo menor que o valor de saque!")
    print(f"Seu saldo atual é: {saldo_saque}!\n\n")
    print(f"Saldo = {saldo_saque}\t|\tValor = {valor_saque}\n\n")
def depositar(valor):
    saldo_deposito = saldo
    valor_deposito = valor
    if saldo_deposito > valor_deposito:
        saldo_deposito += valor_deposito
        print(f"{valor_deposito} foi depositado!")
    print(f"Seu saldo atual é: {saldo_deposito}!\n\n")
    print(f"Saldo = {saldo}\t|\tValor = {valor_deposito}\n\n")
print("DEPOSITANDO\n...\n...")
sacar(valor)
print("SACANDO\n...\n...")
depositar(valor)
print("\n\nObrigado por ser nosso cliente, tenha um bom dia!\n\n")

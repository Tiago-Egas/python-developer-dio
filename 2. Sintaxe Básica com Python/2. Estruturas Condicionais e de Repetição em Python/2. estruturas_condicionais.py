"""
Estruturas Condicionais
Nesta aula vimos como validar informações em variáveis utilizando os operadores de comparação para o programa identificar qual caminho o programa deve seguir para sua próxima execução.
"""

"""
## IF comum
forma mais recomendada para validar informações em grandes aplicações
"""

MAIOR_IDADE = 18
print("Validação da idade para habilitar com CNH")
idade = int(input("Informe a sua idade:"))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH!")

"""
## If / Else
Utilizável quando a validação pode ser classificada como "ou um, ou outro"
"""

saldo = 2000
saque = float(input("Informe o valor do saque: "))
if saldo >= saque:
    print("Saldo maior que saque!")
else:
    print("Saldo insuficiente!")

"""
## IF aninhado (If, Elif e Else)
Recomendável de utilizar quando a validação precisa ser precisa na classificação dos dados.  
Cada ocorrência de ELIF será uma validação apropriada para a classificação do dado validado.
"""

import sys
opcao = int(input("Informe uma opção: \n\t[1] Sacar\n\t[2] Exibir saldo.\n"))
saldo = float(2900)
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        print(f"Saque realizado!\nSaldo atual: {saldo}")
elif opcao == 2:
    print("Exibindo extrato...")
    if saldo == 0:
        print("Saldo zerado!")
    elif saldo < 0:
        print(f"Saldo Negativo: {saldo}!")
    else:
        print(f"Seu saldo atual é: {saldo}")
else:
    sys.exit("Opção inválida!")
print("\n\nObrigado por confiar nos nossos serviços!\nVolte sempre!")

conta_normal = False
conta_universitária = False
saldo = 2000
saque = 2200
cheque_especial = 450
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial!")
    else:
        print("Não foi possível realizar o saque!")
elif conta_universitária:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("\n\nSistema não identificou o seu tipo de conta.\nEntre em contato com seu gerente!")

"""
# IF Ternário
Funcionalidade similar ao IF/Else, mas escrito de forma compacta.
Mais utilizado para validações simples e curtas.
"""

saldo = 3000
saque = 2500
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

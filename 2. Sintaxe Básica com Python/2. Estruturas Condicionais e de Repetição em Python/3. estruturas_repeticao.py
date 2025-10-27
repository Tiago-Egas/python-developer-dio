"""
Estruturas de Repetição
Nesta aula aprendemos como realizar repetições e blocos de código.  
As repetições são determinadas conforme cada estrutura, sendo definida ou de forma lógica.
"""

"""
## For
Recomendável quando sabemos a quantidade de itens iteráveis dentro da sequência.
"""

texto = "the crazy dog jumps over the lazy fox"
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()
print("Executa no fim do programa.")

"""
## For / Else
Não muito comum no dia dia, mas é uma escrita mais formal da última execução.
"""

texto = "the crazy dog jumps over the lazy fox"
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no fim do programa.")

"""
## Range
Função imbuída no interpretador Python usada para produzir sequência de números com início e fim delimitados.  
Possui 3 argumentos principais: stop, start e step
"""

for numero in range(1,11):
    print(numero, end="\t")

for numero in range(0,51, 5):
    print(numero, end="\t")

"""
## While
Esta repetição é utilizada quando não temos certeza da quantidade e vezes fixas que o código será executada.  
Melhor utilizada quando há uma validação lógica de quando o usuário está preparado para sair da aplicação.
"""

opcao = 1
while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\nEscolha: "))
    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

"""
## While / Else
Executa da mesma forma que o while, mas com a mesma funcionalidade de execução do fot/else
"""

opcao = 1
while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\nEscolha: "))
    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

"""
## Break e Continue
Duas palavras reservadas específicas para as estruturas de repetição.  
Break faz uma saída do sistema.  
Continue faz passada do iterador atual para evitar algum tipo validação específica.
"""

while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    print(numero, end=" ")

for numero in range(100):
    if not (numero % 2 == 0):
        continue
    if numero == 10:
        break
    print(numero, end=" ")

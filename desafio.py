#Desafio: Sistema bancário
#Operações de saque, depósito e visualização de extrato

menu = """
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

=> """

saldo = 0
limite = 500 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        if valor > 0:
           
           if valor > saldo:
            print("Saldo insuficiente.")

           elif numero_saques >= LIMITE_SAQUES:
            print("Ultrapassado o limite de saques, tente novamente amanhã.")

           elif valor > limite:
            print("O valor limite para saques é de R$ 500,00")

           else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
           print("Digite um valor positivo")

    elif opcao == "e":
        visualizar_extrato = " Extrato "
        print(visualizar_extrato.center(60,"#"))
        print("\n")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
        print("############################################################")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Digite uma das opções a seguir:")
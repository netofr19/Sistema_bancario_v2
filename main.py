from functions import *
import time

saldo = 0
limite = 500
lista_extrato = []
usuarios = []
lista_cpf = []
contas = []
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
numero_conta = 1

while True:

    opcao = menu()
    opcao = opcao.lower()
    
    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))

        saldo, extrato = deposito(valor, saldo)
        if extrato:
            lista_extrato.append(extrato)
    
    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))

        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            valor=valor,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
        if extrato:
            lista_extrato.append(extrato)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=lista_extrato)

    elif opcao == "nu":
        usuarios, lista_cpf = criar_usuario(usuarios, lista_cpf)

    elif opcao == "nc":
        conta = criar_conta(AGENCIA, numero_conta, usuarios, lista_cpf)

        if conta:
            contas.append(conta)
            numero_conta += 1
    
    elif opcao == "lc":
        if len(contas) > 0:
            listar_contas(contas)
        else:
            print("Não existem contas cadastradas!")
            time.sleep(2)

    elif opcao == "q":
        break

    else:
        print("Opção Inválida! Por favor, selecione uma opção válida!")
        time.sleep(2)

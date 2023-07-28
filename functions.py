import time
# Arquivo de funções

# Função do menu
def menu():
    menu = """
    Sistema Bancário
    --------------------------
    Menu de opções
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuario
    [q] Sair
    --------------------------
    """
    print(menu)
    return input("Por favor, digite uma opção: ")

def deposito(valor: float, saldo: float, /):
    """Função que realiza a operação de depósito, os parâmetros de entrada são valor e saldo e os parâmetros de saída são
    o saldo atualizado e o extrato na forma de string
    """
    extrato = ""
    if valor > 0:
        saldo += valor
        extrato = (f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
        time.sleep(2)
    else:
        print("Operação não autorizada! O valor informado é inválido.")
        time.sleep(2)
    return saldo, extrato

def saque(*, saldo: float, valor: float, limite: float, numero_saques: int, limite_saques: int):
    """Função que realiza a operação de saque. Os parâmetros de entrada são o saldo do usuário, o valor a ser sacado, o valor 
    limite para saques, o número de saques já realizados e o limite de saques diários. Como parâmetro de saída, terá o saldo e
    o número de saques atualizados e o extrato em forma de string para ser impresso na tela"""
    extrato = ""
    if valor > 0:
        if valor <= saldo:
            if valor <= limite:
                if numero_saques < limite_saques:
                    saldo -= valor
                    numero_saques += 1
                    extrato = f"Saque: R$ {valor:.2f}"
                    print("Saque realizado com sucesso!")
                    time.sleep(2)
                else:
                    print("Operação não autorizada! Número máximo de saques atingido.")
                    time.sleep(2)
            else:
                print("Operação não autorizada! O valor solicitado excede o limite de saque.")
                time.sleep(2)
        else:
            print("Operação não autorizada! Não há saldo suficiente para o saque.")
            time.sleep(2)
    else:
        print("Operação não autorizada! O valor informado é inválido.")
        time.sleep(2)
    return saldo, extrato, numero_saques

def exibir_extrato(saldo: float, /, *, extrato: list):
    """A função irá exibir o extrato em tela, primeiramente irá exibir todas as movimentações realizadas em ordem de realização, em
    seguida irá exibir o saldo atualizado. Os parâmetros de entrada são o saldo atual e a lista de movimentações realizadas. Esta 
    função tem como objetivo apenas imprimir em tela as informações, não tendo qualquer retorno"""
    print("-------------- Extrato -------------")
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
        time.sleep(2)
    else:
        for i, j in enumerate(extrato):
            print(f"Operação {i+1} - {j}")
            time.sleep(1)
    print(f"SALDO: R$ {saldo:.2f}")
    print("\n")
    time.sleep(2)
        
def criar_usuario(usuarios: list, lista_cpf: list):
    """A função tem como objetivo a criação de um registro de usuário a partir dos dados inseridos pelo usuário. Os parâmetros de
    entrada são a lista de usuários já existentes e a lista de cpf's já cadastrados e irá retornar como parâmetros de saída as mesmas
    listas atualizadas"""
    cpf = input("Informe o CPF (apenas numeros): ")

    if cpf in lista_cpf:
        print("Já existe usuário com este cpf.")
    elif cpf not in lista_cpf:
        lista_cpf.append(cpf)
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("--------- Usuário criado com sucesso! ----------")
        time.sleep(2)

        return usuarios, lista_cpf
    
def filtrar_usuario(usuarios: list, cpf: int):
    """A função tem como objetivo apenas verificar se na lista de usuários, existe algum usuário cadastrado com o cpf mencionado.
    Caso exista tal usuário, a função irá retornar o nome desse usuário."""
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario["nome"]
        return None

def criar_conta(agencia: str, numero_conta: int, usuarios: list, lista_cpf: list):
    """Função que tem como objetivo a criação de uma conta corrente a partir da existência de um cadastro de usuário para o cpf
    mencionado. Caso exista o cadastro de usuário, a função irá retornar um dicionário com as informações da conta-corrente"""
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        print("------ Conta criada com sucesso! ------")
        time.sleep(2)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("--- Usuário não encontrado! Fluxo de criação de conta encerrado! ---")
        time.sleep(2)

def listar_contas(contas: list):
    """A função tem como objetivo listar todas as contas que estão registradas no sistema a partir da lista de dicionários gerada
    pela criação de contas-corrente"""
    for i, conta in enumerate(contas):
        print(f"CONTA {i+1} = Usuário: {conta['usuario']} - Agência: {conta['agencia']} - Conta-Corrente: {conta['numero_conta']}")
        time.sleep(1)


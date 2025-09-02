def menu():
    menu = """\n
    =============== EXTRATO ================
    [d] Depósito
    [s] Saque
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Conta
    [nu] Novo Usuário
    [q] Sair

    -> """

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósitado: R$ {valor:.2f}\n'
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação não concluida! O valor informado é inválido. ")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação Falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação Falhou! Número máximo de saques atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque efetuado com sucesso!")

    else:
        print("Operação falhou! O valor informado está inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=" * 40)

def criar_usuário(usuarios):
    cpf = int(input("Informe o CPF: "))
    usuario = filtrar_usuário(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF! ")
        return
    
    nome = input("Informe nome Completo: ")
    data_nascimento = int(input("Informe a data de nascimento (dd-mm-aaaa): "))
    endereço = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print(" Usuário criado com sucesso! ")

def filtrar_usuário(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF do Usuário: "))
    usuario = filtrar_usuário(cpf, usuarios)

    if usuario:
        print(" Conta Criada com Sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrador, fluxo de criação de conta encerrado! ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        #print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
    
        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Infomr o valor desejado para sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,

            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuário(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
                    
main()

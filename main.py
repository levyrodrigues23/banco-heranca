# main.py
from banco import Banco
from bancoLista import BancoLista

def _criar_banco(bancos: BancoLista):
    nome_banco = input("Digite o nome do novo banco: ")
    agencia_banco = input("Digite a agência do novo banco: ")
    novo_banco = Banco(nome_banco, agencia_banco)
    if bancos.adicionar_banco(novo_banco):
        print(f"Banco '{nome_banco} - {agencia_banco}' criado com sucesso!")
    else:
        print("Erro: Já existe um banco com este nome e agência.")

def _criar_conta(bancos: BancoLista):
    if not bancos.bancos:
        print("Nenhum banco cadastrado. Crie um banco primeiro.")
        return

    bancos.listar_bancos()
    nome_banco = input("Nome do banco onde deseja criar a conta: ")
    agencia_banco = input("Agência do banco: ")
    banco = bancos.buscar_banco(nome_banco, agencia_banco)

    if not banco:
        print("Banco não encontrado.")
        return

    try:
        numero = int(input("Número da nova conta: "))
        if banco.buscar_conta(numero):
            print("Erro: Já existe uma conta com este número neste banco.")
            return
            
        cliente = input("Nome do cliente: ")
        saldo = float(input("Saldo inicial: R$ "))
        
        print("\nTipo de Conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        print("3 - Conta Investimento")
        tipo_conta = input("Escolha o tipo de conta (1/2/3): ")

        if tipo_conta == "1":
            limite = float(input("Limite do cheque especial: R$ "))
            banco.criar_conta_corrente(numero, cliente, saldo, limite)
        elif tipo_conta == "2":
            banco.criar_conta_poupanca(numero, cliente, saldo)
        elif tipo_conta == "3":
            banco.criar_conta_investimento(numero, cliente, saldo)
        else:
            print("Tipo de conta inválido.")
            return
        
        print(f"Conta {numero} criada com sucesso para {cliente} no banco {banco.nome}.")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para os valores monetários.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar a conta: {e}")

def _listar_contas(bancos: BancoLista):
    nome = input("Nome do banco: ")
    agencia = input("Agência: ")
    banco = bancos.buscar_banco(nome, agencia)
    if banco:
        banco.listar_contas()
    else:
        print("Banco não encontrado.")

def _operar_saque(bancos: BancoLista):
    nome = input("Nome do banco: ")
    agencia = input("Agência: ")
    banco = bancos.buscar_banco(nome, agencia)
    if not banco:
        print("Banco não encontrado.")
        return

    try:
        numero = int(input("Número da conta: "))
        valor = float(input("Valor do saque: R$ "))
        banco.sacar_conta(numero, valor)
    except ValueError:
        print("Entrada inválida para número da conta ou valor.")

def _operar_transferencia(bancos: BancoLista):
    nome = input("Nome do banco: ")
    agencia = input("Agência: ")
    banco = bancos.buscar_banco(nome, agencia)
    if not banco:
        print("Banco não encontrado.")
        return

    try:
        num_origem = int(input("Número da conta de origem: "))
        num_destino = int(input("Número da conta de destino: "))
        valor = float(input("Valor da transferência: R$ "))
        banco.transferir_conta(num_origem, num_destino, valor)
    except ValueError:
        print("Entrada inválida para número da conta ou valor.")

def menu():
    bancos = BancoLista()
    # Adiciona um banco inicial para facilitar testes
    bancos.adicionar_banco(Banco("Banco UFC", "0001"))

    while True:
        print("\n=== MENU BANCO HERANÇA ===")
        print("1 - Criar Banco")
        print("2 - Criar Conta em um Banco")
        print("3 - Listar Bancos")
        print("4 - Listar Contas de um Banco")
        print("5 - Realizar Saque")
        print("6 - Realizar Transferência")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            _criar_banco(bancos)
        elif opcao == "2":
            _criar_conta(bancos)
        elif opcao == "3":
            bancos.listar_bancos()
        elif opcao == "4":
            _listar_contas(bancos)
        elif opcao == "5":
            _operar_saque(bancos)
        elif opcao == "6":
            _operar_transferencia(bancos)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
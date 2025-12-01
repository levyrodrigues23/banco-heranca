from contas import ContaCorrente, ContaPoupanca, ContaInvestimento, Conta
from bancoLista import BancoLista

def main():
    while True:
        print("\n Sistema Bancario\n")
        print("1. Cadastrar Banco")
        print("2. Cadastrar Conta")
        print("3. Listar Bancos")
        print("4. Total de Contas")
        print("5. Total de Bancos")
        print("6. Sair")
        escolha = input("escolha uma opção: ")
        banco_lista = BancoLista()
        if escolha == "1":
            nome_banco = input("digite o nome do banco a ser cadastrado: ")
            banco_lista.cadastrar_banco(nome_banco)
        elif escolha == "2":
            tipo_conta = input("digite o tipo de conta (corrente/poupanca/investimento): ").lower()
            numero = input("digite o número da conta: ")
            banco = input("digite o nome do banco: ")
            saldo = float(input("digite o saldo inicial: "))
            if tipo_conta == "corrente":
                limite = float(input("digite o limite do cheque especial: "))
                conta = ContaCorrente(numero, banco, saldo, limite)
            elif tipo_conta == "poupanca":
                taxa_juros = float(input("digite a taxa de juros (%): "))
                conta = ContaPoupanca(numero, banco, saldo, taxa_juros)
            elif tipo_conta == "investimento":
                tipo_investimento = input("digite o tipo de investimento: ")
                conta = ContaInvestimento(numero, banco, saldo, tipo_investimento)
            else:
                print("tipo de conta inválido.")
                continue
            banco_lista.cadastrar_conta(conta)
        elif escolha == "3":
            banco_lista.get_banco()
        elif escolha == "4":
            banco_lista.get_total_contas()
        elif escolha == "5":
            banco_lista.get_total_bancos()
        elif escolha == "6":
            print("saindo do sistema bancario, obrigado por usar.")
            break
        else:
            print("opção invalida, tende novamente.")
        

if __name__ == "__main__":
    main()

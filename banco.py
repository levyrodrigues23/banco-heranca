# banco.py
from contas import Conta, ContaCorrente, ContaPoupanca, ContaInvestimento

class Banco:
    def __init__(self, nome, agencia):
        self._nome = nome
        self._agencia = agencia
        self._contas = []

    @property
    def nome(self):
        return self._nome

    @property
    def agencia(self):
        return self._agencia

    @property
    def contas(self):
        return self._contas

    def criar_conta_corrente(self, numero, cliente, saldo=0.0, limite=500.0):
        conta = ContaCorrente(numero, cliente, saldo, limite)
        self._contas.append(conta)
        return conta

    def criar_conta_poupanca(self, numero, cliente, saldo=0.0):
        conta = ContaPoupanca(numero, cliente, saldo)
        self._contas.append(conta)
        return conta

    def criar_conta_investimento(self, numero, cliente, saldo=0.0):
        conta = ContaInvestimento(numero, cliente, saldo)
        self._contas.append(conta)
        return conta

    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        return None

    def listar_contas(self):
        print(f"\n=== Contas do banco {self._nome} / Agência {self._agencia} ===")
        for conta in self._contas:
            print(conta.detalhes())

    def sacar_conta(self, numero, valor):
        conta = self.buscar_conta(numero)
        if not conta:
            print("Conta não encontrada.")
            return

        print(f"\nTentando sacar R$ {valor:.2f} de {conta.cliente} ({type(conta).__name__})")
        print("Antes:", conta.detalhes())
        ok = conta.sacar(valor)
        if ok:
            print("Saque realizado com sucesso.")
        print("Depois:", conta.detalhes())

    def transferir_conta(self, num_origem, num_destino, valor):
        conta_origem = self.buscar_conta(num_origem)
        conta_destino = self.buscar_conta(num_destino)

        if not conta_origem or not conta_destino:
            print("Conta de origem ou destino não encontrada.")
            return

        print(f"\nTransferindo R$ {valor:.2f} de {conta_origem.cliente} para {conta_destino.cliente}")
        print("Antes:", conta_origem.detalhes(), "|", conta_destino.detalhes())

        if not conta_origem.sacar(valor):
            print("Transferência falhou: saldo insuficiente na origem.")
            return

      
        conta_destino.depositar(valor)
        
        print("Transferência realizada com sucesso.")
        print("Depois:", conta_origem.detalhes(), "|", conta_destino.detalhes())
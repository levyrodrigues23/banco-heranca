# contas.py

class Conta:
    def __init__(self, numero, cliente, saldo=0.0):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito deve ser positivo.")
            return
        self._saldo += valor

    def sacar(self, valor):
        print("Operação de saque não implementada para este tipo de conta.")
        return False

    def detalhes(self):
        return f"Conta {self._numero} - {self._cliente} | Saldo: R$ {self._saldo:.2f}"


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo=0.0, limite=500.0):
        super().__init__(numero, cliente, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor > self._saldo + self._limite:
            print("Saque excede saldo + limite.")
            return False

        self._saldo -= valor
        return True
    
    def detalhes(self):
        detalhes_base = super().detalhes()
        return f"{detalhes_base} | Limite: R$ {self._limite:.2f}"


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente, saldo=0.0):
        super().__init__(numero, cliente, saldo)

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print("Saque excede saldo disponível na poupança.")
            return False

        self._saldo -= valor
        return True


class ContaInvestimento(Conta):
    def __init__(self, numero, cliente, saldo=0.0):
        super().__init__(numero, cliente, saldo)

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print("Saque excede saldo disponível.")
            return False

        self._saldo -= valor
        return True

    def depositar(self, valor):
        """Aplica um bônus de 10% para depósitos/transferências recebidos."""
        if valor <= 0:
            print("Valor de depósito deve ser positivo.")
            return
        
        bonus = valor * 0.10
        valor_total = valor + bonus
        super().depositar(valor_total)
        print(f"Bônus de R$ {bonus:.2f} aplicado para Conta Investimento!")
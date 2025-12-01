class Conta:
    
    def __init__(self, numero, banco, saldo=0.0):
        self._numero = numero
        self._saldo = saldo
        self._banco = banco
        
    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print("voce está com saldo insuficiente!")
    
    def get_saldo(self):
        return self._saldo
    
    
# eu vi num livro que tem um metodo que eu posso usar um decorador property para poder aplicar get e set, desenvolvedores java não vao gostar disso mas é alto como vai ficar abaixo.
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
    
    @property
    def banco(self):
        return self._banco
    
    @banco.setter
    def banco(self, banco):
        self._banco = banco
    
    def encerrar_conta(self):
        self._saldo = 0.0
        print(f"a conta {self._numero} foi encerrada com sucesso!")
        
        
class ContaCorrente(Conta):
    def __init__(self, numero, banco, saldo=0.0, limite=0.0):
        super().__init__(numero, banco, saldo)
        self._limite = limite
    
    def usar_limite(self, valor):
        if valor <= self._limite:
            self._saldo -= valor
            print(f"Você usou {valor} do cheque especial para aplicar no limite")
        else:
            print("sinto muito mas o valor acabou passando o limite permitido.")

class ContaPoupanca(Conta):
    def __init__(self, numero, banco, saldo=0.0, taxa_juros=0.0):
        super().__init__(numero, banco, saldo)
        self._taxa_juros = taxa_juros
        
    def aplicar_juros(self):
        juros = self._saldo * self._taxa_juros / 100
        self._saldo += juros
        print(f"Juros de {juros} aplicados à conta poupança.")
        
class ContaInvestimento(Conta):
    def __init__(self, numero, banco, saldo=0.0, tipo_investimento="Ações"):
        super().__init__(numero, banco, saldo)
        self.tipo_investimento = tipo_investimento
        
    def investir(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"voce investiu {valor} em {self.tipo_investimento}.")
        else:
            print("saldo insuficiente para investir")
        








# bancoLista.py
from banco import Banco

class BancoLista:
    def __init__(self):
        self._bancos = []

    @property
    def bancos(self):
        return self._bancos

    def adicionar_banco(self, banco):
        banco_existente = self.buscar_banco(banco.nome, banco.agencia)
        if banco_existente:
            return False  # Banco já existe
        
        self._bancos.append(banco)
        return True

    def buscar_banco(self, nome, agencia):
        for banco in self._bancos:
            if banco.nome == nome and banco.agencia == agencia:
                return banco
        return None

    def listar_bancos(self):
        print("\n=== Bancos cadastrados ===")
        for banco in self._bancos:
            print(f"- {banco.nome} / Agência {banco.agencia}")
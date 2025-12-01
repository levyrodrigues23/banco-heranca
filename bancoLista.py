from contas import Conta


class BancoLista:
    def __init__(self):
        self._bancos_e_contas = {}
        
    def cadastrar_conta(self, conta: Conta):
        
        nome_banco = conta.banco
        nome_banco = nome_banco.upper()  
    
        if nome_banco in self._bancos_e_contas:  
            
            self._bancos_e_contas[nome_banco].append(conta)  
            print(f"Conta {conta.numero} cadastrada no {nome_banco}.")
        else:
            
            print(f"Erro: O banco '{nome_banco}' não está cadastrado.")
            print("Cadastre o banco primeiro usando cadastrar_banco().")
    
    def cadastrar_banco(self, nome_banco: str):
    
        nome_banco = nome_banco.upper()
        
        
        if nome_banco in self._bancos_e_contas:
            print(f"O banco '{nome_banco}' já está cadastrado.")
        else:
            
            self._bancos_e_contas[nome_banco] = []
            print(f"Banco '{nome_banco}' cadastrado com sucesso!")
            
    def get_total_contas(self):
        if not self._bancos_e_contas:
            print("não há nenhuma conta cadastrada")
            return 0
        total_contas = len(self._bancos_e_contas.values())
        print(f"o total de contas atualmente equivale a {total_contas}")
        return total_contas
        
    def get_total_bancos(self):
        if not self._bancos_e_contas:
            print("não ha nenhum banco cadastrado")
            return 0
        total_bancos = len(self._bancos_e_contas.keys())
        return print(total_bancos)
    
    def get_banco(self):
        if not self._bancos_e_contas:
            print("não tem nada a ser mostrado atualmente")
            return 0
        for i, banco in enumerate(self._bancos_e_contas):
            print(f"{i}.banco: {banco}")
        return banco

    def remover_conta(self, numero):
        conta = self.buscar_conta(numero)
        if conta:
            self._bancos_e_contas.remove(conta)
            print(f"a conta {numero} foi removida com sucesso!")

    def transferir(self, origem, destino, valor):
        conta_origem = self.buscar_conta(origem)
        conta_destino = self.buscar_conta(destino)
        if conta_origem and conta_destino:
            if conta_origem.saldo >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
            else:
                print("Saldo insuficiente na conta de origem!")
        else:
            print("Conta de  origem ou destino não encontrada!")







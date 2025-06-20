
# Constante Global
TAXA_SAQUE = 2.50
class ContaBancaria:
    def __init__(self, titular, saldo = 0): # construtor da classe como fosse a fábrica de vidro
        self.titular = titular  # nome do dono (fixo)
        self.saldo = saldo      # Saldo inicial
        self.historico = []
    
    def depositar(self, valor):  
        self.saldo += valor

    def sacar(self, valor):
        valor_total = valor + TAXA_SAQUE    # Taxa fixa de R$ 2.50 
        if self.saldo >= valor_total:       # Se tiver dinheiro
            self.saldo -= valor_total       # Subtrai do saldo
            return True                     # Saque realizado
        else:
            print("Saldo insuficiente!")    # Aviso
            return False                    # Saque negado
    
    def extrato(self):
        return f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}"
    
    def transferir(self, conta_destino, valor):
        taxa = 1.50 # Taxa fixa por transferência
        valor_total = valor + taxa

        if self.saldo >= valor_total:
            self.saldo -= valor_total
            conta_destino.depositar(valor) # Deposita apenas o valor
            
            self.historico.append(f"Transferência enviada: -R${valor:.2f} (Taxa: R${taxa:.2f})")
            conta_destino.historico.append(f"Transferência recebida: +R${valor:.2f}")
            return True
        else:
            print(f"Saldo insuficiente! Necessário: R${valor_total:.2f}")
            return False
        
    def ver_historico(self):
        print("\Histórico de Operações:")
        for operacao in self.historico:
            print(operacao)

def criar_conta(nome, saldo_inicial=0):
    return ContaBancaria(nome, saldo_inicial)

conta = criar_conta("Fernando", 100) # Usando a função criadora
conta.sacar(20)
print(conta.extrato())

conta2 = criar_conta("Fulano", 50)
conta.transferir(conta2, 30)
conta.ver_historico()
print(conta.extrato())
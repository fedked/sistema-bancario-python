from datetime import datetime

# Constante Global
TAXA_SAQUE = 2.50
class ContaBancaria:
    def __init__(self, titular, saldo = 0): # construtor da classe como fosse a fábrica de vidro
        self.titular = titular  # nome do dono (fixo)
        self.saldo = saldo      # Saldo inicial
        self.historico = []
    
    def depositar(self, valor):  
        self.saldo += valor
        self.historico.append(f"{datetime.now().strftime('Data: %d/%m/%Y - Hora: %H:%M')} | Depósito: +R${valor:.2f}")

    def sacar(self, valor):
        valor_total = valor + TAXA_SAQUE    # Taxa fixa de R$ 2.50 
        if self.saldo >= valor_total:       # Se tiver dinheiro
            self.saldo -= valor_total       # Subtrai do saldo
            self.historico.append(f"{datetime.now().strftime('Data: %d/%m/%Y - Hora: %H:%M')} | Saque -R${valor:.2f} (taxa: R${TAXA_SAQUE:.2f})")
            return True                     # Saque realizado
        else:
            print("Saldo insuficiente!")    # Aviso
            return False                    # Saque negado
    
    def extrato(self):
        return f"\nTitular: {self.titular} | Saldo: R${self.saldo:.2f}"
    
    def transferir(self, conta_destino, valor):
        taxa = 1.50 # Taxa fixa por transferência
        valor_total = valor + taxa

        if self.saldo >= valor_total:
            self.saldo -= valor_total
            conta_destino.depositar(valor) # Deposita apenas o valor
            timestime = datetime.now().strftime('%d/%m/%Y %H:%M')
            self.historico.append(f"{timestime} | Transferência enviada: -R${valor:.2f} (Taxa: R${taxa:.2f})")
            conta_destino.historico.append(f" {timestime} | Transferência recebida: +R${valor:.2f}")
            return True
        else:
            print(f"Saldo insuficiente! Necessário: R${valor_total:.2f}")
            return False
        
    def ver_historico(self):
        print("\nHistórico de Operações:")
        for operacao in self.historico:
            print(operacao)

def criar_conta(nome, saldo_inicial=0):
    return ContaBancaria(nome, saldo_inicial)

conta = criar_conta("Fernando", 100) # Usando a função criadora
conta.sacar(20)
conta.ver_historico()
print(conta.extrato())
print("------------")

conta2 = criar_conta("Fulano", 50)
conta2.sacar(5)
conta2.ver_historico()
print(conta.extrato())
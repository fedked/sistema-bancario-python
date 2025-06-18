
# Constante Global
TAXA_SAQUE = 2.50
class ContaBancaria:
    def __init__(self, titular, saldo = 0): # construtor da classe como fosse a fábrica de vidro
        self.titular = titular  # nome do dono (fixo)
        self.saldo = saldo      # Saldo inicial
    
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

def criar_conta(nome, saldo_inicial=0):
    return ContaBancaria(nome, saldo_inicial)

conta = criar_conta("Fulano", 100) # Usando a função criadora
conta.sacar(20)
print(conta.extrato())
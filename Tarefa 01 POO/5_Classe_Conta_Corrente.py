class contaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
        
        def alterarNome(self, novoNome):
            self.nomeCorrentista = novoNome
        
        def deposito(self, total):
            self.saldo += total    
        
        def saque(self, total):
            self.saldo -= total

        def printTotal(self,total, printTotal):
            print(printTotal)
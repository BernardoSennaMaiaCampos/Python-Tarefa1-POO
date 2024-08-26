class quadrado:
    def __init__(self, tamanhoDoLado):
        self.tamanhoDoLado = tamanhoDoLado
        
    def mudarValorDoLado(self, mudarValor):
        self.tamanhoDoLado = mudarValor
        
    def retornarValorDoLado(self):
        return self.tamanhoDoLado
        
    def calcularArea(self):
        self.tamanhoDoLado ** 2
            
        
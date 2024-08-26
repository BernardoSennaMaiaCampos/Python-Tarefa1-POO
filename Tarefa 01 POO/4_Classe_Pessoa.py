class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, idade, altura):
        if idade >= 21:
            calcularIdade = idade + 1
            print("Sua idade é: "+calcularIdade)
        else:
            calcularIdade = idade + 1
            calcularAltura = altura + 0.5
            print("Sua idade é: "+calcularIdade)
            print("Sua altura é: "+calcularAltura)
    
    def engordar(self):
        self.peso+=1
        
        
    def emagrecer(self):
        self.peso-=1
    
    def crescer(self):
        self.altura+=0.5
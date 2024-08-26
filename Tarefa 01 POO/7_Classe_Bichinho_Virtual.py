class Bichinho_Virtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        
        
    def alterarNome(self, novoNome):
        self.nome = novoNome

    def retornarNome(self):
        return self.nome
    
    def statusFome(self):
        return self.fome
    
    def statusSaude(self):
        return self.saude 
    
    def statusIdade(self):
        return self.idade
    
    def humor(self,fome,saude):
        self.fome + self.saude
        print(fome+saude)
    

    
    
        
    
    
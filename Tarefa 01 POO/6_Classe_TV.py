class tv:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume
        self.canal_minimo = 1
        self.canal_maximo = 100
        self.volume_minimo = 0
        self.volume_maximo = 100
        
    def mudarCanal(self, novoCanal):
        if self.canal_minimo <= novoCanal <= self.canal_maximo:
            self.canal = novoCanal
        else:
            print("Canal inválido")
    
    def aumentarVolume(self):
        if self.volume < self.volume_maximo:
            self.volume +=1
        else:
            print("Volume máximo")
    
    def diminuirVolume(self):
        if self.volume > self.volume_mínimo:
            self.volume -=1
        else: 
            print("Volume está no mínimo")
            
    def mostrarStatus(self):
        print(f"Canal atual: {self.canal}")
        print(f"Volume atual: {self.volume}")
class Carro:
    def __init__(self, consumo, combustivel):
        self.consumo = consumo
        self.combustivel = 0  
        self.nivel_combustivel = 0

    def abastecer(self, combustivel, nivel_combustivel):
        gasolina = input("Quanta gasolina deseja adcionar?" )
        nivel_combustivel = gasolina + combustivel  

    def adicionar_gasolina(self, quantidade):
        self.nivel_combustivel += quantidade

    def andar(self, distancia):
       
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
        else:
            print("Combustível insuficiente para percorrer a distância solicitada.")

    def obter_gasolina(self):
        return self.nivel_combustivel




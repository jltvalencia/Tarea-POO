class carro:
    def __init__ (self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        
    def tablero(self):
        print("Bienvenido a tu nuevo carro,su marca es",self.marca,"el modelo de tu carro es ",self.modelo,"el año de tu veiculo es de: ",self.año)
    def cierrepantalla(self):
        print("Disfruta de tu nuevo vehiculo",self.modelo)
        
class deportivo(carro):
    def __init__ (self,marca,modelo,año,velocidad):
        super(). __init__ (marca,modelo,año)
        self.velocidad=velocidad
    def velocidad_max(self):
        print("Velocidad maxima activado,tu velocidd es de ",self.velocidad,"km/m")
        
vehiculo = deportivo("Lamborghini", "Huracán", 2024, 325) 
vehiculo.tablero()
vehiculo.velocidad_max()
        
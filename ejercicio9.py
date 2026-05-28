class Vehiculo:
    def __init__(self,modelo,marca,precio_dia):
        self.modelo=modelo 
        self.marca=marca
        self.precio_dia=precio_dia
    def informacion(self):
        print("---INFORMACION DEL VEICULO---")
        print(F"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio por dia: {self.precio_dia}")
class autoRenta(Vehiculo):
    def __init__(self, modelo, marca, precio_dia,dias_renta,tipo_combustible):
        super().__init__(modelo, marca, precio_dia)
        self.dias_renta=dias_renta
        self.tipo_combustible=tipo_combustible
        self.precio_T=0
    def infoAlquiler(self):
        print("--DATOS DE RENTA--")
        print(f"Dias de renta: {self.dias_renta}")
        print(f"Tipo de combustible: {self.tipo_combustible}")
    def total(self):
        self.precio_T=self.precio_dia*self.dias_renta
        print(f"Presio total: {self.precio_T}")
        
Nmodelo=input("Ingrese el modelo del vehiculo: ")
Nmarca=input("Ingresar la marca del vehiculo: ")
Ppordia=int(input("Ingrese el precio por dia: "))
Drenta=int(input("Ingrese el numero de dias: " ))
Tcombustibles=input("Ingrese el tipo de combustible: ")

auto_renta=autoRenta(Nmodelo,Nmarca,Ppordia,Drenta,Tcombustibles)
auto_renta.informacion()
auto_renta.infoAlquiler()
auto_renta.total()






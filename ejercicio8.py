class Entradacine():
    def __init__(self,nombre_cliente,Fecha,nombre_pelicula,precio):
        self.nombre_cliente=nombre_cliente
        self.Fecha=Fecha
        self.nombre_pelicula=nombre_pelicula
        self.precio=precio
    def ticket(self):
        print("----Ticket General---")
        print(f"Nombre del cliente: {self.nombre_cliente}")
        print(f"Fecha de la función: {self.Fecha}")
        print(f"Nombre de la pelicula: {self.nombre_pelicula}")
        print(f"El costo de la entrada es de: {self.precio}")
class VIP(Entradacine):
    def __init__(self, nombre_cliente, Fecha, nombre_pelicula,precio,numero_asiento,combo_snacks):
        super().__init__(nombre_cliente, Fecha, nombre_pelicula,precio)
       
        self.numero_asiento = numero_asiento
        self.combo_snacks = combo_snacks
        self.precio=precio            
    def descuento(self):
        self.descuento=self.precio*0.15
        self.pago_T=self.precio-self.descuento
    def ticketVIP(self):
        print("----TICKET VIP")
        print(f"Numero de asiento: {self.numero_asiento}")
        print(f"Conbo de snacks incluido: {self.combo_snacks}")
        print(f"El valor de la entrada es de : {self.pago_T}")
        
nomc=input("Ingrese el nombre del cliente: ")
fec=input ("Ingrese la fecha de la funcion: ")
nomP=input("Ingrese el nombre de la pelicula: ")
Nasiento=int(input("Ingrese el numero del asiento: "))
Precio=int(input("Ingrese el valor de la entrada: "))
tik_vip=VIP(nomc,fec,nomP,Precio,Nasiento,"Papas fritas,doritos,cola")
tik_vip.descuento()
tik_vip.ticketVIP()


    
        
        
        
        
        
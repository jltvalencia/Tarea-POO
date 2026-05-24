class Ropa:
    def __init__(self,prenda,marca,precio):
        self.prenda=prenda
        self.marca=marca
        self.precio=precio
        
    def detalle_ropa(self):
        print(f"La {self.prenda} es de la marca {self.marca} la cual tien un valor de {self.precio}")
    def descuento(self):
        descuento=self.precio * 0.10
        self.precio -= descuento
        print(f"Se le realizara un descunto del 10%,su nuevo precio es de: {self.precio} ")
        
class Calzado(Ropa):
    def __init__(self,prenda,marca,precio,talla):
        super().__init__(prenda,marca,precio)
        self.talla=talla
    def detalle_calzado(self):
        print ("La talla de su calzado es: ", self.talla,"la marca es", self.marca)
    def disponivilidad(self):
        print (f"En este momento estamos revisando si disponemos {self.prenda} en talla {self.talla}")

prenda1 = Ropa("Camisa","adidas",35)
Calzado1 = Calzado("Tacones","nike",25,40)

print("-----detalle de su compra ")
prenda1.detalle_ropa()
prenda1.descuento()
Calzado1.detalle_calzado()


    


 
        
    
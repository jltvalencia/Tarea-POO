class Producto:
    def __init__(self,nombre,precio,marca):
        self.nombre=nombre
        self.precio=precio
        self.marca=marca
    def detalle(self):
        print(f"Nombre del producto: {self.nombre}")
        print(f"Precio del producto:  {self.precio}")
        print(f"Marca del producto:  {self.marca}")
class Lapto(Producto):
    
    def __init__(self, nombre, precio, marca,procesador,ram):
        super().__init__(nombre, precio, marca)
        self.procesador=procesador
        self.ram=ram
        
    def calcular(self):
        self.precio_t=self.precio * 1.15
    def factura(self):
        print("-------Fatura-------")
        print(f"Tipo de procesador:  {self.procesador}")
        print(f"Su memoria RAM es de:  {self.ram}")
        print(f"El precio total mas el IVA: {self.precio_t}")

nombre_p=input("Ingrese el nombre del producto: ")
precio_p=int(input("Ingrese el valor del producto: "))
marca_c=input("Ingrese la marca del producto: ")
procesador_l=input("Tipo de procesador: ")
ram_l=input("Me moria RAM: ")
Detalle_g=Lapto(nombre_p,precio_p,marca_c,procesador_l,ram_l)


Detalle_g.detalle()
Detalle_g.calcular()
Detalle_g.factura()


        
        
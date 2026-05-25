class PedidoPiza:
    def __init__ (self,tamaño,ingredientes,precio_pizza):
        self.tamaño=tamaño
        self.ingredeintes=ingredientes
        self.precio_pizza=precio_pizza
    def pedido_base(self):
        print("Detalle del pedido")
        print(f"Tamaño de la pizza: {self.tamaño}")
        print(f"Ingredientes principal: {self.ingredeintes}")
        print(f"Precio d ela pizza: {self.precio_pizza}")
class pedido_envio(PedidoPiza):
      def __init__(self, tamaño, ingredientes, precio_pizza,direccion,costo_envio):
           super().__init__(tamaño, ingredientes, precio_pizza)
           self.direccion=direccion
           self.costo_envio=costo_envio
           self.pagot=0
      def calcular_total(self):
            self.pagot=self.precio_pizza+self.costo_envio
      def tiket(self):
          print(f"Dirección de entrega: {self.direccion}")
          print(f"Costo de envio: {self.costo_envio}")
          print(f"Costo total: {self.pagot}")
tam=input("Ingrese el tamaño de pizza (ej.Mediana,Familiar): ")
ingredientes=input("Ingrese 3 ingredientes de su preferencia: ")
preciop=int(input("Ingrese el valor de la pizza:$ "))
dirección=input("Ingrese la dirección: ")
costoen=int(input("Ingrese el valor del envio:$ "))
mi_pedido=pedido_envio(tam,ingredientes,preciop,dirección,costoen)

mi_pedido.pedido_base()
mi_pedido.calcular_total()
mi_pedido.tiket()

        
        
          
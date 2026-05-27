class computer:

    def __init__(self, marca,color):
        self.marca=marca
        self.color=color
       


    def encender(self):
        print("bien venidoo la marca de este computador es de: ",self.marca,"el color es:",self.color)


# Crear objeto
computer1 = computer("HP","rojo")

# Usar método
computer1.encender()
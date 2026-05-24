class banco:
    def __init__(self, nombreban, titular, fecha):
        self.nombreban = nombreban
        self.titular = titular
        self.fecha = fecha

    def detalleban(self):
        print(f"----Binvenido somos el {self.nombreban}")
        print(f"nombre del titular:{self.titular}")
        print(f"Fcha: {self.fecha}")


class retiro(banco):
    def __init__(self, nombreban, titular, fecha, saldo_actual, cantidad_retiro):
        super().__init__(nombreban, titular, fecha)
        self.saldo_actual = saldo_actual
        self.cantidad_retiro = cantidad_retiro
        
    def realizar_retiro(self):
        # El IF que valida si te alcanza el dinero
        if self.cantidad_retiro <= self.saldo_actual:
            self.saldo_actual -= self.cantidad_retiro
            print(f"¡Retiro exitoso! Retiraste: ${self.cantidad_retiro}")
            print(f"Tu nuevo saldo es: ${self.saldo_actual}")
        else:
            print("Error: Fondos insuficientes para realizar el retiro.")




# 1. Pedimos el monto al usuario
monto = int(input("Ingrese el valor que va a retirar:$"))

# 2. Creamos el objeto de la clase 'retiro' pasando todos los datos en orden:
# nombreban, titular, fecha, saldo_actual (500), cantidad_retiro (monto)
cuenta_usuario = retiro("Banco de Pichincha", "Leonardo Valencia", "24/05/2026", 500, monto)

# 3. Ejecutamos los métodos para ver el resultado en pantalla
cuenta_usuario.detalleban()
cuenta_usuario.realizar_retiro()
            
            
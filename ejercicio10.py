class empleado:
    def __init__(self, Nombre_E, Cedula_E, Eda_E): 
        self.nombre = Nombre_E
        self.cedula = Cedula_E
        self.edad = Eda_E

    def Datos(self):
        print("\n--Datos del Empleado--")
        print(f"Nombre del empleado: {self.nombre}")
        print(f"Cédula del empleado: {self.cedula}")
        print(f"Edad del Empleado: {self.edad}")


class sueldo(empleado):
    def __init__(self, Nombre_E, Cedula_E, Eda_E, sueldo_E, Comicion_E): 
        super().__init__(Nombre_E, Cedula_E, Eda_E)
        self.sueldo_E = sueldo_E
        self.comicion = Comicion_E
        self.pagoT = 0

    def Datos_S(self):
        print("--Nómina de pago--")
        print(f"El sueldo base del empleado es: {self.sueldo_E}")

    def sueldoT(self): 
        self.pagoT = self.sueldo_E + self.comicion
        print(f"El sueldo total más comisiones es de: {self.pagoT}")


# --- Bloque Principal de Ejecución (Sin espacios al inicio) ---

nombre_e = input("Ingrese el nombre del Empleado: ")
cedula_e = input("Ingrese el número de cédula: ")  # Se deja como texto para evitar fallos con ceros a la izquierda
edad_e = int(input("Ingrese la edad del empleado: "))
sueldo_e = int(input("Ingrese el sueldo del empleado: $"))
comicion_e = int(input("Ingrese las comisiones del empleado: $"))

# Creación del objeto (Instanciación)
Sueldo_E = sueldo(nombre_e, cedula_e, edad_e, sueldo_e, comicion_e)

# Llamada a los métodos para mostrar los resultados en pantalla
Sueldo_E.Datos()
Sueldo_E.Datos_S()
Sueldo_E.sueldoT()
class empleado:
    def __init__(self,nombre,cedula,puesto):
        self.nombre=nombre
        self.cedula=cedula
        self.puesto=puesto
    def detalle_empleado(self):
        print(f"---Detalle de empleado")
        print(f"Nombre:{self.nombre}")
        print(f"Cedula:{self.cedula}")
        print(f"Puesto:{self.puesto}")
        
class empledo_hora(empleado):
    def __init__(self, nombre, cedula, puesto,horas_trabajadas,valor_hora,bono_extra):
        super().__init__(nombre, cedula, puesto)
        self.horas_trabajadas=horas_trabajadas
        self.valor_hora=valor_hora
        self.bono_extra=bono_extra
        self.sueldo_base=0
    def calcular(self):
        self.sueldo_base=self.horas_trabajadas*self.valor_hora
        
    def mostrar_pago(self):
        if self.horas_trabajadas>40:
            self.sueldo_total=self.sueldo_base+self.bono_extra
            print(f"Felisidades trabajste:  {self.horas_trabajadas} tu sueldo total sumado tu bono es de:$ {self.sueldo_total}")
            
        else:
            print(f"Tu sueldo normal es de: {self.sueldo_base}")
            
monto=int(input("Ingres el valor por hora:$ "))
horas=int(input("Ingrese el numero de horas trabajadas: "))
Trabajador=empledo_hora("Leonardo Valencia",1728726041,"Gerente",horas,monto,50)

print("----Nomina del Empleado---")
Trabajador.detalle_empleado()
Trabajador.calcular()
Trabajador.mostrar_pago()


            
            
                 
        
        
        
    
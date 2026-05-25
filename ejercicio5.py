class cita:
    def __init__(self,nombre_paciente,cedula_paciente,fecha_consulta):
        self.nombre_paciente=nombre_paciente
        self.cedula_paciente=cedula_paciente
        self.fecha_consulta=fecha_consulta
    def detalle_consulta(self):
        print("-----Detalles de la cita medica-----")
        print(f"Nombre del paciente: {self.nombre_paciente}")
        print(f"Cedula del paciente: {self.cedula_paciente}")
        print(f"Fecha de la consulta: {self.fecha_consulta}")
class citaespecifica(cita):
    def __init__(self, nombre_paciente, cedula_paciente, fecha_consulta,nombre_doctor,nombre_especialidad):
        super().__init__(nombre_paciente, cedula_paciente, fecha_consulta)
        self.nombre_doctor=nombre_doctor
        self.nombre_especialidad=nombre_especialidad
    def detalle_especialidad(self):
        print(f"Dr.{self.nombre_doctor}")
        print(f"Especialidad de la consulta: {self.nombre_especialidad}")
nombre_p=input("Ingrese el nombre del paciente ")
cedula_p=input("Ingrese el numero de cedula del paciente")
fecha_c=input("Ingrese la fecha de la consulta (ej.10/05/2026)")
nombre_doc=input("Ingrese el nombre del doctor: ")
nombre_es=input("Ingrese el nombre de la especialidad de la consulta: ")
detalle=citaespecifica(nombre_p,cedula_p,fecha_c,nombre_doc,nombre_es)

detalle.detalle_consulta()
detalle.detalle_especialidad()
    
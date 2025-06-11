from datetime import datetime
from validaciones import validar_existencia_paciente, validar_existencia_medico, validar_turno_no_duplicado, validar_especialidad_en_dia

class Paciente:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento):
            self.__nombre = nombre
            self.__apellido = apellido
            self.__dni = dni
            self.__fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

    def obtener_dni(self):
            return self.__dni
        
    def __str__(self):
            fecha_str = self.__fecha_nacimiento.strftime("%d/%m/%Y") 
            return f"{self.__nombre } {self.__apellido} - DNI: {self.__dni} - Fecha Nac: {fecha_str}"

class Medico:
    def __init__(self,nombre,apellido,matricula,especialidades):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__matricula = matricula
        self.__especialidades = [especialidades]

    def obtener_matricula(self):
        return self.__matricula
    
    def _str_(self):
        return f"{self.__nombre} {self.__apellido} - Matricula: {self.__matricula} - Especialidad: {self.__especialidades}"
    
    def agregar_especialidad(self, especialidad):
        self.__especialidades.append(especialidad)

    def obtener_especialidad_para_dia(self, dia):
        for especialidad in self.__especialidades:
            for d in especialidad.__dias:
                if d == dia:
                    return especialidad.__tipo
                else: 
                    ...

class Especialidad:
    def __init__(self, tipo, dias):
        self.__tipo = tipo
        self.__dias = [dias]

    def obtener_especialidad(self):

        return self.__tipo
    
    def verificar_dia(self, dia):
        for i in self.__dias:
            if i == dia:
                return True
            else:
                ...

    def _str_(self): 
        return f"Nombre de especialidad {self.__tipo} - Dias: {self.__dias}"

class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = (datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M"))
        self.__especialidad = especialidad

    def obtener_medico(self):
        return self.__medico
    
    def obtener_fecha_hora(self):
        return self.__fecha_hora
    
    def _str_(self):
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"Turno: {fecha_str} - Paciente: {self.__paciente} - Medico: {self.medico} - Especialidad: {self.__especialidad}"

class Receta:
    def __init__(self, paciente, medico, fecha, medicamentos):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_emision = datetime.strptime(fecha, "%d/%m/%Y")
        self.__medicamentos = [medicamentos]

    def __str__(self):
            fecha_str = self.__fecha_emision.strftime("%d/%m/%Y")
            return f"Receta - Fecha: {fecha_str} - Paciente: {self.__paciente} - Medico: {self.__medico} - Medicamentos: {', '.join(self.medicamentos)}"

class HistoriaClinica:
    def __init__(self,paciente,turnos,recetas):
        self.__paciente = paciente
        self.__turnos = [turnos]
        self.__recetas = [recetas]

    def agregar_turno(self, turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta):
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return self.__turnos
    
    def obtener_recetas(self):
        return self.__recetas
    
    def _str_(self): 
        return f"Historia Clinica de {self.__paciente} - Turnos: {len(self.__turnos)} - Recetas: {len(self.__recetas)}"

class Clinica:
    def __init__(self):
        self.__pacientes= {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}
    
    def agregar_paciente(self,paciente):
        self.__pacientes[paciente.obtener_dni()] = paciente
        self.__historias_clinicas[paciente.obtener_dni()] = []

    def agregar_medico(self,medico):
        self.__medicos[medico.obtener_matricula()] = medico

    def obtener_pacientes(self):
        return self.__pacientes
    
    def obtener_medico(self):
        return self.__medicos

    def obtener_medico_por_matricula(self, matricula):
        for m in self.__medicos:
            return m[matricula]

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):

        paciente = validar_existencia_paciente(dni)
        medico = validar_existencia_medico(matricula)
        fecha = validar_turno_no_duplicado(matricula, fecha_hora)
        esp = validar_especialidad_en_dia(matricula, especialidad, fecha_hora)
        
        if(paciente == True):
            if(medico == True):
                if(fecha == True):
                    if(esp == True):
                        nuevoTurno = Turno(dni, matricula, especialidad, fecha_hora)
                        print(nuevoTurno._str_)
    def obtener_turnos(self):
        return self.__turnos
    
    def emitir_receta(self, dni, matricula, medicamentos):
        nuevaReceta =  Receta(dni, matricula, datetime.now(), medicamentos)
        print(nuevaReceta.__str__)


    def obtener_historia_clinica(self, dni):
        for i in self.__historias_clinicas:
            return i[dni]      

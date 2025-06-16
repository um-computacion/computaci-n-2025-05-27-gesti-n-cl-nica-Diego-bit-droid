from datetime import datetime
from validaciones import validar_existencia_paciente, validar_existencia_medico, validar_turno_no_duplicado, validar_especialidad_en_dia, obtener_dia_semana_en_espanol
from excepciones import EspecialidadYaExistente, ErrorPaciente, ErrorMedico, RecetaInvalidaException

class Paciente:
    def __init__(self, nombre: str, apellido: str, dni: str, fecha_nacimiento: str):
            self.__nombre: str = nombre
            self.__apellido: str = apellido
            self.__dni: str = dni
            self.__fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

    def obtener_dni(self):
            return self.__dni
        
    def __str__(self):
            fecha_str = self.__fecha_nacimiento.strftime("%d/%m/%Y") 
            return f"{self.__nombre } {self.__apellido} - DNI: {self.__dni} - Fecha Nac: {fecha_str}"

class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo = tipo
        self.__dias = dias
    def obtener_especialidad(self):
        return self.__tipo
    
    def verificar_dia(self, dia):
        return dia.lower() in [d.lower() for d in self.__dias]

    def __str__(self): 
        return f"Nombre de especialidad {self.__tipo} - Dias: {self.__dias}"
    
class Medico:
    def __init__(self,nombre: str,apellido: str,matricula: str,especialidades: list[Especialidad]):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__matricula = matricula
        self.__especialidades = especialidades

    def obtener_matricula(self):
        return self.__matricula
    
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} - Matricula: {self.__matricula} - Especialidad: {self.__especialidades}"
    
    def agregar_especialidad(self, especialidad: Especialidad):
        nombres = [n.obtener_especialidad() for n in self.__especialidades]

        if( especialidad.obtener_especialidad() in nombres ):
            raise EspecialidadYaExistente()
        else:
            self.__especialidades.append(especialidad)

    def obtener_especialidad_para_dia(self, dia):
        for especialidad in self.__especialidades:
            if(especialidad.verificar_dia(dia)):
                return especialidad.obtener_especialidad()
            else:
                return None

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: Especialidad):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = (datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M"))
        self.__especialidad = especialidad

    def obtener_medico(self):
        return self.__medico
    
    def obtener_fecha_hora(self):
        return self.__fecha_hora
    
    def __str__(self):
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"Turno: {fecha_str} - Paciente: {self.__paciente} - Medico: {self.medico} - Especialidad: {self.__especialidad}"

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_emision: datetime, medicamentos: list[str]):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_emision = fecha_emision
        self.__medicamentos = medicamentos

    def __str__(self):
        fecha_str = self.__fecha_emision.strftime("%d/%m/%Y %H:%M")
        return (f"Receta - Fecha: {fecha_str} - Paciente: {self.__paciente} - "
                f"Medico: {self.__medico} - Medicamentos: {', '.join(self.__medicamentos)}")

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.__paciente = paciente
        self.__turnos: list[Turno] = []
        self.__recetas: list[Receta] = []

    def agregar_turno(self, turno: Turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos)
    
    def obtener_recetas(self):
        return list(self.__recetas)
    
    def __str__(self): 
        return f"Historia Clinica de {self.__paciente} - Turnos: {len(self.__turnos)} - Recetas: {len(self.__recetas)}"

class Clinica:
    def __init__(self):
        self.__pacientes: dict[str, Paciente] = {}
        self.__medicos: dict[str, Medico] = {}
        self.__turnos: list[Turno] = []
        self.__historias_clinicas: dict[str, HistoriaClinica] = {}
    
    def agregar_paciente(self,paciente: Paciente):
        dni = paciente.obtener_dni();
        if dni in self.__pacientes:
            raise ErrorPaciente("El cliente ya se encuentra registrado.")
        else:
            self.__pacientes[dni] = paciente
            self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self,medico: Medico):
        matricula = medico.obtener_matricula()

        if matricula in self.__medicos:
            raise ErrorMedico("El medico ya se encuentra registrado")
        else:
            self.__medicos[matricula] = medico

    def obtener_pacientes(self):
        return self.__pacientes
    
    def obtener_medicos(self):
        return self.__medicos

    def obtener_medico_por_matricula(self, matricula):
        validar_existencia_medico(matricula)
        return self.__medicos[matricula]

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):

        validar_existencia_medico(matricula)
        validar_existencia_paciente(self.__pacientes, dni)
        validar_turno_no_duplicado(matricula, fecha_hora)

        medico = self.__medicos[matricula]
        paciente = self.__pacientes[dni]
        dia = obtener_dia_semana_en_espanol(fecha_hora)

        validar_especialidad_en_dia(medico, dia)

        turno = Turno(paciente, medico, fecha_hora, especialidad)

        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)


    def obtener_turnos(self):
        return self.__turnos
    
    def emitir_receta(self, dni, matricula, medicamentos: list[str], fecha_emision: datetime = None):
        validar_existencia_medico(self.__medicos, matricula)
        validar_existencia_paciente(self.__pacientes, dni)
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]

        if len(medicamentos) < 1:
            raise RecetaInvalidaException("Debes tener al menos un medicamento en la receta.")

        if fecha_emision is None:
            fecha_emision = datetime.now()

        nueva_receta = Receta(paciente, medico, fecha_emision, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(nueva_receta)

    def obtener_historia_clinica(self, dni):
        validar_existencia_paciente(self.__pacientes, dni)
        return self.__historias_clinicas[dni]
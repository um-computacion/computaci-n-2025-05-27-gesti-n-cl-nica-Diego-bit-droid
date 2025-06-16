from datetime import datetime
from excepciones import TurnoOcupadoException, MedicoNoDisponibleExcepcion, PacienteNoEncontradoExcepcion, MedicoNoEncontrado,ErrorPaciente,ErrorMedico


def validar_existencia_paciente(pacientes: dict, dni: str):
    if dni not in pacientes:
        raise ErrorPaciente("No se ha encontrado al paciente.")

def validar_existencia_medico(medicos: dict, matricula: str):
    if matricula not in medicos:
        raise ErrorMedico("No se ha encontrado al medico.")
def validar_turno_no_duplicado(self, matricula, fecha_hora):
    fecha = (datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M"))
    for t in self.__turnos:
        if(t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora):
            raise TurnoOcupadoException(f"El turno para el dia {fecha_hora} con el doctor con matricula numero {matricula} se encuentra ocupado.")
            
def obtener_dia_semana_en_espanol(fecha_hora):
    fecha = (datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M"))
    dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    return dias[fecha.weekday()]

def obtener_especialidad_disponible(medico: "Medico", dia):
    return medico.obtener_especialidad_para_dia(dia)

def validar_especialidad_en_dia(medico: "Medico", especialidad, dia):
    med = obtener_especialidad_disponible(medico, dia)

    if med == None:
        raise MedicoNoDisponibleExcepcion("El medico no se encuentra disponible.")
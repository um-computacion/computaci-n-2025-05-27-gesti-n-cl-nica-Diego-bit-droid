from datetime import datetime
from excepciones import TurnoOcupadoException, MedicoNoDisponibleExcepcion

def validar_existencia_paciente(self, dni):
        for p in self.__pacientes:
            if p.__dni == dni:
                return True
            else:
                ...
                #excepcion
    
def validar_existencia_medico(self, matricula):
    for m in self.__medicos:
            if m.__matricula == matricula:
                return True
            else:
                ...
                #excepcion

def validar_turno_no_duplicado(self, matricula, fecha_hora):
    fecha = (datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M"))
    for t in self.__turnos:
        if(t.matricula == matricula):
            if(fecha not in t.fecha_hora):
                return True
            else:
                raise TurnoOcupadoException()
    
def obtener_dia_semana_en_espanol(self, fecha_hora):
    fecha = (datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M"))
    dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    return dias[fecha.weekday()]

    
def obtener_especialidad_disponible(self, matricula, dia):
     ...

def validar_especialidad_en_dia(self, matricula, especialidad, dia):
    if matricula in self.__medicos:

        medico = self.__medicos[matricula]

        for e in medico.__especialidades:
            if(e.__tipo == especialidad):
                fecha = obtener_dia_semana_en_espanol(dia)
                if fecha in e.__dias:
                    return True
                else:
                    raise MedicoNoDisponibleExcepcion()
                
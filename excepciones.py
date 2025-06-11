class PacienteNoEncontradoExcepcion(Exception):
    print('No se ha encontrado al paciente.')

class MedicoNoDisponibleExcepcion(Exception):
    print('El medico no se encuentra disponible.')

class TurnoOcupadoException(Exception):
    print('El turno solicitado ya se encuentra ocupado.')

class RecetaInvalidaException(Exception):
    print("Receta no valida.")

class ErrorAlAgregarPaciente(Exception):
    print("Ocurrio un error al agregar al paciente.")

class ErrorAlAgregarMedico(Exception):
    print("Ocurrio un error al agregar el medico")
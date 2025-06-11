from Turnosclinica import Paciente, Medico, Turno, Receta, HistoriaClinica, Clinica, Especialidad
from excepciones import ErrorAlAgregarMedico, ErrorAlAgregarPaciente

clinica = Clinica()
def menu():

    while True:
        print("Menu Principal")
        print("1- Agregar Paciente")
        print("2- Agregar Medico")
        print("3- Agendar Turno")
        print("4- Agregar Especialidad")
        print("5- Emitir Receta")
        print("6- Ver Historia Clinica")
        print("7- Ver todos los Turnos")
        print("8- Ver todos los Pacientes")
        print("9- Ver todos los Medicos")
        print("0- Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:

            print("Agregar Paciente")

            try:

                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                dni = input("Ingrese su DNI: ")
                fechaNac = input("Ingrese su fecha de nacimiento(dd/mm/aaaa)")

                paciente =Paciente(nombre, apellido, dni, fechaNac)

                clinica.agregar_paciente(paciente)

                print("Paciente Agregado Correctamente!")
            except:
                raise ErrorAlAgregarPaciente()
        
        if opcion == 2:

            print("Agregar Medico")

            try:
                
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                matricula = input("Ingrese el numero de matricula: ")
                especialidadTipo = input("Ingrese el tipo de Especialidad: ")
                especialidadDias = input("Ingrese los dias de atencion(separados por coma): ")

                dias = [especialidadDias.strip().capitalize() for d in especialidadDias.split(",") if d.split()]

                especialidad = Especialidad(especialidadTipo, dias)

                nuevoMedico = Medico(nombre, apellido, matricula, especialidad)

                clinica.agregar_medico(nuevoMedico)

                print("Medico Agregado Correctamente!")

            except:
                raise ErrorAlAgregarMedico()
        
        if opcion == 3:

            print("Agendar Turno")

            try:
                dni = input("Ingrese el dni del paciente: ")
                matricula = input("Ingrese la matricula del medico: ")
                especialidad = input("Ingrese la especialidad del medico: ")
                fechaHora = input("Ingrese la fecha y la hora del turno(dd/mm/aaaa hh:mm): ")


            
            except:
                ...
if __name__ == "__main__":
    menu()
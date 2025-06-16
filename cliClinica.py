
from Turnosclinica import Paciente, Medico, Turno, Receta, HistoriaClinica, Clinica, Especialidad
from excepciones import ErrorAlAgregarMedico, ErrorAlAgregarPaciente, ErrorGeneralTurno
from datetime import datetime

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

            
            dni = input("Ingrese el dni del paciente: ")
            matricula = input("Ingrese la matricula del medico: ")
            especialidad = input("Ingrese la especialidad del medico: ")
            fechaHora = input("Ingrese la fecha y la hora del turno(dd/mm/aaaa hh:mm): ")

            try:
                fecha = datetime.strptime(fechaHora, "%d/%m/%Y %H:%M")
            except:
                raise ErrorGeneralTurno("Formato de fecha incorrecto")
            
            clinica.agendar_turno(dni, matricula, especialidad, fecha)
            print("Turno agendado correctamente.")

        if opcion == 4:
            ...

        if opcion == 5:
            ...
        
        if opcion == 6:
            dni = input("Ingrese el dni del paciente: ")
            print(f'Historia Clinica de Paciente con dni numero {dni}')
            
            historia = clinica.obtener_historia_clinica(dni)
            print(historia)

        if opcion == 7:
            print("Todos los turnos")

            turnos = clinica.obtener_turnos()

            if len(turnos) == 0:
                print("No hay turnos agendados")
            else:
                for t in turnos:
                    print(t)

        if opcion == 8:
            print("Todos los Pacientes: ")
            
            pacientes = clinica.obtener_pacientes()

            if len(pacientes) == 0:
                print("Todavia no hay pacientes registrados.")
            else:
                for p in pacientes:
                    print(p)

        if opcion == 9:
            print("Todos los Medicos: ")
            
            medicos = clinica.obtener_medicos()

            if len(medicos) == 0:
                print("Todavia no hay medicos registrados.")
            else:
                for m in medicos:
                    print(m)

        if opcion == 0:
            ...
if __name__ == "__main__":
    menu()
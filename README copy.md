# Sistema de Gestion para Clinica Medica

## Como ejecutar el sistema

1. Abrir la consola o terminal  
2. Ejecutar el comando: -m cli.cliClinica
                        
3. Aparecera un menu con las siguientes opciones  
              1. Agregar Paciente  
              2. Agregar Medico  
              3. Agendar Turno  
              4. Agregar Especialidad  
              5. Emitir Receta  
              6. Ver Historia Clinica  
              7. Ver todos los Turnos  
              8. Ver todos los Pacientes  
              9. Ver todos los Medicos  
              0. Salir  

## Como ejecutar las pruebas

- Desde la consola ejecutar: python -m unittest discover test

- Para ejecutar un archivo de prueba específico usar:
test_clases= python -m unittest test.test_clases
testexepcion= python -m unittest test.testexepcion
---

## Diseño general

El sistema se compone de las siguientes clases principales

- **Paciente** almacena los datos personales de cada paciente  
- **Medico** contiene informacion del medico y sus especialidades  
- **Especialidad** define las especialidades medicas y los dias disponibles  
- **Turno** representa los turnos agendados entre paciente y medico  
- **Receta** guarda los medicamentos indicados por el medico  
- **Historia Clinica** reune los turnos y recetas de cada paciente  
- **Clinica** clase central que administra pacientes medicos turnos y recetas

Ademas el sistema incluye manejo de excepciones para controlar errores comunes como duplicados o turnos ocupados
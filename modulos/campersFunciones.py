import os
from .funciones import guardarCamper, imprimirBusquedaCamper, buscarCamper

def nuevoEstudiante():
    os.system('clear')
    print("""
        #################################
        #     Formulario del Camper     #
        #################################
          """)
    
    IdCamper = verificarExistenciaEstudiante()
    Nombre = input("Ingrese el nombre del estudiante: ")
    Apellido = input("Ingrese los apellidos del estudiante: ")
    Direccion = input("Ingrese la dirección del estudiante: ")
    Acudiente = acudiente()
    Fijo = int(input("Ingrese el teléfono fijo del estudiante: "))
    Celular = int(input("Ingrese el teléfono celular del estudiante: "))
    Estado = "Inscrito"
    Examen1 = "No Rindio"
    Examen2 = "No Rindio"
    
    estudiante = {
        "Id Camper": IdCamper,
        "Nombre": Nombre,
        "Apellido": Apellido,
        "Direccion": Direccion,
        "Acudiente": Acudiente,
        "Telefonos": {
            "Fijo": Fijo,
            "Celular": Celular
        },
        "Estado": Estado,
        "Examen 1": Examen1,
        "Examen 2": Examen2
    }
    
    guardarCamper(estudiante)   
    
def buscarEstudiante():
    os.system('clear')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscar = input("Ingrese la ID del camper a buscar: ")
    
    resultados = buscarCamper(buscar)

    if not resultados:
        print("No se encontró ningún estudiante con la ID proporcionada.")
    else:
        imprimirBusquedaCamper(buscar)

def acudiente():
    while True:
        rpta = input("¿Tiene acudiente?: S por Sí - N por No: ").upper()
        if rpta == "S":
            return "Si tiene"
        elif rpta == "N":
            return "No tiene"
        else:
            print("Respuesta no válida. Por favor, ingrese 'S' por Sí o 'N' por No.")
            
def verificarExistenciaEstudiante():
    while True:
        IdCamper = input("Ingrese ID del camper: ")
        if not buscarCamper(IdCamper):
            break
        else:
            print("El ID del camper ya existe. Por favor, ingrese un nuevo ID.")
    
    return IdCamper

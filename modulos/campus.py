import os
from .variables import *

Camper= Camper()
RutaEntrenamiento= RutaEntrenamiento()
Prueba=Prueba()
AreaEntrenamiento=AreaEntrenamiento()
RutaEntrenamiento=RutaEntrenamientoCreada()
Entrenador=Entrenador()
Matricula=Matricula()
Evaluacion=Evaluacion()

def menu():
    menu= ["Campers ","Trainers ","Administracion ","Salir "]
    while True:
        os.system('cls')
        print("""
        #################################
        #        Menu del Campus        #
        #################################
          """)
        print(".".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: Camper()
                    case 2: Trainers()
                    case 3: Administracion()
                    case 4: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def Camper():
    menu= ["Guardar","Buscar","Volver", "Salir"]
    while True:
        os.system('cls')
        print("""
        #################################
        #        Menu del camper        #
        #################################
          """)
        print(".".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: createEstudiante()
                    case 2: SearchStudent()
                    case 3: menu()
                    case 4: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def Trainers():
    menu= ["Guardar","Buscar","Volver", "Salir"]
    while True:
        os.system('cls')
        print("""
        ##################################
        #        Menu de Trainers        #
        ##################################
          """)
        print(".".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: create()
                    case 2: read()
                    case 3: menu()
                    case 4: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def Administracion():
    menu= ["Actualizar","Borrar","Asignar", "Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #        Menu Administrativo        #
        #####################################
          """)
        print(".".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: update()
                    case 2: delete()
                    case 3: asignar()
                    case 4: menu()
                    case 5: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')


def createEstudiante():
    os.system('cls')
    print("""
        #################################
        #     Formulario del Camper     #
        #################################
          """)

    id = int(input("Ingresa tu ID: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    apellidos = input("Ingrese los apellidos del estudiante: ")
    direccion = input("Ingrese la dirección del estudiante: ")
    telefono_celular = input("Ingrese el teléfono celular del estudiante: ")
    telefono_fijo = input("Ingrese el teléfono fijo del estudiante: ")
    estado = input("Ingrese el estado del estudiante: ")
    nuevo_camper=(id, nombre, apellidos, direccion, telefono_celular, telefono_fijo, estado)

    campers_totales.append(nuevo_camper)
    print("Datos agregados con exito")
    os.system('pause')


# ALLAN, Hay que hacer un for que me ayude a leer los elementos de una lista dentro de otra lista
# y asi encuentre el id en cada uno, pensaba en usar LAMBDA



def SearchStudent():
    os.system('cls')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscar=input("Ingrese la ID del camper a buscar: ")
    for i in campers_totales:
        if buscar in campers_totales:
            print("Se encuentra registrado")
        elif buscar  not in campers_totales:
            print("No se encuentra registrado")
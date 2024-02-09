import os
from .variables import *

Camper= Camper()
RutaEntrenamiento= RutaEntrenamiento()
Prueba= Prueba()
AreaEntrenamiento= AreaEntrenamiento()
RutaEntrenamiento= RutaEntrenamientoCreada()
Entrenador= Entrenador()
Matricula= Matricula()
Evaluacion= Evaluacion()

def menu():
    menu= ["Campers ","Trainers ","Administracion "," Reportes ", "Salir "]
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
                    case 4: Reportes()
                    case 5: break
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
                    case 2: searchStudent()
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
                    case 1: createTrainer()
                    case 2: searchTrainer()
                    case 3: menu()
                    case 4: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def Administracion():
    menu= ["Actualizar","Asignar", "Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #        Menu Administrativo        #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: updateData()
                    case 2: assignmentData()
                    case 3: menu()
                    case 4: break
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

    id = int(input("Ingrese ID del camper: "))
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


# Hay que hacer un for que me ayude a leer los elementos de una lista dentro de otra lista
# y asi encuentre el id en cada uno, pensaba en usar LAMBDA


print(campers_totales)
def searchStudent():
    os.system('cls')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscar=input("Ingrese la ID del camper a buscar: ")
    for student in campers_totales:
        if buscar in student:
            print(f"Camper encontrado: {student}")
            break
    else:
        print("Camper no encontrado.")

def createTrainer():
    os.system('cls')
    print("""
        #################################
        #     Formulario Instructor     #
        #################################
          """)
    
    idTrainer = input("Ingrese ID del Trainer: ")
    nombreTrainer = input("Ingrese nombre del Trainer: ")
    trainer_totales=(idTrainer,nombreTrainer)

    Trainers.append(trainer_totales)


def searchTrainer():
    os.system('cls')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscarTrainer=input("Ingrese la ID del Trainer a buscar: ")
    for student in Trainers:
        if buscarTrainer in student:
            print(f"Trainer encontrado: {student}")
            break
    else:
        print("Trainer no encontrado.")


def updateData():
    menu= ["Campers","Trainers","Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #        Menu Administrativo        #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: updateDataCampers()
                    case 2: updateDataTrainers()
                    case 3: menu()
                    case 4: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')


def updateDataCampers():
    menu= ["Actualizar datos del Camper","Eliminar datos del Camper","Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #        Menu Administrativo        #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: addDataCamper()
                    case 2: deleteDataCamper()
                    case 3: menu()
                    case 4: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')


def updateDataTrainers():
    menu= ["Actualizar datos del Trainer","Eliminar datos del Trainer","Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #        Menu Administrativo        #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: addDataTrainer()
                    case 2: deleteDataTrainer()
                    case 3: menu()
                    case 4: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')


def assignmentData():
    menu= ["Seleccion el Trainer para empezar","Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #        Menu Administrativo        #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: ()
                    case 2: menu()
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')


def Reportes():
    os.system('cls')
    print("""
        #################################
               #     REPORTES     #
        #################################
          """)
    
    print(campers_totales)
    print(Trainers)
    print(Matricula)
    os.system('pause')
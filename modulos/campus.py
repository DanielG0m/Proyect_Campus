import os
from variables import *

Camper= Camper()
RutaEntrenamiento= RutaEntrenamiento()
Prueba=Prueba()
AreaEntrenamiento=AreaEntrenamiento()
RutaEntrenamiento=RutaEntrenamiento()
Entrenador=Entrenador()
Matricula=Matricula()
Evaluacion=Evaluacion()

Camper.Datos()


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
                    case 2: read()
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
    
    os.system('pause')

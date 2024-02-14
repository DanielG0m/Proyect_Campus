import os
from .variables import *
from tabulate import tabulate
import json

Camper= Camper()
RutaEntrenamiento= RutaEntrenamiento()
Prueba= Prueba()
AreaEntrenamiento= AreaEntrenamiento()
RutaEntrenamiento= RutaEntrenamientoCreada()
Entrenador= Entrenador()
Matricula= Matricula()
Evaluacion= Evaluacion()

exist_trainer=readDataTrainerJson()
data_trainer=readDataTrainerJson()

add_camper=readDataCamperJson()
data_camper=readDataCamperJson()

data=readDataCamperJson()

addruta=addRutas()
loadruta=loadRutas()

addsalas=addSalas()
loadsalas=loadSalas()

studentAprobado="Aprobado"

def menu():
    menu= ["Campers ","Trainers ","Administracion "," Reportes ", "Salir "]
    while True:
        os.system('cls')
        print("""
        #################################
        #        Menu del Campus        #
        #################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
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
    menu= ["Guardar","Buscar","Volver"]
    while True:
        os.system('cls')
        print("""
        #################################
        #        Menu del camper        #
        #################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: createEstudiante()
                    case 2: searchStudent()
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def Trainers():
    menu= ["Guardar","Buscar", "Salir"]
    while True:
        os.system('cls')
        print("""
        ##################################
        #        Menu de Trainers        #
        ##################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: createTrainer()
                    case 2: searchTrainer()
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def Administracion():
    menu= ["Actualizar","Registrar rutas","Buscar Rutas", "Salir"]
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
                    case 2: registrar_ruta()
                    case 3: search_ruta()
                    case 4: assigment_ruta()
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
    
    data_Camper={
        "ID": int(input("Ingrese su ID: ")),
        "Nombre": input("Ingrese sus nombres: "),
        "Apellidos":input("Ingrese sus apellidos: "),
        "Direccion":input("Ingrese una direccion: "),
        "Telefeno": input("Ingrese un numero de contacto: "),
        "Estado": "",
        "Primer examen": "",
        "Segundo examen":"",
    }
    add_camper.append(data_Camper)
    addDataCamperJson(add_camper)
    print("Datos guardados Correctamente")
    os.system('pause')

def searchStudent():
    os.system('cls')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscar_student = input("Ingrese la ID del camper a buscar: ")
    for student_camper in data:
        if buscar_student in student_camper:
            print("Camper no encontrado")
            break
    else:
        print(f"Camper encontrado: {student_camper}")
    os.system('pause')

def createTrainer():
    os.system('cls')
    print("""
        #################################
        #     Formulario Instructor     #
        #################################
          """)
    
    data_Trainer={
        "ID": int(input("Ingrese su ID: ")),
        "Nombre": input("Ingrese su nombre completo: "),
        "Apellidos":input("Ingrese su apellido completo: "),
    }

    exist_trainer.append(data_Trainer)
    addDataTrainerJson(exist_trainer)
    os.system('pause')

def searchTrainer():
    os.system('cls')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscarTrainer=input("Ingrese la ID del Trainer a buscar: ")
    for student in data_trainer:
        if buscarTrainer in student:
            print(f"Trainer no encontrado.")
            break
    else:
        print(f"Trainer encontrado: {student}")
    os.system('pause')
    
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
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def updateDataCampers():
    menu= ["Actualizar datos del Camper","Eliminar datos del Camper","Salir"]
    while True:
        os.system('cls')
        print("""
        ####################################
        #   Menu Administrativo (campers)  #
        ####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: addDataCamper()
                    case 2: deleteDataCamper() 
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def updateDataTrainers():
    menu= ["Actualizar datos del Trainer","Eliminar datos del Trainer","Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #   Menu Administrativo (trainers)  #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: addDataTrainer()
                    case 2: deleteDataTrainer()
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def addDataCamper():
    os.system('cls')
    print("""
    #####################################
    #           Editar Camper           #
    #####################################
        """)
    buscar_camper=int(input("Ingrese ID del Camper: "))
    for i, student in enumerate(data_camper):
        if buscar_camper in student:
            print("Camper no encontrado")
            break
    else:
        edit = {
        "ID": int(input("Ingrese su ID: ")),
        "Nombre": input("Ingrese sus nombres: "),
        "Apellidos":input("Ingrese sus apellidos: "),
        "Direccion":input("Ingrese una direccion: "),
        "Telefeno": input("Ingrese un numero de contacto: "),
    }
        
    addDataCamperJson(edit)
    print("Datos del camper actualizados.")
    os.system('pause')

def deleteDataCamper():
    buscar_camper=input("Ingrese ID del Camper: ")
    for student in enumerate(data_camper):
        if buscar_camper in student:
            print("Camper no encontrado")
            break
    else:
        print("""
        Esta seguro que desea eliminar el camper?
        1. si
        2. no
        """)
        opc = int(input(": "))
        if opc == 1:
            data_camper.pop(buscar_camper)
            print("El camper fue eliminado correctamente")
            os.system("pause")
            os.system("cls")
        elif opc == 2:
            print("Eliminación cancelada.")
            os.system("pause")
            os.system("cls")
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")    

def addDataTrainer():
    os.system('cls')
    print("""
    #####################################
    #           Editar Trainer          #
    #####################################
        """)
    buscar_trainer=int(input("Ingrese ID del Trainer: "))
    for student in enumerate(data_trainer):
        if buscar_trainer in student:
            print("Camper no encontrado")
            break
    else:
        edit = {
        "ID": int(input("Ingrese su ID: ")),
        "Nombre": input("Ingrese su nombre completo: "),
        "Apellidos":input("Ingrese su apellido completo: "),
    }
        
    addDataTrainerJson(edit)
    print("Datos del trainer actualizados.")
    os.system('pause')
    
# def deleteDataTrainer():
def registrar_ruta():
    os.system("cls")
    print("""
                *************************
                *      Crear Rutas      *
                *************************
        """)
    rutas = {
        "Nombre": str(input("Ingrese nombre de ruta: ")),
        "Modulos": {
            "Fundamentos de programacion": ["Introduccion a la algoritmia","PSeInt","Python"],
            "Programacion Web": ["HTML", "CSS", "Bootstrap"],
            "Programacion formal": ["Java", "JavaScript", "C#"],
            "Bases de datos": {
                "Base de datos principal": input("Ingrese base de datos principal: "),
                "Base de datos Secundario": input("Ingrese base de datos secundaria: ")
            },
            "Backend": ["NetCore", "Spring Boot", "NodeJS","Express"]
        }
    }
    loadRutas.append(rutas)
    addRutas(loadRutas)
    os.system("pause")
    os.system("cls")

def search_ruta():
    os.system('cls')
    print("""
        #################################
        #      Busqueda de Rutas        #
        #################################
          """)
    buscarRuta=input("Ingrese la ID del Trainer a buscar: ")
    for student in loadruta:
        if buscarRuta in student:
            print(f"Ruta no encontrado.")
            break
    else:
        print(f"Ruta encontrado: {student}")
    os.system('pause')

def create_salas():
    os.system("cls")
    print("""
                *************************
                *    Creacion Sala      *
                *************************
    """)
    salas = {
        "Nombre": input("Ingrese Nombre de la sala: "),
        "Capacidad Mañana 1": 33,
        "Capacidad Mañana 2": 33,
        "Capacidad Tarde 1": 33,
        "Capacidad Tarde 2": 33,
        "Mañana jornada 1": 1,
        "Mañana jornada 2": 1,
        "Tarde jornada 1": 1,
        "Tarde jornada 2": 1
    }

    loadsalas.append(salas)
    addSalas(loadsalas)
    print("Sala Ingresada con exito")
    os.system("pause")
    os.system("cls")

def assigment_ruta():
    





# def Reportes():
#     os.system('cls')
#     print("""
#         #################################
#                #     REPORTES     #
#         #################################
#           """)
    
#     print(campers_totales)
#     print(trainers_ingresados)
#     os.system('pause')
import os
import json
from .variables import *
from modulos import *
from tabulate import tabulate
from .datos.funciones import *

studentAprobado="Aprobado"
studentRiesgo="En Riesgo"
studentInscrito="Pre-Inscrito"
Ruta_nodejs= "NodeJS"
Ruta_Java="Java"
Ruta_Core="NetCore"
estado= 'Pre-Inscrito'
trainer=''


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
                    case 1: editCamper()
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
                    case 1: editTrainer()
                    case 2: deleteDataTrainer()
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def Reportes():
    menu = ["Campers inscritos","campers que aproboran el examen inicial","lista de entrenadores","estudiantes con bajo rendimiento","campers y entrenadores asociados en una ruta","Campers que perdieron y aprobaron cada uno de los modulos","Regresar"]
    while(True):
        os.system("cls")
        print("""
                *************************
                *         Reportes      *
                *************************
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input(": "))
            if(opc<=len(menu) and opc>0):
                match (opc):
                    case 1: campers_inscritos()
                    case 2: campers_aprobaron()
                    case 3: readDataTrainerJson()
                    case 4: lowNotes()
                    case 5: campers_trainers_ruta()
                    case 6: pass
                    case 7: break
        except ValueError:
            print(f"La opcion no es valida")
            os.system("pause")

def createEstudiante():
    os.system('clear')
    print("""
        #################################
        #     Formulario del Camper     #
        #################################
          """)
    id_camper = int(input("Ingrese ID del camper: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    apellidos = input("Ingrese los apellidos del estudiante: ")
    direccion = input("Ingrese la dirección del estudiante: ")
    telefono_celular = input("Ingrese el teléfono celular del estudiante: ")
    telefono_fijo = input("Ingrese el teléfono fijo del estudiante: ")
    estado = "Inscrito"
    nuevo_camper = (id_camper, nombre, apellidos, direccion, telefono_celular, telefono_fijo, estado)
    campers_totales.append(nuevo_camper)

    data_camper={
        "ID": id_camper,
        "Nombre" : nombre,
        "Apellidos" : apellidos,
        "Direccion" : direccion,
        "Tel Celular" : telefono_celular,
        "Tel Fijo" : telefono_fijo 
    }

    try:
        with open('modulos/json/campers.json', "r") as archivo:
            datos_existentes = json.load(archivo)
    except FileNotFoundError:
        datos_existentes = []
    datos_existentes.append(data_camper)

    with open('modulos/json/campers.json', "w") as archivo:
        json.dump(datos_existentes, archivo, indent=4)

    print("Datos agregados con exito")

def searchStudent():
    os.system('clear')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscar = input("Ingrese la ID del camper a buscar: ")
    for student in campers_totales:
        if buscar in student:
            print(f"Camper encontrado: {student}")
            break
    else:
        print("Camper no encontrado.")

def editCamper():
    os.system('cls')
    print("""
    #####################################
    #           Editar Camper           #
    #####################################
        """)
    buscar=input("Ingrese la ID del camper a buscar: ")
    for i, student in enumerate(campers_totales):
        if buscar in student:
            print("Camper no encontrado")
            break
    else:
        nombre = input("Ingrese el nombre del estudiante: ")
        apellidos = input("Ingrese los apellidos del estudiante: ")
        direccion = input("Ingrese la dirección del estudiante: ")
        telefono_celular = input("Ingrese el teléfono celular del estudiante: ")
        telefono_fijo = input("Ingrese el teléfono fijo del estudiante: ")
        nuevo_camper = (nombre, apellidos, direccion, telefono_celular, telefono_fijo)
        campers_totales.append(nuevo_camper)

        data_camper={
        "Nombre" : input("Ingrese el nombre del estudiante: "),
        "Apellidos" : input("Ingrese los apellidos del estudiante: "),
        "Direccion" : input("Ingrese la dirección del estudiante: "),
        "Tel Celular" : input("Ingrese el teléfono celular del estudiante: "),
        "Tel Fijo" : input("Ingrese el teléfono fijo del estudiante: ")
        }

    try:
        with open('modulos/json/campers.json', "r") as archivo:
            datos_existentes = json.load(archivo)
    except FileNotFoundError:
        datos_existentes = []
    datos_existentes.append(data_camper)

    with open('modulos/json/campers.json', "w") as archivo:
        json.dump(datos_existentes, archivo, indent=4)
        os.system('pause')

def createTrainer():
    os.system('clear')
    print("""
        #################################
        #     Formulario Instructor     #
        #################################
          """)
    id_trainer = input("Ingrese ID del Trainer: ")
    nombre_trainer = input("Ingrese nombre del Trainer: ")
    especialidad = input("Ingrese especialidad del trainer: ")
    trainer_totales = (id_trainer, nombre_trainer, especialidad)
    Trainers.append(trainer_totales)

    data_trainer={
        "ID": id_trainer,
        "Nombre" : nombre_trainer,
        "Especialidad" : especialidad    
    }

    try:
        with open('modulos/json/campers.json', "r") as archivo:
            datos_existentes = json.load(archivo)
    except FileNotFoundError:
        datos_existentes = []
    datos_existentes.append(data_trainer)

    with open('modulos/json/campers.json', "w") as archivo:
        json.dump(datos_existentes, archivo, indent=4)

def searchTrainer():
    os.system('clear')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscarTrainer = input("Ingrese la ID del Trainer a buscar: ")
    for trainer in Trainers:
        if buscarTrainer in trainer:
            print(f"Trainer encontrado: {trainer}")
            break
    else:
        print("Trainer no encontrado.")

def editTrainer():
    os.system('cls')
    print("""
    #####################################
    #           Editar Trainer          #
    #####################################
        """)
    buscar=input("Ingrese la ID del Trainer a buscar: ")
    for i, trainer in enumerate(trainers_ingresados):
        if buscar in trainer:
            print("Camper no encontrado")
            break
    else:
        nombre= input("Ingrese el nuevo nombre: ")
        trainers_ingresados[i] = list(trainers_ingresados[i])  # Convertir la tupla a lista
        trainers_ingresados[i][1] = nombre
        apellido=input("Ingrese el nuevo apellido: ")
        trainers_ingresados[i][2] = apellido
        print("Cambios realizados con exito. ")
    os.system('pause')

def registrar_ruta():
    os.system("cls")
    print("""
                *************************
                *      Crear Rutas      *
                *************************
        """)
    datos = {
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

def campers_inscritos():
    imprimir_datos_camper()
    os.system('pause')

def campers_aprobaron():
    imprimir_datos_camper()
    os.system('pause')

def readDataTrainerJson():
    imprimir_datos_trainer()
    os.system('pause')

def lowNotes():
    imprimir_datos_evaluaciones()
    os.system('pause')

def campers_trainers_ruta():
    imprimir_datos_ruta_entrenamiento()
    os.system('pause')
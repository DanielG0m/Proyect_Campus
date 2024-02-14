import os
from .variables import *
from tabulate import tabulate

Camper= Camper()
RutaEntrenamiento= RutaEntrenamiento()
Prueba= Prueba()
AreaEntrenamiento= AreaEntrenamiento()
RutaEntrenamiento= RutaEntrenamientoCreada()
Entrenador= Entrenador()
Matricula= Matricula()
Evaluacion= Evaluacion()
studentAprobado="Aprovado"

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
    menu= ["Guardar","Buscar","Volver", "Salir"]
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
    menu= ["Actualizar","Prueba inicial","Notas Modulos","Salir"]
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
                    case 2: assigmentNotes()
                    case 3: modulesNotes()
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
    acudiente= input("Ingrese un acudiente: ")
    estado= 'Inscrito'
    nuevo_camper=(id, nombre, apellidos, direccion, acudiente, estado)

    campers_totales.append(nuevo_camper)
    print("Datos agregados con exito")
    os.system('pause')

# Hay que hacer un for que me ayude a leer los elementos de una lista dentro de otra lista
# y asi encuentre el id en cada uno, pensaba en usar LAMBDA

def searchStudent():
    os.system('cls')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscar_student=input("Ingrese la ID del camper a buscar: ")
    for student_camper in campers_totales:
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
    
    idTrainer = int(input("Ingrese ID del Trainer: "))
    nombreTrainer = input("Ingrese nombre del Trainer: ")
    trainer_totales=(idTrainer,nombreTrainer)

    trainers_ingresados.append(trainer_totales)
    print("Datos agregados con exito")
    os.system('pause')

def searchTrainer():
    os.system('cls')
    print("""
        #################################
        #         Buscar Camper         #
        #################################
          """)
    buscarTrainer=input("Ingrese la ID del Trainer a buscar: ")
    for student in trainers_ingresados:
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
        #####################################
        #     Menu Administrativo (campers) #
        #####################################
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
    menu= ["Cambiar Nombres y Apellidos","Cambiar Direccion y Acudiente", "Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #     Menu Administrativo (campers) #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                match opc:
                    case 1: nombreApellidoCamper()
                    case 2: direccionAcudienteCamper()
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')

def nombreApellidoCamper():
    buscar=input("Ingrese la ID del camper a buscar: ")
    for i, student in enumerate(campers_totales):
        if buscar in student:
            print("Camper no encontrado")
            break
    else:
        nombre= input("Ingrese el nuevo nombre: ")
        campers_totales[i] = list(campers_totales[i])  # Convertir la tupla a lista
        campers_totales[i][1] = nombre
        apellido=input("Ingrese el nuevo apellido: ")
        campers_totales[i][2] = apellido
        print("Cambios realizados con exito. ")
    os.system('pause')

def direccionAcudienteCamper():
    buscar=input("Ingrese la ID del camper a buscar: ")
    for i, student in enumerate(campers_totales):
        if buscar in student:
            print("Camper no encontrado")
            break
    else:
        direccion= input("Ingrese la nueva direccion: ")
        campers_totales[i] = list(campers_totales[i])  # Convertir la tupla a lista
        campers_totales[i][3] = direccion
        acudiente=input("Ingrese el nuevo acudiente: ")
        campers_totales[i][4] = acudiente
        print("Cambios realizados con exito. ")
    os.system('pause')

def deleteDataCamper():
    buscar=input("Ingrese la ID del camper a buscar: ")
    for i, student in enumerate(campers_totales):
        if buscar in student:
            print("Camper no encontrado")
            break
    else:
        del campers_totales[i]
        print("Camper eliminado...")
    os.system('pause')

def addDataTrainer():
    buscar=input("Ingrese la ID del camper a buscar: ")
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

def deleteDataTrainer():
    buscar=input("Ingrese la ID del camper a buscar: ")
    for i, trainer in enumerate(trainers_ingresados):
        if buscar in trainer:
            print("Camper no encontrado")
            break
    else:
        del trainers_ingresados[i]
        print("Camper eliminado...")
    os.system('pause')

def assigmentNotes():
    while True:
        buscar_student=int(input("Ingrese la ID del camper a buscar: "))
        for i, student in enumerate(campers_totales):
            if buscar_student in student:
                print(student)
                nota_teorica= int(input("Ingrese la nota teorica del estudiante: "))
                nota_practica= int(input("Ingrese la nota practica del estudiante: "))
                promedio=(nota_teorica + nota_practica)/2
                if promedio >= 60:
                    for i, student in enumerate(campers_totales):
                        if buscar_student in student:
                            campers_totales[i] = list(campers_totales[i])  # Convertir la tupla a lista
                            campers_totales[i][5] = studentAprobado
                            estudiantes_aprobados.append(campers_totales[i])
                            print(campers_totales[i])
                            print("El estado del camper ha sido pre-inscrito. ")
                            os.system('pause')
                            break
                elif promedio<60:
                            print("No paso la prueba")
                            break
            else:
                print("Camper no Encontrado")
                os.system('pause')
                break
        break




def Reportes():
    os.system('cls')
    print("""
        #################################
               #     REPORTES     #
        #################################
          """)
    
    print(campers_totales)
    print(trainers_ingresados)
    os.system('pause')
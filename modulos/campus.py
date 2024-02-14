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
    

def searchStudent():
    

def createTrainer():
    
def searchTrainer():
    
    
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
    

def direccionAcudienteCamper():


def deleteDataCamper():
  

def addDataTrainer():


def deleteDataTrainer():

def assigmentNotes():
  

def modulesNotes():


def Reportes():
    os.system('cls')
    print("""
        #################################
               #     REPORTES     #
        #################################
          """)
    table_campers_totales=[campers_totales]
    print(inscritos_inscritos)
    print(estudiantes_aprobados)
    print(trainers_ingresados)
    print("")
    print("Campers con bajo rendimiento")
    print(bajo_rendimiento)

    print("")
    print(tabulate(table_campers_totales, headers=["ID","Nombre", "Apellidos", "Direccion", "Acudiente", "Estado", "Ruta", "Trainer", "Sala", "Horario"] ))

    os.system('pause')
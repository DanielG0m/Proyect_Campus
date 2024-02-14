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


loadruta=loadRutas()

loadsalas=loadSalas()


loadclases=loadClases()


loadnotas=loadNotas()

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
    os.system("cls")
    print("""
        ***********************
        *   Asingar Clases    *
        ***********************
    """)
    buscar_student = input("Ingrese la ID del camper a buscar: ")
    codigo_trainer = int(input("Ingrese codigo del profesor: "))
    codigo_ruta = int(input("Ingrese codigo de rutas: "))
    horario = input("Ingrese el horario del estudiante (Mañana/Tarde): ")
    for student_camper in data:
        if buscar_student in student_camper:
            print("Camper no encontrado")
            break
        else:
            print(f"Camper encontrado: {student_camper}")
    os.system('pause')

    if horario not in ["Mañana", "Tarde"]:
        print("Horario ingresado no valido. ")
        os.system("pause")
        os.system("cls")
        return
    
    elegir_sala = None
    for sala in data_trainer.get("Salas elegidas", []):
        if sala["Horario"] == f"{horario} jornada 1":
            elegir_sala = sala
            break
        elif sala["Horario"] == f"{horario} jornada 2":
            elegir_sala = sala
            break

    if not elegir_sala:
        print("El profesor no tiene asignada una sala para el horario ingresado.")
        os.system("pause")
        os.system("cls")
        return
    
    clase = loadsalas[elegir_sala["Codigo de la sala"] - 1]
    capacidad_key = f"Capacidad {horario} {elegir_sala['Codigo de la sala']}"
    
    if data_camper["Estado"] == "Inscrito" and clase[capacidad_key] > 0:
        var = {
            "Nombre": data_camper.get("Nombre"),
            "ID": data_camper.get("ID"),
            "Ruta": loadruta.get("Nombre"),
            "Modulos": loadruta.get('Modulos'),
            "Trainer": data_trainer.get("Nombre"),
            "Sala": loadclases.get("Nombre"),
            "FechaInicio": input("Ingrese fecha de inicio DD/MM/YYYY: "),
            "FechaFinalizacion": input("Ingrese fecha de finalizacion DD/MM/YYYY: ")
        }
        addclases.append(var)
        addsalas(loadsalas)
        addsalas(loadclases)
        print("Estudiante ingresado a la clase con exito")
    else:
        print("El camper no está en estado Inscrito O la sala ya cuenta con 33 estudiantes ")
    os.system("pause")
    os.system("cls") 

def notas():
    os.system("cls")
    print("""
        ***********************
        *    Notas Campers    *
        ***********************
    """)
    print("""
        Que modulo quieres evaluar al camper
        1 - Fundamentos de programacion
        2 - programacion web 
        3 - programacion formal
        4 - Base de datos
        5 - Backend
        6 - Salir
            """)
    
    calificar = {
        1: "Fundamentos",
        2: "Programacion web",
        3: "Programacion formal",
        4: "Base de datos",
        5: "backend"
    }

    while(True):
        opc = int(input(": "))
        if opc == 6:
            break
        if opc not in calificar:
            print("Opcion invalida. ")
            continue

        moduloElegido = calificar[opc]
        buscar_camper= int(input("Ingrese codigo del camper a calificar: "))

        for i, val in enumerate(notas, start=0):
            if val.get("ID") == buscar_camper:
                pruebaTeorica = int(input("Ingrese nota de la prueba teorica: "))
                pruebaPractica = int(input("Ingrese nota de la prueba practica: "))
                notasVarias = int(input("Se hizo mas de una actividad tipo quiz, trabajo o examen. si es asi inserte cuantas actividades hubo: "))
                notasModulo = []
                for i in range(notasVarias):
                    actividad = int(input(f"Ingrese nota de la actividad {i+1}: "))
                    notasModulo.append(actividad)
                
                totalNotas =  (sum(notasModulo) / notasVarias) * 0.10
                TotalTeorica = pruebaTeorica * 0.30
                TotalPractica =  pruebaPractica * 0.60
                Resultado = totalNotas + TotalPractica + TotalTeorica
                
                if Resultado >= 60:
                    val[moduloElegido] = "Aprobado"
                    val["Estado Actual"] = "Cursando"
                else: 
                    val[moduloElegido] = "Desaprobado"
                    val["Reportado"] += 1
                    if val["Reportado"] == 1:
                        print("El camper ha sido reportado por bajo rendimiento en este módulo.")
                        val["Estado Actual"] = "Riesgo"
                    elif val["Reportado"] == 2:
                        print("El camper ha sido reportado por bajo rendimiento en este módulo y otro más.")
                        val["Estado Actual"] = "Bajo rendimiento"
                        val["Reportado"] += 2 
                        break
        addnotas(notas)
        otro = input("¿Desea elegir otro módulo? (s/n): ")
        if otro.lower() != "s":
            break

def campers_riesgos():
    os.system("cls")
    for i,val in enumerate(loadnotas, start=0):
        if val["Estado Actual"] == "Riesgo":
            print(f"""
            ____________________________
            Codigo: {val.get("codigo")}
            Nombre: {val.get("Nombre")}
            ____________________________
            """)
    os.system("pause")

def campers_incritos():
    os.system("cls")
    for i,val in enumerate(data_camper, start=0):
        if val["Estado"] == "Inscrito":
            print(f"""
            ___________________________
            Codigo: {i+1}
            Nombre: {val.get("Nombre")}
            CC: {val.get("CC")}
            Estado: {val.get("Estado")}
            ____________________________
            """)
    
    os.system("pause")
        
def campers_aprobaron():
    os.system("cls")
    for i,val in enumerate(data_camper, start=0):
        if val['Examen 1'] == "Aprobado":
            print(f"""
            ___________________________
            Codigo: {i+1}
            Nombre: {val.get("Nombre")}
            CC: {val.get("CC")}
            ___________________________
            """)
    os.system("pause")

def campers_bajo_rendimiento():
    os.system("cls")
    for i,val in enumerate(loadnotas, start=0):
        if val["Estado Actual"] == "Bajo rendimiento":
            print(f"""
            ____________________________
            Codigo: {val.get("codigo")}
            Nombre: {val.get("Nombre")}
            ____________________________
            """)
    os.system("pause")

def campers_trainers_ruta():
    os.system("cls")
    Ruta = input("Ingrese nombre de la ruta que quieres ver: ")
    trainer = input("Ingrese nombre del trainer: ")

    print(f"Estos son los estudiantes que estan con el trainer {trainer} en la ruta de {Ruta}")
    for i,val in enumerate(loadclases, start=0):
            if Ruta == val['Ruta'] and trainer == val['Trainer']:
                print(f"""
                ______________________________
                Nombre: {val.get("Nombre")}
                CC: {val.get("CC")}
                """)
    os.system("pause")

def Campers_Aprobaron_Perdieron():
    while(True):
        os.system("cls")
        print("""
            Que modulo quieres ver 
            1 - Fundamentos de programacion
            2 - programacion web 
            3 - programacion formal
            4 - Base de datos
            5 - Backend
            6 - Salir
                """)
        modulos = {
            1: "Fundamentos",
            2: "Programacion web",
            3: "Programacion formal",
            4: "Base de datos",
            5: "backend"
        }
        opc = int(input(": "))
        if opc == 6:
            break
        if opc not in modulos:
            print("Opcion invalida. ")
            continue

        moduloElegido = modulos[opc]
        trainer = input("Ingrese nombre del trainer: ")
        ruta = input("Ingrese nombre de la ruta: ")

        campers_aprobaron = []
        campers_perdieron = []

        for camper in notas:
            if camper['Nombre'] in [camp['Nombre'] for camp in loadclases if camp['Ruta'] == ruta and camp['Trainer'] == trainer]:
                if camper[moduloElegido] == "Aprobado":
                    campers_aprobaron.append(camper)
                elif camper[moduloElegido] == "Desaprobado":
                    campers_perdieron.append(camper)
        
        print(f"Campers que aprobaron en el módulo {moduloElegido}:")
        for camper in campers_aprobaron:
            print(f"Nombre: {camper['Nombre']}")

        print(f"\nCampers que perdieron en el módulo {moduloElegido}:")
        for camper in campers_perdieron:
            print(f"Nombre: {camper['Nombre']}")

        otro = input("¿Desea elegir otro módulo? (s/n): ")
        if otro.lower() != "s":
            break


def Reportes():
    menu = ["Campers inscritos","campers que aproboran el examen inicial","lista de entrenadores","estudiantes con bajo rendimiento","campers y entrenadores asociados en una ruta","Campers que perdieron y aprobaron cada uno de los modulos","Regresar"]
    while(True):
        os.system("cls")
        print("""
                *************************
                *       Menu Notas      *
                *************************
            """)
        print("".join([f"{i+1}. {val}\n" for i,val in enumerate(menu)]))
        try:
            opc = int(input(": "))
            if(opc<=len(menu) and opc>0):
                match (opc):
                    case 1: campers_incritos()
                    case 2: campers_aprobaron()
                    case 3: readDataTrainerJson()
                    case 4: campers_bajo_rendimiento()
                    case 5: campers_trainers_ruta()
                    case 6: Campers_Aprobaron_Perdieron()
                    case 7: break
        except ValueError:
            print(f"La opcion no es valida")
            os.system("pause")
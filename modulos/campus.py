import os
from .campersFunciones import nuevoEstudiante, buscarEstudiante
from .trainersFunciones import nuevoTrainer, buscarEntrenador
from .administracionFunciones import actualizarDatos, registrarRuta, listarRutas, registrarSala, listarSalas, asignarRuta, actualizarNotas
from .reportesFunciones import listarCampersInscritos, listarCampersAprobados, listarTrainers, listarCampersRendimientoBajo, listarCampersTrainersRuta, mostrarModulosAprobados

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
                    case 1: nuevoEstudiante()
                    case 2: buscarEstudiante()
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
                    case 1: nuevoTrainer()
                    case 2: buscarEntrenador()
                    case 3: break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')
            
def Administracion():
    menu= ["Actualizar Datos","Registrar Rutas","Listar Rutas", "Registrar Sala", "Listar Sala", "Asignar Rutas", "Actualizar Notas", "Salir"]
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
                    case 1: actualizarDatos()
                    case 2: registrarRuta()
                    case 3: listarRutas()
                    case 4: registrarSala()
                    case 5: listarSalas()
                    case 6: asignarRuta()
                    case 7: actualizarNotas()
                    case 8: break
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
                    case 1: listarCampersInscritos()
                    case 2: listarCampersAprobados()
                    case 3: listarTrainers()
                    case 4: listarCampersRendimientoBajo()
                    case 5: listarCampersTrainersRuta()
                    case 6: mostrarModulosAprobados()
                    case 7: break
        except ValueError:
            print(f"La opcion no es valida")
            os.system("pause")
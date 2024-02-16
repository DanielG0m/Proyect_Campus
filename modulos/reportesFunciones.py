import os
from .funciones import cargarCampers, cargarTrainers, cargarNotas, cargarRutas

def listarCampersInscritos():
    campers = cargarCampers()
    inscritos = [camper for camper in campers if camper["Estado"] == "Inscrito"]
    
    if inscritos:
        print("Campers inscritos:")
        for camper in inscritos:
            print(f"{camper['Nombre']} {camper['Apellido']}")
    else:
        print("No hay campers inscritos.")
        os.system('pause')

def listarCampersAprobados():
    campers = cargarCampers()
    aprobados = [camper for camper in campers if camper["Examen 1"] == "Aprobado" and camper["Examen 2"] == "Aprobado"]
    
    if aprobados:
        print("Campers que aprobaron el examen inicial:")
        for camper in aprobados:
            print(f"{camper['Nombre']} {camper['Apellido']}")
            os.system('pause')
    else:
        print("No hay campers que aprobaron el examen inicial.")
        os.system('pause')

def listarTrainers():
    trainers = cargarTrainers()
    if trainers:
        print("Lista de todos los entrenadores:")
        for trainer in trainers:
            print(f"{trainer['Nombre']} {trainer['Apellido']}")
            os.system('pause')
    else:
        print("No hay entrenadores registrados.")
        os.system('pause')

def listarCampersRendimientoBajo():
    campers = cargarCampers()
    bajo_rendimiento = [camper for camper in campers if camper["Estado"] == "Bajo rendimiento"]
    
    if bajo_rendimiento:
        print("Campers con bajo rendimiento:")
        for camper in bajo_rendimiento:
            print(f"{camper['Nombre']} {camper['Apellido']}")
            os.system('pause')
    else:
        print("No hay campers con bajo rendimiento.")
        os.system('pause')

def listarCampersTrainersRuta():
    campers = cargarCampers()
    trainers = cargarTrainers()
    ruta = input("Ingrese el nombre de la ruta de entrenamiento: ")
    campers_trainer_ruta = [camper for camper in campers if camper.get("Ruta", "") == ruta]
    trainers_ruta = [trainer for trainer in trainers if trainer.get("Ruta", "") == ruta]
    
    if campers_trainer_ruta:
        print(f"Campers asociados a la ruta {ruta}:")
        for camper in campers_trainer_ruta:
            print(f"{camper['Nombre']} {camper['Apellido']}")
            os.system('pause')
    else:
        print(f"No hay campers asociados a la ruta {ruta}.")
        os.system('pause')
    
    if trainers_ruta:
        print(f"Entrenadores asociados a la ruta {ruta}:")
        for trainer in trainers_ruta:
            print(f"{trainer['Nombre']} {trainer['Apellido']}")
            os.system('pause')
    else:
        print(f"No hay entrenadores asociados a la ruta {ruta}.")
        os.system('pause')

def mostrarModulosAprobados():
    campers = cargarCampers()
    ruta = input("Ingrese el nombre de la ruta de entrenamiento: ")
    modulos_aprobados = {}
    for camper in campers:
        if camper.get("Ruta", "") == ruta:
            for modulo, estado in camper.items():
                if modulo.startswith("Modulo") and estado == "Aprobado":
                    modulos_aprobados.setdefault(modulo, 0)
                    modulos_aprobados[modulo] += 1
                    os.system('pause')
    
    print(f"Aprobaciones de módulos para la ruta {ruta}:")
    for modulo, cantidad in modulos_aprobados.items():
        print(f"{modulo}: {cantidad} campers aprobados.")
        os.system('pause')

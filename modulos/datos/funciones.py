from .datos import *

def imprimir_datos_camper():
    campers = cargar_datos_camper()

    print("Campers cargados:")
    for camper in campers:
        for key, value in camper.items():
            print(f"{key}: {value}")
        print()
        
def imprimir_busqueda_camper(valor):
    resultados = buscar_datos_camper(valor)
    print("Campers cargados:")
    for resultado in resultados:
        for key, value in resultado.items():
            print(f"{key}: {value}")
        print()
    
def guardar_datos_camper(datos):
    guardar_datos_camper(datos)
    
def imprimir_datos_trainer():
    trainers = cargar_datos_trainer()

    print("Trainer cargados:")
    for trainer in trainers:
        for key, value in trainer.items():
            print(f"{key}: {value}")
        print()
        
def imprimir_busqueda_trainer(valor):
    resultados = buscar_datos_trainer(valor)
    print("Trainer cargados:")
    for resultado in resultados:
        for key, value in resultado.items():
            print(f"{key}: {value}")
        print()
    
def guardar_datos_trainer(datos):
    guardar_datos_trainer(datos)
    
def imprimir_datos_ruta_entrenamiento():
    rutas = cargar_datos_ruta_entrenamiento()

    print("Rutas de Entrenamiento cargadas:")
    for ruta in rutas:
        for key, value in ruta.items():
            print(f"{key}: {value}")
        print()
        
def imprimir_busqueda_ruta(valor):
    resultados = buscar_datos_ruta_entrenamiento(valor)
    print("Rutas de Entrenamiento cargadas:")
    for resultado in resultados:
        for key, value in resultado.items():
            print(f"{key}: {value}")
        print()
        
def guardar_datos_ruta(datos):
    guardar_datos_ruta_entrenamiento(datos)
    
def imprimir_datos_evaluaciones():
    rutas = cargar_datos_evaluaciones()

    print("Rutas de Entrenamiento cargadas:")
    for ruta in rutas:
        for key, value in ruta.items():
            print(f"{key}: {value}")
        print()
        
def imprimir_busqueda_evaluaciones(valor):
    resultados = buscar_datos_evaluaciones(valor)
    print("Rutas de Entrenamiento cargadas:")
    for resultado in resultados:
        for key, value in resultado.items():
            print(f"{key}: {value}")
        print()
        
def guardar_datos_evaluacion(datos):
    guardar_datos_evaluaciones(datos)
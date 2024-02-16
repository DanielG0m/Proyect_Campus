import os
import json

ruta_directorio_actual = os.path.dirname(os.path.abspath(__file__))

ruta_json_camper = os.path.join(ruta_directorio_actual, 'datos_camper.json')
ruta_json_trainer = os.path.join(ruta_directorio_actual, 'datos_trainer.json')
ruta_json_ruta_entrenamiento = os.path.join(ruta_directorio_actual, 'datos_ruta_entrenamiento.json')
ruta_json_evaluaciones = os.path.join(ruta_directorio_actual, 'datos_evaluaciones.json')
    
def cargar_datos_camper():
    with open(ruta_json_camper) as json_file:
        campers = json.load(json_file)
    return campers

def guardar_datos_camper(datos):
    with open(ruta_json_camper) as json_file:
        json.dump(datos, json_file, indent=9)
        
def buscar_datos_camper(valor):
    with open(ruta_json_camper) as json_file:
        campers = json.load(json_file)
             
    resultados = []
    
    for camper in campers:
        if camper["id_camper"] == valor:
            resultados.append(camper)
        elif camper["nombre_camper"] == valor:
            resultados.append(camper)
        elif camper["apellidos_camper"] == valor:
            resultados.append(camper)
    
    return resultados

def cargar_datos_trainer():
    with open(ruta_json_trainer) as json_file:
        trainer = json.load(json_file)
    return trainer

def guardar_datos_trainer(datos):
    with open(ruta_json_trainer) as json_file:
        json.dump(datos, json_file, indent=4)
        
def buscar_datos_trainer(valor):
    with open(ruta_json_trainer) as json_file:
        trainers = json.load(json_file)
             
    resultados = []
    
    for trainer in trainers:
        if trainer["id_trainer"] == valor:
            resultados.append(trainer)
        elif trainer["nombre_trainer"] == valor:
            resultados.append(trainer)
        elif trainer["apellidos_trainer"] == valor:
            resultados.append(trainer)
    
    return resultados

def cargar_datos_ruta_entrenamiento():
    with open(ruta_json_ruta_entrenamiento) as json_file:
        rutas = json.load(json_file)
    return rutas

def guardar_datos_ruta_entrenamiento(datos):
    with open(ruta_json_ruta_entrenamiento) as json_file:
        json.dump(datos, json_file, indent=5)
        
def buscar_datos_ruta_entrenamiento(valor):
    with open(ruta_json_ruta_entrenamiento) as json_file:
        rutas = json.load(json_file)
             
    resultados = []
    
    for ruta in rutas:
        if ruta["nombre"] == valor:
            resultados.append(ruta)
        elif ruta["area"] == valor:
            resultados.append(ruta)
    
    return resultados

def cargar_datos_evaluaciones():
    with open(ruta_json_evaluaciones) as json_file:
        evaluaciones = json.load(json_file)
    return evaluaciones

def guardar_datos_evaluaciones(datos):
    with open(ruta_json_evaluaciones) as json_file:
        json.dump(datos, json_file, indent=5)
        
def buscar_datos_evaluaciones(valor):
    with open(ruta_json_evaluaciones) as json_file:
        evaluaciones = json.load(json_file)
             
    resultados = []
    
    for evaluacion in evaluaciones:
        if evaluacion["id_camper"] == valor:
            resultados.append(evaluacion)
        elif evaluacion["ruta_entrenamiento"] == valor:
            resultados.append(evaluacion)
    
    return resultados
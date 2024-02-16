import json

def guardarCamper(datos):
    try:
        with open('modulos/json/campers.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    
    for existing_camper in existing_data:
        if existing_camper["Id Camper"] == datos["Id Camper"]:
            existing_camper.update(datos)
            break
    else:
        existing_data.append(datos)
    
    with open('modulos/json/campers.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

def guardarCamper2(campers):
    with open('modulos/json/campers.json', 'w') as file:
        json.dump(campers, file, indent=4)
        
def cargarCamper():
    try:
        with open('modulos/json/campers.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def buscarCampers(valor):
    campers = cargarCamper()
    
    resultado = []
    
    for camper in campers:
        if camper["Id Camper"] == valor:
            resultado.append(camper)
    
    return resultado



import json

def guardarSala(datos):
    try:
        with open('modulos/json/salas.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
        
    existing_data.append(datos)
    
    with open('modulos/json/salas.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
        
def cargarSala():
    try:
        with open('modulos/json/salas.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def buscarSala(valor):
    salas = cargarSala()
    
    resultado = []
    
    for sala in salas:
        if sala["Nombre"] == valor:
            resultado.append(sala)
    
    return resultado                                                                        
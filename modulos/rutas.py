import json

def guardarRuta(datos):
    try:
        with open('modulos/json/rutas.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
        
    existing_data.append(datos)
    
    with open('modulos/json/rutas.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
        
def cargarRuta():
    try:
        with open('modulos/json/rutas.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def buscarRuta(valor):
    salas = cargarRuta()
    
    resultado = []
    
    for sala in salas:
        if sala["Nombre"] == valor:
            resultado.append(sala)
    
    return resultado                                                                        
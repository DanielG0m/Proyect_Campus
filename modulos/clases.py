import json

def guardarClase(datos):
    try:
        with open('modulos/json/clases.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
        
    existing_data.append(datos)
    
    with open('modulos/json/clases.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
        
def cargarClase():
    try:
        with open('modulos/json/clases.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def buscarClase(valor):
    clases = cargarClase()
    
    resultado = []
    
    for clase in clases:
        if clase["Nombre"] == valor:
            resultado.append(clase)
    
    return resultado                                                                        
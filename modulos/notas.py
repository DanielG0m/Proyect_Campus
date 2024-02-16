import json

def guardarNota(datos):
    try:
        with open('modulos/json/notas.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
        
    existing_data.append(datos)
    
    with open('modulos/json/notas.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
        
def cargarNota():
    try:
        with open('modulos/json/notas.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def buscarNota(valor):
    notas = cargarNota()
    
    resultado = []
    
    for nota in notas:
        if nota["Nombre"] == valor:
            resultado.append(nota)
    
    return resultado                                                                        
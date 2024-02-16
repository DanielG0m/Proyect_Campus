import json

def guardarTrainer(datos):
    try:
        with open('modulos/json/trainers.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    
    for existing_trainer in existing_data:
        if existing_trainer["Id Trainer"] == datos["Id Trainer"]:
            existing_trainer.update(datos)
            break
    else:
        existing_data.append(datos)
    
    with open('modulos/json/trainers.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

def guardarTrainer2(trainers):
    with open('modulos/json/trainers.json', 'w') as file:
        json.dump(trainers, file, indent=4)

def cargarTrainer():
    try:
        with open('modulos/json/trainers.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    if isinstance(data[-1], list):
            data = data[:-1]
    return data

def buscarTrainers(valor):
    trainers = cargarTrainer()
    
    resultado = []
    
    for trainer in trainers:
        if trainer["Id Trainer"] == valor:
            resultado.append(trainer)
    
    return resultado
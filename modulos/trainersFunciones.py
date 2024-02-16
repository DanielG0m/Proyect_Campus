import os
from .funciones import guardarTrainers, cargarCampers, cargarTrainers, cargarSalas, imprimirBusquedaTrainer, buscarTrainer

def nuevoTrainer():
    os.system('clear')
    print("""
                *************************
                *     Crear Trainer     *
                *************************
        """)
    
    campers = cargarCampers()
    trainers = cargarTrainers()
    salas = cargarSalas()
    
    idTrainer = verificarId(trainers, campers)
    nombre = input("Ingrese nombre del Trainer: ")
    apellido = input("Ingrese apellido del Trainer: ")
    salasElegidas = seleccionarSalas(salas)
    
    trainer = {
        "Id Trainer": idTrainer,
        "Nombre": nombre,
        "Apellido" : apellido,
        "Salas elegidas": salasElegidas
    }
    
    guardarTrainers(trainer)

def buscarEntrenador():
    os.system('clear')
    print("""
        #################################
        #         Buscar Trainer         #
        #################################
          """)
    
    buscar = input("Ingrese la ID del trainer a buscar: ")
    
    resultados = buscarTrainer(buscar)

    if not resultados:
        print("No se encontró ningún trainer con la ID proporcionada.")
    else:
        imprimirBusquedaTrainer(buscar)

def verificarId(trainers, campers):
    while True:
        idTrainer = input("Ingrese cédula del Trainer: ")
        
        if any(trainer.get("Id Trainer") == idTrainer for trainer in trainers):
            print("La cédula ingresada ya existe en los datos de los trainers.")
            os.system("pause")
            continue
        
        if any(camper.get("Id Camper") == idTrainer for camper in campers):
            print("La cédula ingresada ya existe en los datos de los campers.")
            os.system("pause")
            continue
        
        return idTrainer
    
def seleccionarSalas(salas):
    salas_disponibles = [sala for sala in salas if any(sala.get(horario) == 0 for horario in ["Manana jornada 1", "Manana jornada 2", "Tarde jornada 1", "Tarde jornada 2"])]
    
    if not salas_disponibles:
        print("No hay salas disponibles en ningún horario.")
        return []

    salas_elegidas = []
    while True:
        print("Salas disponibles:")
        for i, sala in enumerate(salas_disponibles, start=1):
            print(f"{i}. {sala['Nombre']}")
        
        opcion_sala = int(input("Ingrese el número correspondiente a la sala deseada: "))
        if opcion_sala < 1 or opcion_sala > len(salas_disponibles):
            print("Opción inválida. Por favor, ingrese un número válido.")
            continue
        
        sala_elegida = salas_disponibles[opcion_sala - 1]
        
        print("""
            Horarios disponibles:
            1. Mañana jornada 1
            2. Mañana jornada 2
            3. Tarde jornada 1
            4. Tarde jornada 2
        """)

        opcion_horario = int(input("Ingrese el número correspondiente al horario deseado: "))
        
        horarios = {
            1: "Manana jornada 1",
            2: "Manana jornada 2",
            3: "Tarde jornada 1",
            4: "Tarde jornada 2"
        }
        
        if opcion_horario not in horarios:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")
            continue
        
        horario_elegido = horarios[opcion_horario]
        
        if sala_elegida[horario_elegido] > 0:
            print("Esa sala en este horario ya está ocupada.")
            continue
        
        sala_elegida[horario_elegido] += 1
        salas_elegidas.append({
            "Nombre": sala_elegida["Nombre"],
            "Horario": horario_elegido,
            "Codigo de la sala": opcion_sala
            
        })
        
        otro = input("¿Desea elegir otra sala? (s/n): ")
        if otro.lower() != "s":
            break
    
    return salas_elegidas

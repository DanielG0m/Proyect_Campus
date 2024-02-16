from .campers import guardarCamper, cargarCamper, buscarCampers, guardarCamper2
from .trainers import guardarTrainer, cargarTrainer, buscarTrainers, guardarTrainer2
from .salas import cargarSala, guardarSala
from .rutas import cargarRuta, guardarRuta
from .clases import cargarClase, guardarClase
from .notas import cargarNota, guardarNota

##  CAMPERS

def guardarCampers(datos):
    guardarCamper(datos)

def guardarCampers2(datos):
    guardarCamper2(datos)
        
def cargarCampers():
    campers = cargarCamper()
    return campers
    
def imprimirCamper():
    campers = cargarCamper()
    
    print("Campers cargados:")
    
    for camper in campers:
        print("Id Camper:", camper["Id Camper"])
        print("Nombre:", camper["Nombre"])
        print("Apellido:", camper["Apellido"])
        print("Direccion:", camper["Direccion"])
        print("Acudiente:", camper["Acudiente"])
        print("Telefonos:")
        for tipo, numero in camper["Telefonos"].items():
            print(f"  {tipo}: {numero}")
        
        print("Estado:", camper["Estado"])
        print("Examen 1:", camper["Examen 1"])
        print("Examen 2:", camper["Examen 2"])
        print()
        
def imprimirBusquedaCamper(valor):
    resultados = buscarCampers(valor)
    
    print("Camper:")
        
    for resultado in resultados:
        print("Id Camper:", resultado["Id Camper"])
        print("Nombre:", resultado["Nombre"])
        print("Apellido:", resultado["Apellido"])
        print("Direccion:", resultado["Direccion"])
        print("Acudiente:", resultado["Acudiente"])
        print("Telefonos:")
        for tipo, numero in resultado["Telefonos"].items():
            print(f"  {tipo}: {numero}")
            
        print("Estado:", resultado["Estado"])
        print("Examen 1:", resultado["Examen 1"])
        print("Examen 2:", resultado["Examen 2"])
        print()
  
def buscarCamper(IdCamper):
    campers = cargarCamper()
    
    for camper in campers:
        if camper["Id Camper"] == IdCamper:
            return camper
    
    return None

def editarCamper(id_camper):
    campers = cargarCamper()
    for index, camper in enumerate(campers):
        if camper["Id Camper"] == id_camper:
            print(f"Editando datos del Camper con ID {id_camper}...")
            
            nuevo_nombre = input("Ingrese el nuevo nombre del Camper: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del Camper: ")

            camper_modificado = {
                "Id Camper": id_camper,
                "Nombre": nuevo_nombre,
                "Apellido": nuevo_apellido
            }
            
            guardarCamper(camper_modificado)
            print("Datos del Camper actualizados correctamente.")
            return
    print(f"No se encontró ningún Camper con la ID {id_camper}.")

def borrarCamper(id_camper):
    campers = cargarCamper()
    index = 0
    while index < len(campers):
        if campers[index]["Id Camper"] == id_camper:
            print(f"Eliminando Camper con ID {id_camper}...")
            del campers[index]
            guardarCampers2(campers) 
            print("Camper eliminado correctamente.")
            return
        index += 1
    print(f"No se encontró ningún Camper con la ID {id_camper}.")
    
##  TRAINERS

def guardarTrainers(datos):
    guardarTrainer(datos)

def guardarTrainers2(datos):
    guardarTrainer2()

def cargarTrainers():
    trainers = cargarTrainer()
    return trainers

def imprimirBusquedaTrainer(valor):
    resultados = buscarTrainers(valor)
    
    if resultados:
        print("Trainers encontrados:")
        
        for resultado in resultados:
            print("Id Trainer:", resultado["Id Trainer"])
            print("Nombre:", resultado["Nombre"])
            print("Apellido:", resultado["Apellido"])
            print("Salas elegidas:")
            for sala in resultado["Salas elegidas"]:
                print(f"  Sala Elegida: {sala['Nombre']}")
                print(f"  Horario: {sala['Horario']}")
                print(f"  Código de la sala: {sala['Codigo de la sala']}")
            print()
      
def buscarTrainer(IdTrainer):
    trainers = cargarTrainer()
    
    for trainer in trainers:
        if trainer["Id Trainer"] == IdTrainer:
            return trainer
    
    return None

def editarTrainer(id_trainer):
    trainers = cargarTrainer()
    for index, trainer in enumerate(trainers):
        if trainer["Id Trainer"] == id_trainer:
            print(f"Editando datos del Trainer con ID {id_trainer}...")
            
            nuevo_nombre = input("Ingrese el nuevo nombre del Trainer: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del Trainer: ")
            
            trainer_modificado = {
                "Id Trainer": id_trainer,
                "Nombre": nuevo_nombre,
                "Apellido": nuevo_apellido
            }
            
            guardarTrainer(trainer_modificado)
            print("Datos del Trainer actualizados correctamente.")
            return
    
    print(f"No se encontró ningún Trainer con la ID {id_trainer}.")


def borrarTrainers():
    id_trainer = input("Ingrese la ID del trainer a eliminar: ")
    borrarTrainer(id_trainer)

def borrarTrainer(id_trainer):
    trainers = cargarTrainer()
    for trainer in trainers:
        if trainer["Id Trainer"] == id_trainer:
            
            salas_elegidas = trainer.get("Salas elegidas", [])
            
            for sala in salas_elegidas:
                if "Nombre" in sala:  # Verificar si el campo "Nombre" está presente
                    nombre_sala = sala["Nombre"]
                    horario = sala["Horario"]
                    codigo_sala = sala["Codigo de la sala"]
                
                    salas = cargarSalas()
                    for sala_db in salas:
                        if sala_db["Nombre"] == nombre_sala and sala_db[horario] > 0:
                        
                            sala_db[horario] -= 1
                
                    guardarSala(salas)
            
            print(f"Eliminando Trainer con ID {id_trainer}...")
            trainers.remove(trainer)
            guardarTrainer2(trainers)  # Pasar la lista de entrenadores como argumento
            print("Trainer eliminado correctamente.")
            return
    print(f"No se encontró ningún Trainer con la ID {id_trainer}.")




##  SALAS

def guardarSalas(datos):
    guardarSala(datos)

def cargarSalas():
    salas = cargarSala()
    return salas

##  RUTAS

def guardarRutas(datos):
    guardarRuta(datos)

def cargarRutas():
    rutas = cargarRuta()
    return rutas

##  CLASES

def guardarClases(datos):
    guardarClase(datos)

def cargarClases():
    clases = cargarClase()
    return clases

##  NOTAS

def guardarNotas():
    guardarNota()

def cargarNotas():
    notas = cargarNota()
    return notas
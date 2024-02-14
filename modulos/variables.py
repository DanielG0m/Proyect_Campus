from abc import ABC, abstractmethod
import json

class Persona(ABC):
    @abstractmethod
    def Datos(self, id, nombre, apellidos, direccion, telefono_celular, telefono_fijo,estado):
        pass

class Entrenamiento(ABC):
    @abstractmethod
    def datos_entrenamiento(self, nombre, stack_tecnologico, capacidad_maxima):
        pass

class Prueba(ABC):
    @abstractmethod
    def datos_prueba(self, camper, nota_teorica, nota_practica):
        pass

    @abstractmethod
    def es_aprobada(self):
        pass

class Espacio(ABC):
    @abstractmethod
    def lugar(self, nombre, capacidad_maxima):
        pass

class RutaEntrenamientoCreada(ABC):
    @abstractmethod
    def ruta(self, ruta_entrenamiento, sgdb_principal, sgdb_alternativo):
        pass

class Instructor(ABC):
    @abstractmethod
    def trainer(self, nombre, rutas_entrenamiento):
        pass

class Matricula(ABC):
    @abstractmethod
    def ingreso(self, camper, ruta_entrenamiento, entrenador, fecha_inicio, fecha_finalizacion, salon_entrenamiento):
        pass

class Evaluacion(ABC):
    @abstractmethod
    def examen(self, camper, modulo, nota_teoria, nota_practica, quices_trabajos):
        pass

    @abstractmethod
    def es_aprobada(self):
        pass

class Camper(Persona):
    def Datos(self, id, nombre, apellidos, direccion, telefono_celular, telefono_fijo,estado):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono_celular = telefono_celular
        self.telefono_fijo = telefono_fijo
        self.estado = estado

class RutaEntrenamiento(Entrenamiento):
    def datos_entrenamiento(self, nombre, stack_tecnologico, capacidad_maxima):
        self.nombre = nombre
        self.stack_tecnologico= stack_tecnologico
        self.capacidad_maxima= capacidad_maxima

class Prueba(Prueba):
    def datos_prueba(self, camper, nota_teorica, nota_practica):
        self.camper = camper
        self.nota_teorica=nota_teorica
        self.nota_practica=nota_practica

    def es_aprobada(self):
        promedio=(self.nota_teorica + self.nota_practica)/2
        return promedio >= 60

class AreaEntrenamiento(Espacio):
    def lugar(self,nombre,capacidad_maxima):
        self.nombre = nombre
        self.capacidad_maxima=capacidad_maxima

class RutaEntrenamientoCreada(RutaEntrenamientoCreada):
    def ruta(self, ruta_entrenamiento, sgdb_principal, sgdb_alternativo):
        self.ruta_entrenamiento = ruta_entrenamiento
        self.sgdb_principal = sgdb_principal
        self.sgdb_alternativo = sgdb_alternativo

class Entrenador(Instructor):
    def trainer(self, idTrainer, nombreTrainer):
        self.idTrainer = idTrainer
        self.nombreTrainer = nombreTrainer

class Matricula(Matricula):
    def ingreso(self, camper, ruta_entrenamiento, entrenador, fecha_inicio, fecha_finalizacion, salon_entrenamiento):
        self.camper = camper
        self.ruta_entrenamiento = ruta_entrenamiento
        self.entrenador = entrenador
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.salon_entrenamiento = salon_entrenamiento

class Evaluacion(Evaluacion):
    def examen(self, camper, modulo, nota_teoria, nota_practica, quices_trabajos):
        self.camper = camper
        self.modulo = modulo
        self.nota_teoria = nota_teoria
        self.nota_practica = nota_practica
        self.quices_trabajos = quices_trabajos

    def es_aprobada(self):
        nota_final = (self.nota_teoria * 0.3) + (self.nota_practica * 0.6) + (self.quices_trabajos * 0.1)
        return nota_final >= 60
    
#json

def addDataCamperJson(data):
    with open('modulos/JSON/Campers.json', 'w') as file:
        json.dump(data, file, indent=4)

def readDataCamperJson():
    try: # Intenta abrir el archivo JSON en modo de lectura
        with open('modulos/JSON/Campers.json', 'r') as file: # Carga los datos existentes del archivo JSON
            data = json.load(file) # Si el archivo no existe o está vacío, crea una lista vacía
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

def addDataTrainerJson(data):
    with open('modulos/JSON/Trainers.json', 'w') as file:
        json.dump(data, file, indent=4)

def readDataTrainerJson():
    try:
        with open('modulos/JSON/Trainers.json', 'r') as file: 
            data = json.load(file) 
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

def addRutas(data):
    with open('modulos/JSON/Rutas.json', 'w') as file:
        json.dump(data, file, indent=4)

def loadRutas():
    try:
        with open('modulos/JSON/Rutas.json', 'r') as file: 
            data = json.load(file) 
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

def addSalas(data):
    with open('modulos/JSON/Salas.json', 'w') as file:
        json.dump(data, file, indent=4)

def loadSalas():
    try:
        with open('modulos/JSON/Salas.json', 'r') as file: 
            data = json.load(file) 
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data



campers_totales = []
inscritos_inscritos = []
estudiantes_aprobados = []
entrenadores = []
bajo_rendimiento = []
filtrados = []
no_filtrados = []
trainers_ingresados = []

# Clases abstractas
# Firmas
camper = list()

def save(data):
    camper.append(data)

def getAll():
    return camper

class Camper:
    def Datos(self, id, nombre, apellidos, direccion, telefono_celular, telefono_fijo,estado):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono_celular = telefono_celular
        self.telefono_fijo = telefono_fijo
        self.estado = estado

class RutaEntrenamiento:
    def datos_entrenamiento(self, nombre, stack_tecnologico, capacidad_maxima):
        self.nombre = nombre
        self.stack_tecnologico= stack_tecnologico
        self.capacidad_maxima= capacidad_maxima

class Prueba:
    def datos_prueba(self, camper, nota_teorica, nota_practica):
        self.camper = camper
        self.nota_teorica=nota_teorica
        self.nota_practica=nota_practica

    def es_aprobada(self):
        promedio=(self.nota_teorica + self.nota_practica)/2
        return promedio >= 60

class AreaEntrenamiento:
    def lugar(self,nombre,capacidad_maxima):
        self.nombre = nombre
        self.capacidad_maxima=capacidad_maxima

class RutaEntrenamientoCreada:
    def ruta(self, ruta_entrenamiento, sgdb_principal, sgdb_alternativo):
        self.ruta_entrenamiento = ruta_entrenamiento
        self.sgdb_principal = sgdb_principal
        self.sgdb_alternativo = sgdb_alternativo

class Entrenador:
    def trainer(self, nombre, rutas_entrenamiento):
        self.nombre = nombre
        self.rutas_entrenamiento = rutas_entrenamiento

class Matricula:
    def ingreso(self, camper, ruta_entrenamiento, entrenador, fecha_inicio, fecha_finalizacion, salon_entrenamiento):
        self.camper = camper
        self.ruta_entrenamiento = ruta_entrenamiento
        self.entrenador = entrenador
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.salon_entrenamiento = salon_entrenamiento

class Evaluacion:
    def examen(self, camper, modulo, nota_teoria, nota_practica, quices_trabajos):
        self.camper = camper
        self.modulo = modulo
        self.nota_teoria = nota_teoria
        self.nota_practica = nota_practica
        self.quices_trabajos = quices_trabajos

    def es_aprobada(self):
        nota_final = (self.nota_teoria * 0.3) + (self.nota_practica * 0.6) + (self.quices_trabajos * 0.1)
        return nota_final >= 60

campers = []
rutas_entrenamiento = []
pruebas = []
areas_entrenamiento = []
rutas_entrenamiento_creadas = []
entrenadores = []
matriculas = []
evaluaciones = []

# Clases abstractas
# Firmas
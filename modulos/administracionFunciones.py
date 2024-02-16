import os
from .funciones import editarCamper, editarTrainer, borrarCamper, borrarTrainer, cargarRutas, guardarRutas, cargarSalas, guardarSalas, cargarCampers, cargarTrainers, cargarClases, guardarClases, cargarNotas, guardarNotas

def actualizarDatos():
    menu= ["Campers","Trainers","Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #        Menu Administrativo        #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                if opc == 1:
                    actualizarDatosCamper()
                elif opc == 2:
                    actualizarDatosTrainer()
                elif opc == 3:
                    break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')
    
def registrarRuta():
    rutasExistentes = cargarRutas()
    os.system("cls")  
    print("""
                *************************
                *      Crear Rutas      *
                *************************
        """)
    
    datos = {
        "Nombre": str(input("Ingrese nombre de ruta: ")),
        "Modulos": {
            "Fundamentos de programacion": ["Introduccion a la algoritmia","PSeInt","Python"],
            "Programacion Web": ["HTML", "CSS", "Bootstrap"],
            "Programacion formal": ["Java", "JavaScript", "C#"],
            "Bases de datos": {
                "Base de datos principal": input("Ingrese base de datos principal: "),
                "Base de datos Secundario": input("Ingrese base de datos secundaria: ")
            },
            "Backend": ["NetCore", "Spring Boot", "NodeJS","Express"]
        }
    }  
    
    rutasExistentes.append(datos)
    guardarRutas(rutasExistentes)
    os.system("pause")
    os.system("cls")

def listarRutas():
    os.system("cls")
    rutas = cargarRutas()
    
    if not rutas:
        print("No existen rutas")
    else:
        print("""
                *************************
                *       Ver Rutas       *
                *************************
        """)
        for i, val in enumerate(rutas, start=1):
            print(f"""
                _______________________
                Código: {i}
                Nombre: {val.get("Nombre")}
                Fundamentos de programación: {val['Modulos']['Fundamentos de programacion']}
                Programación Web: {val['Modulos']['Programacion Web']}
                Programación formal: {val['Modulos']['Programacion formal']}
                Bases de datos: {val['Modulos']['Bases de datos']}
                Backend: {val['Modulos']['Backend']}
                """)
    os.system("pause")
    os.system("cls")

def registrarSala():
    os.system("cls")
    salas = cargarSalas()
    
    print("""
                *************************
                *      Crear Sala       *
                *************************
    """)
    datos = {
        "Nombre": input("Ingrese Nombre de la sala: "),
        "Capacidad Mañana 1": 33,
        "Capacidad Mañana 2": 33,
        "Capacidad Tarde 1": 33,
        "Capacidad Tarde 2": 33,
        "Mañana jornada 1": 0,
        "Mañana jornada 2": 0,
        "Tarde jornada 1": 0,
        "Tarde jornada 2": 0
    }
    
    salas.append(datos)
    guardarSalas(salas)
    print("Sala ingresada con éxito")
    os.system("pause")
    os.system("cls")

def listarSalas():
    os.system("cls")
    salas = cargarSalas()
    
    if not salas:
        print("No existen salas registradas.")
    else:
        print("""
                *************************
                *     Buscar Salas      *
                *************************
        """)
        for i, sala in enumerate(salas, start=1):
            print(f"""
                _______________________
                Código: {i}
                Nombre: {sala.get("Nombre")}
                Capacidad Mañana 1: {sala.get("Capacidad Mañana 1")}
                Capacidad Mañana 2: {sala.get("Capacidad Mañana 2")}
                Capacidad Tarde 1: {sala.get("Capacidad Tarde 1")}
                Capacidad Tarde 2: {sala.get("Capacidad Tarde 2")}
                Mañana jornada 1: {sala.get("Mañana jornada 1")}
                Mañana jornada 2: {sala.get("Mañana jornada 2")}
                Tarde jornada 1: {sala.get("Tarde jornada 1")}
                Tarde jornada 2: {sala.get("Tarde jornada 2")}
            """)
    os.system("pause")
    os.system("cls")

def asignarRuta():
    os.system("cls")
    campers, rutas, trainers, salas, clases = cargarDatosAsignarRuta()
    
    print("""
        ***********************
        *   Asignar Clases    *
        ***********************
    """)
    codigo_camper = int(input("Ingrese código del camper al que desea asignar la ruta: "))
    codigo_trainer = int(input("Ingrese código del profesor: "))
    codigo_ruta = int(input("Ingrese código de la ruta: "))
    horario = input("Ingrese el horario del estudiante (Mañana/Tarde): ")

    camper = obtenerCamperPorCodigo(campers, codigo_camper)
    if not camper:
        os.system("pause")
        os.system("cls")
        return
    
    if not validarHorario(horario):
        os.system("pause")
        os.system("cls")
        return
    
    trainer = trainers[codigo_trainer - 1]
    ruta = rutas[codigo_ruta - 1]
    
    sala_asignada = obtenerAsignacionDeSala(trainer, horario)
    if not sala_asignada:
        os.system("pause")
        os.system("cls")
        return
    
    clase = obtenerClasePorSala(salas, sala_asignada["Codigo de la sala"])
    if not clase:
        os.system("pause")
        os.system("cls")
        return
    
    capacidad_key = f"Capacidad {horario} {sala_asignada['Codigo de la sala']}"
    
    if camper["Estado"] == "Inscrito" and clase[capacidad_key] > 0:
        var = {
            "Nombre": camper.get("Nombre"),
            "CC": camper.get("CC"),
            "Ruta": ruta.get("Nombre"),
            "Modulos": ruta.get('Modulos'),
            "Trainer": trainer.get("Nombre"),
            "Sala": clase.get("Nombre"),
            "FechaInicio": input("Ingrese fecha de inicio DD/MM/YYYY: "),
            "FechaFinalizacion": input("Ingrese fecha de finalización DD/MM/YYYY: ")
        }
        clase[capacidad_key] -= 1
        clases.append(var)
        guardarSalas(salas)
        guardarClases(clases)
        print("Estudiante ingresado a la clase con éxito.")
    else:
        print("El camper no está en estado 'Inscrito' o la sala ya cuenta con la capacidad máxima de estudiantes.")
    os.system("pause")
    os.system("cls")
    
def actualizarNotas():
    campers = cargarCampers()
    notas = cargarNotas()
    os.system("cls")
    print("""
        ***********************
        *    Notas Campers    *
        ***********************
    """)
    print("""
        Qué módulo quieres evaluar al camper
        1 - Fundamentos de programación
        2 - Programación web 
        3 - Programación formal
        4 - Base de datos
        5 - Backend
        6 - Salir
            """)
    
    calificar = {
        1: "Fundamentos",
        2: "Programación web",
        3: "Programación formal",
        4: "Base de datos",
        5: "backend"
    }

    while True:
        opc = int(input(": "))
        if opc == 6:
            break
        if opc not in calificar:
            print("Opción inválida. ")
            continue

        moduloElegido = calificar[opc]
        codigo = int(input("Ingrese código del camper a calificar: "))
        if codigo < 1 or codigo > len(campers):
            print("Código de camper inválido. Por favor, ingrese un código válido.")
            continue

        for i, val in enumerate(notas, start=0):
            if val.get("codigo") == codigo:
                pruebaTeorica = int(input("Ingrese nota de la prueba teórica: "))
                pruebaPractica = int(input("Ingrese nota de la prueba práctica: "))
                notasVarias = int(input("¿Se hicieron más de una actividad tipo quiz, trabajo o examen? Si es así, ingrese cuántas actividades hubo: "))
                notasModulo = []
                for j in range(notasVarias):
                    actividad = int(input(f"Ingrese nota de la actividad {j+1}: "))
                    notasModulo.append(actividad)
                
                totalNotas =  (sum(notasModulo) / notasVarias) * 0.10
                TotalTeorica = pruebaTeorica * 0.30
                TotalPractica =  pruebaPractica * 0.60
                Resultado = totalNotas + TotalPractica + TotalTeorica
                
                if Resultado >= 60:
                    notas[i][moduloElegido] = "Aprobado"
                    notas[i]["Estado Actual"] = "Cursando"
                else: 
                    notas[i][moduloElegido] = "Desaprobado"
                    notas[i]["Reportado"] += 1
                    if notas[i]["Reportado"] == 1:
                        print("El camper ha sido reportado por bajo rendimiento en este módulo.")
                        notas[i]["Estado Actual"] = "Riesgo"
                    elif notas[i]["Reportado"] == 2:
                        print("El camper ha sido reportado por bajo rendimiento en este módulo y otro más.")
                        notas[i]["Estado Actual"] = "Bajo rendimiento"
                        notas[i]["Reportado"] += 2 
                        break

        guardarNotas(notas)
        otro = input("¿Desea elegir otro módulo? (s/n): ")
        if otro.lower() != "s":
            break    
    
def cargarDatosAsignarRuta():
    campers = cargarCampers()
    rutas = cargarRutas()
    trainers = cargarTrainers()
    salas = cargarSalas()
    clases = cargarClases()

    return campers, rutas, trainers, salas, clases

def obtenerCamperPorCodigo(camper, idCamper):
    if idCamper <= 0 or idCamper > len(camper):
        print("Código de camper no válido.")
        return None
    return camper[idCamper - 1]

def validarHorario(horario):
    return horario in ["Mañana", "Tarde"]

def obtenerAsignacionDeSala(trainer, horario):
    for sala in trainer.get("Salas elegidas", []):
        if sala["Horario"] == f"{horario} jornada 1" or sala["Horario"] == f"{horario} jornada 2":
            return sala
    print("El profesor no tiene asignada una sala para el horario ingresado.")
    return None

def obtenerClasePorSala(salas, idSala):
    if idSala <= 0 or idSala > len(salas):
        print("Código de sala no válido.")
        return None
    return salas[idSala - 1]

def actualizarDatosCamper():
    menu= ["Actualizar datos del Camper","Eliminar datos del Camper","Salir"]
    while True:
        os.system('cls')
        print("""
        ####################################
        #   Menu Administrativo (campers)  #
        ####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                if opc == 1:
                    editarCampers()
                elif opc == 2:
                    borrarCampers()
                elif opc == 3:
                    break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')
            
def actualizarDatosTrainer():
    menu= ["Actualizar datos del Trainer","Eliminar datos del Trainer","Salir"]
    while True:
        os.system('cls')
        print("""
        #####################################
        #   Menu Administrativo (trainers)  #
        #####################################
          """)
        print(" ".join([f"{i+1}. {val} " for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if opc<=len(menu) and opc>0:
                if opc == 1:
                    editarTrainers()
                elif opc == 2:
                    borrarTrainers()
                elif opc == 3:
                    break
        except ValueError:
            print("La opcion no es valida")
            os.system('cls')           

def editarCampers():
    id = input("Ingrese la ID del camper a editar: ")
    editarCamper(id)

def editarTrainers():
    id = input("Ingrese la ID del trainer a editar: ")
    editarTrainer(id)

def borrarCampers():
    id = input("Ingrese la ID del camper a eliminar: ")
    borrarCamper(id)

def borrarTrainers():
    id = input("Ingrese la ID del trainer a eliminar: ")
    borrarTrainer(id)
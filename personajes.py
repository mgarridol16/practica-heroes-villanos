from datetime import datetime
from logs import Log
from models import Heroes, Villanos
import  random

log = Log()


personajes = {

}

def crearHeroeOVillano():
    try:
        heroeOVillano = 0
        opcionSelecMal = True
        while opcionSelecMal:
            heroeOVillano = input("Que deseas crear heroe(1) o villano(2) o salir(0): ")

            if heroeOVillano == "0":
                return None

            if heroeOVillano not in ["1", "2"]:
                print("Error debes selecionar el numero 1 si quieres crear un heroe o 2 si quieres villano")
                continue

            nombre = input("Introduce el nombre: ").strip()
            if not nombre:
                print("Error: el nombre no puede estar vacío.")
                continue
            if nombre in personajes:
                log.escribir("WARNING", f"Intento de crear personaje duplicado: {nombre}")
                print("Error: ya existe un personaje con ese nombre.")
                continue

            apellidos = input("Introduce los apellidos: ").strip()
            if not apellidos:
                print("Error: los apellidos no pueden estar vacíos.")
                continue

            fecha_str = input("Introduce la fecha de nacimiento (DD/MM/AAAA): ").strip()
            try:
                fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y").date()
            except ValueError:
                log.escribir("WARNING", f"Formato de fecha incorrecto introducido: {fecha_str}")
                print("Error: formato de fecha incorrecto. Debe ser DD/MM/AAAA.")
                continue

            if heroeOVillano == "1":
                nuevo_pj = Heroes(nombre, apellidos, fecha_nacimiento)
                nuevo_pj.puntuacionTotal = nuevo_pj.definirPuntuacionTotalHeroe()
                personajes[nuevo_pj.nombre] = nuevo_pj
                log.escribir("INFO", f"Héroe creado: {nuevo_pj.nombre}")
                return nuevo_pj

            elif heroeOVillano == "2":
                nuevo_pj = Villanos(nombre, apellidos, fecha_nacimiento)
                nuevo_pj.puntuacionTotal = nuevo_pj.definirPuntuacionTotalVillano()
                personajes[nuevo_pj.nombre] = nuevo_pj
                log.escribir("INFO", f"Villano creado: {nuevo_pj.nombre}")
                return nuevo_pj
    except Exception as e:
        log.escribir("ERROR", f"Error en crearHeroeOVillano: {e}")
        print(f"Error en crearHeroeOVillano: {e}")
        return None


def buscarPersonaje():
    try:
        opcionSelMal = True
        personajesEncontrados = {}
        atributos_texto = [
            "nombre",
            "apellidos",
            "fecha_nacimiento"
        ]
        atributos_numericos = [
            "puntuaciontotal",
            # Cualidades Héroe
            "codigolimpio",
            "biendocumentado",
            "gitgod",
            "arquitecto",
            "detallista",
            # Cualidades Villano
            "chagepeteador",
            "entregadortardio",
            "ausencias",
            "hablador"
        ]


        todos_atributos = atributos_texto + atributos_numericos + ["identificador"] # pongo aqui el id para buscar solo por ese id
        while opcionSelMal:
            print("---- Buscar personaje por cualidad o atributo ----")
            print("-- ATRIBUTOS COMUNES: Nombre, Apellidos, fecha_nacimiento, Identificador, Puntuacióntotal ")
            print("-- CUALIDADES HEROE: CodigoLimpio, BienDocumentado, GITGod, Arquitecto, Detallista ")
            print("-- CUALIDADES HEROE: Chagepeteador, EntregadorTardío, Ausencias, Hablador ")
            buscarHeroe = input("Introduce la cualidad o el atributo a buscar: ").strip().lower()

            if buscarHeroe not in todos_atributos:
                print("Error debes buscar por un atributo o una cualidad valida")
                continue

            if buscarHeroe in atributos_texto:
                valor_buscado = input("Introduce el valor a buscar: ").strip().lower()
                for p in personajes.values():
                    if buscarHeroe == "nombre" and p.nombre.lower() == valor_buscado:
                        personajesEncontrados[p.nombre] = p
                    elif buscarHeroe == "apellidos" and p.apellidos.lower() == valor_buscado:
                        personajesEncontrados[p.nombre] = p
                    elif buscarHeroe == "fecha_nacimiento":
                        fecha_en_texto = p.fecha_nacimiento.strftime("%d/%m/%Y")
                        if fecha_en_texto == valor_buscado:
                            personajesEncontrados[p.nombre] = p
                return personajesEncontrados
            elif buscarHeroe == "identificador":
                entrada_id = input("Introduce el ID exacto a buscar: ").strip()
                if not entrada_id.isdigit():
                    print("Error: El ID debe ser un número entero.")
                    continue

                id_buscado = int(entrada_id)

                for p in personajes.values():
                    if p.id == id_buscado:
                        personajesEncontrados[p.nombre] = p

                return personajesEncontrados

            elif buscarHeroe in atributos_numericos:
                opcionMala = True
                while opcionMala:
                    entrada_num = input("Introduce el valor numérico: ").strip()
                    if not entrada_num.isdigit():
                        print("Error: debes introducir un número entero.")
                        continue
                    valor_num = int(entrada_num)

                    if buscarHeroe != "identificador" and (valor_num < 0 or valor_num > 100):
                        print("Error: las cualidades deben estar entre 0 y 100.")
                        continue


                    print("¿Qué tipo de comparación deseas hacer?")
                    print("1. Mayor que (>)")
                    print("2. Menor que (<)")
                    print("3. Igual a (==)")
                    criterio = input("Elige una opción (1/2/3): ").strip()

                    if criterio not in ["1", "2" ,"3"]:
                        print(f"Error eligue una opcion correcta")
                        continue
                    for p in personajes.values():
                        valor_a_comparar = None

                        if buscarHeroe == "puntuaciontotal":
                            valor_a_comparar = p.puntuacionTotal
                        elif buscarHeroe == "identificador":
                            valor_a_comparar = p.id

                        elif type(p) == Heroes:
                            if buscarHeroe == "codigolimpio":
                                valor_a_comparar = p.codigoLimpio
                            elif buscarHeroe == "biendocumentado":
                                valor_a_comparar = p.bienDocumentado
                            elif buscarHeroe == "gitgod":
                                valor_a_comparar = p.gitGOD
                            elif buscarHeroe == "arquitecto":
                                valor_a_comparar = p.arquitecto
                            elif buscarHeroe == "detallista":
                                valor_a_comparar = p.detallista

                        elif type(p) == Villanos:
                            if buscarHeroe == "chagepeteador":
                                valor_a_comparar = p.chagepeteador
                            elif buscarHeroe == "entregadortardio":
                                valor_a_comparar = p.entregadorTardio
                            elif buscarHeroe == "ausencias":
                                valor_a_comparar = p.ausencias
                            elif buscarHeroe == "hablador":
                                valor_a_comparar = p.hablador

                        if valor_a_comparar is not None:
                            if criterio == "1" and valor_a_comparar > valor_num:
                                personajesEncontrados[p.nombre] = p
                            elif criterio == "2" and valor_a_comparar < valor_num:
                                personajesEncontrados[p.nombre] = p
                            elif criterio == "3" and valor_a_comparar == valor_num:
                                personajesEncontrados[p.nombre] = p

                    return  personajesEncontrados
    except Exception as e:
        log.escribir("ERROR", f"Error inesperado en la busqueda: {e}")
        print(f"Error inesperado en la busqueda: {e}")
        return {}


def consultarEdadPersonajes():
    try:
        print("--- CONSULTORIO EDAD PERSONAJES ---")
        opcionMala = True
        personajesEdad = {}
        while opcionMala:
            tipoPersonaje = input("De que quieres consultar la edad (1)Villano o (2)Heroe: ")
            if tipoPersonaje not in ["1", "2"]:
                print("Error debes selecionar entre el heroe o el villano")
                continue

            if tipoPersonaje == "1":
                print("Buscando edad de Villanos...")
                for p in personajes.values():
                    if type(p) == Villanos:
                        personajesEdad[p.nombre] = p.getEdad()
                return personajesEdad


            if tipoPersonaje == "2":
                print("Buscando edad de Heros...")
                for p in personajes.values():
                    if type(p) == Heroes:
                        personajesEdad[p.nombre] = p.getEdad()
                return personajesEdad

    except Exception as e:
        log.escribir("ERROR", f"Error inesperado en consultar edad: {e}")
        print(f"Error inesperado en consultar edad personajes: {e}")
        return {}


def emparejarPersonajes():
    try:
        lista_heroes = []
        lista_villanos = []

        for p in personajes.values():
            if type(p) == Heroes:
                lista_heroes.append(p)
            elif type(p) == Villanos:
                lista_villanos.append(p)

        if len(lista_heroes) == 0 or len(lista_villanos) == 0:
            log.escribir("WARNING", "Emparejamiento fallido: Faltan personajes en algún bando.")
            print("Error: se necesita al menos un heroe y 1 villano para emparejarlos")
            return None

        heroe_elegido = random.choice(lista_heroes)
        villano_elegido = random.choice(lista_villanos)

        diferencia = 0
        if heroe_elegido.puntuacionTotal >= villano_elegido.puntuacionTotal:
            diferencia = heroe_elegido.puntuacionTotal - villano_elegido.puntuacionTotal
        else:
            diferencia = villano_elegido.puntuacionTotal - heroe_elegido.puntuacionTotal

        umbral_para_diferencia = 20
        if diferencia <= umbral_para_diferencia:
            log.escribir("INFO", f"Resultado combate: EQUILIBRADO (Dif: {diferencia})")
            print(f"Estan equilibrados. Puntuaciones similares (Diferencia de: {diferencia} pts)")
        else:
            log.escribir("INFO", f"Resultado combate: DESBALANCEADO (Dif: {diferencia})")
            print(f"Existe una alta desviación en el combate (Diferencia de {diferencia} pts).")

    except Exception as e:
        log.escribir("ERROR", f"Error en emparejarPersonajes: {e}")
        print(f"Error inesperado al emparejar: {e}")


from personajes import crearHeroeOVillano, buscarPersonaje, consultarEdadPersonajes, emparejarPersonajes
from logs import Log
import  os

log = Log()

def menu():

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1) Crear heroe o villano")
        print("2) Buscar personaje")
        print("3) Consultar Edad villanos o Heroes")
        print("4) Emparejar héroes y villanos")
        print("5) Salir")

        opt = input("Introduce la opción deseada: ").strip()

        if opt == "1":
            personaje_creado = crearHeroeOVillano()
            if personaje_creado is not None:
                log.escribir("INFO", f"Personaje creado: {personaje_creado.nombre}")
                print(f"-> {personaje_creado.nombre} creado y guardado con éxito.")

        elif opt == "2":
            encontrados = buscarPersonaje()
            if encontrados:
                log.escribir("INFO", f"Búsqueda realizada con {len(encontrados)} resultados")
                print("Personajes encontrados:")
                for p in encontrados.values():
                    print(f"- {p.nombre} (Puntuación: {p.puntuacionTotal})")
            else:
                log.escribir("WARNING", "Búsqueda sin coincidencias")
                print("No se encontró ningún personaje.")

        elif opt == "3":
            edades = consultarEdadPersonajes()
            if edades:
                log.escribir("INFO", f"Consulta de edades realizada. Resultados: {len(edades)}")
                print("Resultados de edades:")
                for nombre, edad in edades.items():
                    print(f"- {nombre}: {edad} años")
            else:
                log.escribir("WARNING", "Consulta de edades sin resultados (lista vacía).")
                print("No hay personajes registrados de ese tipo.")


        elif opt == "4":
            log.escribir("INFO", "Iniciando proceso de emparejamiento aleatorio.")
            emparejarPersonajes()

        elif opt == "5":
            log.escribir("INFO", "FIN EJECUCIÓN")
            print("Hasta pronto.")
            break


        else:
            log.escribir("WARNING", f"Opción de menú no reconocida : {opt}")
            print("Error: Selecciona una opción válida del 1 al 5.")
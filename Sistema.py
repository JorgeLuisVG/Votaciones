ListaPeliculas = {}

def AgregarPeliculas():
    def MejorPelicula():
        print("Mejor Pelicula")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin): ").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
        print()

    def MejorDireccion():
        print("Mejor Direccion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin): ").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Direccion", "Votos": 0}
        print()

    def MejorFotografia():
        print("Mejor Fotografía")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin): ").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Fotografía", "Votos": 0}
        print()

    def MejorActuacion():
        print("Mejor Actuación")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin): ").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Actuacion", "Votos": 0}
        print()

    def MejoresEfectosEspeciales():
        print("Mejores Efectos Especiales")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin): ").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejores Efectos Especiales", "Votos": 0}
        print()

    MejorPelicula()
    MejorFotografia()
    MejorDireccion()
    MejorActuacion()
    MejoresEfectosEspeciales()

def registrar_peliculas():
    try:
        categoria = input("Ingrese la categoría: ").strip().title()
        titulo = input("Ingrese el título de la película: ").strip().title()

        for peli, info in ListaPeliculas.items():
            if peli == titulo and info["Categoria"] == categoria:
                print("Esta película ya está registrada en esta categoría.")
                return

        ListaPeliculas[titulo] = {"Categoria": categoria, "Votos": 0}
        print(f"{titulo} registrada en {categoria}.")
    except Exception as e:
        print(f"Ocurrió un error al registrar la película: {e}")

def votar():
    def votar_categoria(nombre_categoria):
        for peli, info in ListaPeliculas.items():
            if info["Categoria"] == nombre_categoria:
                print(f"- {peli}")

        try:
            votarA = input("Ingrese el nombre de la película a la cual desea votar: ").title()
            if votarA in ListaPeliculas and ListaPeliculas[votarA]["Categoria"] == nombre_categoria:
                ListaPeliculas[votarA]["Votos"] += 1
            else:
                raise ValueError("Película no encontrada en esta categoría.")
        except ValueError as e:
            print(f"Error: {e}")

    votar_categoria("Mejor Pelicula")
    votar_categoria("Mejor Direccion")
    votar_categoria("Mejor Fotografía")
    votar_categoria("Mejor Actuacion")
    votar_categoria("Mejores Efectos Especiales")

def mostrar_resultados():
    if not ListaPeliculas:
        print("No hay películas registradas todavía.")
        return

    print("\nResultados de votación:")
    categorias_vistas = set(info["Categoria"] for info in ListaPeliculas.values())

    for categoria in categorias_vistas:
        print(f"\nCategoría: {categoria}")
        for peli, info in ListaPeliculas.items():
            if info["Categoria"] == categoria:
                print(f"{peli}: {info['Votos']} voto(s)")


while True:
    print("\nIngrese la opción que desea:")
    print("1 = Añadir películas por categoría")
    print("2 = Votar")
    print("3 = Ver votos")
    print("4 = Salir")
    print("5 = Registrar película individual")

    try:
        opcion = input("Opción: ").strip()
        if opcion == "1":
            AgregarPeliculas()
        elif opcion == "2":
            if not ListaPeliculas:
                print("No hay películas agregadas.")
            else:
                votar()
        elif opcion == "3":
            if not ListaPeliculas:
                print("No hay películas.")
            else:
                mostrar_resultados()
        elif opcion == "4":
            print("Ganadores por categoría:")

            if not ListaPeliculas:
                print("No hay películas registradas.")
            else:
                categorias = ["Mejor Pelicula", "Mejor Direccion", "Mejor Fotografía", "Mejor Actuacion", "Mejores Efectos Especiales"]

                for categoria in categorias:
                    mayor_votos = -1
                    ganadora = ""

                    for peli, info in ListaPeliculas.items():
                        if info["Categoria"] == categoria:
                            if info["Votos"] > mayor_votos:
                                mayor_votos = info["Votos"]
                                ganadora = peli

                    if ganadora != "":
                        print(f"{categoria}: {ganadora} con {mayor_votos} voto(s)")
                    else:
                        print(f"{categoria}: No se registraron películas")

            print("Programa finalizado.")
            break

        elif opcion == "5":
            registrar_peliculas()
        else:
            raise ValueError("Opción inválida.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

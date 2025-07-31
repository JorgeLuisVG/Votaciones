ListaPeliculas = {}

def AgregarPeliculas():
    def MejorPelicula():
        print("Mejor Pelicula")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
        print()
    def MejorDireccion():
        print("Mejor direccion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
        print()
    def MejorFotografía():
        print("Mejor fotografía")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
        print()
    def MejorActuacion():
        print("Mejor actuacion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
        print()
    def MejoresEfectosEspeciales():
        print("Mejores efectos especiales")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
        print()
    
    MejorPelicula()
    MejorFotografía()
    MejorDireccion()
    MejorActuacion()
    MejoresEfectosEspeciales()

def votar():
    def votarMejorPelicula():
        ListaMP = []
        for Peli, Info in ListaPeliculas.items():
            if Info["Categoria"] == "Mejor Pelicula":
                ListaMP.append(ListaPeliculas)
                print(f"{ListaMP}")

while True:
    print("Ingrese la opcion que desea")
    print("1 = Añadir peliculas")
    print("2 = votar")
    print("3 = Ver votos")
    opcion = input()

    if opcion == "1":
        AgregarPeliculas()
    elif opcion == "2":
        if not ListaPeliculas:
            print("No hay peliculas agregadas")
        else:
            print()
            for Peli, Info in ListaPeliculas.items():
                print(f"Pelicula: {Peli}, Categoria: {Info["Categoria"]}, Votos: {Info["Votos"]}")


    elif opcion == "3":
        if not ListaPeliculas:
            print("No hay peliculas")
        else: 
            print()

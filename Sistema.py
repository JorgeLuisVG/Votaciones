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
    def MejorDireccion():
        print("Mejor direccion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
    def MejorFotografía():
        print("Mejor fotografía")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
    def MejorActuacion():
        print("Mejor actuacion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
    def MejoresEfectosEspeciales():
        print("Mejores efectos especiales")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
    
    MejorPelicula()
    MejorFotografía()
    MejorDireccion()
    MejorActuacion()
    MejoresEfectosEspeciales()

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
    elif opcion == "3":
        if not ListaPeliculas:
            print("No hay peliculas")
        else: 
            print()
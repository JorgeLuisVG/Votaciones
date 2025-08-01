ListaPeliculas = {}

def AgregarPeliculas():
    def MejorPelicula():
        print("Mejor Pelicula")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Pelicula", "Votos": 0}
        print()
    def MejorDireccion():
        print("Mejor direccion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Direccion", "Votos": 0}
        print()
    def MejorFotografía():
        print("Mejor fotografía")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Fotografía", "Votos": 0}
        print()
    def MejorActuacion():
        print("Mejor actuacion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejor Actuacion", "Votos": 0}
        print()
    def MejoresEfectosEspeciales():
        print("Mejores efectos especiales")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para terminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                ListaPeliculas[Nombre] = {"Categoria": "Mejores Efectos Especiales", "Votos": 0}
        print()

    MejorPelicula()
    MejorFotografía()
    MejorDireccion()
    MejorActuacion()
    MejoresEfectosEspeciales()

def votar():
    def votarMejorPelicula():
        for Peli, Info in ListaPeliculas.items():
            if Info["Categoria"] == "Mejor Pelicula":
                print(f"Pelicula: {Info['Categoria']}")
        
        votarA = input("Ingrese el nombre de la pelicula a la cual desea votar").title()

        for Peli, Info in ListaPeliculas.items():
            if votarA in ListaPeliculas:
                ListaPeliculas[votarA]["Votos"] += 1
            else:
                print("Película no encontrada")

    def votarDireccion():
        for Peli, Info in ListaPeliculas.items():
            if Info["Categoria"] == "Mejor Direccion":
                print(f"Pelicula: {Info['Categoria']}")
        
        votarA = input("Ingrese el nombre de la pelicula a la cual desea votar").title()

        for Peli, Info in ListaPeliculas.items():
            if votarA in ListaPeliculas:
                ListaPeliculas[votarA]["Votos"] += 1
            else:
                print("Película no encontrada")

    def votarFotografia():
        for Peli, Info in ListaPeliculas.items():
            if Info["Categoria"] == "Mejor Fotografía":
                print(f"Pelicula: {Info['Categoria']}")
        
        votarA = input("Ingrese el nombre de la pelicula a la cual desea votar").title()

        for Peli, Info in ListaPeliculas.items():
            if votarA in ListaPeliculas:
                ListaPeliculas[votarA]["Votos"] += 1
            else:
                print("Película no encontrada")
    
    def votarActuacion():
        for Peli, Info in ListaPeliculas.items():
            if Info["Categoria"] == "Mejor Actuacion":
                print(f"Pelicula: {Info['Categoria']}")
        
        votarA = input("Ingrese el nombre de la pelicula a la cual desea votar").title()

        for Peli, Info in ListaPeliculas.items():
            if votarA in ListaPeliculas:
                ListaPeliculas[votarA]["Votos"] += 1
            else:
                print("Película no encontrada")
    
    def votarEfectosEspeciales():
        for Peli, Info in ListaPeliculas.items():
            if Info["Categoria"] == "Mejores Efectos Especiales":
                print(f"Pelicula: {Info['Categoria']}")
        
        votarA = input("Ingrese el nombre de la pelicula a la cual desea votar").title()

        for Peli, Info in ListaPeliculas.items():
            if votarA in ListaPeliculas:
                ListaPeliculas[votarA]["Votos"] += 1
            else:
                print("Película no encontrada")
    
    votarMejorPelicula()
    votarDireccion()
    votarFotografia()
    votarActuacion()
    votarEfectosEspeciales()

while True:
    print("Ingrese la opcion que desea")
    print("1 = Añadir peliculas")
    print("2 = votar")
    print("3 = Ver votos")
    print("4 = salir")
    opcion = input()

    if opcion == "1":
        AgregarPeliculas()
    elif opcion == "2":
        if not ListaPeliculas:
            print("No hay peliculas agregadas")
        else:
            votar()
    elif opcion == "3":
        if not ListaPeliculas:
            print("No hay peliculas")
        else: 
            print()
    elif opcion == "4":
        break



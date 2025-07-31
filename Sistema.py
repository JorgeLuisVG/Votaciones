ListaPeliculas = []

def AgregarPeliculas():
    Pelicula ={}
    def MejorPelicula():
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            Pelicula[Nombre] = {"Categoria": "Mejor Prlicula"}
            ListaPeliculas.append(Pelicula)
            
            
            
            
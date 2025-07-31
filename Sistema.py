ListaPeliculas = []

def AgregarPeliculas():
    Pelicula ={}
    def MejorPelicula():
        print("Mejor Pelicula")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                Pelicula[Nombre] = {"Categoria": "Mejor Pelicula"}
                ListaPeliculas.append(Pelicula)
    def MejorDireccion():
        print("Mejor direccion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                Pelicula[Nombre] = {"Categoria": "Mejor direccion"}
                ListaPeliculas.append(Pelicula)
    def MejorFotografía():
        print("Mejor fotografía")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                Pelicula[Nombre] = {"Categoria": "Mejor Fotografía"}
                ListaPeliculas.append(Pelicula)
    def MejorActuacion():
        print("Mejor actuacion")
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                Pelicula[Nombre] = {"Categoria": "Mejor Actuacion"}
                ListaPeliculas.append(Pelicula)
    def MejoresEfectosEspeciales():
        while True:
            Nombre = input("Ingrese el nombre de la pelicula (para tereminar escriba fin)").title()
            if Nombre == "Fin":
                break
            else:
                Pelicula[Nombre] = {"Categoria": "Mejores Efectos Especiales"}
                ListaPeliculas.append(Pelicula)
    
    MejorPelicula()
    MejorFotografía()
    MejorDireccion()
    MejorActuacion()
    MejoresEfectosEspeciales()

        
            
            
            
            
peliculas = {}
def registrar_peliculas():
    categoria = input("Ingrese la categoria: ").strip()
    titulo = input("Ingrese el título de la pelicula: ").strip()

    if categoria not in peliculas:
        peliculas[categoria] = {}

    if titulo in peliculas[categoria]:
        print("Esta pelicula ya esta registrada en esta categoria: ")
        return 
    
    peliculas[categoria][titulo] = 0
    print(f"{titulo} registrada en {categoria}")
    
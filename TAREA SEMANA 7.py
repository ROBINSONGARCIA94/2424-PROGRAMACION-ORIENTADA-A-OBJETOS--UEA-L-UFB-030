class Libro:
    def __init__(self, titulo, autor):
        """Constructor que inicializa los atributos del objeto."""
        self.titulo = titulo
        self.autor = autor
        self.leido = False
        print(f"Se ha creado el libro: {self.titulo} de {self.autor}")

    def leer(self):
        """Simula la lectura del libro."""
        if not self.leido:
            self.leido = True
            print(f"Ahora estás leyendo: {self.titulo}")
        else:
            print(f"Ya has leído: {self.titulo}")

    def __del__(self):
        """Destructor que se llama cuando el objeto es destruido."""
        print(f"Se está eliminando el libro: {self.titulo}")

# Ejemplo de uso de la clase Libro
if __name__ == "__main__":
    # Crear instancias de Libro
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("1984", "George Orwell")

    # Leer los libros
    libro1.leer()
    libro2.leer()
    libro2.leer()  # Intentar leer el libro nuevamente

    # Eliminar referencias a los libros
    del libro1
    del libro2  # Esto llamará al destructor

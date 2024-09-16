class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Tupla (nombre, apellido)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros {isbn: Libro}
        self.usuarios = set()  # Conjunto de IDs de usuarios

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            for usuario in self.usuarios:
                if usuario.id_usuario == id_usuario:
                    usuario.libros_prestados.append(libro)

    def devolver_libro(self, isbn, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                if isbn in [libro.isbn for libro in usuario.libros_prestados]:
                    usuario.libros_prestados = [libro for libro in usuario.libros_prestados if libro.isbn != isbn]

    def buscar_libro(self, criterio):
        resultados = []
        for libro in self.libros.values():
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor[0].lower() or criterio.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario.libros_prestados
        return []


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", ("Gabriel", "García Márquez"), "Ficción", "978-3-16-148410-0")
libro2 = Libro("El amor en los tiempos del cólera", ("Gabriel", "García Márquez"), "Ficción", "978-3-16-148411-7")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("978-3-16-148410-0", "001")

# Listar libros prestados
prestados = biblioteca.listar_libros_prestados("001")
print("Libros prestados a Juan Pérez:")
for libro in prestados:
    print(libro)

# Buscar libro
resultados_busqueda = biblioteca.buscar_libro("Gabriel")
print("\nResultados de búsqueda para 'Gabriel':")
for libro in resultados_busqueda:
    print(libro)
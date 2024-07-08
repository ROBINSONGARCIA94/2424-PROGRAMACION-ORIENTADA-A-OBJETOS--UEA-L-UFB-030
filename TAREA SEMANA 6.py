# Definición de la clase base (Animal)
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación del nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def hacer_sonido(self):
        pass  # Método que será implementado en las subclases


# Definición de una clase derivada (Perro) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamada al constructor de la clase base
        self.__raza = raza  # Encapsulación de la raza

    def hacer_sonido(self):
        return "¡Guau!"  # Polimorfismo: método sobrescrito

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza


# Definición de otra clase derivada (Gato) que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # Llamada al constructor de la clase base
        self.__color = color  # Encapsulación del color

    def hacer_sonido(self):
        return "¡Miau!"  # Polimorfismo: método sobrescrito

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


# Crear instancias de las clases y utilizar métodos
if __name__ == "__main__":
    # Crear un perro y un gato
    mi_perro = Perro("Bobby", "Labrador")
    mi_gato = Gato("Mittens", "Gris")

    # Acceder a los atributos encapsulados usando métodos getter
    print(f"Nombre del perro: {mi_perro.get_nombre()}, Raza: {mi_perro.get_raza()}")
    print(f"Nombre del gato: {mi_gato.get_nombre()}, Color: {mi_gato.get_color()}")

    # Utilizar métodos para demostrar polimorfismo
    print(mi_perro.hacer_sonido())  # Output: ¡Guau!
    print(mi_gato.hacer_sonido())  # Output: ¡Miau!

    # Modificar atributos encapsulados usando métodos setter
    mi_perro.set_raza("Pastor Alemán")
    mi_gato.set_color("Blanco")

    # Mostrar los cambios
    print(f"Nuevo raza del perro: {mi_perro.get_raza()}")
    print(f"Nuevo color del gato: {mi_gato.get_color()}")

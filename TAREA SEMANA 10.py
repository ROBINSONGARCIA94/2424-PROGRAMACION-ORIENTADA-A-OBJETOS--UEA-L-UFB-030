import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_string(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            open(self.archivo, 'w').close()  # Crear archivo si no existe
            print("Archivo de inventario creado.")
        else:
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        id, nombre, cantidad, precio = linea.strip().split(',')
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self.productos[id] = producto
                print("Inventario cargado desde el archivo.")
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(producto.to_string() + '\n')
            print("Inventario guardado en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print(f"Error: Ya existe un producto con ID {producto.id}.")
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print(f"Producto añadido: {producto}")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"Error: No se encontró producto con ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto actualizado: {producto}")
        else:
            print(f"Error: No se encontró producto con ID {id}.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con nombre '{nombre}'.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opción = input("Seleccione una opción: ")

        if opción == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opción == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opción == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco si no desea actualizar): ")
            precio = input("Ingrese nuevo precio (deje en blanco si no desea actualizar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opción == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opción == "5":
            inventario.mostrar_todos_los_productos()

        elif opción == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu()

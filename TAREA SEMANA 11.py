import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_atributos(self):
        return {
            'ID': self.id_producto,
            'Nombre': self.nombre,
            'Cantidad': self.cantidad,
            'Precio': self.precio
        }

    def establecer_atributos(self, nombre=None, cantidad=None, precio=None):
        if nombre is not None:
            self.nombre = nombre
        if cantidad is not None:
            self.cantidad = cantidad
        if precio is not None:
            self.precio = precio

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        if id_producto in self.productos:
            self.productos[id_producto].establecer_atributos(nombre, cantidad, precio)
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [producto.obtener_atributos() for producto in self.productos.values() if producto.nombre == nombre]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre {nombre}.")

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto.obtener_atributos())

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: producto.obtener_atributos() for id, producto in self.productos.items()}, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                self.productos = {id: Producto(id, **info) for id, info in data.items()}
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe.")

# Función principal de la interfaz de usuario
def menu():
    inventario = Inventario()
    archivo = 'inventario.json'

    while True:
        print("\nMenú:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado.")

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nombre if nombre else None, cantidad, precio)
            print("Producto actualizado.")

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            inventario.guardar_inventario(archivo)
            print("Inventario guardado.")

        elif opcion == '7':
            inventario.cargar_inventario(archivo)
            print("Inventario cargado.")

        elif opcion == '8':
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()

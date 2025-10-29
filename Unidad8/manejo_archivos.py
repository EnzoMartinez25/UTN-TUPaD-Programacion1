def mostrar_productos():
    with open("productos.txt", "r") as archivo: 
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}")

def agregar_producto():
    nombre = input("Ingresa un nuevo producto: ")
    precio = input("Ingresa su precio: ")
    cantidad = input("Ingresa la cantidad: ")

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado")

def cargar_productos():
    productos = []

    with open("productos.txt", "r") as archivo:
        for linea in archivo: 
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre" : nombre,
                "precio" : float(precio),
                "cantidad" : int(cantidad)
            }

            productos.append(producto)
    return productos

def buscar_productos(productos):

    nombre_buscar = input("Ingrese el nombre a buscar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            break
    else:
        print("Error no se encontro el producto")


def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = (f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
            archivo.write(linea)
    print("Se actualizo correctamenete")

while True:
    print("=== Gestor de Productos ===")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Guardar productos")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        mostrar_productos()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        productos = cargar_productos()
        buscar_productos(productos)
    elif opcion == "4":
        productos = cargar_productos()
        guardar_productos(productos)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida. Intente nuevamente.")

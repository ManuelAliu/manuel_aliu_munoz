# Diccionario para almacenar los productos
productos = {}

# Función para registrar productos
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    stock = int(input(f"Ingrese la cantidad en stock de {nombre}: "))
    
    # Registrar el producto en el diccionario
    productos[nombre] = {'precio': precio, 'stock': stock}
    print(f"Producto '{nombre}' registrado con éxito.\n")

# Función para mostrar la información de productos registrados
def mostrar_productos():
    print("Información de productos registrados:")
    for nombre, info in productos.items():
        print(f"{nombre} - Precio: {info['precio']}, Stock: {info['stock']}")
    print("\n")

# Programa principal
def menu():
    while True:
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("Gracias por usar el sistema de inventario de 'Mil Antojitos'.")
            break
        else:
            print("Opción no válida. Inténtelo nuevamente.\n")

# Ejecutar el menú
menu()

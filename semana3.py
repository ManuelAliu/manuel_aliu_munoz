def obtener_datos():
    while True:
        try:
            # Solicitar datos al usuario
            cantidad_inventario = int(input("Ingrese la cantidad actual en inventario: "))
            if cantidad_inventario < 0:
                print("Error: La cantidad en inventario no puede ser negativa. Intente denuevo.")
                continue  # Vuelve a solicitar los datos

            cantidad_vendida = int(input("Ingrese la cantidad vendida en el día: "))
            if cantidad_vendida < 0:
                print("Error: La cantidad vendida no puede ser negativa. Intente denuevo.")
                continue  # Vuelve a solicitar los datos
            
            # Verificar si la cantidad vendida es mayor que el inventario
            if cantidad_vendida > cantidad_inventario:
                print("Error: La cantidad vendida no puede exceder la cantidad en inventario.")
                continue  # Vuelve a solicitar los datos
            
            return cantidad_inventario, cantidad_vendida
        
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}. Por favor, intente de nuevo.")

def main():
    print("Bienvenido al sistema de control de inventario de Chocolamú")
    inventario, vendido = obtener_datos()
    nuevo_inventario = inventario - vendido
    print(f"La nueva cantidad en inventario es: {nuevo_inventario}")
    print("Gracias por utilizar el sistema de control de inventario.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

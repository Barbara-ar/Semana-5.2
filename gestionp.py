productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el precio.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para la cantidad.")
    
    producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    if not productos:
        print("No hay productos en el inventario.")
        return
    
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    nombre = input("Introduce el nombre del producto que quieres actualizar: ")
    
    for producto in productos:
        if producto['nombre'] == nombre:
            print("Deja en blanco si no deseas cambiar un campo.")
            nuevo_nombre = input(f"Introduce el nuevo nombre del producto (actual: {producto['nombre']}): ")
            nuevo_precio = input(f"Introduce el nuevo precio (actual: {producto['precio']}): ")
            nueva_cantidad = input(f"Introduce la nueva cantidad (actual: {producto['cantidad']}): ")

            # Si el usuario no cambia algún campo, se deja el valor anterior
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio:
                try:
                    producto['precio'] = float(nuevo_precio)
                except ValueError:
                    print("Precio inválido. Se mantiene el valor actual.")
            if nueva_cantidad:
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                except ValueError:
                    print("Cantidad inválida. Se mantiene el valor actual.")

            print(f"Producto '{nombre}' actualizado correctamente.")
            return
    
    print(f"El producto '{nombre}' no fue encontrado.")

def eliminar_producto():
    ver_productos()
    nombre = input("Introduce el nombre del producto que quieres eliminar: ")
    
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    
    print(f"El producto '{nombre}' no fue encontrado.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente en productos.txt.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("El archivo productos.txt no existe, se creará uno nuevo al guardar.")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()

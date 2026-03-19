""" 
Módulo de inventario.

Permite agregar productos al inventario y mostrarlos en pantalla.
Cada producto contiene nombre, precio y cantidad.
"""

inventario =[]

def agregar_producto():
    """Esta función solicita datos al usuario y agrega un producto al inventario"""

    nombre=str(input("Ingrese el producto a registrar:"))
    try:
        cantidad=int(input("Ingrese cuantas unidades desea registras:"))
    except:
        print("Cantidad invalidad")
        return
    try:
        precio=float(input("Ingrese el precio unitario de el producto:"))
    except:
        print("Precio invalido")
        return

    producto_registrado={"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto_registrado)
    print("Producto registrado")

def mostrar_inventario ():
    """Muestra todos los productos almacenados en el inventario"""

    if not inventario:
        print("No hay nada en el inventario")
    else:
        print("\n--- INVENTARIO ---\n")
        for producto_registrado in inventario:
            print("Producto:", producto_registrado["nombre"],
            "|Precio:", producto_registrado["precio"], 
            "|Cantidad:", producto_registrado["cantidad"],"\n")

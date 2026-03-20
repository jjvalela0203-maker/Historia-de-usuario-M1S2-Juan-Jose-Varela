""" 
Módulo de inventario.

Permite agregar productos al inventario y mostrarlos en pantalla.
Cada producto contiene nombre, precio y cantidad.
"""

from validaciones import pedir_texto_no_vacio, pedir_entero_positivo, pedir_float_positivo


inventario =[]

def agregar_producto():
    """Solicita datos al usuario y agrega un producto al inventario."""
    nombre = pedir_texto_no_vacio("Ingrese el producto a registrar: ")
    cantidad = pedir_entero_positivo("Ingrese cuantas unidades desea registrar: ")
    precio = pedir_float_positivo("Ingrese el precio unitario del producto: ")

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

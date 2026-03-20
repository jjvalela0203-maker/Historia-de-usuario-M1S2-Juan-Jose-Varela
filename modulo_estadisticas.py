"""
Módulo de estadísticas.

Permite calcular información básica del inventario como el valor total
de los productos almacenados y la cantidad de productos registrados.
"""
from modulo_inventario import inventario


def calcular_estadisticas():
    """Calcula el valor total del inventario y la cantidad de productos registrados."""
    if not inventario:
        print("No hay productos para calcular estadísticas.\n")
        return

    valor_total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
    cantidad_productos_registrados = len(inventario)
    cantidad_total_unidades = sum(producto["cantidad"] for producto in inventario)

    print("\n--- ESTADISTICAS ---")
    print("Valor total del inventario:", valor_total)
    print("Cantidad de productos registrados:", cantidad_productos_registrados)
    print("Cantidad total de unidades:", cantidad_total_unidades)
    print()

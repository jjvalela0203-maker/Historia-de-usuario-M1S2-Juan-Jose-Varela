
from validaciones import pedir_opcion_menu
import modulo_estadisticas
import modulo_inventario


def menu():
    """Muestra el menú principal y controla el flujo del programa."""
    while True:
        print("=" * 15, "MENU", "=" * 15)
        print("1) Agregar producto")
        print("2) Mostrar inventario")
        print("3) Calcular estadisticas")
        print("4) Salir")

        opcion = pedir_opcion_menu()

        if opcion == 1:
            modulo_inventario.agregar_producto()
        elif opcion == 2:
            modulo_inventario.mostrar_inventario()
        elif opcion == 3:
            modulo_estadisticas.calcular_estadisticas()
        elif opcion == 4:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    menu()

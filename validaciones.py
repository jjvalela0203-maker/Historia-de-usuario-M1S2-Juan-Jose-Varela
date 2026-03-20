"""
Módulo de validaciones.

Contiene funciones para validar la entrada de datos del usuario,
asegurando que los valores ingresados sean correctos y evitando
errores de ejecución por datos inválidos.
"""
def pedir_texto_no_vacio(mensaje):
    """Solicita un texto al usuario y valida que no esté vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El dato no puede estar vacío.")


def pedir_entero_positivo(mensaje):
    """Solicita un número entero y valida que sea mayor que cero."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Ingrese un número entero mayor que 0.")
        except ValueError:
            print("Ingrese un número entero válido.")


def pedir_float_positivo(mensaje):
    """Solicita un número decimal y valida que sea mayor que cero."""
    while True:
        try:
            texto = input(mensaje).strip().replace(",", ".")
            valor = float(texto)
            if valor > 0:
                return valor
            print("Ingrese un número mayor que 0.")
        except ValueError:
            print("Ingrese un valor numérico válido.")


def pedir_opcion_menu():
    """Solicita una opción del menú y valida que esté entre 1 y 4."""
    while True:
        try:
            opcion = int(input("Ingrese su opcion (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            print("Opcion no existente")
        except ValueError:
            print("Ingrese una opcion valida")

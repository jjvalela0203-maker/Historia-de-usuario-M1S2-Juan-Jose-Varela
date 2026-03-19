import modulo_inventario

sw= True
while sw is True:
    print("="*15, "MENU", "="*15)
    print("1) Agregar porducto")
    print("2) Mostrar inventario")
    print("3) Calcular estadisticas")
    print("4) Salir")

    try:
        opcion=int(input("Ingrese su opcion (1-4):"))
        if opcion < 1 or opcion > 4:
            print("Opcion no existente")
            opcion=int(input("Ingrese su opcion (1-4):"))
    except ValueError:
        print("Ingrese una opcion valida")
        opcion=int(input("Ingrese su opcion (1-4):"))
        if opcion <1 or opcion > 4:
            print("Opcion no existente")
            opcion=int(input("Ingrese su opcion (1-4):"))

    if opcion == 1:
        modulo_inventario.agregar_producto()
    


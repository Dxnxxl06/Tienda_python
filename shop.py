productos = ["Pan","Leche","Cafe","Tostado","Coca-Cola ☠︎"]
#             0      1        2      3          4
precios = [1500, 3700, 8500, 1000, 4500]
nombreTienda = "⛩︎  OTIA TIO ⛩︎"
carrito = [productos]
cantidad = []
total = 0

print (f"Bienvenidos a {nombreTienda}")
print ("Compre o no entre")


while True: 
    menu = f"""
    MENU
    1. Producto
    2. Mi carrito ({len(carrito)} : ${total})
    3. Finalizar
    """



    print(menu)
    opcion = input("Seleccione una opcion:")
    if opcion == "1":
        print (f"Productos disponibles: {len(productos)}")
        for posicion in range(5):
            print("----------------------------")
            print(f"{posicion+1}. {productos[posicion]} $ {precios[posicion]}") 
        busqueda = int(input("ingrese la posicion del producto: ")) - 1 #No olvidar incremento para la interfaz del usuario. Yo veo de 0 a 4 y el usuario de 1-5

    elif opcion == "2":
        print(f"Productos disponibles: {len(productos)}")
        for posicion in range(5):
            print("----------------------------")
            print(f"{posicion+1}. {productos[posicion]} $ {precios[posicion]}") 
        busqueda = int(input("Ingrese la posicion del producto: "))
        if busqueda < 0 or busqueda > len(productos):
            print("Seleccione un rasgo especifico valido!")
            input("Continuar...")
            continue
        cantidad_busqueda = int(input(f"Ingrese la cantidad del profucto: {productos[busqueda]} ${precios[busqueda]}"))
        carrito.append(productos[busqueda])
        cantidad.append(cantidad_busqueda)
        total = total + (cantidad_busqueda * precios[busqueda])
        print(carrito)
        print()


    elif opcion == "3":
        print("Gracias por comprar! \nHasta la proxima")
        input("Continuar...")
        break 

    else:
        print("Opcion no valida...")
        input("Continuar...")






    
UtiliesEscolares = ["Lapiz", "Cuadernos", "Lapiceros", "Reglas"]

NombreTienda = ("Colegio robinhood")



print("")
print(NombreTienda)
while True:
    menu = f"""
      Menu
        1. Listar los utiles
        2. Agregar nuevos utiles
        3. Listar todos los utiles
        3. Actualizar un util
        4. Eliminar util 
        5.Salir
"""
    print(menu)

    opcion = input("Seleccionaste la opcion: ")
    print("")
    if opcion == "1":
        print(f"Productos disponible : {len(UtiliesEscolares)}")
        for posicion, item in enumerate(UtiliesEscolares):
            print(f"{posicion+1}. {item}")
        input("Continuar...")

    if opcion == "2":
        UtiliesEscolares.append(input("Ingrese el nuevo util escolar :"))

    if opcion == "3":
        print("Actualizar un util  : ")
        for item in UtiliesEscolares:
            respuesta = input(f"Quiere actualizar el valor de : {item}\ns\n")
            if respuesta == "s":
                item = input("ingrese el nuevo nombre: ")
                UtiliesEscolares[posicion- 1] = item
            print(f"Valor nuevo: {item}")
    if opcion == "4":
        print(f"Productos disponible : {len(UtiliesEscolares)}")
        for posicion, item in enumerate(UtiliesEscolares):
            print(f"{posicion+1}. {item}")
        input("Continuar...")
        print("")
        Elemento_eliminado = input("Ingrese el util escolar que quieres eliminar de la lista: ")
        print("")
        lista_lower = [item.lower() for item in UtiliesEscolares]
        if Elemento_eliminado in lista_lower:
            
            index = lista_lower.index(Elemento_eliminado)
          
            UtiliesEscolares.pop(index)
            print(f"Elemento eliminado correctamente: {Elemento_eliminado}")
        else:
            print(f"El elemento no se encuentra en la lista: {Elemento_eliminado}")
    if opcion == 5:
        print ("Estas seguro que quieres salir?:(")
        break

import os

libros = {}
prestamos = []
historial = []

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

# ----------------- GESTIÓN DE LIBROS -----------------

def agregarLibro():
    codigo = input("Código del libro: ")
    if codigo in libros:
        print("El libro ya existe.")
        return
    nombre = input("Nombre del libro: ")
    autor = input("Autor: ")
    editorial = input("Editorial: ")
    libros[codigo] = {"nombre": nombre, "autor": autor, "editorial": editorial}
    print("Libro agregado correctamente.")

def actualizarLibro():
    codigo = input("Código del libro a actualizar: ")
    if codigo not in libros:
        print("Libro no encontrado.")
        return
    print("Datos actuales:", libros[codigo])
    nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
    autor = input("Nuevo autor: ")
    editorial = input("Nueva editorial: ")
    if nombre:
        libros[codigo]["nombre"] = nombre
    if autor:
        libros[codigo]["autor"] = autor
    if editorial:
        libros[codigo]["editorial"] = editorial
    print("Libro actualizado.")

def eliminarLibro():
    codigo = input("Código del libro a eliminar: ")
    if codigo in libros:
        del libros[codigo]
        print("Libro eliminado.")
    else:
        print("Libro no encontrado.")

def menuGestionLibros():
    while True:
        print("\n--- Gestión de Libros ---")
        print("1. Agregar Libro")
        print("2. Actualizar Libro")
        print("3. Eliminar Libro")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        limpiarConsola()
        if opcion == "1":
            agregarLibro()
        elif opcion == "2":
            actualizarLibro()
        elif opcion == "3":
            eliminarLibro()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

# ----------------- PRÉSTAMO -----------------

def crearPrestamo():
    codigo = input("Código del libro: ")
    if codigo not in libros:
        print("El libro no existe.")
        return
    nombre = input("Nombre de la persona: ")
    documento = input("Documento: ")
    fecha = input("Fecha del préstamo (YYYY-MM-DD): ")
    prestamo = {"codigo": codigo, "nombre": nombre, "documento": documento, "fecha": fecha, "devuelto": False}
    prestamos.append(prestamo)
    historial.append(prestamo.copy())
    print("Préstamo registrado.")

# ----------------- DEVOLUCIÓN -----------------

def crearDevolucion():
    documento = input("Documento del usuario: ")
    encontrados = [p for p in prestamos if p["documento"] == documento and not p["devuelto"]]
    if not encontrados:
        print("No hay préstamos activos para este documento.")
        return
    for p in encontrados:
        p["devuelto"] = True
    print("Todos los préstamos marcados como devueltos.")

# ----------------- LISTADOS -----------------

def listarLibros():
    print("\n--- Libros Registrados ---")
    if not libros:
        print("No hay libros.")
        return
    for codigo, info in libros.items():
        print(f"{codigo} - {info['nombre']} ({info['autor']}, {info['editorial']})")

def listarLibrosPrestados():
    print("\n--- Libros Prestados (sin devolución) ---")
    activos = [p for p in prestamos if not p["devuelto"]]
    if not activos:
        print("No hay libros prestados.")
        return
    for p in activos:
        libro = libros.get(p["codigo"], {})
        print(f"{p['nombre']} ({p['documento']}) → {libro.get('nombre', 'Libro no encontrado')} - {p['fecha']}")

def historialPrestamos():
    print("\n--- Historial de Préstamos ---")
    if not historial:
        print("No hay historial.")
        return
    for h in historial:
        estado = "Devuelto" if h["devuelto"] else "Activo"
        libro = libros.get(h["codigo"], {"nombre": "Desconocido"})
        print(f"{h['nombre']} ({h['documento']}) → {libro['nombre']} | {h['fecha']} | {estado}")

# ----------------- MENÚ PRINCIPAL -----------------

def menuPrincipal():
    while True:
        print("\n===== BIBLIO CAMPUS =====")
        print("1. Gestión de Libros")
        print("2. Préstamo de Libros")
        print("3. Devolución de Libros")
        print("4. Listar Libros")
        print("5. Listar Libros Prestados")
        print("6. Historial de Préstamos")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        limpiarConsola()
        if opcion == "1":
            menuGestionLibros()
        elif opcion == "2":
            crearPrestamo()
        elif opcion == "3":
            crearDevolucion()
        elif opcion == "4":
            listarLibros()
        elif opcion == "5":
            listarLibrosPrestados()
        elif opcion == "6":
            historialPrestamos()
        elif opcion == "7":
            print("Gracias por usar Biblio Campus.")
            break
        else:
            print("Opción inválida.")

# ----------------- EJECUCIÓN -----------------
menuPrincipal()
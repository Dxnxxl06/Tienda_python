palabras = []

palabras.append("Python")
palabras.append(5)
palabras.append(True)
palabras.append(input("Ingrese un descripcion!: "))

palabras.insert(10, "ID: 2")


print("Por elementos: ")
for item in palabras:
    print(item)

palabras[3] = False

print("Por elementos despues del update: ")
for item in palabras:
    respuesta = input(f"Quiere actualizar el valor de: {item} \ns\\n")
    if respuesta == "s":
        item = input("Ingrese el nuevo valor: ")
    print(f"Valor nuevo {item}")

print("Por elemento final: ")
for item in palabras:
    print(item)





#print(f"Palabras: {len(palabras)}")
#for item in palabras:
 #   print(item)


#print("Por posicion: ")
#print(palabras[2])
#print("por indice: ")



#for indice in range(len(palabras)): 
#   print(indice)
#  print(palabras[indice])
# print(type(indice))
#print(palabras[indice])
#print(type(palabras[indice]))

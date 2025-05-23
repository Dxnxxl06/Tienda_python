# Nota: 1- 5 
# Si tiene mas de 3.5 es aprobado
#elsesi no es desaprobado
nombre = input("Ingrese su nombre: ")
input("Su nota va de 1-5")

Nota = float(input("Ingrese su nota: "))
aprobado = ("Usted ha sido aprobado con: ")
desaprobado = ("Usted no ha aprobado con: ")
rec = ("puedes ir a recuperaciones con:")

if Nota >= 3.5:
    print(nombre,aprobado,Nota)
elif Nota >= 2.5 < 3.5:
    print(nombre,rec,Nota)
else:
    print(nombre,desaprobado,Nota)    

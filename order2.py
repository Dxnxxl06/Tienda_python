lista = [500, 3, 9, 4, 7, 0, 15, 80, 200, -1, 73, 7, 15, 69, 72]

def ordenar():

    for izq in range(len(lista) -1):
       for der in range(izq +1,len(lista)):
           if lista[izq] <lista[der]:
            tem =lista [izq]
            lista[izq] =lista[der]
            lista[der] = tem

           
            print(f"der: {lista}") 
    print(f"izq: {lista}")


ordenar()
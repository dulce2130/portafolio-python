def ordenar(matriz):
    for fila in matriz:
        print("[", end = " ")
        for elemento in fila:
            print("{:4}".format(elemento), end="")
        print("]")
    return matriz

a=[]
#1. Llenado de matrices
def llenado(filas, columnas):
    for i in range(filas):
        a.append([])
        for j in range(columnas):
            valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
            a[i].append(valor)
    return a
b=[]
def llenadoB(filas, columnas):
    for i in range(filas):
        b.append([])
        for j in range(columnas):
            valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
            b[i].append(valor)
    return b

print("---- Llenado Matriz A ----")
fA = int(input("Introduce el número de filas: "))
cA = int(input("Introduce el número de columnas: "))
a=llenado(fA, cA)
a=ordenar(a)
print("Matriz sin ordenar: ", a)
print()
print("---- Llenado Matriz B ----")
fB = int(input("Introduce el número de filas: "))
cB = int(input("Introduce el número de columnas: "))
b=llenadoB(fB, cB)
b=ordenar(b)
print("Matriz sin ordenar: ",b)
print()

#2. Verifica si la matriz es nula
def nula(a, fA, cA):
    for i in range(fA):
        for j in range(cA):
            if a[i][j] == 0:
                print("La matriz es nula")
                break  
            else:
                print("La matriz no es nula")
                break
        break
    
    return a
#3. Imprimir la diagonal Principal
def diagonal(matriz, fila, columna):
    a=[]
    if fila == columna:
        for i in range(fila):
            a.append(matriz[i][i])
    else:
        print("La matriz no tiene diagonal principal")
    return a
#4. Imprimir la traza Matriz 
suma = "No hay diagonal principal, por tanto, no hay traza"
def traza(a,columnas):
    global suma
   
    if len(a[0]) != len(a):
        print()
    else:
        suma = sum(a[i][i] for i in range(columnas))
    return suma
#5. Imprimir la Diagonal Secundaria
sumaDS = "La matriz no tiene diagonal secundaria"
def sumaDiaSec(a, columnas, filas):
    global sumaDS
    if len(a[0]) == len(a):
        sumaDS = sum(a[i][columnas-i-1] for i in range(columnas))
    else:
        print()  
    return sumaDS
#6. Verifica si la Matriz es Superior
def superior(a, columnas, filas):
    i = 0
    band = True

    while((band) and (i<columnas)):
        for j in range(i+1, filas):
            if(a[j][i] != 0):
                band=False
                break
        i = i+1
    if(band):
        print("La matriz es triangular superior")
    else:
        print("La matriz no es triangular superior")
    return a
#7. Verifica si la Matriz es Inferior
def inferior(a, columnas, filas):
    i = int(0)
    band = True
    while((band) and (i < columnas)):
        for j in range(i+1, filas):
            if(a[i][j] != 0):
                band=False
                break
        i = i+1
    if(band):
        print("La matriz es triangular inferior")
    else:
        print("La matriz no es triangular inferior")
    return a
# 8. Verifica si la Matriz es Diagonal,si es, verificar si es identidad
def matrizDiagonal(a, columnas, filas):
    i = 0
    d = []
    band = True

    while((band) and (i<columnas)):
        for j in range(i+1, filas):
            if(a[j][i-1] != 0) and (a[i][j-1] != 0):
                band=False
                break
        i = i+1
        
    if(band): 
        print("La matriz es diagonal")
        for i in range(filas):
            d.append(a[i][i])
            if(a[i][i] == 1):
                print("Es una matriz identidad")
                break
            else:
                print("No es una matriz identidad")
                break
    else:
        print("La matriz no es diagonal")
    return a
#9. Imprimir la Matriz Opuesta
def opuesta(a, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            a[i][j]= a[i][j]*(-1)
    print("La matriz opuesta es: ")
    return a
#10. Imprimir la Matriz Transpuesta
def transpuesta(m):
    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
    print("La matriz transpuesta es:")
    tO = ordenar(t)
    print()
    return tO
#11. Imprime el resultado de multiplicar las 2 matrices
def multiplicacion(m1, m2):
    if len(m1[0])== len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
        print()
        print("Multiplicación de A x B")
        return m3
    else:
        return None
#12. Salir
def salir():
    return "Saliendo..."

#Menú
def menu():
    opc = int(input("---- Operaciones con Matrices ----\n"+
                    "1.-  Verificación de Matriz Nula\n"+
                    "2.-  Diagonal principal\n"+
                    "3.-  Traza de la Matriz\n"+
                    "4.-  Suma de la Diagonal Secundaria\n"+
                    "5.-  Verificación si la Matriz es Superior\n"+
                    "6.-  Verificación si la Matriz es Inferior\n"+
                    "7.-  Verificación de Matriz Diagonal (y/o identidad)\n"+
                    "8.-  Matriz Opuesta\n"+
                    "9.-  Matriz Transpuesta\n"+
                    "10.- Multiplicación de A x B\n"+
                    "11.- Salir\n"
                    "\nElije una Opcion: "))
    return opc

opcion = 0

while opcion != 11:
    opcion = menu()

    if opcion == 1:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            nulaA = nula(a, fA, cA)
            print(nulaA)
        elif op == 2:
            nulaB = nula(b, fB, cB)
            print(nulaB)
        print()

    if opcion == 2:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            diagA = diagonal(a, fA, cA)
            print("La diagonal principal de A es: ", diagA)
        elif op == 2:
            diagB = diagonal(b, fB, cB)
            print("La diagonal principal de B es: ", diagB)
        print()

    if opcion == 3:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            trazaA = traza(a, cA)
            print("La traza de A es: ", trazaA)
        elif op == 2:
            trazaB = traza(b, cB)
            print("La traza de B es: ", trazaB)
        print()

    if opcion == 4:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            sumDSA= sumaDiaSec(a, cA, fA)
            print("La Suma de la Diagonal Secundaria de A es: ", sumDSA)
        elif op == 2:
            sumDSB= sumaDiaSec(b, cB, fB)
            print("La Suma de la Diagonal Secundaria de B es: ", sumDSB)
        print()

    if opcion == 5:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            superiorA=superior(a, cA, fA)
            print(superiorA)
        elif op == 2:
            superiorB=superior(b, cB, fB)
            print(superiorB)
        print()

    if opcion == 6:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            inferiorA = inferior(a, cA, fA)
            print(inferiorA)
        elif op == 2:
            inferiorB = inferior(b, cB, fB)
            print(inferiorB)
        print()

    if opcion == 7:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            MaDiA = matrizDiagonal(a, cA, fA)
            print(MaDiA)
        elif op == 2:
            MaDiB = matrizDiagonal(b, cB, fB)
            print(MaDiB)
        print()

    if opcion == 8:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            opuestaA = opuesta(a, fA, cA)
            opA = ordenar(opuestaA)
            print("Matriz sin ordenar: ", opA)
        elif op == 2:
            opuestaB = opuesta(b, fB, cB)
            opB = ordenar(opuestaB)
            print("Matriz sin ordenar: ", opB)
        print()

    if opcion == 9:
        op = int(input("Escriba 1 para usar «A» ó 2 para usar «B»: "))
        if op == 1:
            matrizTA = transpuesta(a)
            print("Matriz sin ordenar: ", matrizTA)
        elif op == 2:
            matrizTB = transpuesta(b)
            print("Matriz sin ordenar: ", matrizTB)
        print()

    if opcion == 10:
        mult = multiplicacion(a, b)
        if mult == None:
            print("No se pueden multiplicar")
        else:
            orden = ordenar(mult)
        print("Matriz sin ordenar: ", mult)
    print()

    if opcion == 11:
        salir()
        print("Saliendo del programa")

    if opcion > 11:
        print("Opción invalida")
    
    
    
            
            
        






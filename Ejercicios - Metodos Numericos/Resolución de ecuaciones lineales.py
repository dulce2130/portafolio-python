from matplotlib import pyplot
print("Programa que soluciona un sistema de ecuaciones de primer grado")
print(" ")

print("Datos de la ecuación 1: ")
x1=int(input("Ingresa el valor del coeficiente de x: "))
y1=int(input("Ingresa el valor del coeficiente de y: "))
c1=int(input("Ingresa el valor del término independiente: "))

def Ecuacion1(n):
    return (c1-(x1*n))/y1
n = range(-10,10)
pyplot.plot(n,[Ecuacion1 (i) for i in n])

print("")
print("Datos de la ecuación 2: ")
x2=int(input("Ingresa el valor del coeficiente de x: "))
y2=int(input("Ingresa el valor del coeficiente de y: "))
c2=int(input("Ingresa el valor del termino independiente: "))

def Ecuacion2(m):
    return (c2-(x2*m))/y2
m=range(-10,10)
pyplot.plot(m,[Ecuacion2 (i) for i in m])

pyplot.axhline(0, color=("black"))
pyplot.axvline(0, color=("black"))

pyplot.xlim(-10,10)
pyplot.ylim(-10,10)

D= (x1*y2)-(y1*x2)
Nx= (c1*y2)-(y1*c2)
x= Nx/D
Ny= (x1*c2)-(c1*x2)
y= Ny/D

print("Las soluciones son: x= ",x," & y= ",y,)
pyplot.show()






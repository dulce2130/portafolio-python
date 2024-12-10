import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import numpy
import math
import pandas as pd
import matplotlib.pyplot as plot

datos=[]
def guardarDatos():
    cantDat=num.get()
    datos.append(num.get())
    print(datos)
    dat.set("Los números que introdujo son: "+str(datos))

def moda():
    n = len(datos) #Obtener los cantidad de elementos de la lista
    c = 0 #Contador de las veces que se repite cada elemento
    mayor = 0
    for i in range(n):
        c = 0 #Reinicia la cuenta antes de proceder a contar los siguientes elementos
        for j in range(n):#Comparación de números
            if (datos[i] == datos[j]):
                c = c + 1 #Contar las ocurrencias del elemento
        if (c > mayor):
            mayor = c #intercambio de variables
            m = datos[i]
    modaR.set("La moda es: "+str(m)+ " y se repite "+str(mayor)+ " veces")
    return m


def media():
    suma = 0
    for i in datos:
        suma += i
        promed = suma/len(datos)
    mediaR.set("La media es: "+str(promed))
    return promed

def ordenar(datos):

    n = len(datos)
    for i in range(n):
        if datos[i]<datos[i-1]:
            v = datos[i]
            j = i
            #Desplazamientos
            while j > 0 and v < datos[j-1]:
                datos[j]=datos[j-1]
                j=j-1
                datos[j]=v
       
        i=i+1 #Incremento   
    return datos

orden = ordenar(datos)


def mediana():
    orden = ordenar(datos)
    lon = len(orden)#Obtener longitud
    mitad = int(lon/2)
  #Sila longitud es par, promediar elementos centrales
    if lon % 2 == 0:
        medi = (orden[mitad - 1] + orden[mitad])/2
    else:
        medi = orden[mitad]

    medianaR.set("La mediana es: "+str(medi))
    return medi




def graficaFrecuencia():
    intervalos =  range(min(datos), max(datos)+2)#Calculamos los extremos

    
    plot.hist(x = datos, bins = intervalos, color="lavender", edgecolor='black',rwidth=2)
    plot.title("Moda, Mediana y Media")
    plot.xlabel("Datos")
    plot.ylabel("Frecuencia")
    
    plot.xticks(intervalos)

    mo = moda()
    ypoints = mo
    plot.axvline(ypoints,0,1, label="Moda",color='teal')
    plot.legend()

    medA = media()
    ypoints = medA
    plot.axvline(ypoints,0,1, label="Media",color='brown')
    plot.legend()

    med1 = mediana()
    ypoints = med1
    plot.axvline(ypoints,0,1, label="Mediana")
    plot.legend()

    plot.show()
    
def rango():
    orden = ordenar(datos)
    mayor = orden[-1]
    menor = orden[0]

    r = mayor - menor

    rangoR.set("El rango es: "+str(r))
    return r

def varianza():
   suma = 0
   n = len(datos)
   num = 0
   x = 0
   y = 0
   for i in datos:
       suma = suma + i
       promed = suma/n
   for j in datos:
       num = j - promed
       x = num*num
       y = y+x
       z = y/n

   varianzaR.set("La varianza es: "+str(z))
   return z


def desviacionEstandar():
    suma = 0
    n = len(datos)
    num = 0
    x = 0
    y = 0
    for i in datos:
        suma = suma + i
        promed = suma/n
    for j in datos:
        num = j - promed
        x = num*num
        y = y+x
        z = y/n

    desv = math.sqrt(z)
    desviacionR.set("La desviación estándar es: "+str(desv))
    return desv
    
def graficaVar():
    intervalos =  range(min(datos), max(datos)+2)

    plot.hist(x = datos, bins = intervalos, color="lavender", edgecolor='black',rwidth=2)
    plot.title("Varianza y Desviación estandar")
    plot.xlabel("Datos")
    plot.ylabel("Frecuencia")
    
    plot.xticks(intervalos)

    n = len(datos) 
    c = 0 
    mayor = 0
    for i in range(n):
        c = 0 
        for j in range(n):
            if (datos[i] == datos[j]):
                c = c + 1
        if (c > mayor):
            mayor = c 
            m = datos[i]
    
    vari = mayor
    ypoints = vari
    plot.axhline(ypoints,0,1,color='orange')


    for i in range(n):
        c = 0 
        for j in range(n):
            if (datos[i] == datos[j]):
                c = c + 1 
        if (c < mayor):
            mayor = c 
            m = datos[i]

    desv = mayor
    ypoints = desv
    plot.axhline(ypoints,0,1,color='violet')
    #plot.legend()


    plot.show()


def pares():
    par = []

    for n in datos:
        if n % 2 == 0:
            par.append(n)
  
    n = len(par)
   
    for i in range(n-1):
        for j in range(n-1):
            if par[j] > par[j+1]:
                t = par[j]
                par[j] = par[j+1]
                par[j+1]= t

    for i in range(n//2):
        par[i], par[n-i-1] = par[n-i-1], par[i]

    paresR.set("Pares en orden descendente son: "+str(par))
    return par     

def inpares():
    inpar = []
    for n in datos:
        if n % 2 != 0:
            inpar.append(n)
  
    suma = 0
    for elemento in inpar:
         suma += elemento

    inparesR.set("La suma de los números impares es: "+str(suma))
    return suma

def primos():
     primo = []
     for n in datos:
          cont=0
          for i in range(1,n+1):
               if n%i == 0:
                    cont += 1
          if cont==2:
               primo.append(n)

     primosR.set("Primos en orden ascendente: "+str(primo))
     return ordenar(primo)

def multiplos():
     multiplo = []
     for n in datos:
          if n % 3 == 0 and n % 5 == 0:
               multiplo.append(n)

     multiplosR.set("Los multiplos entre 3 y 5: "+str(multiplo))
     return multiplo



#Ventana
ventana=tk.Tk()
ventana.title("Programa Tkinter")
ventana.configure(background="snow")
ventana.geometry("800x830")

#Variables
num = tk.IntVar()
dat = tk.StringVar()
modaR = tk.StringVar()
mediaR = tk.StringVar()
medianaR = tk.StringVar()
rangoR = tk.StringVar()
varianzaR = tk.StringVar()
desviacionR = tk.StringVar()
paresR = tk.StringVar()
inparesR = tk.StringVar()
primosR = tk.StringVar()
multiplosR = tk.StringVar()

#Etiqueta
bienvenida = tk.Label(ventana,font="Helvica 14", text = "¡BIENVENIDO!", fg="maroon")
bienvenida.pack(padx = 5, pady =4, ipadx = 5, ipady=5, fill=tk.X)

textoN=tk.Label(ventana,font="Helvica 10",
                text="1.Introduzca un número\n2.Presione guardar\n3.Borre Ael número\nRepita esto para guardar todos los números deseados",
                bg = "light sea green", fg = "white")
textoN.pack(padx = 5, pady =4, ipadx = 5, ipady=5, fill=tk.X)
#caja de texto
caja=tk.Entry(ventana,textvariable=num)
caja.pack(padx = 5, pady =4, ipadx = 5, ipady=5, fill=tk.X)
#Etiqueta resultado
textoR=tk.Label(ventana,textvariable=dat)
textoR.pack(padx = 5, pady =4, ipadx = 5, ipady=5, fill=tk.X)
#Boton
boton=tk.Button(ventana,font="Helvica 11",text="Guardar",command=guardarDatos,bg="medium orchid",fg="white")
boton.pack(padx = 5, pady =4, ipadx = 5, ipady=5, fill=tk.X)

botonMo=tk.Button(ventana,font="Helvica 9",text="Moda",command = moda,bg="sky blue",fg="white")
botonMo.place(x=10, y=300, width=100, height=30)
resulMo=tk.Label(ventana,font="Helvica 8",textvariable=modaR)
resulMo.place(x=120, y=300, width=300, height=30)

botonPro=tk.Button(ventana,font="Helvica 9",text="Media",command = media,bg="light salmon",fg="white")
botonPro.place(x=10, y=350, width=100, height=30)
resulPro=tk.Label(ventana,font="Helvica 8",textvariable=mediaR)
resulPro.place(x=120, y=350, width=300, height=30)

botonMe=tk.Button(ventana,font="Helvica 9",text="Mediana",command = mediana,bg="plum",fg="white")
botonMe.place(x=10, y=400, width=100, height=30)
resulMe=tk.Label(ventana,font="Helvica 8",textvariable=medianaR)
resulMe.place(x=120, y=400, width=300, height=30)

botonRa=tk.Button(ventana,font="Helvica 9",text="Rango",command = rango,bg="gold2",fg="white")
botonRa.place(x=10, y=450, width=100, height=30)
resulRa=tk.Label(ventana,font="Helvica 8",textvariable=rangoR)
resulRa.place(x=120, y=450, width=300, height=30)

botonVa=tk.Button(ventana,font="Helvica 9",text="Varianza",command = varianza,bg="slate blue",fg="white")
botonVa.place(x=10, y=500, width=100, height=30)
resulVa=tk.Label(ventana,font="Helvica 8",textvariable=varianzaR)
resulVa.place(x=120, y=500, width=300, height=30)

botonDe=tk.Button(ventana,font="Helvica 9",text="Desviación estándar",command = desviacionEstandar,bg="peru",fg="white")
botonDe.place(x=10, y=550, width=140, height=30)
resulDe=tk.Label(ventana,font="Helvica 8",textvariable=desviacionR)
resulDe.place(x=160, y=550, width=260, height=30)

botonPar=tk.Button(ventana,font="Helvica 9",text="Pares ordenados",command = pares,bg="medium aquamarine",fg="white")
botonPar.place(x=10, y=600, width=140, height=30)
resulPar=tk.Label(ventana,font="Helvica 8",textvariable=paresR)
resulPar.place(x=160, y=600, width=260, height=30)

botonInpar=tk.Button(ventana,font="Helvica 9",text="Suma de inpares",command = inpares,bg="violet",fg="white")
botonInpar.place(x=10, y=650, width=140, height=30)
resulInpar=tk.Label(ventana,font="Helvica 8",textvariable=inparesR)
resulInpar.place(x=160, y=650, width=260, height=30)

botonPrimos=tk.Button(ventana,font="Helvica 9",text="Primos ordenados",command = primos,bg="tan",fg="white")
botonPrimos.place(x=10, y=700, width=140, height=30)
resulPrimos=tk.Label(ventana,font="Helvica 8",textvariable=primosR)
resulPrimos.place(x=160, y=700, width=260, height=30)

botonMul=tk.Button(ventana,font="Helvica 9",text="Multiplos de 3 y 5",command = multiplos,bg="coral",fg="white")
botonMul.place(x=10, y=750, width=140, height=30)
resulMul=tk.Label(ventana,font="Helvica 8",textvariable=multiplosR)
resulMul.place(x=160, y=750, width=260, height=30)


botonFrec=tk.Button(ventana,font="Helvica 11",text="Moda, Media y Mediana \n (Gráfica)",command = graficaFrecuencia,
                    bg="cornFlowerBlue",fg="white")
botonFrec.place(x=500, y=400, width=220, height=90)

botonFrec=tk.Button(ventana,font="Helvica 11",text="Varianza y Desviación Estándar \n (Gráfica)",
                    command = graficaVar,bg="DarkTurquoise",fg="white")
botonFrec.place(x=500, y=550, width=220, height=90)

ventana.mainloop()


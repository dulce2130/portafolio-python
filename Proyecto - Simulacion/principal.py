# ISC 5M Simulación Proyecto Final

from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox as mb
import random

ventana = Tk()

ventana.title("Proyecto Final de Simulación")
ventana.geometry("1400x700")
fuente = Font(family="Rockwell",size='20')
imagen = PhotoImage(file = "aguacate.png")
background = Label(image = imagen, text = "Imagen S.O de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
background.config(bg = "DarkSeaGreen2")

hectareas = StringVar()
precio = StringVar()
tAguacate = StringVar()
edadMisma = StringVar()
estadoP = StringVar()
suelo= StringVar()

Label( text = "Producción de Aguacate", font = ('Comic Sans MS', 28, 'bold'), fg="SpringGreen4", bg = "DarkSeaGreen2").place(x=480, y=20)

Label( text = "Produccion aproximada (kg): ", font =fuente, fg="DarkGreen",bg = "DarkSeaGreen1").place(x=900, y=130)
Label( text = "Dinero total obtenido($MXN):", font =fuente, fg="DarkGreen",bg = "DarkSeaGreen1").place(x=900, y=230)
Label( text = "Ganancia obtenida ($MXN):", font =fuente, fg="DarkGreen",bg = "DarkSeaGreen1").place(x=900, y=330)
Label( text = "Pérdidas calculadas ($MXN): ", font =fuente, fg="DarkGreen",bg = "DarkSeaGreen1").place(x=900, y=430)
Label( text = "Dias de maduración: ", font =fuente, fg="DarkGreen",bg = "DarkSeaGreen1").place(x=900, y=530)



def limpiarEspacio():
    Label( text = "                                      ", font = fuente,bg="LightYellow2", fg = "black").place(x=900, y=180)
    Label( text = "                                      ", font = fuente,bg="LightYellow2", fg = "black").place(x=900, y=280)
    Label( text = "                                      ", font = fuente,bg="LightYellow2", fg = "black").place(x=900, y=380)
    Label( text ="                                       ", font = fuente,bg="LightYellow2", fg = "black").place(x=900, y=480)
    Label( text ="                                       ", font = fuente,bg="LightYellow2", fg = "black").place(x=900, y=580)


def met():
    limpiarEspacio()
    plantas = 0
    if(isFloat(hectareas.get()) and isFloat(precio.get())and isFloat(edadMisma.get())):
        for i in range(int(hectareas.get())):
            plants=random.randint(100,120)
            plantas+=plants
    
        if(estadoP.get()=='Tierno' and int(edadMisma.get())>2):
            madurar=random.randint(8,15)
            Label( text = madurar, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=580)
        elif(estadoP.get()=='Oscuro' and int(edadMisma.get())>2):
            madurar=random.randint(3,7)
            Label( text = madurar, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=580)
        
        if(tAguacate.get()=="Hass"):
            kilos=0
            if(int(edadMisma.get())>=12):
                for i in range(plantas):
                    if(suelo.get()=="Humedo"):
                        kilosCalculados=random.randint(100,150)
                        kilos+=kilosCalculados
                    elif(suelo.get()=="Reseco"):
                        kilosCalculados=random.randint(90,120)
                        kilos+=kilosCalculados

                Label( text = str(kilos) +" Kilos", font =fuente,bg="LightYellow2", fg = "black").place(x=900, y=180)
                dinero=kilos*int(precio.get())
                Label( text = dinero, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=280)

                invertido=0

                for i in range(plantas):
                    inverti=random.randint(500,800)
                    invertido+=inverti

                Label( text = invertido, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=380)
                ganancia=dinero-invertido
                Label( text = ganancia, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=480)

            elif(  int(edadMisma.get())>7 ):
                for i in range(plantas):
                    if(suelo.get()=="Humedo"):
                        kilosCalculados=random.randint(50,80)
                        kilos+=kilosCalculados
                    elif(suelo.get()=="Reseco"):
                        kilosCalculados=random.randint(40,60)
                        kilos+=kilosCalculados
                    Label( text = str(kilos) +" Kilos", font =fuente,bg="LightYellow2", fg = "black").place(x=900, y=180)
                    dinero=kilos*int(precio.get())
                    Label( text = dinero, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=280)
                invertido=0
                for i in range(plantas):
                    inverti=random.randint(400,700)
                    invertido+=inverti
                Label( text = invertido, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=380)
                ganancia=dinero-invertido
                Label( text = ganancia, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=480)

            elif(  int(edadMisma.get())>2 ):
                for i in range(plantas):
                    if(suelo.get()=="Humedo"):
                        kilosCalculados=random.randint(25,30)
                        kilos+=kilosCalculados
                    elif(suelo.get()=="Reseco"):
                        kilosCalculados=random.randint(15,25)
                    kilos+=kilosCalculados
                    Label( text = str(kilos) +" Kilos", font =fuente,bg="LightYellow2", fg = "black").place(x=900, y=180)
                    dinero=kilos*int(precio.get())
                    Label( text = dinero, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=280)
                invertido=0
                for i in range(plantas):
                    inverti=random.randint(300,400)
                    invertido+=inverti
                Label( text = invertido, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=380)
                ganancia=dinero-invertido
                Label( text = ganancia, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=480)

            else:
                mb.showinfo("Mensaje","La planta no produce aun")
            



        elif(tAguacate.get()=="Fuerte"):
            kilos=0
            if(int(edadMisma.get())>=12):
                for i in range(plantas):
                    if(suelo.get()=="Humedo"):
                        kilosCalculados=random.randint(80,110)
                        kilos+=kilosCalculados
                    elif(suelo.get()=="Reseco"):
                        kilosCalculados=random.randint(70,100)
                        kilos+=kilosCalculados
                Label( text = str(kilos) +" Kilos", font =fuente,bg="LightYellow2", fg = "black").place(x=900, y=180)
                dinero=kilos*int(precio.get())
                Label( text = dinero, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=280)
                invertido=0
                for i in range(plantas):
                    inverti=random.randint(400,700)
                    invertido+=inverti
                Label( text = invertido, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=380)
                ganancia=dinero-invertido
                Label( text = ganancia, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=480)


            elif(int(edadMisma.get())>7 ):
                for i in range(plantas):
                    if(suelo.get()=="Humedo"):
                        kilosCalculados=random.randint(50,70)
                        kilos+=kilosCalculados
                    elif(suelo.get()=="Reseco"):
                        kilosCalculados=random.randint(30,50)
                        kilos+=kilosCalculados
                    Label( text = str(kilos) +" Kilos", font =fuente,bg="LightYellow2", fg = "black").place(x=900, y=180)
                    dinero=kilos*int(precio.get())
                    Label( text = dinero, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=280)
                invertido=0
                for i in range(plantas):
                    inverti=random.randint(150,200)
                    invertido+=inverti
                Label( text = invertido, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=380)
                ganancia=dinero-invertido
                Label( text = ganancia, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=480)

            elif(int(edadMisma.get())>2 ):
                for i in range(plantas):
                    if(suelo.get()=="Humedo"):
                        kilosCalculados=random.randint(10,20)
                        kilos+=kilosCalculados
                    elif(suelo.get()=="Reseco"):
                        kilosCalculados=random.randint(10,50)
                        kilos+=kilosCalculados
                    Label( text = str(kilos) +" Kilos", font =fuente,bg="LightYellow2", fg = "black").place(x=900, y=180)
                    dinero=kilos*int(precio.get())
                    Label( text = dinero, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=280)
                invertido=0
                for i in range(plantas):
                    inverti=random.randint(150,200)
                    invertido+=inverti
                Label( text = invertido, font =fuente,bg="LightYellow2", fg="black").place(x=900, y=380)
                ganancia=dinero-invertido
            
            else:
                mb.showinfo("Mensaje","La planta no produce aun")

    promedios=[]
    promedios.append(kilos)
    promedios.append(dinero)
    promedios.append(ganancia)
    promedios.append(invertido)
    promedios.append(madurar)


    metodoLista(promedios)

pila=[]

def metodoLista(lista):
    pila.append(lista)
    print(pila)

    print(len(pila))
    pk,pd,pg,pi,pm=0,0,0,0,0


    for i in range(len(pila)):
        pk+=pila[i][0]
        pd+=pila[i][1]
        pg+=pila[i][2]
        pi+=pila[i][3]
        pm+=pila[i][4]

    print(f"Kilos promedios: {pk/len(pila)}  ")
    print(f"Dinero promedio:    {pd/len(pila)}")
    print(f"Promedio de ganancia:   {pg/len(pila)}")
    print(f"Promedio dinero invertido:  {pi/len(pila)}")
    print(f"Promedio tiempo de maduración:{pm/len(pila)} ")

Label( text = "Hectareas de aguacate: ", font =fuente, fg="black",bg = "DarkSeaGreen2").place(x=20, y=150)
Entry(textvariable=hectareas,font=fuente, width=20, highlightcolor= "Yellow", highlightthickness = 3).place(x=320,y=150)
Label(ventana,text="Tipo de aguacate: ",font=fuente, bg = "DarkSeaGreen2").place(x=20, y=200)
codigos = ttk.Combobox(ventana, textvariable=tAguacate, width=25, foreground="black",font=('Rockwell',18,'bold'))
codigos['values'] =['Hass','Fuerte']
codigos['state'] = 'readonly'
codigos.place(x=320,y=200)
codigos.current(0)


Label(ventana,text="Edad del aguacate: ",bg="DarkSeaGreen2",font=fuente).place(x=20, y=250)
Entry(textvariable=edadMisma,font=fuente, width=20, highlightcolor= "Yellow", highlightthickness = 3).place(x=320,y=250)
        
Label(ventana,text="Precio-Promedio: ",bg="DarkSeaGreen2",font=fuente).place(x=20, y=300)
Entry(textvariable=precio,font=fuente, width=20, highlightcolor= "Yellow", highlightthickness = 3).place(x=320,y=300)

Label(ventana,text="Estado del producto: ",bg="DarkSeaGreen2",font=fuente).place(x=20, y=350)
codigos=ttk.Combobox(ventana, textvariable=estadoP, width=25, foreground="black",font=('Rockwell',18,'bold'))
codigos['values'] = ['Tierno','Oscuro']
codigos['state'] = 'readonly'
codigos.place(x=320,y=350)
codigos.current(0)

Label(ventana,text="Suelo: ",bg="DarkSeaGreen2",font=fuente).place(x=20, y=400)
codigos=ttk.Combobox(ventana, textvariable=suelo, width=25, foreground="black",font=('Rockwell',18,'bold'))
codigos['values'] =['Reseco','Humedo']
codigos['state'] = 'readonly'
codigos.place(x=320,y=400)
codigos.current(0)

Button(text="Calcular Datos",font=fuente,bg="Green",fg="white",width=15,command=met, cursor="hand2").place(x=50, y=540)

def limpiarCajas():
    hectareas.set("")
    precio.set("")
    edadMisma.set("")
    

Button(text="Borrar Datos",font=fuente,bg="Green",fg="white",width=15,command=limpiarCajas, cursor="hand2").place(x=350, y=540)


def isFloat(element: str) -> bool:  #para saber si es una cadena de numeros o strings
    try:
        float(element)
        return True
    except ValueError:
        return False
        

ventana.mainloop()


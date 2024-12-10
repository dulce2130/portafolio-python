import tkinter.ttk as tkk
from tkinter.ttk import Treeview
from tkinter import *
from tkinter.font import Font
from tkinter import  Frame, Tk, Button, Entry, Label, Toplevel, messagebox, ttk
mascaraClaseC='255.255.255.0'
class Ventana(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x800")
        self.title("Cadena de tiendas")
        self.config(bg="grey")

        #self.panelCiudad=Tabla(self).grid(column=0, row=0)



def binario_a_decimal(binario):#5
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal


def formulaDosM(hostSubredes):#4
    
    hostSubredes.sort()#de menor a mayor
    hostSubredes.reverse()#voltea alreves el array
    
    global pilaDatosFinal
    
    pilaDatosFinal=[]
    
    global mascarasNuevas
    mascarasNuevas=[]
    dip=direccionRedIp[:-1]
    direccionRedIp1=direccionRedIp[len(direccionRedIp)-1]
    #dip=direccionRedIp1[:-1]
    for i in range(len(hostSubredes)):#33,126,10
        pilaDatos=[]
        pilaDatos.append(i+1)#numero de subred
        numero=hostSubredes[i]
        hostSolicitados=hostSubredes[i]
        potencia=0
        host=0
        numero=numero+2
        print("Subred Numero "+str(i+1)+" ")
        while(host<numero):#
            potencia+=1#2,3,4,5,6
            host=pow(2,potencia)#2,4,8,16,32
        

        prefijo=8-potencia#para sacar el numero ejemplo: 192.168.0.1/26
        bits=prefijo
        prefijo=prefijo+24#se le suman los 24 bits anterior
        #print("prefijo ",prefijo)
        hostDisponibles=host-2
        pilaDatos.append(host)
        pilaDatos.append(hostSolicitados)
        
        print("Host totales "+str(host)+" host disponibles para la subred "+str(hostDisponibles))#
        print("________________________________________________")
        #ip=direccionRedIp1[len(direccionRedIp1)-1]
        
        if(i==0):
            direccion=direccionRedIp
            #print("Gateway o direccion de red: "+str(direccionRedIp)+"/ "+str(prefijo))
            print("Gateway o direccion de red: "+str(direccion)+"/ "+str(prefijo))
        else:
            direccionRedIp1=int(direccionRedIp1)+1
            print("direc    --> ",direccionRedIp1)
            print("dipp -->",dip)
            direccion=dip+str(direccionRedIp1)
            #direccionRedIp1=dip+str(direccionRedIp1)
            print("Gateway o direccion de red: "+str(direccion)+"/ "+str(prefijo))
            #direccionRedIp1=dip+str(direccionRedIp1)


        ip=int(direccionRedIp1)
        #direccionRedIp1=dip+str(ip)
        #print("Gateway o direccion de red: "+str(direccionRedIp1)+"/ "+str(prefijo))
        
        
        primerIp=int(ip)
        primerIp=primerIp+1
        pi=primerIp
        primerIp=dip+str(primerIp)
        print("primer ip solicitada: ",primerIp)


        ultimaIp=hostSolicitados-1
        ultimaIp=pi+ultimaIp
        ultimaIp=dip+str(ultimaIp)
        print("ultima ip solicitada: ",ultimaIp)



        ultimaIpDisp=hostDisponibles-1
        ultimaIpDisp=int(pi)+int(ultimaIpDisp)
        uid=ultimaIpDisp
        ultimaIpDisp=dip+str(ultimaIpDisp)
        print("ultima ip disponible: ",ultimaIpDisp)

        broadcas=uid+1
        direccionRedIp1=broadcas
        broadcas=dip+str(broadcas)
        print("Broadcast: ",broadcas)
        mascara=""
        for i in range(bits): 
            mascara=mascara+"1"
        #print("unos acumulados ",mascara)
        #print("potenciaaaaaaa    --> ",potencia)
        for i in range(potencia):
            mascara=mascara+"0"
            
        #mascaraNueva='255.255.255.'+mascara

        #print("mascara ,  ",mascaraNueva)#ultimo octeto binario aun
        decimal=binario_a_decimal(mascara)
        mascaraNuevaDecimal='255.255.255.'+str(decimal)
        print("mascara con decimal el ultimo octeto ",mascaraNuevaDecimal)

        pilaDatos.append(mascaraNuevaDecimal)
        pilaDatos.append(direccion)#Este es el gateway
        pilaDatos.append(primerIp)
        pilaDatos.append(ultimaIp)
        pilaDatos.append(ultimaIpDisp)
        pilaDatos.append(hostSolicitados+2)#mas 2 por el gateway y broadcast
        #pilaDatos.append(hostDisponibles)
        pilaDatos.append(host-(hostSolicitados+2))
        pilaDatos.append(broadcas)
        pilaDatosFinal.append(pilaDatos)
        
        #direccionRedIp1=broadcas
        print("\n\n_______________________>")

    print("pila de datos ",pilaDatosFinal)
    
    
    
"""""
def numeroSubreds(numeroSubredes):#3
    global hostSubredes
    hostSubredes=[]
    i=1
    while(i<numeroSubredes+1):
        try:
            numHost=int(input("Ingresa el numero de host para la subred numero "+str(i)+":  ")) 
        except:
            print("Porfavor ingrese un numero valido")
        else:
            i+=1
            hostSubredes.append(numHost)
    
    hostSubredes.sort()#de menor a mayor
    hostSubredes.reverse()#voltea alreves el array
    print("subredes ",hostSubredes)
    formulaDosM()#Ahora mandamos a llamar a la funcion 2 a la m -2
"""""

"""""
def pideNumeroSubredes():#2
    try:
        numeroSubredes=int(input("Ingresa el numero de subredes:  "))
    except :
        print("!Ingrese un numero entero, no una cadena!")
        pideNumeroSubredes()
    else:
        numeroSubreds(numeroSubredes)
"""""


def direccionRed(diIP):#1
    global direccionRedIp, ip

    try:
        #direccionRedIp=input("INGRESA la direccion de red, IP: ")
        direccionRedIp = diIP

        dir=direccionRedIp.replace(".","")
        dir=dir
        formato="000.000.000.000"
        #ip="192.168.0.0"
        ip=direccionRedIp
        ip=ip.split('.')
        if(len(ip)<=len(formato)):#<12
            if(len(ip)==4):#validar que haya 3 puntos
                contador=0

                for i in range(len(ip)):
                    if(len(ip[i])<=3):#validar que cada octeto tenga maximo 3 caracteres
                        if(i==0):
                            print("i : ",i)
                            if(int(ip[i])>=192 and int(ip[i])<223):
                                contador+=1
                        elif(i==1):
                            print("i : ",i)
                            if(int(ip[i])>=0 and int(ip[i])<225):
                                contador+=1
                        elif(i==2):
                            print("i : ",i)
                            if(int(ip[i])>=0 and int(ip[i])<225):
                                
                                contador+=1
                        elif(i==3):
                            print("i : ",i)
                            if(int(ip[i])>=0 and int(ip[i])<225):
                                contador+=1

                if(contador!=4):
                    direccionRed(diIP)
                    print("Direccion ip incorrecta, verifiquela")

            else:

                direccionRed(diIP)
                print("Direccion ip incorrecta, verifiquela")
        else:
            direccionRed(diIP)
            print("Direccion ip incorrecta, verifiquela")
    except:
            print("excepción, porfavor ingresa una direccion correcta")
            direccionRed(diIP)
    #else:
        #pideNumeroSubredes()#
#direccionRed()


class Tabla(Frame):
    def __init__(self, container):
        super().__init__(container, bg='MediumOrchid1')
        self.container=container
        self.fuente=Font(family='Roboto',size='14')
        self.crearTabla()
        


    def crearTabla(self):
        self.fijarEstiloTabla()
        self.tabla=Treeview(style="mystyle.Treeview",height=4, columns=("#0","#1","#2","#3","#4","#5","#6","#7","#8","#9"))
        self.tabla.column('#0',width=50,anchor=CENTER)
        self.tabla.column('#1',width=120,anchor=CENTER)
        self.tabla.column('#2',width=120,anchor=CENTER)
        self.tabla.column('#3',width=200,anchor=CENTER)
        self.tabla.column('#4',width=120,anchor=CENTER)
        self.tabla.column('#5',width=120,anchor=CENTER)
        self.tabla.column('#6',width=120,anchor=CENTER)
        self.tabla.column('#7',width=120,anchor=CENTER)
        self.tabla.column('#8',width=60,anchor=CENTER)
        self.tabla.column('#9',width=60,anchor=CENTER)
        self.tabla.column('#10',width=150,anchor=CENTER)

        self.tabla.heading('#0',text='Sub',anchor=CENTER)
        self.tabla.heading('#1',text='Host-Encontrado',anchor=CENTER)
        self.tabla.heading('#2',text='Host-Soli',anchor=CENTER)
        self.tabla.heading('#3',text='Mascara',anchor=CENTER)
        self.tabla.heading('#4',text='Gateway',anchor=CENTER)
        self.tabla.heading('#5',text='Primer ip a usar',anchor=CENTER)
        self.tabla.heading('#6',text='Ultima ip a usar',anchor=CENTER)
        self.tabla.heading('#7',text='Ultima ip disponible',anchor=CENTER)
        self.tabla.heading('#8',text='Ips usadas',anchor=CENTER)
        self.tabla.heading('#9',text='Ips disponibles',anchor=CENTER)
        self.tabla.heading('#10',text='Broadcas',anchor=CENTER)
        

        self.tabla.place(x=10,y=380)
        Label(text="VLSM", font="ar 19 bold", fg="Black",bg="grey").place(x=500,y=300)
        self.listar()
        return self.tabla
    
    def fijarEstiloTabla(self):
        style=ttk.Style()
        style.theme_use("clam")
        style.configure("mystyle.Treeview.Heading",background="Black",foreground="orange red",font=('Calibri',12,'bold'))
        style.configure("mystyle.Treeview",highlightthickness=0,foreground="Black",bd=0,font=('Calibri',10))

    def listar(self):
        ta=pilaDatosFinal

        subred_values = []
        hosts_encontrados = []
        hosts_soli = []
        mascara = []
        gateway = []
        primera_ip = []
        ultima_ip_usar = [] 
        ultima_ip_dis = []
        ips_usadas = []
        ips_disponibles = []
        broadcast = []

        for i in range(len(ta)):

            subred_values.append(ta[i][0])
            hosts_encontrados.append(ta[i][1])
            hosts_soli.append(ta[i][2])
            mascara.append(ta[i][3])
            gateway.append(ta[i][4])
            primera_ip.append(ta[i][5])
            ultima_ip_usar.append(ta[i][6])
            ultima_ip_dis.append(ta[i][7])
            ips_usadas.append(ta[i][8])
            ips_disponibles.append(ta[i][9])
            broadcast.append(ta[i][10])

            #self.tabla.insert("",'end',text=ta[i][0], values=(ta[i][1],ta[i][2],ta[i][3],ta[i][4],ta[i][5],ta[i][6],ta[i][7],ta[i][8],ta[i][9],ta[i][10]))
            #print((ta[i][1],ta[i][2],ta[i][3],ta[i][4],ta[i][5],ta[i][6],ta[i][7],ta[i][8],ta[i][9],ta[i][10]))
        
        mascaras = []
    
        for datos in pilaDatosFinal:
            elemento = datos[3]
            mascaras.append(elemento)

        #print(mascaras)
        return mascaras, subred_values, hosts_encontrados, hosts_soli, mascara, gateway, primera_ip, ultima_ip_usar, ultima_ip_dis, ips_usadas, ips_disponibles, broadcast

if __name__=="__main__":
    window=Ventana()
    #fondo=PhotoImage(file='fondo2.png')
    #window.mainloop()



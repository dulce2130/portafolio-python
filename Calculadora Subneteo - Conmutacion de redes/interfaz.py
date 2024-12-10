from select import select
from tkinter import  Tk, Button, Entry, Label, messagebox, ttk, PhotoImage
from  tkinter import *
import tkinter.ttk as tkk
from tkinter import  StringVar,Scrollbar,Frame
from tkinter import messagebox as mb

from calculadora2 import *
from calculadoraVLSM import*
from calculadoraVLSM import Tabla 
from calculadoraCIDR import*

class Ventana(Frame):
    def __init__(self, master, *args):
        super().__init__( master, *args)

        self.menu = True
        self.color = True
        self.cajas_de_texto = []


        self.frame_inicio = Frame(self.master, bg='#96c4c4', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='#96c4c4', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        self.frame_top = Frame(self.master, bg='#96c4c4', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='#96c4c4')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.widgets()
    
    def pantalla_inicial(self):
        self.paginas.select([self.frame_uno])
    

    def pantalla_calculadora_normal(self):
        self.paginas.select([self.frame_normal])
        self.frame_normal.columnconfigure(0, weight=1)
        self.frame_normal.columnconfigure(1, weight=1)
        self.frame_normal.rowconfigure(2, weight=1)
        self.frame_normal.columnconfigure(0, weight=1)
        self.frame_normal.rowconfigure(0, weight=1)
    
    def pantalla_vlsm(self):
        self.paginas.select([self.frame_vlsm])
        self.frame_vlsm.columnconfigure(0, weight=1)
        self.frame_vlsm.columnconfigure(1, weight=1)
        self.frame_vlsm.rowconfigure(2, weight=1)
        self.frame_vlsm.columnconfigure(0, weight=1)
        self.frame_vlsm.rowconfigure(0, weight=1)
        #self.generar_cajas_de_texto()

    def pantalla_cidr(self):
        self.paginas.select([self.frame_cidr])
        self.frame_cidr.columnconfigure(0, weight=1)
        self.frame_cidr.columnconfigure(1, weight=1)
        self.frame_cidr.rowconfigure(2, weight=1)
        self.frame_cidr.columnconfigure(0, weight=1)
        self.frame_cidr.rowconfigure(0, weight=1)
        #self.datos_totales_per()
    
   
   
    def menu_lateral(self):
        if self.menu is True:
            for i in range(50,270,10):				
                self.frame_menu.config(width= i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_cerrar.grid_forget()
                if clik_inicio is None:		
                    self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
                    self.bt_inicio.grid_propagate(0)
                    self.bt_inicio.config(width=i)
                    self.pantalla_inicial()
            self.menu = False
        else:
            for i in range(270,50,-10):
                self.frame_menu.config(width=  i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.bt_inicio.grid_forget()
                if clik_inicio is   None:
                    self.frame_menu.grid_propagate(0)		
                    self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
                    self.bt_cerrar.grid_propagate(0)
                    self.bt_cerrar.config(width=i)
                    self.pantalla_inicial()
            self.menu = True
    

    def widgets(self):
        self.imagen_inicio = PhotoImage(file ='inicio.png')
        self.imagen_menu = PhotoImage(file ='menu.png')
        self.imagen_datos = PhotoImage(file ='datos.png')
        self.imagen_registrar = PhotoImage(file ='escribir.png')
        self.imagen_actualizar = PhotoImage(file ='actualizar.png')
        self.imagen_buscar = PhotoImage(file ='buscar.png')
    
        self.logo = PhotoImage(file ='logo.png')
        self.tiendita = PhotoImage(file ='fondo.png')
        self.imagen_uno = PhotoImage(file ='imagen_uno.png')
        self.imagen_dos= PhotoImage(file ='imagen_dos.png')
        self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='#96c4c4',activebackground='#c7f7f7', bd=0, command = self.menu_lateral)
        self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
        self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='#96c4c4',activebackground='#c7f7f7', bd=0, command = self.menu_lateral)
        self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)

        Button(self.frame_menu, image=self.imagen_actualizar, bg='#96c4c4', activebackground='#c7f7f7', bd=0, command=self.pantalla_calculadora_normal).grid(column=0, row=1, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_registrar, bg='#96c4c4', activebackground='#c7f7f7', bd=0, command=self.pantalla_vlsm).grid(column=0, row=2, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_actualizar, bg='#96c4c4', activebackground='#c7f7f7', bd=0, command=self.pantalla_cidr).grid(column=0, row=3, pady=20, padx=10)

        Button(self.frame_menu, text='Subneteo Normal', bg='#96c4c4', fg='#ffffff',activebackground='#c7f7f7', bd=0, font=('Lucida Sans', 12, 'bold'), command=self.pantalla_calculadora_normal).grid(column=1, row=1, pady=20, padx=2)
        Button(self.frame_menu, text='Calculadora VLSM', bg='#96c4c4', fg='#ffffff', activebackground='#c7f7f7', bd=0,font=('Lucida Sans', 12, 'bold'), command=self.pantalla_vlsm).grid(column=1, row=2, pady=20, padx=2)
        Button(self.frame_menu, text='Calculadora CIDR', bg='#96c4c4', fg='#ffffff', activebackground='#c7f7f7', bd=0, font=('Lucida Sans', 12, 'bold'), command=self.pantalla_cidr).grid(column=1, row=3, pady=20, padx=2)

        #Paginas
        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook", background='ghost white', foreground='black', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='ghost white', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="ghost white", borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected", 'ghost white')])
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'ghost white')], foreground=[("selected", 'black')])

        #CREACCION DE LAS PAGINAS 
        self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
        self.paginas.grid(column=0,row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='ghost white')


        self.frame_normal= Frame(self.paginas, bg='ghost white')
        self.frame_vlsm = Frame(self.paginas, bg='ghost white')
        self.frame_cidr= Frame(self.paginas, bg='ghost white')


        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_normal)
        self.paginas.add(self.frame_vlsm)
        self.paginas.add(self.frame_cidr)
        
       


         ##############################         PAGINAS       #############################################
        #Título
        self.titulo = Label(self.frame_top,text= 'Calculadora de Subneteo', bg='#96c4c4', fg= '#ffffff', font= ('Imprint MT Shadow', 15, 'bold'))
        self.titulo.pack(expand = 1)

        #Ventana Principal
        Label(self.frame_uno, text= 'Subnetting', bg='ghost white', fg= '#96c4c4', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno ,image = self.tiendita , bg='snow').pack(expand=1)

        #ESTILO DE LAS TABLAS DE DATOS TREEVIEW
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font= ('Helvetica', 12), foreground='black',  background='white')  #, fieldbackground='yellow'
        estilo_tabla.map('Treeview',background=[('selected', '#aedddd')], foreground=[('selected','black')] )		
        estilo_tabla.configure('Heading',background = '#96c4c4', foreground='white',padding=5, font= ('Arial', 12, 'bold'))
        estilo_tabla.configure('Item',foreground = 'white', focuscolor ='#c7f7f7')
        estilo_tabla.configure('TScrollbar', arrowcolor = '#aedddd',bordercolor  ='black', troughcolor= '#aedddd',background ='white')
   
        #Pantalla Calculadora Normal-------------------------------------------------------
        Label(self.frame_normal, text= 'Calculadora de Subneteo', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 18, 'bold')).place(x = 410, y = 0)

        fuente = ('Helvica', 11, 'bold')

        self.ip_label = Label(self.frame_normal, text='IP: ', bg='ghost white', font= fuente).place(x = 10, y = 50)
        self.ip_entry = Entry(self.frame_normal, font=('Helvica', 11), highlightbackground="DarkOrchid1", highlightcolor="palevioletred", highlightthickness=2)
        self.ip_entry.place(x=46, y=50)

        self.subredes_label = Label(self.frame_normal, text='No. de subredes: ', bg='ghost white', font= fuente).place(x = 10, y = 80)
        self.subredes_entry = Entry(self.frame_normal, font=('Helvica', 11), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2)
        self.subredes_entry.place(x = 160, y = 80)

        self.hosts_label = Label(self.frame_normal, text='No. de Hosts: ', bg='ghost white', font= fuente).place(x = 10, y = 110)
        self.hosts_entry = Entry(self.frame_normal, font=('Helvica', 11), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2)
        self.hosts_entry.place(x = 120, y = 110)
        
        self.cal_button = Button(self.frame_normal, command= self.validar_campos, text='Calcular', font=('Helvica',12,'bold',), fg='white', bg = '#aedddd', width= 14, cursor="hand2")
        self.cal_button.place(x = 10, y = 150)
  
        
        #Pantalla VLSM--------------------------------------------------------------

        Label(self.frame_vlsm, text= 'Calculadora VLSM', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 410, y = 0)

        self.ip_label = Label(self.frame_vlsm, text='IP: ', bg='ghost white', font= fuente).place(x = 10, y = 50)
        self.ip_vlsm = Entry(self.frame_vlsm, font=('Helvica', 11), highlightbackground="DarkOrchid1", highlightcolor="palevioletred", highlightthickness=2)
        self.ip_vlsm.place(x=46, y=50)

        self.subredes_label = Label(self.frame_vlsm, text='No. de subredes: ', bg='ghost white', font= fuente).place(x = 10, y = 90)
        self.subredes_vlsm = Entry(self.frame_vlsm, font=('Helvica', 11), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2)
        self.subredes_vlsm.place(x = 140, y = 90)

        self.cal_button_vlsm = Button(self.frame_vlsm, command= self.generar_cajas_de_texto, text='Ingresar host', font=('Helvica',12,'bold',), fg='white', bg = '#aedddd', width= 16, cursor="hand2")
        self.cal_button_vlsm.place(x = 10, y = 130)
        
        #Pantalla CIDR----------------------------------------------
        Label(self.frame_cidr, text= 'Calculadora CIDR', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 18, 'bold')).place(x = 450, y = 0)

        self.ip_label = Label(self.frame_cidr, text='IP: ', bg='ghost white', font= fuente).place(x = 10, y = 50)
        self.ip_cidr = Entry(self.frame_cidr, font=('Helvica', 11), highlightbackground="DarkOrchid1", highlightcolor="palevioletred", highlightthickness=2)
        self.ip_cidr.place(x=46, y=50)

        self.subredes_label = Label(self.frame_cidr, text='No. de subredes: ', bg='ghost white', font= fuente).place(x = 10, y = 90)
        self.subredes_cidr = Entry(self.frame_cidr, font=('Helvica', 11), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2)
        self.subredes_cidr.place(x = 140, y = 90)

        self.cal_button_cidr = Button(self.frame_cidr, command= self.tabla_CIDR, text='Calcular', font=('Helvica',12,'bold',), fg='white', bg = '#aedddd', width= 16, cursor="hand2")
        self.cal_button_cidr.place(x = 10, y = 130)

        #self.limp_button = Button(self.frame_cidr, command= self.limpiar_CIDR, text='limpiar', font=('Helvica',12,'bold',), fg='white', bg = '#aedddd', width= 16, cursor="hand2")
        #self.limp_button.place(x = 10, y = 170)



    def generar_cajas_de_texto(self):
        cantidad_subredes = self.subredes_vlsm.get()
        ip = self.ip_vlsm.get()
        c = 170
        if not self.validar_ip_C(ip):
                messagebox.showerror("Error", "La dirección IP debe estar en el formato '000.000.000.000' y/o estar en el rango de la clase C")
        else:

            if not cantidad_subredes.isdigit() or int(cantidad_subredes) <= 0:
                messagebox.showerror("Error", "La cantidad de subredes debe ser un número entero positivo.")
            
            else:
                cantidad_subredes = int(cantidad_subredes)
                for entry in self.cajas_de_texto:
                    entry.destroy()
                    self.cajas_de_texto.clear()


                def validate_integer(host):
                    if host == "":
                        return True
                    if host.isdigit() and int(host) >= 0:
                        return True
                    return False
            
                host_validation = self.frame_vlsm.register(validate_integer)

                # Generar dinámicamente las cajas de texto y colocarlas en la interfaz usando grid
                for i in range(cantidad_subredes):
                    label = Label(self.frame_vlsm,  bg='ghost white', text=f"Subred {i + 1}: ", font= ('Comic Sans MS', 12, 'bold'))
                    label.place(x = 20, y = c)
            
                    entry = Entry(self.frame_vlsm, font=('Helvica', 11), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2)
                    entry.place(x = 120, y = c)
                    self.cajas_de_texto.append(entry)

                    entry.config(validate="key", validatecommand=(host_validation, "%P"))

                    

                    c = c + 40

                    
                self.vlsm_button = Button(self.frame_vlsm, command= self.tabla_VLSM, text='Calcular VLSM', font=('Helvica',12,'bold',), fg='white', bg = '#aedddd', width= 16, cursor="hand2")
                self.vlsm_button.place(x = 10, y = c)


    

    def validar_campos(self):
        global ip, subredes, hosts

        ip = self.ip_entry.get()
        subredes = self.subredes_entry.get()
        hosts = self.hosts_entry.get()

        # Verificar si alguno de los campos está vacío
        if not ip or not subredes or not hosts:
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
        else:
        # Validar la dirección IP
            if not self.validar_ip(ip):
                messagebox.showerror("Error", "La dirección IP debe estar en el formato '0.0.0.0'.")
            else:
            # Validar que subredes y hosts sean enteros
                if not self.es_entero(subredes) or not self.es_entero(hosts):
                    messagebox.showerror("Error", "El número de subredes y hosts debe ser un número entero.")
                else:
                # Todos los campos están llenos y son válidos, realizar el cálculo
                    self.tabla_subneteo()
    
    
    def validar_ip(self, ip):
        # Validar el formato de la dirección IP
        partes = ip.split(".")
        if len(partes) != 4:
            return False
        for parte in partes:
            if not parte.isdigit() or not (0 <= int(parte) <= 255):
                return False
        return True
    
    def es_entero(self, valor):
        try:
            int(valor)
            return True
        except ValueError:
            return False
    
    def validar_ip_C(self, ip):
        # Validar el formato de la dirección IP
        partes = ip.split(".")
        if len(partes) != 4:
            return False
        for parte in partes:
            try:
                valor = int(parte)
                if valor < 0 or valor > 255:
                    return False
            except ValueError:
                # Si no se puede convertir a un entero, no es un número válido
                return False
    
        # Verificar que la dirección IP está en el rango de una Clase C
        primer_octeto = int(partes[0])
        if 192 <= primer_octeto <= 223:
            return True
        else:
            return False

    

    def focus_normal(self):
        self.ip_entry.focus_set()

        self.ip_entry.bind('<Return>', lambda event=None: self.subredes_entry.focus_set())
        self.subredes_entry.bind('<Return>', lambda event=None: self.hosts_entry.focus_set())
        self.hosts_entry.bind('<Return>', lambda event=None: self.validar_campos())
        self.cal_button.bind('<Return>', lambda event=None: self.validar_campos())
    
    def focus_vlsm(self):
        self.ip_vlsm.focus_set()

        self.ip_vlsm.bind('<Return>', lambda event=None: self.subredes_vlsm.focus_set())
        self.subredes_vlsm.bind('<Return>', lambda event=None: self.generar_cajas_de_texto())
        self.cal_button_vlsm.bind('<Return>', lambda event=None: self.generar_cajas_de_texto())
    
    def focus_cidr(self):
        self.ip_cidr.focus_set()

        self.ip_cidr.bind('<Return>', lambda event=None: self.subredes_cidr.focus_set())
        self.subredes_cidr.bind('<Return>', lambda event=None: self.tabla_CIDR())
        self.cal_button_cidr.bind('<Return>', lambda event=None: self.tabla_CIDR())

        

    def tabla_subneteo(self):

        salto, clase, subred_values, hosts_encontrados, hostss, mascara, gateway, primera_ip, ultima_ip_usar, ultima_ip_dis, ips_usadas, ips_disponibles, broadcast =  tabla(ip, int(subredes), int(hosts))

        Label(self.frame_normal, text= "Resultado",bg='ghost white', fg= 'Blue2',font=('Freehand521 BT',14,'bold')).place(x=780, y = 40)

        Label(self.frame_normal, text= 'Clase: ', bg='ghost white', fg= 'DeepSkyBlue4', font= ('Helvica', 12, 'bold')).place(x = 750, y = 80)
        Label(self.frame_normal, text= clase, bg='ghost white', fg= 'black', font= ('Helvica', 12)).place(x = 810, y = 80)

        Label(self.frame_normal, text= 'Máscara: ', bg='ghost white', fg= 'DeepSkyBlue4', font= ('Helvica', 12, 'bold')).place(x = 750, y = 120)
        Label(self.frame_normal, text= mascara, bg='ghost white', fg= 'black', font= ('Helvica', 12)).place(x = 830, y = 120)
        
        Label(self.frame_normal, text= 'Rango: ', bg='ghost white', fg= 'DeepSkyBlue4', font= ('Helvica', 12, 'bold')).place(x = 750, y = 160)
        Label(self.frame_normal, text= salto, bg='ghost white', fg= 'black', font= ('Helvica', 12)).place(x = 820, y = 160)

        Label(self.frame_normal, text= "Tabla",bg='ghost white', fg= 'Blue2',font=('Freehand521 BT',14, 'bold')).place(x = 550, y = 200) 
        

        #Tabla
        self.frame_tabla_rango = Frame(self.frame_normal, bg= 'gray90')
        self.frame_tabla_rango.place(x=10, y = 240)		
        self.tabla_rango = tkk.Treeview(self.frame_tabla_rango,  style='Custom.Treeview') 
        self.tabla_rango.grid(column=0, row=0, sticky='nsew')
        

        ladox = ttk.Scrollbar(self.frame_tabla_rango, orient = 'horizontal', command= self.tabla_rango.xview)
        ladoy = ttk.Scrollbar(self.frame_tabla_rango, orient ='vertical', command = self.tabla_rango.yview)

        ladoy.config(command=self.tabla_rango.yview, takefocus=0)
        ladox.config(command=self.tabla_rango.xview, takefocus=0)
        self.tabla_rango.config(yscrollcommand=ladoy.set, xscrollcommand=ladox.set)

        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy.grid(column = 1, row = 0, sticky='ns')


        self.tabla_rango.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_rango['columns'] = ("Host encontrados", "Host solicitados", "Máscara de subred", "Gateway", "1era IP a usar", "Última IP a usar", "Última IP disponible", "IPs usadas", "IPs disponibles", "Broadcast")
        self.tabla_rango.column('#0', minwidth=10, width=40, anchor='center')
        self.tabla_rango.column('Host encontrados', minwidth=30, width=75, anchor='center')
        self.tabla_rango.column('Host solicitados', minwidth=30, width=75, anchor='center')
        self.tabla_rango.column('Máscara de subred', minwidth=30, width=150 , anchor='center')
        self.tabla_rango.column('Gateway', minwidth=40, width=125 , anchor='center')
        self.tabla_rango.column('1era IP a usar', minwidth=40, width=125 , anchor='center')
        self.tabla_rango.column('Última IP a usar', minwidth=40, width=125 , anchor='center')
        self.tabla_rango.column('Última IP disponible', minwidth=40, width=125 , anchor='center')
        self.tabla_rango.column('IPs usadas', minwidth=40, width=75, anchor='center')
        self.tabla_rango.column('IPs disponibles', minwidth=40, width=75, anchor='center')
        self.tabla_rango.column('Broadcast', minwidth=40, width=125 , anchor='center')


        self.tabla_rango.heading('#0', text='Subred', anchor ='center')
        self.tabla_rango.heading('Host encontrados', text='Host encontrados', anchor='center')
        self.tabla_rango.heading('Host solicitados', text='Host solicitados', anchor='center')
        self.tabla_rango.heading('Máscara de subred', text='Máscara de subred', anchor='center')
        self.tabla_rango.heading('Gateway', text='Gateway', anchor='center')
        self.tabla_rango.heading('1era IP a usar', text='1era IP a usar', anchor='center')
        self.tabla_rango.heading('Última IP a usar', text='Última IP a usar', anchor='center')
        self.tabla_rango.heading('Última IP disponible', text='Última IP disponible', anchor='center')
        self.tabla_rango.heading('Gateway', text='Gateway', anchor='center')
        self.tabla_rango.heading('IPs usadas', text='IPs usadas', anchor='center')
        self.tabla_rango.heading('IPs disponibles', text='IPs disponibles', anchor='center')
        self.tabla_rango.heading('Broadcast', text='Broadcast', anchor='center')

        #print(clase, ran, subred_values, host_enc, can_hosts, mascara, gateway, primera_ip, ultima_ip_usar, ultima_ip_dis, ips_usadas, ips_disponibles, broadcast)


        for row in self.tabla_rango.get_children():
            self.tabla_rango.delete(row)

        # Recorre las listas y agrega cada fila a la tabla
        for i in range(len(subred_values)):  # Supongo que todas las listas tienen la misma longitud
            data = (
             hosts_encontrados, hostss, mascara, gateway[i], primera_ip[i], ultima_ip_usar[i], 
            ultima_ip_dis[i], ips_usadas, ips_disponibles, broadcast[i]
            )
            self.tabla_rango.insert('', 'end', text=subred_values[i], values=data)

    def obtener_valores_vlsm(self):
        valores = []
        for entry in self.cajas_de_texto:
            valor = entry.get()
            valores.append(valor)
        return valores
    
    def tabla_VLSM(self):
        hosts = self.obtener_valores_vlsm()
        ip = self.ip_vlsm.get()
        #noSubredes = self.subredes_vlsm.get()

        hostSubredes =  [int(a) for a in hosts]

        #print(hostSubredes)
        direccionRed(ip)
        formulaDosM(hostSubredes)

        mascaras, subred_values, hosts_encontrados, hosts_soli, mascara, gateway, primera_ip, ultima_ip_usar, ultima_ip_dis, ips_usadas, ips_disponibles, broadcast = Tabla.listar(self)

        Label(self.frame_vlsm, text= "Máscaras",bg='ghost white', fg= 'Blue2',font=('Freehand521 BT',14, 'bold')).place(x = 720, y = 70) 
        c = 110
        for l in range(len(mascaras)):
            Label(self.frame_vlsm, text= (f"Subred {l+1}: {mascaras[l]}" ), bg='ghost white', fg= 'black', font= ('Helvica', 14, 'bold')).place(x = 650, y = c)
            c = c + 55


        #Tabla
        self.frame_tablaVLSM = Frame(self.frame_vlsm, bg= 'gray90')
        self.frame_tablaVLSM.place(x=10, y = 440)		
        self.tabla_vlsm = tkk.Treeview(self.frame_tablaVLSM,  style='Custom.Treeview') 
        self.tabla_vlsm.grid(column=0, row=0, sticky='nsew')
        

        ladox = ttk.Scrollbar(self.frame_tablaVLSM, orient = 'horizontal', command= self.tabla_vlsm.xview)
        ladoy = ttk.Scrollbar(self.frame_tablaVLSM, orient ='vertical', command = self.tabla_vlsm.yview)

        ladoy.config(command=self.tabla_vlsm.yview, takefocus=0)
        ladox.config(command=self.tabla_vlsm.xview, takefocus=0)
        self.tabla_vlsm.config(yscrollcommand=ladoy.set, xscrollcommand=ladox.set)

        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy.grid(column = 1, row = 0, sticky='ns')


        self.tabla_vlsm.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_vlsm['columns'] = ("Host encontrados", "Host solicitados", "Máscara de subred", "Gateway", "1era IP a usar", "Última IP a usar", "Última IP disponible", "IPs usadas", "IPs disponibles", "Broadcast")
        self.tabla_vlsm.column('#0', minwidth=10, width=40, anchor='center')
        self.tabla_vlsm.column('Host encontrados', minwidth=30, width=75, anchor='center')
        self.tabla_vlsm.column('Host solicitados', minwidth=30, width=75, anchor='center')
        self.tabla_vlsm.column('Máscara de subred', minwidth=30, width=150 , anchor='center')
        self.tabla_vlsm.column('Gateway', minwidth=40, width=125 , anchor='center')
        self.tabla_vlsm.column('1era IP a usar', minwidth=40, width=125 , anchor='center')
        self.tabla_vlsm.column('Última IP a usar', minwidth=40, width=125 , anchor='center')
        self.tabla_vlsm.column('Última IP disponible', minwidth=40, width=125 , anchor='center')
        self.tabla_vlsm.column('IPs usadas', minwidth=40, width=75, anchor='center')
        self.tabla_vlsm.column('IPs disponibles', minwidth=40, width=75, anchor='center')
        self.tabla_vlsm.column('Broadcast', minwidth=40, width=125 , anchor='center')


        self.tabla_vlsm.heading('#0', text='Subred', anchor ='center')
        self.tabla_vlsm.heading('Host encontrados', text='Host encontrados', anchor='center')
        self.tabla_vlsm.heading('Host solicitados', text='Host solicitados', anchor='center')
        self.tabla_vlsm.heading('Máscara de subred', text='Máscara de subred', anchor='center')
        self.tabla_vlsm.heading('Gateway', text='Gateway', anchor='center')
        self.tabla_vlsm.heading('1era IP a usar', text='1era IP a usar', anchor='center')
        self.tabla_vlsm.heading('Última IP a usar', text='Última IP a usar', anchor='center')
        self.tabla_vlsm.heading('Última IP disponible', text='Última IP disponible', anchor='center')
        self.tabla_vlsm.heading('Gateway', text='Gateway', anchor='center')
        self.tabla_vlsm.heading('IPs usadas', text='IPs usadas', anchor='center')
        self.tabla_vlsm.heading('IPs disponibles', text='IPs disponibles', anchor='center')
        self.tabla_vlsm.heading('Broadcast', text='Broadcast', anchor='center')
        
        for row in self.tabla_vlsm.get_children():
            self.tabla_vlsm.delete(row)

        # Recorre las listas y agrega cada fila a la tabla
        for i in range(len(subred_values)):  # Supongo que todas las listas tienen la misma longitud
            data = (
                hosts_encontrados[i], hosts_soli[i], mascara[i], gateway[i], primera_ip[i], ultima_ip_usar[i], 
                ultima_ip_dis[i], ips_usadas[i], ips_disponibles[i], broadcast[i]
            )
            self.tabla_vlsm.insert('', 'end', text=subred_values[i], values=data)
    

    def tabla_CIDR(self):
        ip = self.ip_cidr.get()
        subredes = self.subredes_cidr.get()

        if not self.validar_ip_C(ip):
                messagebox.showerror("Error", "La dirección IP debe estar en el formato '000.000.000.000' y/o estar en el rango de la clase C")
        else:

            if not subredes.isdigit() or int(subredes) <= 0:
                messagebox.showerror("Error", "La cantidad de subredes debe ser un número entero positivo.")
            
            else:

                binaria, decimal, salto, hosts_encontrados, hostss, gateway, primera_ip, ultima_ip_usar, ultima_ip_dis, ips_usadas, ips_disponibles, broadcas = listasCIDR(ip, int(subredes))
        
                Label(self.frame_cidr, text= "Resultado",bg='ghost white', fg= 'Blue2',font=('Freehand521 BT',15,'bold')).place(x=780, y = 50)
                
                Label(self.frame_cidr, text= 'Máscara binaria: ', bg='ghost white', fg= 'DeepSkyBlue4', font= ('Helvica', 13, 'bold')).place(x = 570, y = 90)
                Label(self.frame_cidr, text= binaria, bg='ghost white', fg= 'black', font= ('Helvica', 13)).place(x = 720, y = 90)

                Label(self.frame_cidr, text= 'Máscara decimal: ', bg='ghost white', fg= 'DeepSkyBlue4', font= ('Helvica', 13, 'bold')).place(x = 570, y = 130)
                Label(self.frame_cidr, text= decimal, bg='ghost white', fg= 'black', font= ('Helvica', 13)).place(x = 720, y = 130)
        
                Label(self.frame_cidr, text= 'Rango: ', bg='ghost white', fg= 'DeepSkyBlue4', font= ('Helvica', 13, 'bold')).place(x = 570, y = 170)
                Label(self.frame_cidr, text= salto, bg='ghost white', fg= 'black', font= ('Helvica', 13)).place(x = 640, y = 170)

                Label(self.frame_cidr, text= "Tabla",bg='ghost white', fg= 'Blue2',font=('Freehand521 BT',14, 'bold')).place(x = 500, y = 240) 

                #Tabla
                self.frame_tablaCIDR = Frame(self.frame_cidr, bg= 'gray90')
                self.frame_tablaCIDR.place(x=10, y = 290)		
                self.tabla_cdr = tkk.Treeview(self.frame_tablaCIDR,  style='Custom.Treeview') 
                self.tabla_cdr.grid(column=0, row=0, sticky='nsew')
        

                ladox = ttk.Scrollbar(self.frame_tablaCIDR, orient = 'horizontal', command= self.tabla_cdr.xview)
                ladoy = ttk.Scrollbar(self.frame_tablaCIDR, orient ='vertical', command = self.tabla_cdr.yview)

                ladoy.config(command=self.tabla_cdr.yview, takefocus=0)
                ladox.config(command=self.tabla_cdr.xview, takefocus=0)
                self.tabla_cdr.config(yscrollcommand=ladoy.set, xscrollcommand=ladox.set)

                ladox.grid(column=0, row = 1, sticky='ew') 
                ladoy.grid(column = 1, row = 0, sticky='ns')


                self.tabla_cdr.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
                self.tabla_cdr['columns'] = ("Host encontrados", "Host solicitados", "Máscara de subred", "Gateway", "1era IP a usar", "Última IP a usar", "Última IP disponible", "IPs usadas", "IPs disponibles", "Broadcast")
                self.tabla_cdr.column('#0', minwidth=10, width=40, anchor='center')
                self.tabla_cdr.column('Host encontrados', minwidth=30, width=75, anchor='center')
                self.tabla_cdr.column('Host solicitados', minwidth=30, width=75, anchor='center')
                self.tabla_cdr.column('Máscara de subred', minwidth=30, width=150 , anchor='center')
                self.tabla_cdr.column('Gateway', minwidth=40, width=125 , anchor='center')
                self.tabla_cdr.column('1era IP a usar', minwidth=40, width=125 , anchor='center')
                self.tabla_cdr.column('Última IP a usar', minwidth=40, width=125 , anchor='center')
                self.tabla_cdr.column('Última IP disponible', minwidth=40, width=125 , anchor='center')
                self.tabla_cdr.column('IPs usadas', minwidth=40, width=75, anchor='center')
                self.tabla_cdr.column('IPs disponibles', minwidth=40, width=75, anchor='center')
                self.tabla_cdr.column('Broadcast', minwidth=40, width=125 , anchor='center')


                self.tabla_cdr.heading('#0', text='Subred', anchor ='center')
                self.tabla_cdr.heading('Host encontrados', text='Host encontrados', anchor='center')
                self.tabla_cdr.heading('Host solicitados', text='Host solicitados', anchor='center')
                self.tabla_cdr.heading('Máscara de subred', text='Máscara de subred', anchor='center')
                self.tabla_cdr.heading('Gateway', text='Gateway', anchor='center')
                self.tabla_cdr.heading('1era IP a usar', text='1era IP a usar', anchor='center')
                self.tabla_cdr.heading('Última IP a usar', text='Última IP a usar', anchor='center')
                self.tabla_cdr.heading('Última IP disponible', text='Última IP disponible', anchor='center')
                self.tabla_cdr.heading('Gateway', text='Gateway', anchor='center')
                self.tabla_cdr.heading('IPs usadas', text='IPs usadas', anchor='center')
                self.tabla_cdr.heading('IPs disponibles', text='IPs disponibles', anchor='center')
                self.tabla_cdr.heading('Broadcast', text='Broadcast', anchor='center')
        
                for row in self.tabla_cdr.get_children():
                    self.tabla_cdr.delete(row)

                # Recorre las listas y agrega cada fila a la tabla
                for i in range(int(subredes)):  
                    data = (
                            hosts_encontrados, hostss, decimal, gateway[i], primera_ip[i], ultima_ip_usar[i], 
                            ultima_ip_dis[i], ips_usadas, ips_disponibles, broadcas[i]
                        )
                    self.tabla_cdr.insert('', 'end', text= i +1 , values=data)

###########################################################3



if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Subnetting')
    ventana.minsize(height= 475, width=795)
    ventana.geometry('1200x750')
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))	
    app = Ventana(ventana)
    app.focus_normal()
    app.focus_vlsm()
    app.focus_cidr()
    app.mainloop()
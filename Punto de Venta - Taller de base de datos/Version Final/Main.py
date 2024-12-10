from select import select
from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage
import tkinter
import tkinter.ttk as tkk
from tkinter import  StringVar,Scrollbar,Frame
from numpy import insert, integer
from tkinter import messagebox as mb
from tkcalendar import Calendar, DateEntry
from Conexion import*
import time

#conexionMetodos = Metodos('TienditasCadena','root','silverspoon')

class Ventana(Frame):
    def __init__(self, master, *args):
        super().__init__( master, *args)

        self.menu = True
        self.color = True
        self.nom_ciu = StringVar()
        self.lada_ciu = StringVar()
        self.buscar_ciu = StringVar()
        self.Ciudad = TablaCiudad('root','localhost', 'silverspoon')
        self.CodigoPostal = TablaCodigo('root','localhost', 'silverspoon')
        self.Colonia = TablaColonia('root','localhost', 'silverspoon')
        self.Surcursal = TablaTienda('root','localhost', 'silverspoon')
        self.Dimension = TablaDimension('root','localhost', 'silverspoon')
        self.Inventario = TablaProducto('root','localhost', 'silverspoon')
        self.Contrato = TablaContrato('root','localhost', 'silverspoon')
        self.Empresa = TablaEmpresa('root','localhost', 'silverspoon')

        self.cp = StringVar()
        self.ciudad_cp = StringVar()
        self.id_ciu_cp = StringVar
        self.busca_cp = StringVar()

        self.colonia = StringVar()  
        self.nombre_col = StringVar()
        self.cp_col = StringVar()
        self.busca_col = StringVar()

        self.id_tie = StringVar() 
        self.calle_tie = StringVar() 
        self.num_tie = StringVar() 
        self.orientacion_tie = StringVar() 
        self.entrecalles_tie = StringVar() 
        self.tel_tie = StringVar() 
        self.id_col_tie = StringVar() 
        self.id_dimen_tie = StringVar() 

        self.codbar_pro = StringVar()
        self.nom_pro = StringVar()
        self.contenido_pro = StringVar()
        self.umedida_pro = StringVar()
        self.presentacion_pro = StringVar()
        self.id_marca_pro = StringVar()
        self.id_dimen_pro = StringVar()

        self.alto = StringVar()
        self.largo = StringVar()
        self.ancho = StringVar()

        self.ap = StringVar()
        self.am = StringVar()
        self.nombre = StringVar()
        self.edocivil = StringVar()
        self.genero = StringVar()
        self.fnac = StringVar()
        self.tel = StringVar()
        self.mail = StringVar()
        self.calle = StringVar()
        self.num = StringVar()
        self.orientacion = StringVar()
        self.entreca = StringVar()
        self.colonia = StringVar()
        self.fi = StringVar()
        self.ff = StringVar()
        self.puesto = StringVar()
        self.sueldo = StringVar()
        self.hi = StringVar()
        self.hf = StringVar()
        self.tienda = StringVar()

        self.nombre_emp = StringVar()
        self.tel_emp = StringVar()

        self.nom_mar = StringVar()
        self.tipo_mar = StringVar()

        self.fecha_tic = StringVar()
        self.atendio = StringVar()
        self.codbar = StringVar()



        self.frame_inicio = Frame(self.master, bg='thistle2', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='thistle2', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        self.frame_top = Frame(self.master, bg='thistle2', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='thistle2')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.widgets()
    
    def pantalla_inicial(self):
        self.paginas.select([self.frame_uno])
    
    def pantalla_ciudad(self):
        self.paginas.select([self.frame_ciudad])
        self.frame_ciudad.columnconfigure(0, weight=1)
        self.frame_ciudad.columnconfigure(1, weight=1)
        self.frame_ciudad.rowconfigure(2, weight=1)
        self.frame_ciudad.columnconfigure(0, weight=1)
        self.frame_ciudad.rowconfigure(0, weight=1)
    
    def pantalla_codigoPostal(self):
        self.paginas.select([self.frame_codigo])
        self.frame_codigo.columnconfigure(0, weight=1)
        self.frame_codigo.columnconfigure(1, weight=1)
        self.frame_codigo.rowconfigure(2, weight=1)
        #self.frame_tabla_cp.columnconfigure(0, weight=2)
        #self.frame_tabla_cp.rowconfigure(0, weight=2)
    
    def pantalla_colonia(self):
        self.paginas.select([self.frame_colonia])
        self.frame_colonia.columnconfigure(0, weight=1)
        self.frame_colonia.columnconfigure(1, weight=1)
        self.frame_colonia.rowconfigure(2, weight=1)
        self.frame_colonia.columnconfigure(0, weight=1)
        self.frame_colonia.rowconfigure(0, weight=1)
        self.datos_totales_col()
        self.datos_totales_cp_col()
    
    def pantalla_sucursales(self):
        self.paginas.select([self.frame_sucursales])
        self.frame_sucursales.columnconfigure(0, weight=1)
        self.frame_sucursales.columnconfigure(1, weight=1)
        self.frame_sucursales.rowconfigure(2, weight=1)
        self.frame_sucursales.columnconfigure(0, weight=1)
        self.frame_sucursales.rowconfigure(0, weight=1)
        self.datos_totales_col_sur()
        self.listar_dimen_sur()
    
    def pantalla_dimensiones(self):
        self.paginas.select([self.frame_dimensiones])
        self.frame_dimensiones.columnconfigure(0, weight=1)
        self.frame_dimensiones.columnconfigure(1, weight=1)
        self.frame_dimensiones.rowconfigure(2, weight=1)
        self.frame_dimensiones.columnconfigure(0, weight=1)
        self.frame_dimensiones.rowconfigure(0, weight=1)
        self.listar_dimensiones()

    def pantalla_ListaSucursales(self):
        self.paginas.select([self.frame_ListaSurcursales])
        self.frame_ListaSurcursales.columnconfigure(0, weight=1)
        self.frame_ListaSurcursales.columnconfigure(1, weight=1)
        self.frame_ListaSurcursales.rowconfigure(2, weight=1)
        self.frame_ListaSurcursales.columnconfigure(0, weight=1)
        self.frame_ListaSurcursales.rowconfigure(0, weight=1)

        self.datos_totales_sucursales()

    
    def pantalla_personal(self):
        self.paginas.select([self.frame_personal])
        self.frame_personal.columnconfigure(0, weight=1)
        self.frame_personal.columnconfigure(1, weight=1)
        self.frame_personal.rowconfigure(2, weight=1)
        self.frame_personal.columnconfigure(0, weight=1)
        self.frame_personal.rowconfigure(0, weight=1)

    def pantalla_regContrato(self):
        self.paginas.select([self.frame_regContrato])
        self.frame_regContrato.columnconfigure(0, weight=1)
        self.frame_regContrato.columnconfigure(1, weight=1)
        self.frame_regContrato.rowconfigure(2, weight=1)
        self.frame_regContrato.columnconfigure(0, weight=1)
        self.frame_regContrato.rowconfigure(0, weight=1)
    
    def pantalla_ListaContrato(self):
        self.paginas.select([self.frame_lisContrato])
        self.frame_lisContrato.columnconfigure(0, weight=1)
        self.frame_lisContrato.columnconfigure(1, weight=1)
        self.frame_lisContrato.rowconfigure(2, weight=1)
        self.frame_lisContrato.columnconfigure(0, weight=1)
        self.frame_lisContrato.rowconfigure(0, weight=1)
        self.datos_totales_per()
    
    def pantalla_RegistrarEmpresa(self):
        self.paginas.select([self.frame_RegistrarEmpresa])
        self.frame_RegistrarEmpresa.columnconfigure(0, weight=1)
        self.frame_RegistrarEmpresa.columnconfigure(1, weight=1)
        self.frame_RegistrarEmpresa.rowconfigure(2, weight=1)
        self.frame_RegistrarEmpresa.columnconfigure(0, weight=1)
        self.frame_RegistrarEmpresa.rowconfigure(0, weight=1)
        self.listarEmpresas()
        self.listarMarcas()

    def pantalla_Inventario(self):
        self.paginas.select([self.frame_inventario])
        self.frame_inventario.columnconfigure(0, weight=1)
        self.frame_inventario.columnconfigure(1, weight=1)
        self.frame_inventario.rowconfigure(2, weight=1)
        self.frame_inventario.columnconfigure(0, weight=1)
        self.frame_inventario.rowconfigure(0, weight=1)
        self.datos_totales_productos()

    def pantalla_registrar_prod(self):
        self.paginas.select([self.frame_regProd])
        self.frame_regProd.columnconfigure(0, weight=1)
        self.frame_regProd.columnconfigure(1, weight=1)
        self.frame_regProd.rowconfigure(2, weight=1)
        self.frame_regProd.columnconfigure(0, weight=1)
        self.frame_regProd.rowconfigure(0, weight=1)
        self.datos_totales_marcas()

    def pantalla_AcomodoProductos(self):
        self.paginas.select([self.frame_acomodoProductos])
        self.frame_acomodoProductos.columnconfigure(0, weight=1)
        self.frame_acomodoProductos.columnconfigure(1, weight=1)
        self.frame_acomodoProductos.rowconfigure(2, weight=1)
        self.frame_acomodoProductos.columnconfigure(0, weight=1)
        self.frame_acomodoProductos.rowconfigure(0, weight=1)

    def pantalla_controlVentas(self):
        self.paginas.select([self.frame_controlVentas])
        self.frame_controlVentas.columnconfigure(0, weight=1)
        self.frame_controlVentas.columnconfigure(1, weight=1)
        self.frame_controlVentas.rowconfigure(2, weight=1)
        self.frame_controlVentas.columnconfigure(0, weight=1)
        self.frame_controlVentas.rowconfigure(0, weight=1)

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
        self.tiendita = PhotoImage(file ='tiendita.png')
        self.imagen_uno = PhotoImage(file ='imagen_uno.png')
        self.imagen_dos= PhotoImage(file ='imagen_dos.png')
        self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='thistle2',activebackground='thistle', bd=0, command = self.menu_lateral)
        self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
        self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='thistle2',activebackground='thistle', bd=0, command = self.menu_lateral)
        self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)

        #BOTONES Y ETIQUETAS DEL MENU LATERAL 
        Button(self.frame_menu, image= self.imagen_datos, bg='thistle2', activebackground='thistle', bd=0, command = self.pantalla_ciudad).grid(column=0, row=1, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_registrar, bg='thistle2',activebackground='thistle', bd=0, command = self.pantalla_codigoPostal).grid(column=0, row=2, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_actualizar, bg= 'thistle2',activebackground='thistle', bd=0, command = self.pantalla_colonia).grid(column=0, row=3, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_buscar, bg= 'thistle2',activebackground='thistle', bd=0, command = self.pantalla_sucursales).grid(column=0, row=4, pady=20,padx=10)		
        Button(self.frame_menu, image= self.imagen_datos, bg= 'thistle2',activebackground='thistle', bd=0, command = self.pantalla_personal).grid(column=0, row=5, pady=20,padx=10)		
        Button(self.frame_menu, image= self.imagen_registrar, bg= 'thistle2',activebackground='thistle', bd=0, command = self.pantalla_Inventario).grid(column=0, row=6, pady=20,padx=10)		
        Button(self.frame_menu, image= self.imagen_actualizar, bg= 'thistle2',activebackground='thistle', bd=0, command = self.pantalla_AcomodoProductos).grid(column=0, row=7, pady=20,padx=10)		
        Button(self.frame_menu, image= self.imagen_buscar, bg= 'thistle2',activebackground='thistle', bd=0, command = self.pantalla_controlVentas).grid(column=0, row=8, pady=20,padx=10)		


        Label(self.frame_menu, text= 'Ciudad', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text= 'Código Postal ', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text= 'Colonia', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text= 'Control de Sucursales', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)	
        Label(self.frame_menu, text= 'Control de Proveedores', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)
        Label(self.frame_menu, text= 'Inventario', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=6, pady=20, padx=2)
        Label(self.frame_menu, text= 'Acomodo de productos', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=7, pady=20, padx=2)
        Label(self.frame_menu, text= 'Control de Ventas', bg= 'thistle2', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=8, pady=20, padx=2)

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
        self.frame_ciudad= Frame(self.paginas, bg='ghost white')
        self.frame_codigo = Frame(self.paginas, bg='ghost white')
        self.frame_colonia = Frame(self.paginas, bg='ghost white')
        self.frame_sucursales = Frame(self.paginas, bg='ghost white')
        self.frame_ListaSurcursales = Frame(self.paginas, bg='ghost white')
        self.frame_personal = Frame(self.paginas, bg='ghost white')
        self.frame_inventario = Frame(self.paginas, bg='ghost white')
        self.frame_acomodoProductos = Frame(self.paginas, bg='ghost white')
        self.frame_controlVentas = Frame(self.paginas, bg='ghost white')

        self.frame_dimensiones= Frame(self.paginas, bg='ghost white')
        self.frame_regProd= Frame(self.paginas, bg='ghost white')

        self.frame_regContrato= Frame(self.paginas, bg='ghost white')
        self.frame_lisContrato= Frame(self.paginas, bg='ghost white')
        self.frame_RegistrarEmpresa= Frame(self.paginas, bg='ghost white')


        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_ciudad)
        self.paginas.add(self.frame_codigo)
        self.paginas.add(self.frame_colonia)
        self.paginas.add(self.frame_sucursales)
        self.paginas.add(self.frame_ListaSurcursales)
        self.paginas.add(self.frame_personal)
        self.paginas.add(self.frame_inventario)
        self.paginas.add(self.frame_acomodoProductos)
        self.paginas.add(self.frame_controlVentas)
        self.paginas.add(self.frame_controlVentas)


        self.paginas.add(self.frame_dimensiones)
        self.paginas.add(self.frame_regProd)
        self.paginas.add(self.frame_regContrato)
        self.paginas.add(self.frame_lisContrato)
        self.paginas.add(self.frame_RegistrarEmpresa)



    ##############################         PAGINAS       #############################################
        ######################## FRAME TITULO #################
        self.titulo = Label(self.frame_top,text= 'Cadena de Tienditas', bg='thistle2', fg= 'DarkOrchid1', font= ('Imprint MT Shadow', 15, 'bold'))
        self.titulo.pack(expand = 1)

        ######################## VENTANA PRINCIPAL #################
        Label(self.frame_uno, text= 'Cadena de Tienditas: Región Michoacán', bg='snow', fg= 'DarkOrchid1', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno ,image = self.tiendita , bg='snow').pack(expand=1)

        #ESTILO DE LAS TABLAS DE DATOS TREEVIEW
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font= ('Helvetica', 12, 'bold'), foreground='black',  background='white')  #, fieldbackground='yellow'
        estilo_tabla.map('Treeview',background=[('selected', 'DarkOrchid1')], foreground=[('selected','black')] )		
        estilo_tabla.configure('Heading',background = 'lavenderblush2', foreground='navy',padding=3, font= ('Arial', 12, 'bold'))
        estilo_tabla.configure('Item',foreground = 'white', focuscolor ='DarkOrchid1')
        estilo_tabla.configure('TScrollbar', arrowcolor = 'DarkOrchid1',bordercolor  ='black', troughcolor= 'DarkOrchid1',background ='white')
        
        ######################## CIUDAD #################

        Label(self.frame_ciudad, text= 'Ciudades', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 18, 'bold')).place(x = 410, y = 0)
        
        Label(self.frame_ciudad, text = 'Nombre: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 100, y = 65)
        Label(self.frame_ciudad, text = 'Lada: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 130, y = 105) 

        Entry(self.frame_ciudad, textvariable=self.nom_ciu, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 190, y = 65)
        self.enciu = Entry(self.frame_ciudad, textvariable=self.lada_ciu, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 190, y = 105)
 

        Button(self.frame_ciudad, text='Lista de ciudades',fg='white' ,font = ('Arial', 14,'bold'), command= self.datos_totales_ciudad, bg = 'slateblue1', bd = 2, borderwidth=2, cursor="hand2", width = 23).place(x = 330, y =530)
        Button(self.frame_ciudad,command= self.agregar_ciudad, text='Registrar',fg='white', font=('Arial',14,'bold'), bg='orchid', cursor="hand2", width = 23).place(x = 550, y = 65)

        Label(self.frame_ciudad, text = 'Buscar ciudad: ',fg='purple', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 40, y = 185)
        Entry(self.frame_ciudad, textvariable= self.buscar_ciu , font=('Helvica',14), highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=2).place(x = 193, y = 185)

        Button(self.frame_ciudad,command = self.buscar_ciudad, text='Buscar', fg='white', font=('Helvica',14,'bold'), bg='royalblue2', cursor="hand2").place(x = 430, y = 180)
        Button(self.frame_ciudad,command = self.modificar_tabla_ciudad, text='Modificar',fg='white', font=('Helvica',14,'bold'), bg='DarkOrchid4', cursor="hand2", width = 23).place(x = 550, y = 115)

        self.aviso_guardado_ciu = Label(self.frame_ciudad, bg= 'ghost white', font=('Comic Sans MS', 12), fg='black')
        self.aviso_guardado_ciu.place(x = 390, y = 230)

        #TABLA ciudad
        self.frame_tabla_ciudad = Frame(self.frame_ciudad, bg= 'gray90')
        self.frame_tabla_ciudad.place(x=12, y = 270)		
        self.tabla_ciudad = ttk.Treeview(self.frame_tabla_ciudad) 
        self.tabla_ciudad.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_ciudad, orient = 'horizontal', command= self.tabla_ciudad.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_ciudad, orient ='vertical', command = self.tabla_ciudad.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_ciudad.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_ciudad['columns'] = ('Nombre', 'Lada')
        self.tabla_ciudad.column('#0', minwidth=100, width=170, anchor='center')
        self.tabla_ciudad.column('Nombre', minwidth=100, width=470 , anchor='center')
        self.tabla_ciudad.column('Lada', minwidth=100, width=270 , anchor='center')

        self.tabla_ciudad.heading('#0', text='ID', anchor ='center')
        self.tabla_ciudad.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_ciudad.heading('Lada', text='Lada', anchor ='center')
        self.tabla_ciudad.bind("<<TreeviewSelect>>", self.obtener_fila_ciudad) 
    

 #       -------------- Código Postal ---------------
        Label(self.frame_codigo, text= 'Código Postal', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 18, 'bold')).place(x = 410, y = 0)
        
        Label(self.frame_codigo, text = 'Código postal: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 50, y = 65)
        Label(self.frame_codigo, text = 'Ciudad: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 113, y = 105) 

        Entry(self.frame_codigo, textvariable = self.cp, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 200, y = 65)
        Entry(self.frame_codigo, textvariable = self.ciudad_cp, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 200, y = 105)
       

        Label(self.frame_codigo, text = 'Buscar código postal: ',fg='purple', bg ='ghost white', font=('Helvica',12,'bold')).place(x = 10, y = 205)
        Entry(self.frame_codigo, textvariable= self.busca_cp , font=('Helvica',12), highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=2, width=15).place(x = 185, y = 205)
        Button(self.frame_codigo,command = self.buscar_cp, text='Buscar', fg='white', font=('Helvica',12), bg='royalblue2', cursor="hand2" ).place(x = 350, y = 200)

        Label(self.frame_codigo, text = 'Buscar ciudad: ',fg='purple', bg ='ghost white', font=('Helvica',12,'bold')).place(x = 10, y = 260)
        Entry(self.frame_codigo, textvariable= self.buscar_ciu , font=('Helvica',12), highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=2).place(x = 135, y = 260)
        Button(self.frame_codigo,command = self.buscar_ciudad_cp, text='Buscar', fg='white', font=('Helvica',12), bg='royalblue2', cursor="hand2").place(x = 350, y = 255)


        Button(self.frame_codigo, text='Lista de códigos postales',fg='white' ,font = ('Arial', 14,'bold'), command= self.datos_totales_cp, bg = 'slateblue1', bd = 2, borderwidth=2, cursor="hand2", width = 23).place(x = 113, y = 420)
        Button(self.frame_codigo,command= self.agregar_datos_cp, text='Registrar',fg='white', font=('Arial',14,'bold'), bg='orchid', cursor="hand2", width = 23).place(x = 113, y = 350)
        #Button(self.frame_codigo, command= self.modificar_tabla_cp, text='Modificar datos',fg='white', font=('Helvica',14,'bold'), bg='MediumPurple4', cursor="hand2", width = 23).place(x = 113, y = 350)

#        Button(self.frame_codigo,command = self.actualizar_tabla_cp, text='Guardar',fg='white', font=('Helvica',14,'bold'), bg='DarkOrchid4', cursor="hand2", width = 23).place(x = 113, y = 450)
        Button(self.frame_codigo, text='Lista de ciudades',fg='white' ,font = ('Arial', 14,'bold'), command= self.datos_totales_ciudad_cp, bg = 'slateblue1', bd = 2, borderwidth=2, cursor="hand2", width = 23).place(x = 113, y = 500)

        #TABLA Codigo postal
        self.frame_tabla_cp = Frame(self.frame_codigo, bg= 'gray90')
        self.frame_tabla_cp.place(x=480, y = 65)		
        self.tabla_cp = ttk.Treeview(self.frame_tabla_cp) 
        self.tabla_cp.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_cp, orient = 'horizontal', command= self.tabla_cp.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_cp, orient ='vertical', command = self.tabla_cp.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_cp.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_cp['columns'] = ( 'Ciudad')
        self.tabla_cp.column('#0', minwidth=100, width=140, anchor='center')
        self.tabla_cp.column('Ciudad', minwidth=100, width=280 , anchor='center')
    
        self.tabla_cp.heading('#0', text='Código Postal', anchor ='center')
        self.tabla_cp.heading('Ciudad', text='Ciudad', anchor ='center')
        self.tabla_cp.bind("<<TreeviewSelect>>", self.obtener_fila_ciudad) 

        #TABLA ciudad_cp
        self.frame_tabla_cp = Frame(self.frame_codigo, bg= 'gray90')
        self.frame_tabla_cp.place(x=480, y = 335)		
        self.tabla_ciudadp = ttk.Treeview(self.frame_tabla_cp) 
        self.tabla_ciudadp.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_cp, orient = 'horizontal', command= self.tabla_ciudadp.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_cp, orient ='vertical', command = self.tabla_ciudadp.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_ciudadp.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_ciudadp['columns'] = ('Nombre', 'Lada')
        self.tabla_ciudadp.column('#0', minwidth=100, width=90, anchor='center')
        self.tabla_ciudadp.column('Nombre', minwidth=100, width=200 , anchor='center')
        self.tabla_ciudadp.column('Lada', minwidth=100, width=130 , anchor='center')

        self.tabla_ciudadp.heading('#0', text='ID', anchor ='center')
        self.tabla_ciudadp.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_ciudadp.heading('Lada', text='Lada', anchor ='center')
        self.tabla_ciudadp.bind("<<TreeviewSelect>>", self.obtener_fila_ciudad) 

######################## Colonia ##############################

        Label(self.frame_colonia, text= 'Colonias', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 18, 'bold')).place(x = 410, y = 0)
        
        Label(self.frame_colonia, text = 'Nombre de la colonia: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 10, y = 65)
        Label(self.frame_colonia, text = 'Código postal: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 73, y = 105) 

        Entry(self.frame_colonia, textvariable = self.nombre_col, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 220, y = 65)
        Entry(self.frame_colonia, textvariable = self.cp_col, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 220, y = 105)

        Label(self.frame_colonia, text = 'Buscar colonia: ',fg='purple', bg ='ghost white', font=('Helvica',13,'bold')).place(x = 10, y = 200)
        Entry(self.frame_colonia, textvariable= self.busca_col , font=('Helvica',13), highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=2, width=21).place(x = 140, y = 200)
        Button(self.frame_colonia,command = self.buscar_colonia, text='Buscar', fg='white', font=('Helvica',13), bg='royalblue2', cursor="hand2" ).place(x = 350, y = 197)

        Label(self.frame_colonia, text = 'Buscar código postal: ',fg='purple', bg ='ghost white', font=('Helvica',13,'bold')).place(x = 10, y = 250)
        Entry(self.frame_colonia, textvariable= self.busca_cp , font=('Helvica',12), highlightbackground = "DarkOrchid1", highlightcolor= "deep sky blue", highlightthickness=2, width=16).place(x = 189, y = 250)
        Button(self.frame_colonia,command = self.buscar_cp_col, text='Buscar', fg='white', font=('Helvica',13), bg='royalblue2', cursor="hand2" ).place(x = 350, y = 247)

        Button(self.frame_colonia,command= self.agregar_datos_colonia, text='Registrar',fg='white', font=('Arial',14,'bold'), bg='orchid', cursor="hand2", width = 23).place(x = 113, y = 350)
        Button(self.frame_colonia, text='Lista de colonia',fg='white' ,font = ('Arial', 14,'bold'), command= self.datos_totales_col, bg = 'slateblue1', bd = 2, borderwidth=2, cursor="hand2", width = 23).place(x = 113, y = 430)
        Button(self.frame_colonia, text='Lista de códigos postales',fg='white' ,font = ('Arial', 14,'bold'), command= self.datos_totales_cp_col, bg = 'slateblue1', bd = 2, borderwidth=2, cursor="hand2", width = 23).place(x = 113, y = 500)

        #Button(self.frame_colonia, command= self.actualizar_datos_ciudad, text='Actualizar datos',fg='white', font=('Helvica',14,'bold'), bg='MediumPurple4', cursor="hand2", width = 23).place(x = 113, y = 350)
        #Button(self.frame_colonia,command = self.actualizar_tabla_ciudad, text='Guardar',fg='white', font=('Helvica',14,'bold'), bg='DarkOrchid4', cursor="hand2", width = 23).place(x = 113, y = 450)

        #TABLA Colonia
        self.frame_tabla_col = Frame(self.frame_colonia, bg= 'gray90')
        self.frame_tabla_col.place(x=480, y = 65)		
        self.tabla_col = ttk.Treeview(self.frame_tabla_col) 
        self.tabla_col.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_col, orient = 'horizontal', command= self.tabla_col.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_col, orient ='vertical', command = self.tabla_col.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_col.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_col['columns'] = ('Nombre', 'Codigo')
        self.tabla_col.column('#0', minwidth=100, width=140, anchor='center')
        self.tabla_col.column('Nombre', minwidth=100, width=150 , anchor='center')
        self.tabla_col.column('Codigo', minwidth=100, width=150 , anchor='center')
    
        self.tabla_col.heading('#0', text='ID', anchor ='center')
        self.tabla_col.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_col.heading('Codigo', text='Codigo Postal', anchor ='center')
        self.tabla_col.bind("<<TreeviewSelect>>", self.obtener_fila_cp) 
    
        #TABLA Codigo postal_ col
        self.frame_tabla_cp_col = Frame(self.frame_colonia, bg= 'gray90')
        self.frame_tabla_cp_col.place(x=480, y = 335)		
        self.tabla_cp_col = ttk.Treeview(self.frame_tabla_cp_col) 
        self.tabla_cp_col.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_cp_col, orient = 'horizontal', command= self.tabla_cp_col.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_cp_col, orient ='vertical', command = self.tabla_cp_col.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_cp_col.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_cp_col['columns'] = ( 'Ciudad')
        self.tabla_cp_col.column('#0', minwidth=100, width=140, anchor='center')
        self.tabla_cp_col.column('Ciudad', minwidth=100, width=280 , anchor='center')
    
        self.tabla_cp_col.heading('#0', text='Código Postal', anchor ='center')
        self.tabla_cp_col.heading('Ciudad', text='Ciudad', anchor ='center')
        self.tabla_cp_col.bind("<<TreeviewSelect>>", self.obtener_fila_ciudad) 

######################## SUCURSALES ##############################

        Label(self.frame_sucursales, text= 'Sucursales', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 18, 'bold')).place(x = 410, y = 0)
        
        Label(self.frame_sucursales, text = 'Calle: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 70, y = 65)
        Label(self.frame_sucursales, text = 'Número: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 45, y = 100) 
        Label(self.frame_sucursales, text = 'Orientación: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 10, y = 135) 
        Label(self.frame_sucursales, text = 'Entre calles: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 10, y = 170) 
        Label(self.frame_sucursales, text = 'Telefono: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 36, y = 210) 
        Label(self.frame_sucursales, text = 'Colonia: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 45, y = 245) 
        Label(self.frame_sucursales, text = 'Dimension: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 17, y = 280) 


        Entry(self.frame_sucursales, textvariable = self.calle_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 65)
        Entry(self.frame_sucursales, textvariable = self.num_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 100)
        self.my_combobox_orientacion=tkk.Combobox(self.frame_sucursales,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_orientacion.place(x=140, y = 135)
        self.opcionesOrientacion=['Norte','sur','poniente','oriente']
        self.my_combobox_orientacion.set(self.opcionesOrientacion[0])
        self.my_combobox_orientacion['values']=self.opcionesOrientacion
        self.my_combobox_orientacion.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)
        Entry(self.frame_sucursales, textvariable = self.entrecalles_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 170)
        Entry(self.frame_sucursales, textvariable = self.tel_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 210)
        Entry(self.frame_sucursales, textvariable = self.id_col_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 245)
        Entry(self.frame_sucursales, textvariable = self.id_dimen_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 280)
   
        Button(self.frame_sucursales,command= self.agregar_datos_surcursal, text='Registrar',fg='white', font=('Helvica',14,'bold'), bg='orchid', cursor="hand2", width = 25, height=2).place(x = 90, y = 360)
        Button(self.frame_sucursales,command = self.pantalla_ListaSucursales, text='Lista de Surcursales', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2", width = 25, height=2 ).place(x = 90, y = 440)
        Button(self.frame_sucursales,command = self.pantalla_dimensiones, text='Registrar Dimensiones', fg='white', font=('Helvica',14), bg='DarkOrchid4', cursor="hand2", width=25, height=2).place(x = 90, y = 530)


        #TABLA SURCURSALES
        Label(self.frame_ListaSurcursales, text= 'Lista de Sucursales', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 22, 'bold')).place(x = 350, y = 0)

        self.frame_tabla_listaSurcursal = Frame(self.frame_ListaSurcursales, bg= 'gray90')
        self.frame_tabla_listaSurcursal.place(x=20, y = 65)		
        self.tabla_surcursal = ttk.Treeview(self.frame_tabla_listaSurcursal) 
        self.tabla_surcursal.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_listaSurcursal, orient = 'horizontal', command= self.tabla_surcursal.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_listaSurcursal, orient ='vertical', command = self.tabla_surcursal.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_surcursal.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_surcursal['columns'] = ( 'Calle', 'Numero', 'Orientación', 'EntreCalles', 'Teléfono', 'Colonia', 'Dimension')
        self.tabla_surcursal.column('#0', minwidth=50, width=60, anchor='center')
        self.tabla_surcursal.column('Calle', minwidth=100, width=150, anchor='center')
        self.tabla_surcursal.column('Numero', minwidth=50, width=60 , anchor='center')
        self.tabla_surcursal.column('Orientación', minwidth=80, width=100 , anchor='center')
        self.tabla_surcursal.column('EntreCalles', minwidth=100, width=150 , anchor='center')
        self.tabla_surcursal.column('Teléfono', minwidth=90, width=110 , anchor='center')
        self.tabla_surcursal.column('Colonia', minwidth=100, width=150 , anchor='center')
        self.tabla_surcursal.column('Dimension', minwidth=80, width=120 , anchor='center')
    
        self.tabla_surcursal.heading('#0', text='ID', anchor ='center')
        self.tabla_surcursal.heading('Calle', text='Calle', anchor ='center')
        self.tabla_surcursal.heading('Numero', text='No.', anchor ='center')
        self.tabla_surcursal.heading('Orientación', text='Orientación', anchor ='center')
        self.tabla_surcursal.heading('EntreCalles', text='Entre Calles', anchor ='center')
        self.tabla_surcursal.heading('Teléfono', text='Teléfono', anchor ='center')
        self.tabla_surcursal.heading('Colonia', text='Colonia', anchor ='center')
        self.tabla_surcursal.heading('Dimension', text='Dimensión', anchor ='center')
        self.tabla_surcursal.bind("<<TreeviewSelect>>", self.obtener_fila_cp) 
    
        Label(self.frame_ListaSurcursales, text = 'Calle: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 70, y = 350)
        Label(self.frame_ListaSurcursales, text = 'Número: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 45, y = 385) 
        Label(self.frame_ListaSurcursales, text = 'Orientación: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 10, y = 420) 
        Label(self.frame_ListaSurcursales, text = 'Entre calles: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 10, y = 455) 
        Label(self.frame_ListaSurcursales, text = 'Telefono: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 36, y = 490) 
        Label(self.frame_ListaSurcursales, text = 'Colonia: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 45, y = 525) 
        Label(self.frame_ListaSurcursales, text = 'Dimension: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 17, y = 560) 
    
        Entry(self.frame_ListaSurcursales, textvariable = self.calle_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 350)
        Entry(self.frame_ListaSurcursales, textvariable = self.num_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 385)
        self.my_combobox_orientacion=tkk.Combobox(self.frame_ListaSurcursales,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_orientacion.place(x=140, y = 420)
        self.opcionesOrientacion=['Norte','sur','poniente','oriente']
        self.my_combobox_orientacion.set(self.opcionesOrientacion[0])
        self.my_combobox_orientacion['values']=self.opcionesOrientacion
        self.my_combobox_orientacion.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)
        Entry(self.frame_ListaSurcursales, textvariable = self.entrecalles_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 455)
        Entry(self.frame_ListaSurcursales, textvariable = self.tel_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 490)
        Entry(self.frame_ListaSurcursales, textvariable = self.id_col_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 525)
        Entry(self.frame_ListaSurcursales, textvariable = self.id_dimen_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 560)
    
        Label(self.frame_ListaSurcursales, text = 'Buscar sucursal: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 480, y = 350) 
        Entry(self.frame_ListaSurcursales, textvariable = self.id_tie, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 650, y = 350)
        Button(self.frame_ListaSurcursales,command = self.buscar_Sucursal, text='Buscar', fg='white', font=('Helvica',14), bg='DarkOrchid3', cursor="hand2", width=20, height=2).place(x = 600, y = 400)
        Button(self.frame_ListaSurcursales,command = self.modificar_tabla_Sucursal, text='Modificar', fg='white', font=('Helvica',14), bg='DarkOrchid4', cursor="hand2", width=20, height=2).place(x = 600, y = 480)

    
     #TABLA Colonia
        self.frame_tabla_col_sur = Frame(self.frame_sucursales, bg= 'gray90')
        self.frame_tabla_col_sur.place(x=480, y = 50)		
        self.tabla_col_sur = ttk.Treeview(self.frame_tabla_col_sur) 
        self.tabla_col_sur.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_col_sur, orient = 'horizontal', command= self.tabla_col_sur.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_col_sur, orient ='vertical', command = self.tabla_col_sur.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_col_sur.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_col_sur['columns'] = ('Nombre', 'Codigo')
        self.tabla_col_sur.column('#0', minwidth=50, width=70, anchor='center')
        self.tabla_col_sur.column('Nombre', minwidth=100, width=200 , anchor='center')
        self.tabla_col_sur.column('Codigo', minwidth=100, width=115 , anchor='center')
    
        self.tabla_col_sur.heading('#0', text='ID', anchor ='center')
        self.tabla_col_sur.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_col_sur.heading('Codigo', text='Codigo Postal', anchor ='center')
        self.tabla_col_sur.bind("<<TreeviewSelect>>", self.obtener_fila_cp) 
    
        #TABLA DIMENSIONES
        Label(self.frame_sucursales, text= 'Lista de Dimensiones', bg='ghost white', fg= 'deeppink4', font= ('Comic Sans MS', 13, 'bold')).place(x = 600, y = 300)
        self.frame_tabla_dim_sur = Frame(self.frame_sucursales, bg= 'gray90')
        self.frame_tabla_dim_sur.place(x=480, y = 340)		
        self.tabla_dim_sur = ttk.Treeview(self.frame_tabla_dim_sur) 
        self.tabla_dim_sur.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_dim_sur, orient = 'horizontal', command= self.tabla_dim_sur.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_dim_sur, orient ='vertical', command = self.tabla_dim_sur.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_dim_sur.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_dim_sur.column('#0', minwidth=50, width=70, anchor='center')
        self.tabla_dim_sur['columns'] = ('Alto', 'Largo', 'Ancho', "Unidad")
        self.tabla_dim_sur.column('Alto', minwidth=50, width=90 , anchor='center')
        self.tabla_dim_sur.column('Largo', minwidth=50, width=90 , anchor='center')
        self.tabla_dim_sur.column('Ancho', minwidth=50, width=90 , anchor='center')
        self.tabla_dim_sur.column('Unidad', minwidth=50, width=90 , anchor='center')
    
        self.tabla_dim_sur.heading('#0', text='ID', anchor ='center')
        self.tabla_dim_sur.heading('Alto', text='Alto', anchor ='center')
        self.tabla_dim_sur.heading('Largo', text='Largo', anchor ='center')
        self.tabla_dim_sur.heading('Ancho', text='Ancho', anchor ='center')
        self.tabla_dim_sur.heading('Unidad', text='UM', anchor ='center')
        self.tabla_dim_sur.bind("<<TreeviewSelect>>", self.obtener_fila_cp) 

        #****** Pantalla Dimension ******

        Label(self.frame_dimensiones, text= 'Dimensiones para Sucursales', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 18, 'bold')).place(x = 300, y = 0)


        Label(self.frame_dimensiones, text= 'Lista de Dimensiones', bg='ghost white', fg= 'deeppink4', font= ('Comic Sans MS', 13, 'bold')).place(x = 580, y = 100)
        Label(self.frame_dimensiones, text= 'Registrar Dimensiones', bg='ghost white', fg= 'deeppink4', font= ('Comic Sans MS', 13, 'bold')).place(x = 180, y = 100)

        Label(self.frame_dimensiones, text = 'Alto: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 70, y = 150)
        Label(self.frame_dimensiones, text = 'Largo: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 50, y = 190) 
        Label(self.frame_dimensiones, text = 'Ancho: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 45, y = 230) 
       
        Entry(self.frame_dimensiones, textvariable = self.alto, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 150)
        Entry(self.frame_dimensiones, textvariable = self.largo, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 190)
        Entry(self.frame_dimensiones, textvariable = self.ancho, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 140, y = 230)

        Button(self.frame_dimensiones,command = self.registrarDimenTien, text='Registrar', fg='white', font=('Helvica',14), bg='DarkOrchid3', cursor="hand2", width=20, height=2).place(x = 120, y = 300)


        self.frame_tabla_dim = Frame(self.frame_dimensiones, bg= 'gray90')
        self.frame_tabla_dim.place(x=480, y = 140)		
        self.tabla_dim = ttk.Treeview(self.frame_tabla_dim) 
        self.tabla_dim.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_dim, orient = 'horizontal', command= self.tabla_dim.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_dim, orient ='vertical', command = self.tabla_dim.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_dim.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_dim.column('#0', minwidth=50, width=70, anchor='center')
        self.tabla_dim['columns'] = ('Alto', 'Largo', 'Ancho', "Unidad")
        self.tabla_dim.column('Alto', minwidth=50, width=90 , anchor='center')
        self.tabla_dim.column('Largo', minwidth=50, width=90 , anchor='center')
        self.tabla_dim.column('Ancho', minwidth=50, width=90 , anchor='center')
        self.tabla_dim.column('Unidad', minwidth=50, width=90 , anchor='center')
    
        self.tabla_dim.heading('#0', text='ID', anchor ='center')
        self.tabla_dim.heading('Alto', text='Alto', anchor ='center')
        self.tabla_dim.heading('Largo', text='Largo', anchor ='center')
        self.tabla_dim.heading('Ancho', text='Ancho', anchor ='center')
        self.tabla_dim.heading('Unidad', text='UM', anchor ='center')
        self.tabla_dim.bind("<<TreeviewSelect>>", self.obtener_fila_cp) 
        
######################## PERSONAL ##############################

        Label(self.frame_personal, text= 'Control de Personal', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 370, y = 0)
        
        Button(self.frame_personal, command = self.pantalla_regContrato, text='Registrar nuevo contrato', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2", width=35, height=3).place(x = 270, y = 90)
        Button(self.frame_personal, command = self.pantalla_ListaContrato, text='Lista de contratos', fg='white', font=('Helvica',14, 'bold'), bg='Maroon3', cursor="hand2", width=35, height=3).place(x = 270, y = 200)
        Button(self.frame_personal, command = self.pantalla_RegistrarEmpresa, text='Empresas', fg='white', font=('Helvica',14, 'bold'), bg='Magenta4', cursor="hand2", width=35, height=3).place(x = 270, y = 310)

# *** PANTALLA Registrar Contrato ****


        Label(self.frame_regContrato, text= 'Registrar Contrato', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 390, y = 0)
        
        Label(self.frame_regContrato, text = 'Apellido Paterno', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 65)
        Label(self.frame_regContrato, text = 'Apellido Materno: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 100) 
        Label(self.frame_regContrato, text = 'Nombre: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 135) 
        Label(self.frame_regContrato, text = 'Genero: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 170) 
        Label(self.frame_regContrato, text = 'Fecha de nacimiento: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 210) 
        Label(self.frame_regContrato, text = 'Telefono:', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 245) 
        Label(self.frame_regContrato, text = 'E-mail: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 280) 
        Label(self.frame_regContrato, text = 'Estado civil: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 315) 
        Label(self.frame_regContrato, text = 'Calle: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 350) 
        Label(self.frame_regContrato, text = 'Número: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 385) 
        Label(self.frame_regContrato, text = 'Orientación: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 420)      
        Label(self.frame_regContrato, text = 'Entre calles: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 455) 
        Label(self.frame_regContrato, text = 'Colonia: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 490) 
        Label(self.frame_regContrato, text = 'Fecha inicio: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 525) 
        Label(self.frame_regContrato, text = 'Fecha final: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 560) 
        Label(self.frame_regContrato, text = 'Puesto: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 530, y = 65) 
        Label(self.frame_regContrato, text = 'Sueldo: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 530, y = 100) 
        Label(self.frame_regContrato, text = 'Hora de entrada: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 530, y = 135) 
        Label(self.frame_regContrato, text = 'Hora de salida: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 530, y = 170) 
        Label(self.frame_regContrato, text = 'Tienda: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 530, y = 210) 

        Entry(self.frame_regContrato, textvariable = self.ap, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 65)
        Entry(self.frame_regContrato, textvariable = self.am, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 100)
        Entry(self.frame_regContrato, textvariable = self.nombre, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 135)
        #Entry(self.frame_regContrato, textvariable = self.genero, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 170)
        
        self.my_combobox_genero = tkk.Combobox(self.frame_regContrato,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_genero.place(x = 230, y = 170)
        self.opcionesGenero = ["F", "M"]
        self.my_combobox_genero.set(self.opcionesGenero[0])
        self.my_combobox_genero['values']=self.opcionesGenero
        self.my_combobox_genero.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)
        
        self.fnac = DateEntry(self.frame_regContrato,font=('Helvica', 14), bg = "purple", fg = "white", year = 2000-100)
        self.fnac.place(x = 250, y = 210)

        Entry(self.frame_regContrato, textvariable = self.tel, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 245)
        Entry(self.frame_regContrato, textvariable = self.mail, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 280)
        #Entry(self.frame_regContrato, textvariable = self.edocivil, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 315)
        
        self.my_combobox_edoCivil = tkk.Combobox(self.frame_regContrato,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_edoCivil.place(x = 230, y = 315)
        self.opcionesEdoCivil= ["Casado(a)", "Soltero(a)", "Divorciado(a)", "Viudo(a)"]
        self.my_combobox_edoCivil.set(self.opcionesEdoCivil[0])
        self.my_combobox_edoCivil['values']=self.opcionesEdoCivil
        self.my_combobox_edoCivil.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)
        
        Entry(self.frame_regContrato, textvariable = self.calle, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 350)
        Entry(self.frame_regContrato, textvariable = self.num, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 385)
        #Entry(self.frame_regContrato, textvariable = self.orientacion, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 420)
        
        self.my_combobox_orientacion=tkk.Combobox(self.frame_regContrato,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_orientacion.place(x = 230, y = 420)
        self.opcionesOrientacion=['Norte','sur','poniente','oriente']
        self.my_combobox_orientacion.set(self.opcionesOrientacion[0])
        self.my_combobox_orientacion['values']=self.opcionesOrientacion
        self.my_combobox_orientacion.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)

        Entry(self.frame_regContrato, textvariable = self.entreca, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 455)
        #Entry(self.frame_regContrato, textvariable = self.colonia, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 490)
        self.my_combobox_colonias = tkk.Combobox(self.frame_regContrato,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_colonias.place(x = 230, y = 490)
        self.opcionesColonias= self.Contrato.nomColonias()
        self.my_combobox_colonias.set(self.opcionesColonias[0])
        self.my_combobox_colonias['values']=self.opcionesColonias
        self.my_combobox_colonias.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)
        
        #Entry(self.frame_regContrato, textvariable = self.fi, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 525)
        self.fi = DateEntry(self.frame_regContrato,font=('Helvica', 14), bg = "purple", fg = "white")
        self.fi.place(x = 230, y = 525)
        #Entry(self.frame_regContrato, textvariable = self.ff, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 560)
        self.ff = DateEntry(self.frame_regContrato,font=('Helvica', 14), bg = "purple", fg = "white")
        self.ff.place(x = 230, y = 560)

        Entry(self.frame_regContrato, textvariable = self.puesto, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 630, y = 65)
        Entry(self.frame_regContrato, textvariable = self.sueldo, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 630, y = 100)
        Entry(self.frame_regContrato, textvariable = self.hi, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place( x = 690, y = 135)
        Entry(self.frame_regContrato, textvariable = self.hf, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place( x = 680, y = 170)
        #Entry(self.frame_regContrato, textvariable = self.tienda, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place( x = 630, y = 210)

        
        self.my_combobox_tiendas = tkk.Combobox(self.frame_regContrato,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_tiendas.place(x = 630, y = 210)
        self.opcionesTiendas = self.Contrato.idTiendas()
        self.my_combobox_tiendas.set(self.opcionesTiendas[0])
        self.my_combobox_tiendas['values']=self.opcionesTiendas
        self.my_combobox_tiendas.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)

        Button(self.frame_regContrato, command = self.registrarContrato, text='Registrar', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2", width=30).place(x = 560, y = 260)

        ###  Tabla Personas " ##
        Label(self.frame_lisContrato, text= 'Lista de Personal', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 390, y = 0)

        self.frame_tabla_per = Frame(self.frame_lisContrato, bg= 'gray90')
        self.frame_tabla_per.place(x=5, y = 65)		
        self.tabla_per = ttk.Treeview(self.frame_tabla_per) 
        self.tabla_per.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_per, orient = 'horizontal', command= self.tabla_per.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_per, orient ='vertical', command = self.tabla_per.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_per.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_per.column('#0', minwidth=30, width=30, anchor='center')
        self.tabla_per['columns'] = ('Ap', 'Am', 'Nombre', 'Genero', 'Fnac', 'Tel', 'Mail', 'EdoCivil', 'Calle', 'Num', 'Orientacion', 'EntreCalles', 'Colonia')
        self.tabla_per.column('Ap', minwidth=50, width=90 , anchor='center')
        self.tabla_per.column('Am', minwidth=50, width=120 , anchor='center')
        self.tabla_per.column('Nombre', minwidth=50, width=120 , anchor='center')
        self.tabla_per.column('Genero', minwidth=20, width=20 , anchor='center')
        self.tabla_per.column('Fnac', minwidth=50, width=80 , anchor='center')
        self.tabla_per.column('Tel', minwidth=50, width=80 , anchor='center')
        self.tabla_per.column('Mail', minwidth=50, width=80 , anchor='center')
        self.tabla_per.column('EdoCivil', minwidth=50, width=80 , anchor='center')
        self.tabla_per.column('Calle', minwidth=50, width=120 , anchor='center')
        self.tabla_per.column('Num', minwidth=30, width=30 , anchor='center')
        self.tabla_per.column('Orientacion', minwidth=30, width=40 , anchor='center')
        self.tabla_per.column('EntreCalles', minwidth=50, width=120 , anchor='center')
        self.tabla_per.column('Colonia', minwidth=50, width=120 , anchor='center')

        self.tabla_per.heading('#0', text='Id', anchor ='center')
        self.tabla_per.heading('Ap', text='Ap', anchor ='center')
        self.tabla_per.heading('Am', text='Am', anchor ='center')
        self.tabla_per.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_per.heading('Genero', text='Genero', anchor ='center')
        self.tabla_per.heading('Fnac', text='Fnac', anchor ='center')
        self.tabla_per.heading('Tel', text='Tel', anchor ='center')
        self.tabla_per.heading('Mail', text='E-mail', anchor ='center')
        self.tabla_per.heading('EdoCivil', text='Edo. Civil', anchor ='center')
        self.tabla_per.heading('Calle', text='Calle', anchor ='center')
        self.tabla_per.heading('Num', text='Num', anchor ='center')
        self.tabla_per.heading('Orientacion', text='Orientacion', anchor ='center')
        self.tabla_per.heading('EntreCalles', text='EntreCalles', anchor ='center')
        self.tabla_per.heading('Colonia', text='Colonia', anchor ='center')

        self.tabla_per.bind("<<TreeviewSelect>>", self.obtener_fila_cp)
        
        """""
        Button(self.frame_regContrato, command = self.buscar_Producto, text='Buscar Producto', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x = 560, y = 65)
        Button(self.frame_regContrato, command = self.modificar_producto, text='Modificar Producto', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x =560, y = 125)
"""""
    
#       PANTALLA REGISTRAR EMPRESA 

        Label(self.frame_RegistrarEmpresa, text= 'Empresas y Marcas', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 390, y = 0)
        
        Label(self.frame_RegistrarEmpresa, text= 'Registrar empresa', bg='ghost white', fg= 'Purple', font= ('Comic Sans MS', 14, 'bold')).place(x = 120, y = 40)

        Label(self.frame_RegistrarEmpresa, text = 'Nombre: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 85)
        Label(self.frame_RegistrarEmpresa, text = 'Teléfono: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 120) 
        
        Entry(self.frame_RegistrarEmpresa, textvariable = self.nombre_emp, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 150, y = 85)
        Entry(self.frame_RegistrarEmpresa, textvariable = self.tel_emp, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 150, y = 120)
      
        Button(self.frame_RegistrarEmpresa, command = self.registrarEmpresa, text='Registrar', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2", width=25).place(x = 30, y = 165)

        Label(self.frame_RegistrarEmpresa, text= 'Registrar marca', bg='ghost white', fg= 'Purple', font= ('Comic Sans MS', 14, 'bold')).place(x = 120, y = 235)
       
        Label(self.frame_RegistrarEmpresa, text = 'Nombre: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 270)
        Label(self.frame_RegistrarEmpresa, text = 'Tipo: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 310) 
        Label(self.frame_RegistrarEmpresa, text = 'Empresa: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 345) 
        
        Entry(self.frame_RegistrarEmpresa, textvariable = self.nom_mar, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 150, y = 270)
        
        self.my_combobox_TipoMarca = tkk.Combobox(self.frame_RegistrarEmpresa,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_TipoMarca.place(x = 150, y = 310)
        self.opcionesTipoMarca = ['Nacional', 'Local','Internacional']
        self.my_combobox_TipoMarca.set(self.opcionesTipoMarca[0])
        self.my_combobox_TipoMarca['values']=self.opcionesTipoMarca
        self.my_combobox_TipoMarca.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)
        
        self.my_combobox_nomEmpresas = tkk.Combobox(self.frame_RegistrarEmpresa,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_nomEmpresas.place(x = 150, y =345)
        self.opcionesEmpresas = self.Empresa.nomEmpresa()
        self.my_combobox_nomEmpresas.set(self.opcionesEmpresas[0])
        self.my_combobox_nomEmpresas['values']=self.opcionesEmpresas
        self.my_combobox_nomEmpresas.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)

        Button(self.frame_RegistrarEmpresa, command = self.registrarMarca, text='Registrar', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2", width=25).place(x = 30, y = 400)

    #***** Tabla Empresa*****
        Label(self.frame_RegistrarEmpresa, text= 'Lista de marcas', bg='ghost white', fg= 'Purple', font= ('Comic Sans MS', 14, 'bold')).place(x = 630, y = 330)

        self.frame_tabla_mar = Frame(self.frame_RegistrarEmpresa, bg= 'gray90')
        self.frame_tabla_mar.place(x=550, y = 360)		
        self.tabla_mar = ttk.Treeview(self.frame_tabla_mar) 
        self.tabla_mar.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_mar, orient = 'horizontal', command= self.tabla_mar.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_mar, orient ='vertical', command = self.tabla_mar.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_mar.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_mar.column('#0', minwidth=100, width=100, anchor='center')
        self.tabla_mar['columns'] = ( 'Tipo', 'Empresa')
        self.tabla_mar.column('Tipo', minwidth=100, width=130 , anchor='center')
        self.tabla_mar.column('Empresa', minwidth=100, width=120 , anchor='center')
    
        self.tabla_mar.heading('#0', text='Nombre', anchor ='center')
        self.tabla_mar.heading('Tipo', text='Tipo', anchor ='center')
        self.tabla_mar.heading('Empresa', text='Empresa', anchor ='center')
        self.tabla_mar.bind("<<TreeviewSelect>>", self.obtener_fila_cp)

    # ***Tabla EMPRESAS ***

        Label(self.frame_RegistrarEmpresa, text= 'Lista de empresas', bg='ghost white', fg= 'Purple', font= ('Comic Sans MS', 14, 'bold')).place(x = 630, y = 40)

        self.frame_tabla_emp = Frame(self.frame_RegistrarEmpresa, bg= 'gray90')
        self.frame_tabla_emp.place(x=550, y = 80)		
        self.tabla_emp = ttk.Treeview(self.frame_tabla_emp) 
        self.tabla_emp.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_emp, orient = 'horizontal', command= self.tabla_emp.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_emp, orient ='vertical', command = self.tabla_emp.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_emp.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_emp.column('#0', minwidth=100, width=170, anchor='center')
        self.tabla_emp['columns'] = ( 'Telefono')
        self.tabla_emp.column('Telefono', minwidth=100, width=170 , anchor='center')
    
        self.tabla_emp.heading('#0', text='Nombre', anchor ='center')
        self.tabla_emp.heading('Telefono', text='Telefono', anchor ='center')
        self.tabla_emp.bind("<<TreeviewSelect>>", self.obtener_fila_cp)

######################## INVENTARIO ##############################

        Label(self.frame_inventario, text= 'Inventario', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 410, y = 0)
        
        Label(self.frame_inventario, text= 'Lista de Productos', bg='ghost white', fg= 'maroon', font= ('Helvica', 14, 'bold')).place(x = 400, y = 60)

        self.frame_tabla_productos = Frame(self.frame_inventario, bg= 'gray90')
        self.frame_tabla_productos.place(x=20, y = 100)		
        self.tabla_productos = ttk.Treeview(self.frame_tabla_productos) 
        self.tabla_productos.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_productos, orient = 'horizontal', command= self.tabla_productos.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_productos, orient ='vertical', command = self.tabla_surcursal.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_productos.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_productos['columns'] = ( 'Nombre', 'Contenido', 'UM', 'Presentación', 'Marca', 'Dimension')
        self.tabla_productos.column('#0', minwidth=60, width=160, anchor='center')
        self.tabla_productos.column('Nombre', minwidth=100, width=180, anchor='center')
        self.tabla_productos.column('Contenido', minwidth=50, width=105 , anchor='center')
        self.tabla_productos.column('UM', minwidth=40, width=70 , anchor='center')
        self.tabla_productos.column('Presentación', minwidth=100, width=170 , anchor='center')
        self.tabla_productos.column('Marca', minwidth=90, width=100 , anchor='center')
        self.tabla_productos.column('Dimension', minwidth=80, width=95 , anchor='center')
    
        self.tabla_productos.heading('#0', text='ID', anchor ='center')
        self.tabla_productos.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla_productos.heading('Contenido', text='Contenido', anchor ='center')
        self.tabla_productos.heading('UM', text='UM', anchor ='center')
        self.tabla_productos.heading('Presentación', text='Presentación', anchor ='center')
        self.tabla_productos.heading('Marca', text='Marca', anchor ='center')
        self.tabla_productos.heading('Dimension', text='Dimension', anchor ='center')
        self.tabla_productos.bind("<<TreeviewSelect>>", self.obtener_fila_cp) 

        Label(self.frame_inventario, text= 'Escribe el código de barras: ', bg='ghost white', fg= 'purple', font= ('Helvica', 14, 'bold')).place(x = 70, y = 380)
        Entry(self.frame_inventario, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 340, y = 380)
        Button(self.frame_inventario, command = self.buscar_Producto, text='Buscar', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x = 580, y = 375)
        
        Button(self.frame_inventario, command = self.pantalla_registrar_prod, text='Registrar Producto', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x = 280, y = 475)
        #Button(self.frame_inventario, command = self.buscar_Producto, text='Modificar Producto', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x = 485, y = 475)

        # *** Pantalla Registrar Productos ***
        
        Label(self.frame_regProd, text= 'Registrar Productos', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 400, y = 0)

        Label(self.frame_regProd, text = 'Código de barras: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 65)
        Label(self.frame_regProd, text = 'Nombre: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 100) 
        Label(self.frame_regProd, text = 'Contenido: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 135) 
        Label(self.frame_regProd, text = 'Unidad de medida: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 170) 
        Label(self.frame_regProd, text = 'Presentación: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 210) 
        Label(self.frame_regProd, text = 'Marca: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 245) 
        Label(self.frame_regProd, text = 'Dimension: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 280) 


        Entry(self.frame_regProd, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 65)
        Entry(self.frame_regProd, textvariable = self.nom_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 100)
        Entry(self.frame_regProd, textvariable = self.contenido_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 135)
        self.my_combobox_umedida=tkk.Combobox(self.frame_regProd,width=18, font=('Helvica', 14), state="readonly")
        self.my_combobox_umedida.place(x=230, y = 170)
        self.opcionesMedida=['ml','l','g','kg']
        self.my_combobox_umedida.set(self.opcionesMedida[0])
        self.my_combobox_umedida['values']=self.opcionesMedida
        self.my_combobox_umedida.bind("<<ComboboxSelected>>", self.onSeleccionOrientacion)
        Entry(self.frame_regProd, textvariable = self.presentacion_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 210)
        Entry(self.frame_regProd, textvariable = self.id_marca_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 245)
        Entry(self.frame_regProd, textvariable = self.id_dimen_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 280)
   
        Button(self.frame_regProd, command = self.registrarProductos, text='Registrar Producto', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x = 560, y = 195)
        Button(self.frame_regProd, command = self.buscar_Producto, text='Buscar Producto', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x = 560, y = 65)
        Button(self.frame_regProd, command = self.modificar_producto, text='Modificar Producto', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x =560, y = 125)

        self.frame_tabla_mar_prod = Frame(self.frame_regProd, bg= 'gray90')
        self.frame_tabla_mar_prod.place(x=550, y = 350)		
        self.tabla_mar_pro = ttk.Treeview(self.frame_tabla_mar_prod) 
        self.tabla_mar_pro.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_mar_prod, orient = 'horizontal', command= self.tabla_mar_pro.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_mar_prod, orient ='vertical', command = self.tabla_mar_pro.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_mar_pro.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_mar_pro.column('#0', minwidth=60, width=100, anchor='center')
        self.tabla_mar_pro['columns'] = ( 'Tipo', 'Empresa')
        self.tabla_mar_pro.column('Tipo', minwidth=50, width=90 , anchor='center')
        self.tabla_mar_pro.column('Empresa', minwidth=50, width=120 , anchor='center')
    
        self.tabla_mar_pro.heading('#0', text='Nombre', anchor ='center')
        self.tabla_mar_pro.heading('Tipo', text='Tipo', anchor ='center')
        self.tabla_mar_pro.heading('Empresa', text='Empresa', anchor ='center')
        self.tabla_mar_pro.bind("<<TreeviewSelect>>", self.obtener_fila_cp)

######################## ACOMODO DE PRODUCTOS ##############################

        Label(self.frame_acomodoProductos, text= 'Acomodo de  Productos', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 310, y = 0)
        
        Label(self.frame_acomodoProductos, text= 'Máximo: ',fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 65)
        Label(self.frame_acomodoProductos, text = 'Mínimo: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 100)
        Label(self.frame_acomodoProductos, text = 'Id tienda: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 135) 
        

        Entry(self.frame_acomodoProductos, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 65)
        Entry(self.frame_acomodoProductos, textvariable = self.nom_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 100)
        Entry(self.frame_acomodoProductos, textvariable = self.contenido_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 135)
######################## Control de ventas ##############################

        Label(self.frame_controlVentas, text= 'Control de ventas', bg='ghost white', fg= 'maroon3', font= ('Comic Sans MS', 20, 'bold')).place(x = 350, y = 0)
        #Button(self.frame_regProd, command = self.registrarProductos, text='", fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2").place(x = 560, y = 195)

        Label(self.frame_controlVentas, text= 'Fecha: ',fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 65)
        Label(self.frame_controlVentas, text = 'Atendio: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 100)
        Label(self.frame_controlVentas, text = 'Id tienda: ', fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 135) 
        Label(self.frame_controlVentas, text = "Descripción: ", fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 170) 
        Label(self.frame_controlVentas, text = "Código de barras: ", fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 210) 
        Label(self.frame_controlVentas, text = "Cantidad: ", fg='navy', bg ='ghost white', font=('Helvica',14,'bold')).place(x = 30, y = 245) 


        Entry(self.frame_controlVentas, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 65)
        Entry(self.frame_controlVentas, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 100)
        Entry(self.frame_controlVentas, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 135)
        Entry(self.frame_controlVentas, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 170)
        Entry(self.frame_controlVentas, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 210)
        Entry(self.frame_controlVentas, textvariable = self.codbar_pro, font=('Helvica', 14), highlightbackground = "DarkOrchid1", highlightcolor= "palevioletred", highlightthickness = 2).place(x = 230, y = 245)


        Button(self.frame_controlVentas, command = self.buscar_Producto, text='Añadir', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2", width=25).place(x = 90, y =310)
        Button(self.frame_controlVentas, command = self.buscar_Producto, text='Registrar', fg='white', font=('Helvica',14, 'bold'), bg='DarkOrchid3', cursor="hand2", width=25).place(x = 90, y =360)


        self.frame_tabla_ventas = Frame(self.frame_controlVentas, bg= 'gray90')
        self.frame_tabla_ventas.place(x=550, y = 65)		
        self.tabla_ven = ttk.Treeview(self.frame_tabla_ventas) 
        self.tabla_ven.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_tabla_ventas, orient = 'horizontal', command= self.tabla_ven.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_ventas, orient ='vertical', command = self.tabla_ven.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_ven.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla_ven.column('#0', minwidth=60, width=100, anchor='center')
        self.tabla_ven['columns'] = ( 'Descuento', 'Precio')
        self.tabla_ven.column('Descuento', minwidth=50, width=120 , anchor='center')
        self.tabla_ven.column('Precio', minwidth=50, width=120 , anchor='center')

        self.tabla_ven.heading('#0', text='Cantidad', anchor ='center')
        self.tabla_ven.heading('Descuento', text='Descuento', anchor ='center')
        self.tabla_ven.heading('Precio', text='Precio', anchor ='center')
        self.tabla_ven.bind("<<TreeviewSelect>>", self.obtener_fila_cp)

        

##### Funciones#####
    def onSeleccionOrientacion(self,event):
        self.orientacion_tie = self.my_combobox_orientacion.get()



# ---------  Ciudad --------
    def datos_totales_ciudad(self):
        datos = self.Ciudad.listarCiudades()
        self.tabla_ciudad.delete(*self.tabla_ciudad.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_ciudad.insert('',i, text = datos[i][0:1:2], values= datos[i][1:6])
    
    def obtener_fila_ciudad(self, event):
        current_item = self.tabla_ciudad.focus()
        if not current_item:
            return
        data = self.tabla_ciudad.item(current_item)
        self.nombre_borrar = data['values'][0]


    def agregar_ciudad(self):
        nombre = self.nom_ciu.get()
        lada = self.lada_ciu.get()
        datos = (nombre, lada)

        if  nombre and lada !='':
            self.tabla_cp.insert('',0, text = nombre, values= datos)
            self.Ciudad.registrarCiudad(nombre, lada)
            mb.showinfo("Mensaje", "¡Datos Guardados con éxito!")						
        else:
            mb.showinfo("Mensaje", "Ingrese todos los datos")						

    
    def limpiar_datos_ciudad(self):
        self.nom_ciu.set('')
        self.lada_ciu.set('')
        self.buscar_ciu.set('')
    
    def limpiarTablaCiudad(self):
        for item in self.tabla_ciudad.get_children():
            self.tabla_ciudad.delete(item)

    def limpiarTablaCiudadCP(self):
        for item in self.tabla_ciudadp.get_children():
            self.tabla_ciudadp.delete(item)

    def buscar_ciudad(self):
        self.limpiarTablaCiudad()
        nombre = self.buscar_ciu.get()
        #nombre = str("'" + nombre + "'")
        nombre_buscado = self.Ciudad.buscarCiudad(nombre)
        if nombre_buscado == []:
            mb.showinfo("Mensaje", "Lo sentimos, \n esa ciudad no existe")
        else:
            i = -1
            for dato in nombre_buscado:
                i= i+1
                self.tabla_ciudad.insert('',i, text = nombre_buscado[i][0:1:2], values=nombre_buscado[i][1:6])
                self.nom_ciu.set(nombre_buscado[i][1])
                self.lada_ciu.set(nombre_buscado[i][2])
        
        #self.limpiar_datos_ciudad()
   
    def modificar_tabla_ciudad(self):	
        #Id = self.id.get() 	
        nombre = self.nom_ciu.get()
        lada = self.lada_ciu.get()
        self.Ciudad.modificarCiudad( nombre, lada)		
        mb.showinfo("Mensaje", "Datos actualizados con éxito")
        self.limpiar_datos_ciudad()
        self.datos_totales_ciudad()

    
#------------------ CP --------------------
    def datos_totales_cp(self):
        datos = self.CodigoPostal.listarCodigos()
        self.tabla_cp.delete(*self.tabla_cp.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_cp.insert('',i, text = datos[i][0:1], values = datos[i][1:6])
    
    def datos_totales_ciudad_cp(self):
        datos = self.Ciudad.listarCiudades()
        self.tabla_ciudadp.delete(*self.tabla_ciudadp.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_ciudadp.insert('',i, text = datos[i][0:1:2], values = datos[i][1:6])
    
    def obtener_fila_cp(self, event):
        current_item = self.tabla_cp.focus()
        if not current_item:
            return
        data = self.tabla_cp.item(current_item)
        self.nombre_borrar = data['values'][0]


    def agregar_datos_cp(self):
        codigo = self.cp.get()
        ciudad = self.ciudad_cp.get()
        id_ciu = self.CodigoPostal.buscarIdCiudad(ciudad)
        datos = (codigo, ciudad)
        if codigo and ciudad !='':
            self.tabla_cp.insert('',0, text = codigo, values= ciudad)
            self.CodigoPostal.registrarCodigo(codigo, id_ciu)
            mb.showinfo("Mensaje","Dato insertado")

    
    def limpiar_datos_cp(self):
        self.cp.set('')
        self.ciudad_cp.set('')
    
    def limpiarTablaCp(self):
        for item in self.tabla_cp.get_children():
            self.tabla_cp.delete(item)

    def buscar_cp(self):
        self.limpiarTablaCp()
        cp_cod = self.busca_cp.get()
        cp_cod = int(cp_cod)
        cp_cod_buscado = self.CodigoPostal.buscarCodigo(cp_cod)

        if cp_cod_buscado == []:
            mb.showinfo("Mensaje","Dato no encontrado")
        i = -1
        for dato in cp_cod_buscado:
            i= i+1
            self.tabla_cp.insert('',i, text = cp_cod_buscado[i][0:1], values=cp_cod_buscado[i][1:6])
        
        self.cp.set(cp_cod_buscado[i][0])
        self.ciudad_cp.set(cp_cod_buscado[i][1])
           
        #self.limpiar_datos_ciudad()

    def buscar_ciudad_cp(self):
        self.limpiarTablaCiudadCP()
        nombre = self.buscar_ciu.get()
        #nombre = str("'" + nombre + "'")
        nombre_buscado = self.Ciudad.buscarCiudad(nombre)
        if nombre_buscado == []:
            mb.showinfo("Mensaje", "Lo sentimos, \n esa ciudad no existe")
        else:
            i = -1
            for dato in nombre_buscado:
                i= i+1
                self.tabla_ciudadp.insert('',i, text = nombre_buscado[i][0:1:2], values=nombre_buscado[i][1:6])
                self.ciudad_cp.set(nombre_buscado[i][1])
                #self.lada_ciu.set(nombre_buscado[i][2])

    ''''
    def modificar_tabla_cp(self):	
        #Id = self.id.get() 	
        cp = self.cp.get()
        ciudad = self.ciudad_cp.get()
        self.CodigoPostal.modificarCodigo(cp, ciudad)		
        mb.showinfo("Mensaje", "Datos actualizados con éxito")
        self.limpiar_datos_ciudad()
    '''

    #------------------ COLONIAS --------------------

    def datos_totales_col(self):
        datos = self.Colonia.listarColonias()
        self.tabla_col.delete(*self.tabla_col.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_col.insert('',i, text = datos[i][0:1:2], values = datos[i][1:6])
    
    def datos_totales_cp_col(self):
        datos = self.CodigoPostal.listarCodigos()
        self.tabla_cp_col.delete(*self.tabla_cp_col.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_cp_col.insert('',i, text = datos[i][0:1:2], values = datos[i][1:6])
    
    def obtener_fila_colonis(self, event):
        current_item = self.tabla_col.focus()
        if not current_item:
            return
        data = self.tabla_col.item(current_item)
        self.nombre_borrar = data['values'][0]
        
    
    def agregar_datos_colonia(self):
        nombre = self.nombre_col.get()
        cp = self.cp_col.get()
        datos = (nombre, cp)
        if cp and nombre != '':
            self.tabla_col.insert( '',0, text = nombre, values = datos)
            self.Colonia.registrarColonia(nombre, cp)
            mb.showinfo("Mensaje","Dato insertado")

    
    def limpiar_datos_colonia(self):
        self.nombre_col.set('')
        self.cp_col.set('')
    
    def limpiarTablaColonia(self):
        for item in self.tabla_col.get_children():
            self.tabla_col.delete(item)
    
    def limpiarTablaColonia_cp(self):
        for item in self.tabla_cp_col.get_children():
            self.tabla_cp_col.delete(item)

    def buscar_colonia(self):
        self.limpiarTablaColonia()
        nombre = self.busca_col.get()
        #nombre = str("'" + nombre + "'")
        nombre_buscado = self.Colonia.buscarColonia(nombre)
        if nombre_buscado == []:
            mb.showinfo("Mensaje", "Lo sentimos, \n esa ciudad no existe")
        else:
            i = -1
            for dato in nombre_buscado:
                i= i+1
                self.tabla_col.insert('',i, text = nombre_buscado[i][0:1:2], values=nombre_buscado[i][1:6])
            
                self.nombre_col.set(nombre_buscado[i][1])
                self.cp_col.set(nombre_buscado[i][2])
    

    def buscar_cp_col(self):
        self.limpiarTablaColonia_cp()
        cp_cod = self.busca_cp.get()
        cp_cod = int(cp_cod)
        cp_cod_buscado = self.CodigoPostal.buscarCodigo(cp_cod)

        if cp_cod_buscado == []:
            mb.showinfo("Mensaje","Dato no encontrado")
        i = -1
        for dato in cp_cod_buscado:
            i= i+1
            self.tabla_cp_col.insert('',i, text = cp_cod_buscado[i][0:1], values=cp_cod_buscado[i][1:6])
        
            self.nombre_col.set(cp_cod_buscado[i][1])
            self.cp_col.set(cp_cod_buscado[i][0])
    

#------------------ SUCURSALES --------------------

    def datos_totales_sucursales(self):
        datos = self.Surcursal.listarSucursales()
        self.tabla_surcursal.delete(*self.tabla_surcursal.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_surcursal.insert('',i, text = datos[i][0:1], values = datos[i][1:8])
    
    def datos_totales_col_sur(self):
        datos = self.Colonia.listarColonias()
        self.tabla_col_sur.delete(*self.tabla_col_sur.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_col_sur.insert('',i, text = datos[i][0:1:2], values = datos[i][1:6])
    
    def listar_dimensiones(self):
        datos = self.Dimension.listarDimension()
        self.tabla_dim.delete(*self.tabla_dim.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_dim.insert('',i, text = datos[i][0:1], values = datos[i][1:8])
    
    def listar_dimen_sur(self):
        datos = self.Dimension.listarDimension()
        self.tabla_dim_sur.delete(*self.tabla_dim.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_dim_sur.insert('',i, text = datos[i][0:1], values = datos[i][1:8])
    

    def registrarDimenTien(self):
        alto = self.alto.get()
        largo = self.largo.get()
        ancho = self.ancho.get()
        datos = (alto, largo, ancho)

        if  alto and largo and ancho !='':
            self.tabla_dim_sur.insert('',0, text = alto, values= datos)
            self.Dimension.registrarDimenTienda(alto, largo, ancho)
            mb.showinfo("Mensaje", "¡Datos Guardados con éxito!")						
        else:
            mb.showinfo("Mensaje", "Ingrese todos los datos")	

        self.listar_dimen_sur()					


    def agregar_datos_surcursal(self):
        calle = self.calle_tie.get()
        num = self.num_tie.get()
        orientacion = self.my_combobox_orientacion.get()
        entrecalles = self.entrecalles_tie.get()
        tel = self.tel_tie.get()
        colonia = self.id_col_tie.get()
        id_dimen = self.id_dimen_tie.get()

        id_col = self.Surcursal.buscarIdColonia(colonia)

        if calle and num and orientacion and entrecalles and tel and  colonia and id_dimen !='':
 
            self.Surcursal.registrarSucursal(calle, num, orientacion, entrecalles, tel, id_col, id_dimen)
            mb.showinfo("Mensaje","Dato insertado")
    

    def buscar_Sucursal(self):
        #self.limpiarTablaSucursal()
        id = self.id_tie.get()
        #nombre = str("'" + nombre + "'")
        nombre_buscado = self.Surcursal.buscarSucursal(id)
        if nombre_buscado == []:
            mb.showinfo("Mensaje", "Lo sentimos, \n esa ciudad no existe")
        else:
            i = -1
            for dato in nombre_buscado:
                i= i+1
                #self.tabla_surcursal.insert('',i, text = nombre_buscado[i][0:1], values=nombre_buscado[i][1:8])
            
                
                self.calle_tie.set(nombre_buscado[i][1])
                self.num_tie.set(nombre_buscado[i][2])
                self.my_combobox_orientacion.set(nombre_buscado[i][3])
                self.entrecalles_tie.set(nombre_buscado[i][4])
                self.tel_tie.set(nombre_buscado[i][5])
                self.id_col_tie.set(nombre_buscado[i][6])
                self.id_dimen_tie.set(nombre_buscado[i][7])
    
    def limpiarTablaSucursal(self):
        for item in self.tabla_surcursal.get_children():
            self.tabla_surcursal.delete(item)
    
    def limpiar_datos_Sucursal(self):
        self.calle_tie.set('')
        self.num_tie.set('')
        self.my_combobox_orientacion.set([0])
        self.entrecalles_tie.set('')
        self.tel_tie.set('')
        self.id_col_tie.set('')
        self.id_dimen_tie.set('')
    
    def modificar_tabla_Sucursal(self):	
        calle = self.calle_tie.get()
        num = self.num_tie.get()
        orientacion = self.my_combobox_orientacion.get()
        entrecalles = self.entrecalles_tie.get()
        tel = self.tel_tie.get()
        colonia = self.id_col_tie.get()
        id_dimen = self.id_dimen_tie.get()

        id_tie = self.id_tie.get()

        id_col = self.Surcursal.buscarIdColonia(colonia)

        self.Surcursal.modificarSucursal(id_tie, calle, num, orientacion, entrecalles, tel, id_col, id_dimen)		
        mb.showinfo("Mensaje", "Datos actualizados con éxito")
        self.limpiar_datos_ciudad()
        self.datos_totales_sucursales()
  
  #------------------ Productos --------------------

    def datos_totales_productos(self):
        datos = self.Inventario.listarProductos()
        self.tabla_productos.delete(*self.tabla_productos.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_productos.insert('',i, text = datos[i][0:1], values = datos[i][1:7])
    
    def registrarProductos(self):
        codbar = self.codbar_pro.get()
        nombre = self.nom_pro.get()
        umedida = self.umedida_pro.get()
        presentacion = self.presentacion_pro.get()
        marca = self.id_marca_pro.get()
        dimension = self.id_marca_pro.get()
        datos = (codbar, nombre, umedida, presentacion, marca, dimension)

        if  codbar and nombre and umedida and presentacion and marca and dimension !='':
            self.tabla_dim_sur.insert('',0, text = codbar, values= datos)
            self.Inventario.registrarProducto(codbar, nombre, umedida, presentacion, marca, dimension)
            mb.showinfo("Mensaje", "¡Datos guardados con éxito!")						
        else:
            mb.showinfo("Mensaje", "Ingrese todos los datos")	

        self.listar_dimen_sur()		

    def limpiarTablaProductos(self):
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

    def buscar_Producto(self):
        self.limpiarTablaProductos()
        codbar = self.codbar_pro.get()

        codbar_buscado = self.Inventario.buscarProducto(codbar)

        if codbar_buscado == []:
            mb.showinfo("Mensaje","Dato no encontrado")
        i = -1
        for dato in codbar_buscado:
            i= i+1
            self.tabla_productos.insert('',i, text = codbar_buscado[i][0:1], values=codbar_buscado[i][1:7])

            
            self.codbar_pro.set(codbar_buscado[i][0])
            self.nom_pro.set(codbar_buscado[i][1])
            self.contenido_pro.set(codbar_buscado[i][2])
            self.my_combobox_umedida.set(codbar_buscado[i][3])
            self.presentacion_pro.set(codbar_buscado[i][4])
            self.id_marca_pro.set(codbar_buscado[i][5])
            self.id_dimen_pro.set(codbar_buscado[i][6])
       

    def modificar_producto(self):	
        codbar = self.codbar_pro.get()
        #self.Inventario.buscarProducto(codbar)
        nombre = self.nom_pro.get()
        cantidad =self.contenido_pro.get()
        umedida = self.umedida_pro.get()
        presentacion = self.presentacion_pro.get()
        marca = self.Inventario.buscarIdMarca(self.id_marca_pro.get())

        dimension = self.id_dimen_pro.get()

        self.Inventario.modificarProducto(codbar, nombre, cantidad, umedida, presentacion, marca, dimension)		
        mb.showinfo("Mensaje", "Datos actualizados con éxito")
        #self.limpiar_datos_ciudad()
        #self.datos_totales_sucursales()

    def datos_totales_marcas(self):
        datos = self.Inventario.listarMarcas()
        self.tabla_mar_pro.delete(*self.tabla_mar_pro.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_mar_pro.insert('',i, text = datos[i][0:1], values= datos[i][1:3])


    ##  CONTRATO ###
    def registrarContrato(self):
        ap = self.ap.get()
        am = self.am.get()
        nombre = self.nombre.get()
        genero = self.my_combobox_genero.get()
        fnac = self.Contrato.fechasString(self.fnac.get())
        tel = self.tel.get()
        mail = self.mail.get() 
        edocivil = self.my_combobox_edoCivil.get()
        calle = self.calle.get()
        num = self.num.get()  
        orientacion = self.my_combobox_orientacion.get()
        entrecalles = self.entreca.get()
        colonia = self.my_combobox_colonias.get()
        fi = self.Contrato.fechasString(self.fi.get())
        ff = self.Contrato.fechasString(self.ff.get())
        puesto = self.puesto.get() 
        sueldo = self.sueldo.get() 
        hi = self.hi.get()
        hs = self.hf.get()
        tienda = self.my_combobox_tiendas.get()

        if  ap and am and nombre and genero and fnac and tel and mail and edocivil and calle and num and orientacion and entrecalles and colonia and fi and ff and puesto and sueldo and hi and hs and tienda !='':
            self.Contrato.TransaccionContrato(ap, am, nombre, genero, fnac, tel, mail, edocivil, calle, num, 
                            orientacion, entrecalles, colonia, fi, ff, puesto, sueldo, hi, hs, tienda)
            mb.showinfo("Mensaje", "¡Datos guardados con éxito!")						
        else:
            mb.showinfo("Mensaje", "Ingrese todos los datos")	
    
    def datos_totales_per(self):
        datos = self.Contrato.listarPersonal()
        self.tabla_per.delete(*self.tabla_per.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_per.insert('',i, text = datos[i][0:14], values= datos[i][1:14])
    
    def limpiar_datos_Emp(self):
        self.nombre_emp.set('')
        self.tel_emp.set('')
    
    def limpiar_datos_Marca(self):
        self.nom_mar.set('')
        self.my_combobox_TipoMarca.set(self.opcionesTipoMarca[0])
        self.my_combobox_nomEmpresas.set(self.opcionesEmpresas[0])

    
    def registrarEmpresa(self):
        nombre = self.nombre_emp.get()
        telefono = self.tel_emp.get()
        datos = (nombre, telefono)
        if nombre and telefono !='':
            self.Empresa.registrarEmpresa(nombre, telefono)
            #self.tabla_cp.insert('',0, text = codigo, values= ciudad)
            mb.showinfo("Mensaje","Dato insertado")
        else:
            mb.showinfo("Mensaje", "Ingrese todos los datos")	
        
        self.limpiar_datos_Emp()
        self.listarEmpresas()

    def registrarMarca(self):
        nombre = self.nom_mar.get()
        tipo = self.my_combobox_TipoMarca.get()
        empresa = self.my_combobox_nomEmpresas.get()

        #datos = (nombre, telefono)
       
        if nombre and tipo and empresa !='':
            self.Empresa.registrarMarca(nombre, tipo, empresa)
            #self.tabla_cp.insert('',0, text = codigo, values= ciudad)
            mb.showinfo("Mensaje","Dato insertado")
        else:
            mb.showinfo("Mensaje", "Ingrese todos los datos")	
        
        self.limpiar_datos_Marca()
        self.listarMarcas()

    def listarEmpresas(self):
        datos = self.Empresa.listarEmpresa()
        self.tabla_emp.delete(*self.tabla_emp.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_emp.insert('',i, text = datos[i][1], values = datos[i][2:3])
    
    def listarMarcas(self):
        datos = self.Empresa.listarMarcas()
        self.tabla_mar.delete(*self.tabla_mar.get_children())
        i = -1
        for dato in datos:
            i= i+1
            self.tabla_mar.insert('',i, text = datos[i][0:1], values = datos[i][1:3])


if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Cadena de Tienditas')
    ventana.minsize(height= 475, width=795)
    ventana.geometry('1000x680+180+80')
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))	
    app = Ventana(ventana)
    app.mainloop()
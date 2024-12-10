import mysql.connector
import time

# -------- Ciudad -------
class TablaCiudad(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Fallo al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchall()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()

    def listarCiudades(self):
        sql = f"SELECT * FROM ciudad;"
        a = self.ejecutar(sql, "listar")
        ciudades = []
        for i in range(0, len(a)):
            ciudad = []
            b = 0
            for at in a[i]:
                if b == 0:
                    ciudad.append(at)
                elif b == 1:
                    ciudad.append(at)
                elif b == 2:
                    ciudad.append(at) 
                b += 1
            ciudades.append(ciudad)
        return ciudades
    
    def buscarCiudad(self, nom_ciu):
        sql=f"SELECT * FROM ciudad WHERE nom_ciu= '{nom_ciu}';"
        a = self.ejecutar(sql, "buscar")
        ciudad = []
        b = 0
        for at in a:
            if b == 0:
                ciudad.append(at)
            elif b == 1:
                ciudad.append(at) 
            elif b == 2:
                ciudad.append(at)
            b += 1
        return ciudad
    
    def existeCiudad(self, nom_ciu):
        sql=f"SELECT * FROM ciudad WHERE nom_ciu= '{nom_ciu}';"
        a = self.ejecutar(sql,"buscar")
        if a == None:
            return False
        else:
            return True

    def registrarCiudad(self, nom_ciu , lada_ciu):
        sql = f"INSERT INTO ciudad VALUES(null,'{nom_ciu}',{lada_ciu});" 
        self.myCursor.execute(sql) 
        self.con.commit()

    def modificarCiudad(self, nom_ciu , lada_ciu):
        sql = f"UPDATE ciudad SET  lada_ciu = {lada_ciu} WHERE nom_ciu = '{nom_ciu}';"
        self.myCursor.execute(sql) 
        a = self.myCursor.rowcount
        self.con.commit()
        return a
    
    def nombresCiudades(self):
        nombres = self.ejecutar("select nom_ciu from ciudad","listar")
        if(nombres!= []):
            return nombres
        else:
            return 0
    


# -------- Codigo -------
class TablaCodigo(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Falló al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchone()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()

    def listarCodigos(self):
        sql = "SELECT cp_cod, nom_ciu FROM codigo join ciudad on codigo.id_ciu = ciudad.id_ciu"
        a = self.ejecutar(sql, "listar")
        codigos = []
        for i in range(0, len(a)):
            cod = []
            b = 0
            for at in a[i]:
                if b == 0:
                    cod.append(at)
                elif b == 1:
                    cod.append(at)
                b += 1
            codigos.append(cod)
        return codigos
    
    def buscarCodigo(self, cp_cod):
        sql=f"SELECT * FROM codigo WHERE cp_cod= {cp_cod};"
        sql2 = f"SELECT cp_cod, nom_ciu FROM codigo join ciudad on codigo.id_ciu = ciudad.id_ciu WHERE cp_cod= {cp_cod};"

        a = self.ejecutar(sql, "buscar")
        a = self.ejecutar(sql2, "listar")
        cod = []
        b = 0
        for at in a:
            if b == 0:
                cod.append(at)
            elif b == 1:
                cod.append(at) 
            b += 1
        return cod
    
    def existeCodigo(self, cp_cod):
        sql=f"SELECT * FROM codigo WHERE cp_cod= {cp_cod};"
        a = self.ejecutar(sql,"buscar")
        if a == None:
            return False
        else:
            return True

    def registrarCodigo(self, cp_cod, id_ciu):
        sql = f"INSERT INTO codigo VALUES({cp_cod},{id_ciu});" 
        self.myCursor.execute(sql) 
        self.con.commit()


    def buscarIdCiudad(self, nom_ciu):
        sql = f"select id_ciu from ciudad  where nom_ciu = '{nom_ciu}';"
        a = self.ejecutar(sql, "buscar")
        cod = []
        b = 0
        for at in a:
            if b == 0:
                return at
        

    '''''
    def modificarCodigo(self, cp_cod, id_ciu):
        sql = f"UPDATE codigo SET  id_ciu = {id_ciu} WHERE cp_cod = {cp_cod};"
        self.myCursor.execute(sql) 
        self.con.commit()
    '''



# -------- Colonia -------
class TablaColonia(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Falló al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchone()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()

    def listarColonias(self):
        sql = f"SELECT * FROM colonia;"
        a = self.ejecutar(sql, "listar")
        colonias = []
        for i in range(0, len(a)):
            colonia = []
            b = 0
            for at in a[i]:
                if b == 0:
                    colonia.append(at)
                elif b == 1:
                    colonia.append(at)
                elif b == 2:
                    colonia.append(at)
                b += 1
            colonias.append(colonia)
        return colonias
    
    def buscarColonia(self, nom_col):
        sql=f"SELECT * FROM colonia WHERE nom_col= '{nom_col}';"
        a = self.ejecutar(sql, "buscar")
        col = []
        b = 0
        for at in a:
            if b == 0:
                col.append(at)
            elif b == 1:
                col.append(at) 
            elif b == 2:
                col.append(at)
            b += 1
        return col
    
    def existeColonia(self, nom_col):
        sql=f"SELECT * FROM colonia WHERE nom_col = '{nom_col}';"
        a = self.ejecutar(sql,"buscar")
        if a == None:
            return False
        else:
            return True

    def registrarColonia(self, nom_col, cp_cod):
        sql = f"INSERT INTO colonia VALUES(null,'{nom_col}', {cp_cod});" 
        self.myCursor.execute(sql) 
        self.con.commit()


    def modificarColonia(self,  nom_col, cp_cod):
        sql = f"UPDATE colonia SET  cp_cod = {cp_cod} WHERE id_col = '{nom_col}';"
        self.myCursor.execute(sql) 
        self.con.commit()
    
class TablaTienda(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Fallo al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchall()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()

    def listarSucursales(self):
        sql = f"SELECT tienda.id_tie, calle_tie, num_tie, orientacio_tie, entrecalles_tie, tel_tie, nom_col, id_dimen FROM tienda join colonia on colonia.id_col = tienda.id_col;"
        a = self.ejecutar(sql, "listar")
        sucursales = []
        for i in range(0, len(a)):
            tienda = []
            b = 0
            for at in a[i]:
                if b == 0:
                    tienda.append(at)
                elif b == 1:
                    tienda.append(at)
                elif b == 2:
                    tienda.append(at) 
                elif b == 3:
                    tienda.append(at)
                elif b == 4:
                    tienda.append(at)
                elif b == 5:
                    tienda.append(at)
                elif b == 6:
                    tienda.append(at)
                elif b == 7:
                    tienda.append(at)
                b += 1
            sucursales.append(tienda)
        return sucursales
    
    def buscarSucursal(self, id_tie):
        sql=f"SELECT id_tie, calle_tie, num_tie, orientacio_tie, entrecalles_tie, tel_tie, nom_col, id_dimen FROM tienda join colonia on tienda.id_col = colonia.id_col WHERE id_tie= {id_tie};"
        a = self.ejecutar(sql, "buscar")
        tienda = []
        b = 0
        for at in a:
            if b == 0:
                tienda.append(at)
            elif b == 1:
                tienda.append(at) 
            elif b == 2:
                tienda.append(at)
            elif b == 3:
                tienda.append(str(at))
            elif b == 4:
                tienda.append(at)
            elif b == 5:
                tienda.append(at)
            elif b == 6:
                tienda.append(at)
            elif b == 7:
                tienda.append(at)
            b += 1
        return tienda
    
    def existeSucursal(self, id_tie):
        sql=f"SELECT * FROM tienda WHERE id_tie= {id_tie};"
        a = self.ejecutar(sql,"buscar")
        if a == None:
            return False
        else:
            return True

    def registrarSucursal(self, calle_tie, num_tie, orientacion_tie, entrecalles_tie, tel_tie, id_col, id_dimen):
        sql = f"INSERT INTO tienda VALUES(null,'{calle_tie}',{num_tie}, '{orientacion_tie}', '{entrecalles_tie}', '{tel_tie}', {id_col}, {id_dimen});" 
        self.myCursor.execute(sql) 
        self.con.commit()

    def modificarSucursal(self,id_tie, calle_tie, num_tie, orientacion_tie, entrecalles_tie, tel_tie, id_col, id_dimen):
        sql = f"UPDATE tienda SET  calle_tie = '{calle_tie}', num_tie = {num_tie}, orientacio_tie = '{orientacion_tie}', entrecalles_tie='{entrecalles_tie}', tel_tie = '{tel_tie}', id_dimen = {id_dimen}, id_col = {id_col} Where id_tie = {id_tie};"
        self.myCursor.execute(sql) 
        a = self.myCursor.rowcount
        self.con.commit()
        return a

    def buscarIdColonia(self, nom_col):
        sql = f"select id_col from colonia where nom_col = '{nom_col}';"
        a = self.ejecutar(sql, "buscar")
        b = 0
        return a[0][0]
    

class TablaDimension(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Fallo al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchall()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()

    def listarDimension(self):
        sql = f"SELECT  id_dimen, alto_dimen, largo_dim,  ancho_dim, umedida_dim FROM dimension where umedida_dim = 'm' and alto_dimen > 1;"
        a = self.ejecutar(sql, "listar")
        dimensiones = []
        for i in range(0, len(a)):
            dimension = []
            b = 0
            for at in a[i]:
                if b == 0:
                    dimension.append(at)
                elif b == 1:
                    dimension.append(at)
                elif b == 2:
                    dimension.append(at) 
                elif b == 3:
                    dimension.append(at)
                elif b == 4:
                    dimension.append(at)
                b += 1
            dimensiones.append(dimension)
        return dimensiones

    def registrarDimenTienda(self, alto, largo, ancho):
        self.myCursor.callproc(f'sp_RegDimTienda({alto}, {largo}, {ancho});')
        self.con.commit()

class TablaProducto(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Fallo al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchall()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()
    
    def listarProductos(self):
        sql = f"SELECT codbar_pro, nom_pro, contenido_pro, umedida_pro, presentacion_pro, nom_mar, id_dimen FROM producto join marca on producto.id_mar = marca.id_mar;"
        a = self.ejecutar(sql, "listar")
        productos = []
        for i in range(0, len(a)):
            producto = []
            b = 0
            for at in a[i]:
                if b == 0:
                    producto.append(at)
                elif b == 1:
                    producto.append(at)
                elif b == 2:
                    producto.append(at) 
                elif b == 3:
                    producto.append(at)
                elif b == 4:
                    producto.append(at)
                elif b == 5:
                    producto.append(at)
                elif b == 6:
                    producto.append(at)
                b += 1
            productos.append(producto)
        return productos

    def registrarProducto(self, codbar, nombre, contenido, umedida, presentacion, marca, dimension):
        self.myCursor.callproc(f'sp_inserccion({codbar}, {nombre}, {contenido}, {umedida}, {presentacion}, {marca}, {dimension});')
        self.con.commit()
    
    def buscarProducto(self, codbar_pro):
        sql = f"SELECT codbar_pro, nom_pro, contenido_pro, umedida_pro, presentacion_pro, nom_mar, id_dimen FROM producto join marca on producto.id_mar = marca.id_mar WHERE codbar_pro = '{codbar_pro}';"
        a = self.ejecutar(sql, "buscar")
        producto = []
        b = 0
        for at in a:
            if b == 0:
                producto.append(at)
            elif b == 1:
                producto.append(at) 
            elif b == 2:
                producto.append(at)
            elif b == 3:
                producto.append(at)
            elif b == 4:
                producto.append(at)
            elif b == 5:
                producto.append(at)
            elif b == 6:
                producto.append(at)
            b += 1
        return producto
    
    def modificarProducto(self, codbar, nombre, contenido, umedida, presentacion, marca, dimension):

        self.myCursor.callproc(f"sp_modificar('{codbar}', '{nombre}', {contenido}, '{umedida}', '{presentacion}', {marca}, {dimension});")
        self.con.commit()

    def buscarIdMarca(self, marca):
        sql = f"SELECT marca.id_mar from marca join producto where nom_mar = '{marca}' group by nom_mar"
        a = self.ejecutar(sql, "buscar")
        b = 0
        return a[0][0]
    
    def listarMarcas(self):
        sql = f"SELECT nom_mar, tipo_mar, nom_emp FROM marca join empresa on marca.id_emp = empresa.id_emp;"
        a = self.ejecutar(sql, "listar")
        marcas = []
        for i in range(0, len(a)):
            marca = []
            b = 0
            for at in a[i]:
                if b == 0:
                    marca.append(at)
                elif b == 1:
                    marca.append(at)
                elif b == 2:
                    marca.append(at) 
                elif b == 3:
                    marca.append(at)
                elif b == 4:
                    marca.append(at)
                elif b == 5:
                    marca.append(at)
                elif b == 6:
                    marca.append(at)
                b += 1
            marcas.append(marca)
        return marcas

class TablaContrato(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Fallo al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchall()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()


    def TransaccionContrato(self, ap, am, nombre, genero, fnac, tel, mail, edocivil, calle, num, 
                            orientacion, entrecalles, colonia, fi, ff, puesto, sueldo, hi, hs, tienda):
        self.myCursor.callproc(f"sp_ContratoTransaccion('{ap}', '{am}', '{nombre}', '{genero}', '{fnac}', '{tel}', '{mail}','{edocivil}', '{calle}', {num}, '{orientacion}', '{entrecalles}', '{colonia}', '{fi}', '{ff}', '{puesto}', '{sueldo}', '{hi}', '{hs}', {tienda});")
        #self.con.commit()

    def idTiendas(self):
        sql = "SELECT id_tie FROM tienda;"
        a = self.ejecutar(sql, "listar")
        tienda = []
        for i in range(0, len(a)):

            b = 0
            for at in a[i]:
                if b == 0:
                    tienda.append(at)
             
                b += 1
        return tienda
    
    def nomColonias(self):
        sql = "SELECT nom_col FROM colonia;"
        a = self.ejecutar(sql, "listar")
        colonia = []
        for i in range(0, len(a)):

            b = 0
            for at in a[i]:
                if b == 0:
                    colonia.append(at)
             
                b += 1
        return colonia
    
    def fechasString(self, fecha):
        partes = fecha.split('/')
        a = '{}{}{}'.format(partes[2],partes[1],partes[1])
        return a
    
    def listarPersonal(self):
        sql = f"select id_per, ap_per, am_per, nom_per, genero_per, fnac_per, tel_per, mail_per, edocivil_per, calle_per, num_per, orientacion_per, entrecalles_per, nom_col from persona join colonia on persona.id_col = colonia.id_col;"
        a = self.ejecutar(sql, "listar")
        personas = []
        for i in range(0, len(a)):
            persona = []
            b = 0
            for at in a[i]:
                if b == 0:
                    persona.append(at)
                elif b == 1:
                    persona.append(at)
                elif b == 2:
                    persona.append(at) 
                elif b == 3:
                    persona.append(at)
                elif b == 4:
                    persona.append(at)
                elif b == 5:
                    persona.append(at)
                elif b == 6:
                    persona.append(at)
                elif b == 7:
                    persona.append(at)
                elif b == 8:
                    persona.append(at)
                elif b == 9:
                    persona.append(at)
                elif b == 10:
                    persona.append(at)
                elif b == 11:
                    persona.append(at)
                elif b == 12:
                    persona.append(at)
                elif b == 13:
                    persona.append(at)
                elif b == 14:
                    persona.append(at)
                b += 1
            personas.append(persona)
        return personas

class TablaEmpresa(object):
    def __init__(self, baseDatos, usuario, clave):
        self.host="localhost"
        self.database=baseDatos
        self.user=usuario
        self.password=clave
        self.port="3306"
        self.con = self.hacerConexion()
        self.myCursor=self.con.cursor()

    def hacerConexion(self): 
        try:
            return mysql.connector.connect(host="localhost", user="root", password="silverspoon", port="3306", database="TienditasCadena") 
        except :
            print("Fallo al conectar a mysql")
    
    def ejecutar(self, sentenciaSQL, opCrud):
        self.myCursor.execute(sentenciaSQL)
        if opCrud == "buscar":
            return self.myCursor.fetchall()
        if opCrud == "listar":
           return self.myCursor.fetchall()
        if opCrud == "eliminar":
           pass
        self.con.commit()
    
    def cerrarConeccion(self):
        if self.con:self.con.close()
    
    def registrarEmpresa(self, nombre, telefono):
        sql = f"INSERT INTO empresa VALUES(null,'{nombre}','{telefono}');" 
        self.myCursor.execute(sql) 
        self.con.commit()
    
    def listarEmpresa(self):
        sql = f"SELECT * FROM empresa"
        a = self.ejecutar(sql, "listar")
        empresas = []
        for i in range(0, len(a)):
            empresa = []
            b = 0
            for at in a[i]:
                if b == 0:
                    empresa.append(at)
                elif b == 1:
                    empresa.append(at)
                elif b == 2:
                    empresa.append(at) 
                elif b == 3:
                    empresa.append(at)
                b += 1
            empresas.append(empresa)
        return empresas

    def registrarMarca(self, nombre, tipo, empresa):
        self.myCursor.callproc(f"sp_agregarMarca('{nombre}', '{tipo}', '{empresa}');")
        self.con.commit()
    
    def listarMarcas(self):
        sql = f"SELECT nom_mar, tipo_mar, nom_emp FROM marca join empresa on marca.id_emp = empresa.id_emp;"
        a = self.ejecutar(sql, "listar")
        marcas = []
        for i in range(0, len(a)):
            marca = []
            b = 0
            for at in a[i]:
                if b == 0:
                    marca.append(at)
                elif b == 1:
                    marca.append(at)
                elif b == 2:
                    marca.append(at) 
                elif b == 3:
                    marca.append(at)
                elif b == 4:
                    marca.append(at)
                b += 1
            marcas.append(marca)
        return marcas

    def nomEmpresa(self):
        sql = "SELECT nom_emp FROM empresa;"
        a = self.ejecutar(sql, "listar")
        empresa = []
        for i in range(0, len(a)):

            b = 0
            for at in a[i]:
                if b == 0:
                    empresa.append(at)
             
                b += 1
        return empresa

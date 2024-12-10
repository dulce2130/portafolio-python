import Conexion as con

#conexion = con.TablaCiudad("TienditasCadena","root","silverspoon")
#conexion = con.TablaCodigo("TienditasCadena","root","silverspoon")

#conexion = con.TablaProducto("TienditasCadena","root","silverspoon")
#marca = conexion.buscarIdMarca('Marinela')
#dim = conexion.modificarProducto("1234567891234", "Mini Barritas", 184, "g", "Bolsa de celofán", marca, 9)

conexion = con.TablaEmpresa("TienditasCadena","root","silverspoon")
print(conexion.listarMarcas())

#marca = conexion.buscarIdMarca('Marinela')
#print(marca)

#metodos = Metodos.Metodos("TienditasCadena","root","silverspoon")


#ciudades = conexion.listarCiudades()
#print(ciudades)

'''''
if conexion.existeCiudad("zitacuaro"):
    ciudad = conexion.buscarCiudad("zitacuaro")
    print(ciudad)
else:
    print("No existe")
'''
#id_ciu = "zitacuaro"


#ciudad = conexion.buscarProducto("1234567891234")
#print(ciudad)


'''''
conexion.modificarCiudad("Jaripo", 352)
print("Se modifico correctamente una ciudad")
'''''

#nomciudades = conexion.registrarCiudad(45145, "Jaripo")
#print(nomciudades)

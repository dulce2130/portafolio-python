import math

def potencias_de_2(n):
    potencia = 1
    potencias = [potencia]
    
    while potencia < n:
        potencia *= 2
        potencias.append(potencia)
    
    n = len(potencias) - 1
    return potencias, n

def tipo_clase(ip):
    elementos = ip.split(".")
    
    if len(elementos) != 4:
        return "La IP es incorrecta"
    
    lista_ip = [int(elemento) for elemento in elementos]

    for octeto in lista_ip:
        if octeto < 0 or octeto > 255:
            return  "La IP es incorrecta"  
    
    if 0 <= lista_ip[0] <= 127:
        clase = "A"
    elif 128 <= lista_ip[0] <= 191:
        clase = "B"
    elif 192 <= lista_ip[0] <= 223:
        clase = "C"
    elif 224 <= lista_ip[0] <= 239:
        clase = "D"
    elif 240 <= lista_ip[0] <= 255:
        clase = "E"
    else:
        clase = "No se puede determinar"

    #print("Clase:", clase)
    
    return clase

def bits_necesarios(hosts):
    # Usar la fórmula 2^n - 2 >= H para calcular n
    n = math.ceil(math.log2(hosts + 2))
    return n

def adaptar_mascara(ip, subredes, hosts):
    m = bits_necesarios(hosts) 
    #print(m) 
    clase = tipo_clase(ip)
    
    if clase == "A":
        mascara_decimal = mascara_A(subredes)
        print("Mascara decimal: ",mascara_decimal)

    else:
        parte1 = "1" * (32 - m)
        parte2 = "0" * m
        mascara_binaria = parte1 + parte2
        print("Mascara binaria: ", mascara_binaria)
        # Convierte la máscara binaria a la notación decimal
        partes = [int(mascara_binaria[i:i + 8], 2) for i in range(0, 32, 8)]
        mascara_decimal = ".".join(map(str, partes))
        print("Mascara decimal: ",mascara_decimal)

    return mascara_decimal

def salto_red(mascara):
    octetos = mascara.split(".")
    # Encuentra el último octeto no nulo
    ultimo_octeto_no_nulo = 0
    for octeto in octetos[::-1]:
        if octeto != "0":
            ultimo_octeto_no_nulo = int(octeto)
            break
    
    salto = 256 - ultimo_octeto_no_nulo
    print("Salto o rango:", salto)
    return salto

def longitud_subred(hosts):
    potencia = bits_necesarios(hosts)
    lon = 2**potencia 
    #print("Longitud de red:", lon)
    return lon

#longitud_subred(32)

def rangos_C(ip, subredes, hosts):
    #octetos = ip.split(".")
    primer_ip = int(ip.split(".")[-1])
    mascara = adaptar_mascara(ip, subredes, hosts)
    salto = salto_red(mascara)

    gateway = [primer_ip]
    primera_ip = [gateway[0] + 1]
    broadcast = [(primer_ip // 100 * 100 + salto) - 1]
    ultima_ip_dis = [broadcast[-1] - 1]
    ultima_ip_usar = [primer_ip + hosts]
    ip_res = ip[:-1]
    #print(ip_res)

    for _ in range(subredes - 1):
        gateway.append(broadcast[-1] + 1)
        primera_ip.append(gateway[-1] + 1)
        broadcast.append(broadcast[-1] + salto)
        ultima_ip_dis.append(broadcast[-1] - 1)
        ultima_ip_usar.append(gateway[-1] + hosts)

    for i in range(len(gateway)):
        gateway[i] = ip_res + str(gateway[i])

    for k in range(len(primera_ip)):
        primera_ip[k] = ip_res + str(primera_ip[k])

    for j in range(len(broadcast)):
        broadcast[j] = ip_res + str(broadcast[j])
    
    for l in range(len(ultima_ip_dis)):
        ultima_ip_dis[l] = ip_res + str(ultima_ip_dis[l])
    
    for p in range(len(ultima_ip_usar)):
        ultima_ip_usar[p]= ip_res + str(ultima_ip_usar[p])

    #print("Gateway: ", gateway)
    #print("Primera Ip: ", primera_ip)
    #print("Broadcast: ", broadcast)
    #print("Ultima IP dis: ", ultima_ip_dis)
    #print("Ultima IP a usar: ", ultima_ip_usar)

    return salto, gateway, primera_ip, broadcast, ultima_ip_dis, ultima_ip_usar

def rangos_B(ip, subredes, hosts):
    partes = ip.split(".")
    oct1y2 = partes[0] + "." + partes[1] + "." 
    oct3 = int(partes[2])
    oct4 = partes[3]


    mascara = adaptar_mascara(ip, subredes, hosts)
    salto = salto_red(mascara)
    ultima = round(hosts/salto)
    #print(ultima)

    salto_oct3 = [(oct3 + salto) -1]
    salto_oct3_1 = [(oct3)]

    for _ in range(subredes - 1):
        salto_oct3.append(salto_oct3[-1] + salto)
        salto_oct3_1.append(salto_oct3_1[-1] + salto)
    print(salto_oct3)

    gateway = [oct1y2 + str(i) + ".0" for i in salto_oct3_1]
    primera_ip = [oct1y2 + str(i) + ".1" for i in salto_oct3_1]
    ultima_ip_dis = [oct1y2 + str(i) + ".254" for i in salto_oct3]
    ultima_ip_usar = [oct1y2 + str(i) + "." + str(ultima) for i in salto_oct3]
    broadcast =  [oct1y2 + str(i) + ".255"  for i in salto_oct3]

    print("Gateway: ", gateway)
    print("Primera IP : ", primera_ip)    
    print("Ultima IP dis: ", ultima_ip_dis)
    print("Ultima IP a usar: ", ultima_ip_usar)
    print("Broadcast: ", broadcast)

    #print(oct1y2, oct3, oct4)
    return salto, gateway, primera_ip, broadcast, ultima_ip_dis, ultima_ip_usar

def mascara_A(subredes):
    listPo, n = potencias_de_2(subredes)
    octetos_claseA = ["000000000000000000000000"]
    octetos_nuevos = []
    octeto_rango = 0
    for octeto in octetos_claseA:
        mas = '1' * n + octeto[n:]  # Reemplazar ceros a partir del segundo octeto
        octetos_nuevos.append(mas)

    lista = octetos_nuevos[0]
    lon = len(lista) // 3  

    octeto_rango = int(lista[:lon], 2)
    mascara = f"255.{octeto_rango}.0.0"

    print(mascara)
    return mascara

#mascara_A(7)

def rangos_A(ip, subredes, hosts):
    mascara = adaptar_mascara(ip, subredes, hosts)
    salto = salto_red(mascara)
    
    partes = ip.split(".")
    oct1 = int(partes[1]) 
    saltos = [oct1]
    gateway = []
    primera_ip = []
    ultima_ip_dis = []
    ultima_ip_usar = []
    broadcast = []


    for _ in range(subredes - 1):
        saltos.append(saltos[-1] + salto)

    for i in range(len(saltos)):
        gateway.append(partes[0] + "." + str(saltos[i]) + "." + partes[2]  + "." + partes[-1])
    
    for i in range(len(saltos)):
        primera_ip.append(partes[0] + "." + str(saltos[i]) + "." + partes[2]  + ".1" )

    for i in range(len(saltos)):
        ultima_ip_dis.append(partes[0] + "." + str(saltos[i]) + "." + partes[2]  + ".254" )
    
    ultima_ip_usar = ultima_ip_dis.copy()

    for i in range(len(saltos)):
        ultima_octeto = saltos[i] + salto - 1
        broadcast.append(partes[0] + "." + str(ultima_octeto) + ".255" + ".255")

    print("Gateway: ", gateway)
    print("Primera IP : ", primera_ip) 
    print("Ultima IP dis: ", ultima_ip_dis)
    print("Ultima IP a usar: ", ultima_ip_usar)
    print("Broadcast: ", broadcast)

    return salto, gateway, primera_ip, broadcast, ultima_ip_dis, ultima_ip_usar

#rangos_A("10.0.0.0", 8, 0)

def ceros_sobrantes(ip, mascara):
    # Divide la IP y la máscara en octetos
    ip_octetos = ip.split('.')
    mascara_octetos = mascara.split('.')

    if tipo_clase(ip) == "A":
        # Convierte cada octeto de la IP y la máscara en números enteros
        ip_octetos = [int(octeto) for octeto in ip_octetos]
        mascara_octetos = [int(octeto) for octeto in mascara_octetos]

        # Calcula la cantidad de ceros sobrantes en los tres últimos octetos
        sobrantes = sum([8 - bin(mascara_octeto).count('1') for mascara_octeto in mascara_octetos[1:]])
        #print(sobrantes)
        return sobrantes

def cantidad_host_A(ip, subredes, hosts):
    mascara = adaptar_mascara(ip, subredes, hosts)
    m = ceros_sobrantes(ip, mascara)
    cantidad = 2**m - 2
    print("Cantidad Hosts: ", cantidad)
    return cantidad
 
#cantidad_host_A("10.0.0.0", 7, 0)
        
#rangos_A("10.0.0.0", 7, 0)
#rangos_B("177.10.0.0", 10, 1000)
#rangos_C("192.168.1.1", 4, 32)

def tabla(ip, subredes, hosts):

    subred_values = list(i for i in range(1, subredes + 1))
    hosts_encontrados = longitud_subred(hosts)
    mascara = adaptar_mascara(ip, subredes, hosts)
    gateway = []
    primera_ip = []
    ultima_ip_usar = []
    ultima_ip_dis = []
    ips_usadas = hosts + 2
    ips_disponibles = longitud_subred(hosts) - ips_usadas
    broadcast = []

    clase = tipo_clase(ip)

    if clase == "C":
        salto, gateway, primera_ip, broadcast, ultima_ip_dis, ultima_ip_usar = rangos_C(ip, subredes, hosts)

    elif clase == "B":
        salto, gateway, primera_ip, broadcast, ultima_ip_dis, ultima_ip_usar = rangos_B(ip, subredes, hosts)
    
    elif clase == "A":
        salto, gateway, primera_ip, broadcast, ultima_ip_dis, ultima_ip_usar = rangos_A(ip, subredes, hosts)
        hosts_encontrados = cantidad_host_A(ip, subredes, hosts)
        hosts = hosts_encontrados
        ips_usadas = hosts
    else:
        print("No se puede determinar")



    encabezado = ["Subred", "Host encontrados", "Host solicitados", 
                  "Máscara de subred", "Gateway", "1era IP a usar", 
                  "Última IP a usar", "Última IP disponible", 
                  "IPs usadas", "IPs disponibles", "Broadcast"]
    
    print("{:<6} {:<6} {:<12} {:<20} {:<12} {:<12} {:<15} {:<20} {:<10} {:<18} {:<16}".format(*encabezado))

   
    for ik in range(len(gateway)):
        table = "{:<10} {:<16} {:<13} {:<18} {:<15} {:<15} {:<15} {:<20} {:<13} {:<12} {:<10}".format(
        subred_values[ik], hosts_encontrados, hosts, mascara, gateway[ik], primera_ip[ik], ultima_ip_usar[ik], ultima_ip_dis[ik], 
        ips_usadas, ips_disponibles, broadcast[ik])
        print(table)

    return  salto, clase, subred_values, hosts_encontrados, hosts, mascara, gateway, primera_ip, ultima_ip_usar, ultima_ip_dis, ips_usadas, ips_disponibles, broadcast

#tabla("192.168.1.1", 4, 32)
#tabla("177.10.0.0", 10, 1000)
#tabla("10.0.0.0", 7, 0)

#adaptar_mascara("172.17.0.0", 16, 14)
#adaptar_mascara("172.16.0.0", 8, 256)
#adaptar_mascara("172.18.0.0", 4, 2048)

#mascara = adaptar_mascara("177.10.0.0", 10, 1000)
#mascara = adaptar_mascara("192.168.1.1", 4, 32)
#mascara = adaptar_mascara("10.0.0.1", 8, 64)

#salto_red(mascara)
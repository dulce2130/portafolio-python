import math


def bits_mascara(subredes):
    #2^n
    n = math.ceil(math.log2(subredes))
    return n

def adaptar_mascara(subredes):
    n = bits_mascara(subredes)
    #print("n = ", n)
    parte1 = "1" * (24 + n)
    parte2 = "0" * (32 - (24 + n))
    mascara_binaria = parte1 + parte2
    
    binaria = [mascara_binaria[i:i + 8] for i in range(0, 32, 8)]
    bin = ".".join(map(str, binaria))

    # Convierte la máscara binaria a la notación decimal
    partes = [int(mascara_binaria[i:i + 8], 2) for i in range(0, 32, 8)]
    mascara_decimal = ".".join(map(str, partes))
    
    #print("Mascara binaria: ", bin)
    #print("Mascara decimal: ", mascara_decimal)

    return bin, mascara_decimal

def rango(subredes):
    binaria, decimal = adaptar_mascara(subredes)
    
    octetos = binaria.split('.')
    octFin = octetos[-1]
    posicion = octFin.rfind("1")

    nuevo_octeto = "0" * 8
    nuevo_octeto = nuevo_octeto[:posicion] + "1" + nuevo_octeto[posicion + 1:]
    rango = int(nuevo_octeto, 2)

    print(rango)
    return rango

def listasCIDR(ip, subredes):
    binaria, decimal = adaptar_mascara(subredes)
    salto = rango(subredes)

    gateway = [0]
    primera_ip =[1]
    broadcas = [(primera_ip[0] + salto) - 2]
    ultima_ip_usar = [broadcas[-1] - 1]
    ip_res = ip[:-1]

    for _ in range(subredes - 1):
        
        gateway.append(gateway[-1] + salto)
        primera_ip.append(gateway[-1] + 1)
        
        broadcas.append(broadcas[-1] + salto)
        ultima_ip_usar.append(broadcas[-1] - 1)


    for i in range(len(gateway)):
        gateway[i] = ip_res + str(gateway[i])

    for k in range(len(primera_ip)):
        primera_ip[k] = ip_res + str(primera_ip[k])

    for j in range(len(broadcas)):
        broadcas[j] = ip_res + str(broadcas[j])
    
    for l in range(len(ultima_ip_usar)):
        ultima_ip_usar[l] = ip_res + str(ultima_ip_usar[l])
        
    hosts_encontrados = salto
    hostss = hosts_encontrados
    ultima_ip_dis = ultima_ip_usar    
    ips_usadas = salto
    ips_disponibles = 0

    print("Gateway: ",  gateway)
    print("Broadcas: ", broadcas)
    print("Primera IP: ",  primera_ip)
    print("Ultima IP: ",  ultima_ip_usar)

    return binaria, decimal, salto, hosts_encontrados, hostss, gateway, primera_ip, ultima_ip_usar, ultima_ip_dis, ips_usadas, ips_disponibles, broadcas

#listasCIDR("192.168.20.0", 8)
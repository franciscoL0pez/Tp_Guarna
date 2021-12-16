import datetime
#import Menu_principal
x = datetime.datetime.now()
y = x.strftime("%x")
#print(y)
"""
"""

instanteFinal = datetime.datetime.now()
instanteFinal2 = instanteFinal.strftime("%X")
#config = open("configuracion.csv", "r", encoding= "utf-8")
def funcion_ingresar(datos):
    #print(datos)
    with open("archivos.csv", "a") as archivo:
        archivo.write("\n")
        for jugador in datos:
            #print(datos[jugador][0])
            #print(datos[jugador][1])
            linea_nueva = y + ", " + str(instanteFinal2) + ", " + jugador + ", " + str(datos[jugador][0]) + ", " + str(datos[jugador][1]) + "\n"
            archivo.write(linea_nueva)
    
def funcion_etapa9(reiniciar_archivo_partidas):
    with open("archivos.csv", "r+", encoding="utf-8") as archivo:

        archivo_completo = []
        if (reiniciar_archivo_partidas == "False"):
            for line in archivo:
                #print(line)
                if "," in line:
                    archivo_completo.append(line)

        #print(archivo_completo)
        if archivo.writable() and archivo.readable():
            with open("archivos.csv", "w", encoding="utf-8") as archivo2:
                #print("se borro")

                archivo.write("")
        completo2 = []
        for x in archivo_completo:
            completo2.append(x.strip("\n").split(","))
        #print(completo2)
        ordenado = sorted(completo2, key= lambda x : x[3])
        entrada = ""
        for linea in ordenado:
            for palabra in linea:
                entrada += palabra + ","
            entrada = entrada.rstrip(",")
            entrada += "\n"
        entrada = entrada.rstrip("\n")
        envio = entrada.split("\n")
        #print(envio)

        for linea in envio:
            #print(linea)
            linea_nueva = "\n" + linea
            archivo.write(linea_nueva)
    #config.close()

    with open("archivos.csv") as archivo:
        archivo_completo = []
        for line in archivo:
            #print(line)
            if "," in line:
                archivo_completo.append(line)
        completo2 = []
        for x in archivo_completo:
            completo2.append(x.strip("\n").split(","))   
        #print(completo2)
        print("El resumen de las partidas: ")
        posicion = 0
        for linea in completo2:
            #print("partida finalizada el dia {}.".format(linea[0]))
            x = datetime.datetime.now()
            y = x.strftime("%x")
            if linea[0] == y:

                print(archivo_completo[posicion])
            posicion += 1
            #print(linea, end= "")
        #print(archivo_completo)
    """
    with open("archivos.csv", "a+") as archivo:
        archivo.write(linea_nueva)
    """
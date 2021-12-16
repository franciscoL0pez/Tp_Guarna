import datetime
x = datetime.datetime.now()
y = x.strftime("%x")

instanteFinal = datetime.datetime.now()
instanteFinal2 = instanteFinal.strftime("%X")

def funcion_ingresar(datos):
    """
    Ingresa los datos al archivo.csv
    Marco
    """
    with open("Partidas.csv", "a") as archivo:
        archivo.write("\n")
        for jugador in datos:
            linea_nueva = y + ", " + str(instanteFinal2) + ", " + jugador + ", " + str(datos[jugador][0]) + ", " + str(datos[jugador][1]) + "\n"
            archivo.write(linea_nueva)
    
def funcion_etapa9(reiniciar_archivo_partidas):
    """
    marco
    """
    with open("Partidas.csv", "r+", encoding="utf-8") as archivo:
        archivo_completo = []
        if (reiniciar_archivo_partidas == "False"):
            for line in archivo:
                
                if "," in line:
                    archivo_completo.append(line)

        
        if archivo.writable() and archivo.readable():
            with open("Partidas.csv", "w", encoding="utf-8") as archivo2:
                

                archivo.write("")
        completo2 = []
        for x in archivo_completo:
            completo2.append(x.strip("\n").split(","))
        
        ordenado = sorted(completo2, key= lambda x : x[3])
        entrada = ""
        for linea in ordenado:
            for palabra in linea:
                entrada += palabra + ","
            entrada = entrada.rstrip(",")
            entrada += "\n"
        entrada = entrada.rstrip("\n")
        envio = entrada.split("\n")
        

        for linea in envio:
            
            linea_nueva = "\n" + linea
            archivo.write(linea_nueva)


    with open("Partidas.csv") as archivo:
        archivo_completo = []
        for line in archivo:
            if "," in line:
                archivo_completo.append(line)
        completo2 = []
        for x in archivo_completo:
            completo2.append(x.strip("\n").split(","))   

        print("El resumen de las partidas:\n ")

        posicion = 0
        for linea in completo2:
            
            x = datetime.datetime.now()
            y = x.strftime("%x")
            if linea[0] == y:

                print(archivo_completo[posicion])
            posicion += 1
          
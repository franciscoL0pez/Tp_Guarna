import datetime
x = datetime.datetime.now()
y = x.strftime("%x")

instanteFinal = datetime.datetime.now()
instanteFinal2 = instanteFinal.strftime("%X")

def funcion_etapa9(reiniciar_archivo_partidas):
    """
    Pre: esta funcion recibe un dato del archivo configuracion.csv donde limpia el archivo partidas.csv
    y lo ordena, dependiendo del crierio de reinicio o no
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

def resumen():
    """
    Post: el resumen de las partidas jugadas
    marco
    """
    with open("Partidas.csv") as archivo:
        archivo_completo = []
        for line in archivo:
            if "," in line:
                archivo_completo.append(line)
        completo2 = []
        for x in archivo_completo:
            completo2.append(x.strip("\n").split(","))   

        print("El resumen de Todas las partidas: ")

        posicion = 0
        horas = []
        x = datetime.datetime.now()
        y = x.strftime("%x")
        for linea in completo2:
            
            if linea[0] == y:
                if linea[1] not in horas:
                    horas.append(linea[1])
            
            posicion += 1
        nuevo_orden = {}
        for horario in horas:
            for linea in completo2:
                if linea[0] == y:
                    if horario == linea[1]:

                        entrada = ""
                        for palabra in linea:
                            entrada += palabra + ","
                        entrada = entrada.rstrip(",")
                        entrada += "\n"
                        entrada = entrada.rstrip("\n")
                        envio = entrada.split("\n")

                        if horario not in nuevo_orden:
                            nuevo_orden[horario] = envio
                        else:
                            nuevo_orden[horario] += envio

        for horario in nuevo_orden:
            print("\nel resumen de la partida{}:\t".format(horario))
            
            print("{}".format(nuevo_orden[horario]))
def funcion_ingresar(datos, reiniciar_archivo_partidas):
    """
    Pre: Ingresa los datos al archivo.csv
    Marco
    """
    with open("Partidas.csv", "a") as archivo:
        archivo.write("\n")
        for jugador in datos:
            linea_nueva = y + ", " + str(instanteFinal2) + ", " + jugador + ", " + str(datos[jugador][0]) + ", " + str(datos[jugador][1]) + "\n"
            archivo.write(linea_nueva)
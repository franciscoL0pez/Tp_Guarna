import string 
import random
import os
from datetime import datetime
from tkinter import *
import Registro
import Login
import os 
def borrar_pantalla()->None:
    '''
    Pre: -
    Post: Borra la pantalla
    '''
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def crear_tablero(tablero_num:int)->list:
    '''
    Pre: -
    Post: Crea el tablero corto

    Marco
    '''   
    if tablero_num == 3:

        tablero=[[0 for j in range(tablero_num+1)] for x in range(tablero_num -1)]
    else:
        tablero=[[0 for j in range (tablero_num)]for i in range(tablero_num)]

    return tablero

def menu_elegir_tablero()->int:
    '''
    Pre: -
    Post: Configuraciones del juego

    Marco
    ''' 
    print("")
    print("1-Tablero de 4x2")
    print("2-Tablero de 4x4")
    print("3-Salir(si eliges esta opcion quedara fijado el tablero 2x2)")
    print("")
    opciones = validacion_jugadores_y_tablero()
    
    if opciones == 1:              #Cambiar por el tablero de 4x2   
        tamanio_de_tablero = 3
    
    elif opciones == 2:
        tamanio_de_tablero = 4 
    
    else: tamanio_de_tablero = 2

    return tamanio_de_tablero

def pares_de_fichas(tamanio_de_tablero:int)->int:
    '''
    Pre: Recibe el tamanio del tablero
    Post: Returna la cantidad de pares que debe haber en el tablero

    Marco
    '''   
    cantidad_de_pares = 0 

    if tamanio_de_tablero > 2:
        if tamanio_de_tablero == 3:
            cantidad_de_pares = tamanio_de_tablero+1
        else:
            cantidad_de_pares = tamanio_de_tablero*2
    else:
        cantidad_de_pares = tamanio_de_tablero

    return cantidad_de_pares

def imprimir_tablero(tablero:list)->None:
    '''
    Pre: Recibe el tablero
    Post: Marca las filas y columnas del tablero
    
    Marco
    '''   
    cont = 1
    print("\nFILA\tCOLUMNAS")
    lim = len(tablero[0])
    cad = '\t  '
    num = 1

    for i in range (lim):
        cad += str(num)+'  '
        num +=1
    print(cad)
    for fila in tablero:
        print(cont,"\t",fila)
        cont += 1

def validar_menu()->int:
    '''
    Pre: Pide un numero en un rango
    Post: Te responde si el numero esta en el rango

    Martin
    '''
    numero = input("\nIngrese una opcion: ")                        
    while not numero.isnumeric() or (int(numero)) >4 or (int(numero)) <1 :
        print("")
        print("Esa opcion no es valida!")
        print("")
        numero = input("\nIngrese una opcion valida:")

    return int(numero)

def validar_columnas_y_filas(numero:int,tamanio_de_tablero:int,fila_columna:int)->int:
    '''
    Pre: -
    Post: Valida que los datos sean numeros y esten en el rango que se pide

    Martin
    '''
    if tamanio_de_tablero == 3 and fila_columna == 1:
        while (not numero.isnumeric()) or ((int(numero)) > (tamanio_de_tablero-1)) or (int(numero) <1) :
            print("\nERROR")
            numero = input("\nEliga un valor que sea un numero y este en el rango: ")

    elif tamanio_de_tablero == 3 and fila_columna == 2:
        while (not numero.isnumeric()) or ((int(numero)) > (tamanio_de_tablero+1)) or (int(numero) <1) :
            print("\nERROR")
            numero = input("\nEliga un valor que sea un numero y este en el rango: ")
    else:
        while not numero.isnumeric() or (int(numero)) > (tamanio_de_tablero) or int(numero) <1 :
            print("\nERROR")
            numero = input("\nEliga un valor que sea un numero y este en el rango: ")

    return (int(numero)-1)

def validacion_jugadores_y_tablero() -> int:
    """
    PRE: - 
    POST: devuelve data validar, que seria el tamaño del tablero o la cantidad de jugadores
    Martin
    """
    data_validar1 = input("Ingrese una opcion:")
    while data_validar1.isnumeric() == False or int(data_validar1) > 3:
        print("ERROR fuera de rango")
        data_validar1 = input("Ingrese una opcion:")
    data_validar = int(data_validar1)
    
    return data_validar

def validar_lugar_disponible(tamanio_de_tablero:int,tablero:list,matriz:list):
    '''
    Pre: Pide una posicion por fila y columnas
    Post: Valida que las fichas no este ya elegidas

    Martin
    '''
    validar = True

    while validar:
        fila = input("\nIngrese una fila: ")
        fila = validar_columnas_y_filas(fila,tamanio_de_tablero,1)

        columna = input("\nEliga una columna: ")
        columna = validar_columnas_y_filas(columna,tamanio_de_tablero,2)

        if tablero[fila][columna]!=0:
            print("\nError lugar ya seleccionado, seleccione otra ubicacion")
        
        else:
            ficha = matriz[fila][columna]
            tablero[fila][columna] = ficha
            validar = False
    
    return ficha,fila,columna

def cantidad_de_letras(tamanio_de_tablero:int)->int:
    '''
    Pre: -
    Post: Define el tamaño que tiene que tener el tablero de juego  

    Martin
    '''
    if tamanio_de_tablero == 4:
        pares_de_letras = tamanio_de_tablero *  2

    elif tamanio_de_tablero == 3:
        pares_de_letras = tamanio_de_tablero+1

    else: pares_de_letras = tamanio_de_tablero

    return pares_de_letras

def crear_matriz(tamanio_de_tablero:int)->list:
    '''
    Pre: -
    Post: Crea la matriz con las letras que se necesitan para jugar

    Marco
    '''
    letras = string.ascii_letters
    matriz = []
    lista_de_letras_1 = []
    lista_de_letras_2 = []

    pares_de_letras = cantidad_de_letras(tamanio_de_tablero)

    for i in range(pares_de_letras):
        if letras[i] not in lista_de_letras_1:
            lista_de_letras_1.append(letras[i])
            lista_de_letras_2.append(letras[i])
        
        if (len(lista_de_letras_1) == tamanio_de_tablero and tamanio_de_tablero != 3) or (tamanio_de_tablero == 3 and len(lista_de_letras_1) == tamanio_de_tablero +1):
            random.shuffle(lista_de_letras_1)
            random.shuffle(lista_de_letras_2)

            matriz.append(lista_de_letras_1)   
            matriz.append(lista_de_letras_2)

            lista_de_letras_1 = []
            lista_de_letras_2 = []

    random.shuffle(matriz)
    return matriz

#Hasta aca queda asi el programa

def tiempo_jugado(instanteInicial:float)->None:
    '''
    Pre: -
    Post: indica cuanto tiempo tomo terminar una partida y cuantos intentos tuvo el usuario 

    Fede
    '''
    instanteFinal = datetime.now()
    tiempo = instanteFinal - instanteInicial
    print(f"\nEl juego duro un tiempo de: {tiempo} " )

def sumar_puntos(datos:dict)->int:
    '''
    Pre:  -
    Post: Suma los puntos si el jugador encontro un par

    Fede
    '''
    PUNTOS_DEL_JUGADOR = 0
    puntos_totales = 0

    for jugador in datos:
        puntos_totales += datos[jugador][PUNTOS_DEL_JUGADOR]

    return puntos_totales
#-------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------#
def cargar_diccionario_datos(lista_aprobados:list):
    '''
    Pre:  -
    Post: Crea un dic con los datos Puntos - Intentos

    Fede
    '''
    datos = {}
    # Puntos-intentos-ganadas

    for jugador in lista_aprobados:
        if jugador not in datos:
            datos[jugador]= [0,0,0]

    return datos
#-------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------#
def jugador_que_incia(datos:dict)->None:
    '''
    Pre:  Toma los jugadores que vayan a jugar y los mezcla
    Post: Returna el jugador que inicia la partida

    Fran
    '''
    lista_de_jugadores = []
    
    for jugador in datos:
        if jugador not in lista_de_jugadores:
            lista_de_jugadores.append(jugador)

    random.choice(lista_de_jugadores)

    return lista_de_jugadores

def cantidad_de_jugadores()->int:

    data_validar = input("ingrese la cantidad de jugadores : ")

    while data_validar.isnumeric() == False or int(data_validar) < 0:
        print("Error debe ingresar un numero mayor que 0 ")
        data_validar = input("Ingrese una opcion: ")

    data_validar = int(data_validar)
    
    return data_validar


def ganador(datos:dict,lista_de_jugadores:list,cant_de_jugadores:int)->str:
    '''
    Pre: -
    Post: Compara los puntajes y si igualan compara los intentos

    Fran  
    '''
    #Esta funcion hay que cambiarla por la funcion de marcos
    if cant_de_jugadores==2:
        JUGADOR_1 = lista_de_jugadores[0]
        JUGADOR_2 = lista_de_jugadores[1]

        if datos[JUGADOR_1][0] > datos[JUGADOR_2][0]:
            print(f"\nEl jugador {JUGADOR_1} gano la partida y realizo {datos[JUGADOR_1][1]} intentos")
        
        elif datos[JUGADOR_1][0] < datos[JUGADOR_2][0]:
            print(f"\nEl jugador {JUGADOR_2} gano la partida y realizo {datos[JUGADOR_2][1]} intentos")

        else:

            if datos[JUGADOR_1][1] > datos[JUGADOR_2][1]:
                print(f"\nEl ganador fue {JUGADOR_2} con una cantidad de intentos de {datos[JUGADOR_2][1]}")

            else:
                print(f"\nEl ganador fue {JUGADOR_1} con una cantidad de intentos de {datos[JUGADOR_1][1]}")
    else:
        print(f"\nHas ganado {lista_de_jugadores[0]} tuviste una cantidad de intentos de {datos[lista_de_jugadores[0]][1]}") #Si solo juega un jugador



def buscar_fichas(matriz:list,tablero:list,instanteInicial:float,tamanio_de_tablero:int,datos:dict,cant_de_jugadores:int)->None:
    '''
    Pre: Pide dos posiciones que esten en un rango de posibiladades 
    Post: Te devulve las letras que se hallan en esas posiciones ingresadas 

    Fran
    '''
    lista_de_jugadores = jugador_que_incia(datos) #Mezcla la lista de jugadores para que comience cualquiera
    jugador = lista_de_jugadores[0] #Llama al jugador que debe iniciar
    cantidad_de_pares = pares_de_fichas(tamanio_de_tablero) #Dice la cantidad de pares que hay que adivinar
    puntos_totales = 0 #Suma los puntos de los jugadores
    ficha_1 = 0
    ficha_2 =0
    turno = 0 

    while cantidad_de_pares > (puntos_totales+1) : #Buscar la forma de que se sumen los dos y en caso de  que sea uno se sume uno solo
       
        puntos_totales = sumar_puntos(datos)
        print(f"\nEs el turno del jugador: {jugador}")
        imprimir_tablero(tablero)

        ficha_1,fila_1,columna_1 = validar_lugar_disponible(tamanio_de_tablero,tablero,matriz)
        
        imprimir_tablero(tablero) 

        ficha_2,fila_2,columna_2 = validar_lugar_disponible(tamanio_de_tablero,tablero,matriz)
    
        datos[jugador][1]+=1 #Sumamos siempre un intento al jugador 
    
        if ficha_1 != ficha_2:
            imprimir_tablero(tablero)
            tablero[int(fila_1)][int(columna_1)] = 0
            tablero[int(fila_2)][int(columna_2)] = 0
            
            if turno < (cant_de_jugadores-1) and len (lista_de_jugadores) > 1 :
                turno += 1 
                jugador = lista_de_jugadores[turno]
                
            else:
                turno = 0
                jugador  = lista_de_jugadores[turno]

            #borrar_pantalla()
        
        else :
            datos[jugador][0]+=1 #En caso de que encuentre una ficha le sumamos dos puntos

    ganador(datos, lista_de_jugadores,cant_de_jugadores)
    tiempo_jugado(instanteInicial)
    
def archivo_configuracion():
    """
    PRE: recibe el tamaño de tablero y cantidad de jugadores por parametro 
    POST:devuelve un archivo con todos lo datos ingresados y si se reinicio la partida
    """
    CANTIDAD_FICHAS = 16
    MAXIMO_JUGADORES = 2
    MAXIMO_PARTIDAS = 5
    REINICIAR_ARCHIVO_PARTIDAS = False
    
    leyo_el_archivo = False
    try:
    
        with open ("configuracion.csv","r") as archivo_config:
                leyo_el_archivo = True
                contador = 0
                for linea in archivo_config:
                    renglon = linea.split(",")
                    if contador == 0:
                       CANTIDAD_FICHAS = renglon[1]
                    elif contador == 1:
                        MAXIMO_JUGADORES = renglon[1]
                    elif contador == 2:
                        MAXIMO_PARTIDAS = renglon[1]
                    elif contador == 3:
                        REINICIAR_ARCHIVO_PARTIDAS = renglon[1]
                    contador += 1
        
    except FileNotFoundError :
        
        print("\nel archivo no se encontro ")
    print(f"\nla cantidad de fichas totales es: { CANTIDAD_FICHAS }")
    print(f"\nla cantidad de jugadores es: { MAXIMO_JUGADORES }")
    print(f"\nmaximo partidas: { MAXIMO_PARTIDAS }")
    print(f"\nreinicio de la partida: { REINICIAR_ARCHIVO_PARTIDAS }")
    
    if leyo_el_archivo == True:
        print("\nlos valores establecidos fueron dados por configuracion")
    else:
        print("\nlos valores establecidos fueron dados por omision ")

    lista_configuracion = [CANTIDAD_FICHAS,MAXIMO_JUGADORES, REINICIAR_ARCHIVO_PARTIDAS]

    return lista_configuracion

def configuraciones()->int:
    informacion_archivo = archivo_configuracion()
    tamanio_de_tablero = int(informacion_archivo[0]/4) #En caso de que el usuario decida  no configurar nada damos valores predeterminados
    cant_de_jugadores = (informacion_archivo[1])
    maximo_de_partidas = informacion_archivo([2])

    return cant_de_jugadores, tamanio_de_tablero, maximo_de_partidas

def main()->None:
    opcion=0
    lista_de_usuarios = Login.usuarios() #Sacar desp por que esta para no hacer registros
    cant_de_jugadores, tamanio_de_tablero, maximo_de_partidas = configuraciones()
    borrar_pantalla()

    while opcion !=5:
        print("\n-----MENU PRINCIPAL-----")
        print("1. Empezar a jugar")
        print("2. Elegir tablero ")
        print("3- Registrase")
        print("4- Elegir cantidad de jugadores ")
        print("5- Salir.")
        opcion = validar_menu()   

        if opcion == 1 :

            if len(lista_de_usuarios) > 1 : #Pedimos que al menos tenga 1 jugador registrado
                lista_aprobados = Login.jugadores_aprobados(cant_de_jugadores,lista_de_usuarios)
                cant_de_jugadores = len(lista_aprobados) #Definimos la cantidad de jugadores actuales
                datos = cargar_diccionario_datos(lista_aprobados)
                borrar_pantalla()
                instanteInicial = datetime.now()#al empezar a jugar
                tablero = crear_tablero(tamanio_de_tablero) #Genera el tablero con las fichas ocultas 
                matriz = crear_matriz(tamanio_de_tablero) #Genera la matriz con las letras del juego
                buscar_fichas(matriz,tablero,instanteInicial,tamanio_de_tablero,datos,cant_de_jugadores) 

            else:
                print("Debes registrar a menos 1 jugador")

        elif opcion==2:
            tamanio_de_tablero = menu_elegir_tablero()

        elif opcion==3 :
            Registro.main()
            lista_de_usuarios = Login.usuarios()
        
        elif opcion==4 :
            cant_de_jugadores = cantidad_de_jugadores()
main()

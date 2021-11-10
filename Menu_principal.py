import string 
import random
import os
from datetime import datetime

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
    '''   
    tablero=[[0 for j in range (tablero_num)]for i in range(tablero_num)]

    return tablero

def menu_elegir_tablero()->int:
    '''
    Pre: -
    Post: Configuraciones del juego
    ''' 
    print("")
    print("1-Tablero de 4x2")
    print("2-Tablero de 4x4")
    print("3-Salir(si eliges esta opcion quedara fijado el tablero 2x2)")
    print("")
    opciones = (int(input("Eliga una opcion: ")))

    if opciones == 1:              #Cambiar por el tablero de 4x2   
        tamanio_de_tablero = 4 
    
    elif opciones == 2:
        tamanio_de_tablero = 4 
    
    else: tamanio_de_tablero = 2

    return tamanio_de_tablero

def imprir_tablero(tablero:list)->None:
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
    '''
    numero = input("\nIngrese una opcion: ")                        
    while not numero.isnumeric() or (int(numero)) >7 or (int(numero)) <1 :
        print("")
        print("Esa opcion no es valida!")
        print("")
        numero = input("\nIngrese una opcion valida:")

    return int(numero)

def validar_columnas_y_filas(numero:int,tamanio_de_tablero:int)->int:
    '''
    Pre: -
    Post: Valida que los datos sean numeros y esten en el rango que se pide 
    '''
    while not numero.isnumeric() or (int(numero)) > (tamanio_de_tablero) or int(numero) <1 :
        print("\nERROR")
        numero = input("\nEliga un valor que sea un numero y este en el rango: ")

    return (int(numero)-1)

def cantidad_de_letras(tamanio_de_tablero:int)->int:
    '''
    Pre: -
    Post: Define el tamaño que tiene que tener el tablero de juego  
    '''
    if tamanio_de_tablero >2:
        pares_de_letras = tamanio_de_tablero *  2
    
    else: pares_de_letras = tamanio_de_tablero

    return pares_de_letras

def crear_matriz(tamanio_de_tablero:int)->list:
    '''
    Pre: -
    Post: Crea la matriz con las letras que se necesitan para jugar
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
        
        if len(lista_de_letras_1) == tamanio_de_tablero:
            random.shuffle(lista_de_letras_1)
            random.shuffle(lista_de_letras_2)

            matriz.append(lista_de_letras_1)   
            matriz.append(lista_de_letras_2)

            lista_de_letras_1 = []
            lista_de_letras_2 = []

    random.shuffle(matriz)
    return matriz

def tiempo_jugado_y_intentos(instanteInicial:float,intentos_totales:int)->None:
    '''
    Pre: -
    Post: indica cuanto tiempo tomo terminar una partida y cuantos intentos tuvo el usuario 
    '''
    instanteFinal = datetime.now()
    tiempo = instanteFinal - instanteInicial
    print(f"\nTiempo jugado: {tiempo}, la cantidad de intenso fue: {intentos_totales} " )

def cantiad_de_jugadores()->int:
    print("\n1. 1 Solo jugador ")
    print("2. 2 Jugadores")
    cant_de_jugadores = int(input("Ingrese una opcion:"))

    if cant_de_jugadores !=1:
        cant_de_jugadores = 2

    else: cant_de_jugadores = 1 

    return cant_de_jugadores

def datos_de_jugadores(cant_de_jugadores:int,jugador_1:str,jugador_2:str)->None:
    datos = {}
    
    if cant_de_jugadores ==2:
        datos[jugador_1] = [0,0]
        datos[jugador_2] = [0,0]

    else:
        datos[jugador_1] = [0,0]
 
    return datos

def ingresar_jugadores(cant_de_jugadores:int)->dict:
    jugador_1 = ""
    jugador_2 = ""

    if cant_de_jugadores == 2 :
        jugador_1 = input("Ingrese el nombre del jugador 1 :")
        jugador_2 = input("Ingrese el nombre del jugador 2 :")

    if cant_de_jugadores == 1 :
        jugador_1 = input("Ingrese el nombre del jugador:")
    
    datos = datos_de_jugadores(cant_de_jugadores,jugador_1,jugador_2)

    return datos

def jugador_que_incia(datos:dict)->None:
    lista_de_jugadores = []
    
    for jugador in datos:
        if jugador not in lista_de_jugadores:
            lista_de_jugadores.append(jugador)

    random.choice(lista_de_jugadores)

    return lista_de_jugadores
    
def cambiar_turno(datos:dict,jugador:str,cant_de_jugadores:int)->None:
    lista_de_jugador = jugador_que_incia(datos)
    
    if cant_de_jugadores ==2:
        if jugador==lista_de_jugador[0]:
            jugador = lista_de_jugador[1]

        else:
            jugador = lista_de_jugador[0]

    return jugador

def buscar_fichas(matriz:list,tablero:list,instanteInicial:float,tamanio_de_tablero:int,datos:dict,cant_de_jugadores:int)->None:
    '''
    Pre: Pide dos posiciones que esten en un rango de posibiladades 
    Post: Te devulve las letras que se hallan en esas posiciones ingresadas 
    '''
    lista_de_jugadores = jugador_que_incia(datos)
    jugador = lista_de_jugadores[0]

    while tamanio_de_tablero > (datos[jugador][0]) : #Buscar la forma de que se sumen los dos y en caso de  que sea uno se sume uno solo
        borrar_pantalla()
        print(f"Es el turno del jugador: {jugador}")
        imprir_tablero(tablero)

        fila_1 = input("\nIngrese una fila: ")
        fila_1 = validar_columnas_y_filas(fila_1,tamanio_de_tablero)

        columna_1 = input("\nEliga una columna: ")
        columna_1 = validar_columnas_y_filas(columna_1,tamanio_de_tablero)

        ficha_1 = matriz[fila_1][columna_1] 
        tablero[fila_1][columna_1] = ficha_1    

        imprir_tablero(tablero) 

        fila_2 = input("\nEliga otra fila: ")
        fila_2 = validar_columnas_y_filas(fila_2,tamanio_de_tablero)

        columna_2 = input("\nEliga otra columna: ")
        columna_2 = validar_columnas_y_filas(columna_2,tamanio_de_tablero)

        ficha_2 = matriz[fila_2][columna_2]
        tablero[fila_2][columna_2] = ficha_2
        
        datos[jugador][1]+=1

        if ficha_1 != ficha_2:
            imprir_tablero(tablero)
            tablero[int(fila_1)][int(columna_1)] = 0
            tablero[int(fila_2)][int(columna_2)] = 0
            jugador = cambiar_turno(datos, jugador,cant_de_jugadores)
        
        else :
            borrar_pantalla()
            imprir_tablero(tablero) 
            datos[jugador][0]+=1

    #tiempo_jugado_y_intentos(instanteInicial, intentos_totales) #Hay que ponerle los intentos totales del dict

def main()->None:
    opcion=0
    tamanio_de_tablero = 2 #Establecemos un valor predefinido para el tamaño del tablero
    cant_de_jugadores = 1  
    while opcion !=7:
        print("\n-----MENU PRINCIPAL-----")
        print("1. Empezar a jugar")
        print("2. Elegir tablero ")
        print("3. Elegir cantidad de jugadores ")
        print("4.")
        print("5.")
        print("6.")
        print("7. Salir.")
        opcion = validar_menu()   

        if opcion==1:
            datos = ingresar_jugadores(cant_de_jugadores)
            instanteInicial = datetime.now()#al empezar a jugar
            tablero = crear_tablero(tamanio_de_tablero) #Genera el tablero con las fichas ocultas 
            matriz = crear_matriz(tamanio_de_tablero) #Genera la matriz con las letras del juego
            buscar_fichas(matriz,tablero,instanteInicial,tamanio_de_tablero,datos,cant_de_jugadores) 
            

        elif opcion==2:
            tamanio_de_tablero = menu_elegir_tablero()
    
        elif opcion==3:
            cant_de_jugadores = cantiad_de_jugadores()
        
        elif opcion==4:
            pass
        
        elif opcion==5:
            pass
        
        elif opcion==6:
            pass

main()
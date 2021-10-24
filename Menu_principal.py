import string
import random
import os
from datetime import datetime

def borrar_pantalla():
    '''
    Pre: -
    Post:Borra la pantalla 
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
    print("1-Tablero medio 2x2")
    print("2-Tablero largo 4x4")
    print("3-Salir(si eliges esta opcion quedara fijado el tablero 2x2)")
    print("")
    opciones = (int)(input("Eliga una opcion:"))

    if opciones!=3:
        tamaño_de_tablero = opciones*2
    
    else : tamaño_de_tablero = 2

    return tamaño_de_tablero


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

def validar_columnas_y_filas(numero:int):
    '''
    Pre: -
    Post: Valida que los datos sean numeros y esten en el rango que se pide 
    '''
    while not numero.isnumeric() or (int(numero)) >= 2:
        print("ERROR")
        numero = input("\n Eliga un valor que sea un numero y este en el rango: ")

    return int(numero)

def generar_matriz()->None:
    '''
    Pre: -
    Post: Genera la matriz con las letras
    '''
    cadena_completa = string.ascii_letters

    letra1 = random.choice(cadena_completa)
    copia1 = letra1

    letra2 = random.choice(cadena_completa)
    copia2 = letra2

    lista = [letra1, letra2, copia1, copia2]
    random.shuffle(lista)
    matriz = [[lista[0],lista[1]], [lista[2],lista[3]]]

    return matriz

def tiempo_jugado_y_intentos(instanteInicial:float,intentos_totales:int)->None:
    '''
    Pre: -
    Post: indica cuanto tiempo tomo terminar una partida y cuantos intentos tuvo el usuario 
    '''
    instanteFinal = datetime.now()#cuando termina de jugar
    tiempo = instanteFinal - instanteInicial
    print(f"\nTiempo jugado: {tiempo}, la cantidad de intenso fue: {intentos_totales} " )

def buscar_fichas(matriz:list,tablero:list,instanteInicial:float)->str:
    contador = 0 
    intentos_totales = 0
    imprir_tablero(tablero)

    while contador <2:
        fila_1 = input("Ingrese una fila: ")
        fila_1 = validar_columnas_y_filas(fila_1)

        columna_1 = input("\nEliga una columna: ")
        columna_1 = validar_columnas_y_filas(columna_1)

        ficha_1 = matriz[fila_1][columna_1]
        tablero[fila_1][columna_1] = ficha_1

        imprir_tablero(tablero)

        fila_2 = input("\nEliga otra fila: ")
        fila_2 = validar_columnas_y_filas(fila_2)

        columna_2 = input("\nEliga otra columna: ")
        columna_2 = validar_columnas_y_filas(columna_2)

        ficha_2 = matriz[fila_2][columna_2]
        tablero[fila_2][columna_2] = ficha_2
        
        intentos_totales = intentos_totales + 1

        if ficha_1 != ficha_2:
            imprir_tablero(tablero)
            tablero[int(fila_1)][int(columna_1)] = 0
            tablero[int(fila_2)][int(columna_2)] = 0
    
        else :
            imprir_tablero(tablero) 
            contador = contador + 1

    tiempo_jugado_y_intentos(instanteInicial, intentos_totales)

def main()->None:
    opcion=0
    tablero_num = 2 #Establecemos un valor predefinido para el tamaño del tablero
    while opcion !=7:
        print("\n-----MENU PRINCIPAL-----")
        print("1. Empezar a jugar")
        print("2. Elegir tablero ")
        print("3.")
        print("4.")
        print("5.")
        print("6.")
        print("7. Salir.")
        opcion = validar_menu()   

        if opcion==1:
            instanteInicial = datetime.now()#al empezar a jugar
            tablero = crear_tablero(tablero_num) #Genera el tablero con las fichas ocultas 
            matriz = generar_matriz() #Genera la matriz con las letras del juego
            buscar_fichas(matriz,tablero,instanteInicial)
            

        elif opcion==2:
            tablero_num = menu_elegir_tablero()
    
        elif opcion==3:
            pass
        
        elif opcion==4:
            pass
        
        elif opcion==5:
            pass
        
        elif opcion==6:
            pass

main()
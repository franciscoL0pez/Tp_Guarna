import tkinter
from tkinter import *
from tkinter import messagebox
#------------------------------------------------------------------------------#
def modificar_diccionario(datos):
    '''
    PRE: Recibe el diccionario datos con la informacion de la partida.
    POST: Devuelve una lista de listas ordenada de mayor a menor.

    Simon
    '''
    for clave in datos:
        aciertos, intentos = datos[clave][0], datos[clave][1]
        if intentos == 0:
            promedio = 0
        else:
            promedio = (aciertos/intentos)*100
            promedio = round(promedio, 1)
        datos[clave] = [aciertos, intentos,promedio]
    return datos
#------------------------------------------------------------------------------#
def crear_lista_final(datos):
    '''
    PRE: Recibe el numero de partidas hasta el momento, la cantidad maxima de partidas permitidas y la tabla escrita en una cadena.
    POST: Devuelve un booleano que determina si se vuelve a jugar o no.

    Simon
    '''
    datos = modificar_diccionario(datos)
    claves= []
    for clave in datos:
        sub = []
        sub.append(clave)
        for i in datos[clave]:
            sub.append(i)
        claves.append(sub)

    lista_ord = sorted(claves, reverse=True,key=lambda item: item[3])

    return lista_ord
#------------------------------------------------------------------------------#
def crear_cadena_tabla(lista):
    tabla = 'TABLA PUNTAJE\n   ♠-♠-♠\n'
    pos_lista = 0

    while(pos_lista < len(lista)):
        cadena = ''+str(pos_lista+1)+'.-'
        pos_sub = 0
        sub = lista[pos_lista]

        while(pos_sub<len(sub)):
            if pos_sub == len(sub)-1:
                cadena += str(sub[pos_sub])+'%\n'
            else:
                cadena += str(sub[pos_sub])+'\t'
            pos_sub += 1
        tabla += cadena
        pos_lista += 1
    
    return tabla
#------------------------------------------------------------------------------#
'''TESTEO DEL PROGRAMA'''

def imprimir_tabla_ganadores(cantidad:int, cantidad_max:int, datos:dict)->bool:
    lista_ordenada = crear_lista_final(datos) 
    tabla_final = crear_cadena_tabla(lista_ordenada) 

    if cantidad <= cantidad_max:
        
        messagebox.showinfo(message="{}\n".format(tabla_final), title="Tabla de puntajes")
        valido = messagebox.askyesno(message="Volver a jugar?",title = "Atencion!")  

    else:
        
        messagebox.showinfo(message="{}\n FIN DEL JUEGO ".format(tabla_final), title="Tabla de puntajes")
        valido = False 


    return valido

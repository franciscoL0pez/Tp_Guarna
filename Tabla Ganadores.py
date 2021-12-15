import tkinter
from tkinter import *
from tkinter import messagebox
#------------------------------------------------------------------------------#
def seguir_jugando(cantidad, cantidad_max,string):
    valido = None
    root = Tk()
    root.deiconify()
    root.withdraw()
    if cantidad <= cantidad_max:
        valido = messagebox.askyesno(message="{}\nVolver a Jugar?".format(string), title="Atencion!")
    else:
        messagebox.showinfo(message="{}\nVolver a Jugar?".format(string), title="Atencion!")

    return valido
#------------------------------------------------------------------------------#
def modificar_diccionario(datos):
    for clave in datos:
        aciertos, intentos = datos[clave][0], datos[clave][1]
        promedio = aciertos/intentos
        promedio = round(promedio, 1)
        datos[clave].append(promedio)

    return datos
#------------------------------------------------------------------------------#
def crear_lista_final(datos):
    datos = modificar_diccionario(datos)
    dic_ord = {}
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
                cadena += str(sub[pos_sub])+'\n'
            else:
                cadena += str(sub[pos_sub])+'\t'
            pos_sub += 1
        tabla += cadena
        pos_lista += 1

    return tabla
#------------------------------------------------------------------------------#
'''TESTEO DEL PROGRAMA
datos = {"simon":[3,18], "Fran":[2,4],"juan":[4,12], "fede":[4,4]}
lista_ordenada = crear_lista_final(datos)
tabla_final = crear_cadena_tabla(lista_ordenada)
seguir_jugando(2, 3,tabla_final)
seguir_jugando(4, 3,tabla_final)'''
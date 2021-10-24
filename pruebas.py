import random
import string

def crear_matriz(tablero_num:int):
    letras = string.ascii_letters
    lista_final = []
    sublista = []
    sublista2 = []

    for i in range(2):
        if letras[i] not in sublista:
            sublista.append(letras[i])
            sublista2.append(letras[i])

        if len(sublista) == 4:
            random.shuffle(sublista)
            lista_final.append(sublista)   
            lista_final.append(sublista2)    
            sublista = []
            sublista2 = []

    random.shuffle(lista_final)

import random
import string
tablero_num = 4
#def crear_matriz(tablero_num:int):

letras = string.ascii_letters
lista_final = []
sublista = []
sublista2 = []

for i in range(tablero_num):
    if letras[i] not in sublista:
        sublista.append(letras[i])
        sublista2.append(letras[i])

    if len(sublista) == (4/2):
        random.shuffle(sublista)
        lista_final.append(sublista)   
        lista_final.append(sublista2)    
        sublista = []
        sublista2 = []

random.shuffle(lista_final)
print(lista_final)


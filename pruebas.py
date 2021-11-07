import random 

datos = {"fran":[],"tomi":[]}
def jugador_que_incia(datos:dict)->None:
    lista_de_jugadores = []
    
    for jugador in datos:
        if jugador not in lista_de_jugadores:
            lista_de_jugadores.append(jugador)

    jugador_que_empieza = random.choice(lista_de_jugadores)

    return jugador_que_empieza

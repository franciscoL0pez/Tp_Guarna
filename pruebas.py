datos = {"fran":[1,2],"tomi":[1,3]}
diccionario_ordenado = sorted(datos.items() ,key=lambda x:[x[0],x[1]], reverse=True )

print(diccionario_ordenado)
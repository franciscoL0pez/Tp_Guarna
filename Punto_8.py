def leer_registro(archivo_ingresado:str)->list:
    with open(archivo_ingresado, "r") as archivo:
        lista_de_usuarios = []
        for linea in archivo:
            linea = linea.rstrip("\n").split(",")
            lista_de_usuarios.append(linea)

    return lista_de_usuarios

def leer_jugadores_ingresados():
    jugadores = open('Jug_ingresados.csv','r')
    linea = jugadores.readline()

    if linea:
        devolver = linea.rstrip("\n").split(",")

    else:
        devolver = "","","",""

    return devolver

def validar_ingreso(nombre:str,clave:str,lista_de_usuarios:list,lista_de_validados:list)->None:
    '''
    Comparo el usuario y la contraseña que se ingreso en Jug_ingresados.csv y valido que este en los usuarios registrados
    si esta en los usuarios registrados lo meto en la lista de usuarios_validados
    '''
    USUARIOS = 0
    CONTRASENIA = 1

    for i in range(len(lista_de_usuarios)):

        if nombre == lista_de_usuarios[i][USUARIOS] and clave == lista_de_usuarios[i][CONTRASENIA]: 

            if nombre not in lista_de_validados:
                lista_de_validados.append(nombre)

            else: print("\nEse usuario ya se ingreso anteriormente!")

    if nombre not in lista_de_validados:
        print("\nError al ingresar usuario o contraseña")

def terminar_de_validar(lista_de_usuarios:list)->None:
    lista_de_validados = [] 
    nombre,clave = leer_jugadores_ingresados()

    validar_ingreso(nombre, clave, lista_de_usuarios,lista_de_validados)

    return lista_de_validados
        
def main()->None:
    lista_de_usuarios = leer_registro("Registro.csv")
    lista_de_validados = terminar_de_validar(lista_de_usuarios)

main()
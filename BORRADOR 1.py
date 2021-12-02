#============================== IMPORTACIONES ================================#
from tkinter import *
from tkinter import messagebox
#================================ FUNCIONES ==================================#
#-----------------------------------------------------------------------------#
def leer_archivo(linea):
    if linea:
        lista = linea.rstrip("\n").split(',')
    else:
        lista = ""

    return lista
#-----------------------------------------------------------------------------#
def crear_lista_usuarios(archivo_registro, lista_registro):
    linea_registro = archivo_registro.readline()
    sub_lista_registro = leer_archivo(linea_registro)

    while(sub_lista_registro != ""):
        lista_registro.append(sub_lista_registro)
        linea_registro = archivo_registro.readline()
        sub_lista_registro = leer_archivo(linea_registro)

    return lista_registro
#-----------------------------------------------------------------------------#
def verificar_ingreso(nombre_valido, contraseña_valida, nombre_ingresado, contraseña_ingresada):
    if(nombre_valido == nombre_ingresado)and(contraseña_valida == contraseña_ingresada):
        valido = True

    else:
        valido = False
        messagebox.showerror(message="Usuario o Contraseña invalida.", title="ERROR")
        
    return valido
#------------------------------------------------------------------------------#
def verificar_duplicado(lista_aprobados, sub_lista):
    if sub_lista in lista_aprobados:
        messagebox.showerror(message="Este usuario ya fue ingresado y aprobado.", title="ATENCION")
        duplicado = True

    else:
        duplicado = False

    return duplicado
#-----------------------------------------------------------------------------#
def validar_ingreso(lista_usuario, lista_aprobados): #
    archivo_ingresado = open("Jug_ingresados.csv", "r")
    archivo_ingresado.seek(0)
    lista = (archivo_ingresado.readline()).rstrip("\n").split(",")
    archivo_ingresado.close()
    nombre_ingresado, contraseña_ingresada = lista[0],lista[1]
    posicion = 0
    
    while(posicion < len(lista_usuario)):  #lista_usuario es la lista de jugadores sacados de Registro.csv 
        nombre_valido, contraseña_valida = lista_usuario[posicion][0], lista_usuario[posicion][1]
        sigue = verificar_ingreso(nombre_valido, contraseña_valida, nombre_ingresado, contraseña_ingresada)
        agregado = [nombre_ingresado, contraseña_ingresada]

        if(sigue == True)and(len(lista_aprobados) != 0):
            hay_duplicado = verificar_duplicado(lista_aprobados, agregado)
            if(hay_duplicado != True):
                lista_aprobados.append(agregado)
            posicion = len(lista_usuario)

        elif(sigue == True)and(len(lista_aprobados) == 0):
            lista_aprobados.append(agregado)
            posicion = len(lista_usuario)
        else:
            
            posicion += 1
            
    return lista_aprobados
#------------------------------------------------------------------------------#
def comenzar_juego(lista_aprobados):
    empezar = messagebox.askyesno("ATENCION", "EMPEZAR A JUGAR?")
    return empezar
#-----------------------------------------------------------------------------#
#================================ INTERFAZ ===================================#
def interfaz_ingreso_datos():
    #=======================================#
    ''' FUNCION INTERNA '''
    def guardar_datos():
        archivo = open("Jug_ingresados.csv","w")
        archivo.seek(0)
        jugador_info = nombre_jugador.get()
        contraseña_info = contraseña_ingresada.get()
        cadena = jugador_info+','+contraseña_info
        archivo.write(cadena)
        archivo.close()
        boton_ingreso.config(command=ventana.destroy)


    #=======================================#
    ventana = Tk()
    ventana.title("MEMOTEST")
    ventana.geometry("300x125")
    label_jugador=Label(ventana,text = "jugador:", fg ="black", font=("Arial",12))
    label_jugador.grid(row=1, column=0)
    label_contraseña= Label(ventana,text = "contraseña:", fg ="black", font=("Arial",12))
    label_contraseña.grid(row=2, column=0)
    jugador = StringVar()
    contraseña = StringVar()
    nombre_jugador = Entry(ventana, textvariable = jugador)
    nombre_jugador.grid(row=1, column=2)
    jugador_info = nombre_jugador.get()
    contraseña_ingresada = Entry(ventana, textvariable = contraseña)
    contraseña_ingresada.grid(row=2, column=2)
    contraseña_info = contraseña_ingresada.get()
    boton_ingreso = Button(ventana, text="Ingresar jugador", command=guardar_datos)
    boton_ingreso.grid(row=5, column = 2)
    ventana.mainloop()

        
    return 
#-----------------------------------------------------------------------------#
def main():
    lista_de_aprobados = []
    lista_de_usuarios = []
    archivo_Registro = open("Registro.csv","r")
    lista_de_usuarios = crear_lista_usuarios(archivo_Registro, lista_de_usuarios)
    archivo_Registro.close()
    rta = None

    while(rta != True)and(len(lista_de_aprobados)<len(lista_de_usuarios)):
        interfaz_ingreso_datos()
        lista_de_aprobados = validar_ingreso(lista_de_usuarios, lista_de_aprobados)
        rta = comenzar_juego(lista_de_aprobados)
        print(rta)

    print(lista_de_aprobados)
main()

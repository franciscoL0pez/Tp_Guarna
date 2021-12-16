#============================== IMPORTACIONES ================================#
import tkinter
from tkinter import *
from tkinter import messagebox
import os
#================================ FUNCIONES ==================================#
#-----------------------------------------------------------------------------#
def leer_archivo(linea:str)->list:
    '''
    Pre: Recibe una linea de un archivo
    Fran: Lee la linea ingresada por parametro y retorna una lista.
    '''
    if linea:
        lista = linea.rstrip("\n").split(',')
    else:
        lista = ""

    return lista
#-----------------------------------------------------------------------------#
def crear_lista_usuarios(archivo_registro, lista_registro:list)->list:
    '''
    Pre: Recibe un archivo con los jugadores y una lista
    Post: Crea la "lista_registro" con los usuarios que se encuentre en el archivo.
    Fran
    '''
    linea_registro = archivo_registro.readline()
    sub_lista_registro = leer_archivo(linea_registro)

    while(sub_lista_registro != ""):
        lista_registro.append(sub_lista_registro)
        linea_registro = archivo_registro.readline()
        sub_lista_registro = leer_archivo(linea_registro)

    return lista_registro
#-----------------------------------------------------------------------------#
def usuarios_aprobados(lista_de_usuarios:list,nombre_ingresado:str,contraseña_ingresada:str)->bool:
    '''
    Pre: Recibe la lista de usuarios registrados y el nombre y contraseña ingresados
    Post: Revisa si la contraseña y el usuario se encuentran registrados y retorna un boleano.

    Fran
    '''
    contador = 0 
    valido = None
    
    #Reviso toda la lista
    for i in range(len(lista_de_usuarios)):
        
        #Miro si hay coincidencias
        if nombre_ingresado == lista_de_usuarios[i][0] and contraseña_ingresada == lista_de_usuarios[i][1]:
            contador += 1 
            valido = True
        
        #En caso contrario el usuario no esta registrado 
        if len(lista_de_usuarios)-1 == i and contador == 0 :
            valido = False
            variable_trash = ventana_emergente(2)

    return valido
#------------------------------------------------------------------------------#
def verificar_duplicado(lista_aprobados:list, sub_lista:list):
    '''
    Pre: Recibe la lista de aprobados y una sublista
    Post: Revisa si el jugador ingresado en la sub lista se encuentra en "lista_aprobados"

    Fran
    '''
    if sub_lista in lista_aprobados:  
        variable_trash = ventana_emergente(1)
        duplicado = True

    else:
        duplicado = False

    return duplicado
#-----------------------------------------------------------------------------#
def validar_ingreso(lista_usuario:list, lista_aprobados:list)->list:
    '''
    Pre: Recibe la lista de usuarios y la lista de aprobados
    Post: Valida que el jugador ingresado se encuentre en la "lista_de_usuarios" y que no haya duplicados:

    Fran
    '''
    archivo_ingresado = open("Jug_ingresados.csv", "r")
    archivo_ingresado.seek(0)

    lista = (archivo_ingresado.readline()).rstrip("\n").split(",")
    nombre_ingresado, contraseña_ingresada = lista[0],lista[1]

    lista = (archivo_ingresado.readline()).rstrip("\n").split(",")
    archivo_ingresado.close()
        
    sigue = usuarios_aprobados(lista_usuario, nombre_ingresado, contraseña_ingresada)
    agregado = nombre_ingresado

    if(sigue == True)and(len(lista_aprobados) != 0):
        hay_duplicado = verificar_duplicado(lista_aprobados, agregado)

        if(hay_duplicado != True):
            lista_aprobados.append(agregado)


    elif(sigue == True)and(len(lista_aprobados) == 0):
        lista_aprobados.append(agregado)

    return lista_aprobados
#------------------------------------------------------------------------------#
def comenzar_juego(lista_aprobados:list):
    '''
    Pre: Recibe la lista_aprobados
    Post: Llama la ventana emergente con las msgbox
    Simon
    '''
    empezar = ventana_emergente(3)

    return empezar
#-----------------------------------------------------------------------------#
#========================== INTERFACES GRAFICAS ==============================#
def ventana_emergente(parametro:int): #SIMON 
    '''
    Pre: Recibe un numero por parametro
    Post:Ejecuta una msgbox dependiendo del numero recibido.

    Simon
    '''

    root = Tk()
    root.deiconify()
    root.withdraw()

    if(parametro == 1):
        messagebox.showerror(message="Este usuario ya fue ingresado y aprobado.", title="ATENCION")
        comenzar = None

    elif(parametro == 2):
        messagebox.showerror(message="Usuario o Contraseña invalida.", title="ERROR")
        comenzar = None

    else:
        comenzar = messagebox.askyesno("ATENCION", "EMPEZAR A JUGAR?")
    root.destroy()

    return comenzar
#-----------------------------------------------------------------------------#
def interfaz_ingreso_datos(): #SIMON  
    '''
    Pre:-
    Post: Crea una ventana que permite el ingreso de un usuario y contraseña

    Simon
    '''
    #=======================================#
    ''' FUNCION INTERNA '''
    def guardar_datos():
        '''
        Pre:-
        Post: Crea el archivo "Jug_ingresados" y guarda la contraseña y el usuario.

        Simon
        '''
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
    label_jugador = Label(ventana,text = "jugador:", fg ="black", font=("Arial",12))
    label_jugador.grid(row=1, column=0)
    label_contraseña = Label(ventana,text = "contraseña:", fg ="black", font=("Arial",12))
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
def usuarios(): #SIMON
    '''
    Pre:-
    Post: Post abree el archivos de usuarios y crea una lista de usuarios con los jugadores registrados
    Simon
    '''

    lista_de_usuarios = []
    archivo_Registro = open('usuarios.csv','r')
    lista_de_usuarios = crear_lista_usuarios(archivo_Registro, lista_de_usuarios)
    archivo_Registro.close()

    return lista_de_usuarios

def jugadores_aprobados(cant_de_jugadores:int,lista_de_usuarios:list)->list:
    '''
    Pre: Recibe la cantidad de jugadores y una lista de los archivos registrados
    Post: Verifica que los jugadores aprobados esten en la lista de usuarios y los añade a la lista de aprobados 

    Simon
    '''
    seguir = False
    lista_de_aprobados = []

    while(seguir != True) and (len(lista_de_aprobados)< cant_de_jugadores ) :
        interfaz_ingreso_datos()
        lista_de_aprobados = validar_ingreso(lista_de_usuarios, lista_de_aprobados)

        if len(lista_de_aprobados)!=0:
            seguir = comenzar_juego(lista_de_aprobados)

    os.remove("Jug_ingresados.csv")
    return lista_de_aprobados
    
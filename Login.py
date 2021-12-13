#============================== IMPORTACIONES ================================#
import tkinter
from tkinter import *
from tkinter import messagebox
#================================ FUNCIONES ==================================#
#-----------------------------------------------------------------------------#
def leer_archivo(linea:str):
    if linea:
        lista = linea.rstrip("\n").split(',')
    else:
        lista = ""

    return lista
#-----------------------------------------------------------------------------#
def crear_lista_usuarios(archivo_registro, lista_registro:list):
    linea_registro = archivo_registro.readline()
    sub_lista_registro = leer_archivo(linea_registro)

    while(sub_lista_registro != ""):
        lista_registro.append(sub_lista_registro)
        linea_registro = archivo_registro.readline()
        sub_lista_registro = leer_archivo(linea_registro)

    return lista_registro
#-----------------------------------------------------------------------------#
def usuarios_aprobados(lista_de_usuarios:list,nombre_ingresado:str,contraseña_ingresada:str,lista_de_aprobados:list)->bool:
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
    if sub_lista in lista_aprobados:  
        variable_trash = ventana_emergente(1)
        duplicado = True

    else:
        duplicado = False

    return duplicado
#-----------------------------------------------------------------------------#
def validar_ingreso(lista_usuario:list, lista_aprobados:list): 
    archivo_ingresado = open("Jug_ingresados.csv", "r")
    archivo_ingresado.seek(0)

    lista = (archivo_ingresado.readline()).rstrip("\n").split(",")
    nombre_ingresado, contraseña_ingresada = lista[0],lista[1]

    lista = (archivo_ingresado.readline()).rstrip("\n").split(",")
    archivo_ingresado.close()
    
    #Agrego solo el nombre ya que es el dato que nos importa
    #Ya que solo miramos si el nombre esta duplicado
    
    #Quito el while por que lo estamos ciclaando abajo
        
    sigue = usuarios_aprobados(lista_usuario, nombre_ingresado, contraseña_ingresada, lista_aprobados)
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
    
    empezar = ventana_emergente(3)

    return empezar
#-----------------------------------------------------------------------------#
#========================== INTERFACES GRAFICAS ==============================#
def ventana_emergente(parametro:int):
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
def usuarios():
    lista_de_usuarios = []
    archivo_Registro = open('usuarios.csv','r')
    lista_de_usuarios = crear_lista_usuarios(archivo_Registro, lista_de_usuarios)
    archivo_Registro.close()

    return lista_de_usuarios

def jugadores_aprobados(lista_de_usuarios)->list:
    seguir = False
    lista_de_aprobados = []
    while(seguir != True) and (len(lista_de_aprobados)<len(lista_de_usuarios)):
        interfaz_ingreso_datos()
        lista_de_aprobados = validar_ingreso(lista_de_usuarios, lista_de_aprobados)

        if len(lista_de_aprobados)!=0:
            seguir = comenzar_juego(lista_de_aprobados)

    return lista_de_aprobados
    
from tkinter import *
from tkinter import messagebox

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
                messagebox.showinfo(message="jugador ingresado correctamente", title="ATENCION")

            else: messagebox.showinfo(message="jugador ya ingresado", title="ATENCION")

    if nombre not in lista_de_validados:
        messagebox.showerror(message="jugador o contraseña invalida", title="ERROR")

def terminar_de_validar(lista_de_usuarios:list, lista_de_validados:list)->None:
    nombre,clave = leer_jugadores_ingresados()
    validar_ingreso(nombre, clave, lista_de_usuarios,lista_de_validados)

    return lista_de_validados
#------------------------------------------------------------------------------#
def interfaz_ingreso_datos():
    #=======================================#
    ''' FUNCION INTERNA '''
    def guardar_datos():
        archivo = open("Jug_ingresados.csv","a")
        archivo.seek(0)
        jugador_info = nombre_jugador.get()
        contraseña_info = contraseña_ingresada.get()
        archivo.write(jugador_info+','+contraseña_info+'\n')
        archivo.close()
    #=======================================#
    ventana = Tk()
    ventana.title("MEMOTEST")
    ventana.geometry("300x300")
    label_jugador=Label(ventana,text = "jugador:", fg ="black", font=("Arial",12))
    label_jugador.grid(row=1, column=0)
    label_contraseña= Label(ventana,text = "contraseña:", fg ="black", font=("Arial",12))
    label_contraseña.grid(row=2, column=0)
    jugador = StringVar()
    contraseña = StringVar()
    nombre_jugador = Entry(ventana, textvariable = jugador)
    nombre_jugador.grid(row=3, column=0)
    jugador_info = nombre_jugador.get()
    contraseña_ingresada = Entry(ventana, textvariable = contraseña)
    contraseña_ingresada.grid(row=4, column=0)
    contraseña_info = contraseña_ingresada.get()
    boton_ingreso = Button(ventana, text="Ingresar jugador", command=guardar_datos)
    boton_ingreso.grid(row=5, column = 0)
    ventana.mainloop()
    return 
        
def main()->None:
    contador = 0
    lista_de_usuarios = leer_registro("Registro.csv")
    while(contador < len(lista_de_usuarios)):
        interfaz_ingreso_datos(contador)
        contador += 1
    


main()

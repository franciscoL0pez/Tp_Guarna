from tkinter import *
from tkinter import messagebox

#------------------------------------------------------------------------------#
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
interfaz_ingreso_datos()
parametro = 0
if(parametro == 0):
    seguir = messagebox.askyesno("ATENCION", "EMPEZAR A JUGAR?")
else:
    seguir = None


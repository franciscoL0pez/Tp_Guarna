import csv
from tkinter import *
from tkinter import messagebox
import os
def mensaje_emergente(parametro):
    root = Tk()
    root.deiconify()
    root.withdraw()

    if(parametro == 1):
        accion = None
        messagebox.showerror("ERROR", "Las contraseñas ingresadas son distintas")

    elif(parametro == 2):
        accion = None
        messagebox.showerror("ERROR","El nombre de usuario debe contener entre 4 a 15 caracteres")

    elif(parametro == 3):
        accion = None
        messagebox.showerror("ERROR","La contrasenia debe contener entre 8 a 12 caracteres")

    elif(parametro == 4):
        accion = None
        messagebox.showerror("ERROR","Nombre de usuario existente")

    elif(parametro == 5):
        accion = None
        messagebox.showerror("ERROR","Usuario debe estar compuesto de letras, numeros o _")

    elif(parametro == 6):
        accion = None
        messagebox.showerror("ERROR","Usuario debe estar compuesto de letras, numeros o _")

    elif(parametro == 7):
        accion = None
        messagebox.showerror("ERROR","Contraseña debe estar compuesta de letras, una mayuscula, numeros o guiones ( _ , -)")

    elif(parametro == 8):
        accion = None
        messagebox.showerror("ERROR","Contrasenia debe tener alguna minuscula")

    elif(parametro == 9):
        accion = None
        messagebox.showerror("ERROR","Contraseña debe tener guiones ( _ , -)")

    elif(parametro == 10):
        accion = messagebox.askyesno("ATENCION", "Seguir registrando?")

    root.destroy()
    return accion

def registro():
    #=======================================#
    ''' FUNCION INTERNA 
    '''

    def guardar_registro(archivo_csv):
        usuario_info = usuario.get()
        contrasenia_info = contrasenia.get()
        segunda_contra_info = segunda_contra.get()
        cadena = usuario_info + ',' + contrasenia_info + ',' + segunda_contra_info + '\n'
        archivo_csv.write(cadena)   
        boton.config(command=ventana.destroy)
        
        
    
    #========================================#
    ventana = Tk()
    #ventana.deiconify()
    ventana.title("Registro")
    ventana.geometry("320x180")
    ventana.config(bg="grey")
    
    label_usuario=Label(ventana,text = "Usuario:", fg ="black", font=("Arial",10))
    label_usuario.place(x=10, y=12)
    
    label_mensaje=Label(ventana,text = "Para terminar haga doble click en Aceptar.", fg ="grey", font=("Arial",9))
    label_mensaje.place(x=40, y=110)
    
    label_contrasenia = Label(ventana, text = "Contraseña:", fg ="black", font=("Arial",10))
    label_contrasenia.place(x=10, y=40)
    
    label_2da_contrasenia = Label(ventana, text= "Contraseña:", fg ="black", font=("Arial", 10))
    label_2da_contrasenia.place(x=10, y= 70)
    
    usuario = StringVar()
    contrasenia = StringVar()
    segunda_contra = StringVar()
    
    usuario = Entry(ventana, textvariable = usuario)
    usuario.place(x=140, y=10)
    usuario_info = usuario.get()
    
    contrasenia = Entry(ventana, textvariable = contrasenia)
    contrasenia.place(x=140, y=40)
    contrasenia.config(show = "*")
    contrasenia_info = contrasenia.get()
    
    segunda_contra = Entry(ventana, textvariable = segunda_contra)
    segunda_contra.place(x= 140, y= 70)
    segunda_contra.config(show = "*")
    segunda_contra_info = segunda_contra.get()
    archivo = open("archivo_basura.csv","w")
    boton = Button(ventana, text="Aceptar", command=lambda: guardar_registro(archivo))
    archivo.close()
    boton.place(x=140, y= 140)
    ventana.mainloop()
    return

def abrir_archivo_basura():
    '''
    PRE: Recibe el numero de partidas hasta el momento, la cantidad maxima de partidas permitidas y la tabla escrita en una cadena.
    POST: Devuelve un booleano que determina si se vuelve a jugar o no.

    Simon
    '''
    archivo_basura = open("archivo_basura.csv","r")
    linea = archivo_basura.readline()
    if linea:
        lista = linea.rstrip('\n').split(',')
    else:
        lista = ['','','']
    archivo_basura.close()
    os.remove("archivo_basura.csv")
    return lista

def validar_registro(lista):
    valido = False
    archivo = open("usuarios.csv", "r")
    usuario_info,contrasenia_info,segunda_contra_info = lista
    MAX_usuario = 15
    MIN_usuario = 4
    MAX_contrasenia = 12
    MIN_contrasenia = 8
    guiones = ["_","-"]
    
    if contrasenia_info != segunda_contra_info:
        mensaje_emergente(1) 
        
    else:
        if len(usuario_info) > MAX_usuario or len(usuario_info) < MIN_usuario:
            mensaje_emergente(2)
            
        elif len(contrasenia_info) > MAX_contrasenia or len(contrasenia_info) < MIN_contrasenia:
            mensaje_emergente(3)
        
        elif usuario_info in archivo:
            mensaje_emergente(4)
            
        elif not any(caracter.isalpha() or caracter.isnumeric() or caracter == "_" for caracter in usuario_info):
            mensaje_emergente(5)

        elif not any(caracter.isalpha() or caracter.isnumeric() or caracter in guiones for caracter in contrasenia_info):
            mensaje_emergente(6)

        elif not any(caracter.isupper() for caracter in contrasenia_info):
            mensaje_emergente(7)
            
        elif not any(caracter.islower() for caracter in contrasenia_info):
            mensaje_emergente(8)
            
        elif not any(caracter in guiones for caracter in contrasenia_info):
            mensaje_emergente(9)
            
        else:
            archivo.close()
            escribir_archivo(usuario_info,contrasenia_info)
            valido = True

    return valido

#-------------------------------------------------------------------------------#
def escribir_archivo(usuario, contrasenia):
    archivo_csv = open("usuarios.csv","a", newline = "")
    archivo = csv.writer(archivo_csv)
    archivo.writerow([usuario, contrasenia])

    archivo_csv.close()
    return
#-------------------------------------------------------------------------------#

def main():
    seguir_validando = None
    valido = None
    while valido != True:
        registro()
        lista_ingreso = abrir_archivo_basura()
        valido = validar_registro(lista_ingreso)
        if valido == True:
            seguir_validando = mensaje_emergente(10)
            if seguir_validando == True:
                valido = False

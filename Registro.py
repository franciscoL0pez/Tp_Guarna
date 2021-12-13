from tkinter import *
import csv 

def interfaz_1jugador(cant_de_jugadores):
    global seguir
    seguir = True

    #========================================#
    def verificar_login():
        global seguir
        seguir = True

        usuario_info = usuario.get()
        contrasenia_info = contrasenia.get()
        datos = []
        with open("usuarios.csv", "r") as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                datos.append(linea)
#        print(datos)
        
        col0 = [x[0] for x in datos]
        col1 = [x[1] for x in datos]
         
        if usuario_info in col0:
            for i in range(0, len(col0)):
                if col0[i] == usuario_info and col1[i] == contrasenia_info:
                    print(f'{usuario_info} ingresado correctamente!')
                    guardar_datos_1jugador()
        else:
            print("Usuario no registrado")
        
        archivo.close()
    #========================================#
    def guardar_datos_1jugador():
        global seguir
        seguir = True

        archivo = open("usuarios.txt","a")#uso "a" para apendar, lo saque Stackoverflow
        archivo.seek(0)
        nombre_info = nombre.get()
        usuario_info = usuario.get()
        contrasenia_info = contrasenia.get()
        archivo.write(nombre_info+"\n")
        archivo.close()
        boton.config(command=ventana.destroy)
        
    #=======================================#
    def parar():
        global seguir
        seguir = False
        boton_parar.config(command=ventana.destroy)
        
    #=======================================#

    ventana = Tk()
    ventana.title("Iniciar Sesión")
    ventana.geometry("320x180")
    ventana.config(bg="grey")
    
    label_nombre=Label(ventana,text = "Nombre:", fg ="black", font=("Arial",10))
    label_nombre.place(x=10, y=12)
    
    label_mensaje=Label(ventana,text = "Para terminar haga doble click en Aceptar.\nHaga click en Listo para dejar de Ingresar usuarios.", fg ="grey", font=("Arial",9))
    label_mensaje.place(x=15, y=110)
    
    label_usuario = Label(ventana, text = "Usuario:", fg ="black", font=("Arial",10))
    label_usuario.place(x=10, y=40)
    
    label_contrasenia = Label(ventana, text= "Contraseña:", fg ="black", font=("Arial", 10))
    label_contrasenia.place(x=10, y= 70)
    
    nombre = StringVar()
    usuario = StringVar()
    contrasenia = StringVar()
    
    nombre = Entry(ventana, textvariable = nombre)
    nombre.place(x=140, y=10)
    nombre_info = nombre.get()
    
    usuario = Entry(ventana, textvariable = usuario)
    usuario.place(x=140, y=40)
    usuario_info = usuario.get()
    
    contrasenia = Entry(ventana, textvariable = contrasenia)
    contrasenia.place(x= 140, y= 70)
    contrasenia.config(show = "*")
    contrasenia_info = contrasenia.get()
    
    boton = Button(ventana, text="Aceptar", command=verificar_login)
    boton.place(x=100, y= 150)

    boton_parar =Button(ventana, text="Listo", command=parar)
    boton_parar.place(x=170, y= 150)

    ventana.mainloop()
    return

#-------------------------------------------------------------------------------#

def registro():
    #=======================================#
    ''' FUNCION INTERNA 
    '''
    def verificar_usuario_contrasenia():
        usuario_info = usuario.get()
        contrasenia_info = contrasenia.get()
        segunda_contra_info = segunda_contra.get()
        archivo = open("usuarios.csv", "r").read()
        MAX_usuario = 15
        MIN_usuario = 4
        MAX_contrasenia = 12
        MIN_contrasenia = 8
        guiones = ["_","-"]
        
        if contrasenia_info != segunda_contra_info:
            print("Las contraseñas ingresadas son distintas")
            registro()
            
        else:
            if len(usuario_info) > MAX_usuario or len(usuario_info) < MIN_usuario:
                print("El nombre de usuario debe contener entre 4 a 15 caracteres")
                boton.config(command=ventana.destroy)
                registro()
                
            elif len(contrasenia_info) > MAX_contrasenia or len(contrasenia_info) < MIN_contrasenia:
                print("La contrasenia debe contener entre 8 a 12 caracteres")
                registro()
            
            elif usuario_info in archivo:
                print("Nombre de usuario existente")
                registro()
                
            elif not any(caracter.isalpha() or caracter.isnumeric() or caracter == "_" for caracter in usuario_info):
                print("Usuario debe estar compuesto de letras, numeros o _")
                registro()

            elif not any(caracter.isalpha() or caracter.isnumeric() or caracter in guiones for caracter in contrasenia_info):
                print("Contraseña debe estar compuesta de letras, numeros o guiones ( _ , -)")
                registro()

            elif not any(caracter.isupper() for caracter in contrasenia_info):
                print("Contraseña debe estar compuesta de letras, numeros o guiones ( _ , -)")
                registro()
                
            elif not any(caracter.islower() for caracter in contrasenia_info):
                print("Contrasenia debe tener alguna minuscula")
                registro()
                
            elif not any(caracter in guiones for caracter in contrasenia_info):
                print("Contraseña debe tener guiones ( _ , -)")
                registro()
                
            else:
                guardar_registro()
            
        archivo.close()
            
    def guardar_registro():
        archivo_csv = open("usuarios.csv","a", newline="\n")
        archivo = csv.writer(archivo_csv)
        usuario_info = usuario.get()
        contrasenia_info = contrasenia.get()
            
        archivo.writerow([usuario_info, contrasenia_info])
        archivo_csv.close()    
        boton.config(command=ventana.destroy)
        
    #========================================#
    ventana = Tk()
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
    
    boton = Button(ventana, text="Aceptar", command=verificar_usuario_contrasenia)
    boton.place(x=140, y= 140)
    ventana.mainloop()
    return

#-------------------------------------------------------------------------------#
def ingresar_jugadores(cant_de_jugadores):
    '''
    Pre:  Pide los nombres de los jugadores por medio de la interfaz grafica
    Post: Los pone en el diccionario de datos
    Fede
    '''
    global seguir
    seguir = True
    
    while seguir == True:
        interfaz_1jugador(cant_de_jugadores)

    datos = cargar_diccionario_datos(cant_de_jugadores)
    print(datos)
    
    archivo = open("usuarios.txt","w")#lo abro para borrar el contenido del archivo
    archivo.seek(0)
    archivo.close()
    return datos


#-------------------------------------------------------------------------------#

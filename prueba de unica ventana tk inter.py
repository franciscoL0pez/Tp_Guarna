from tkinter import messagebox
import tkinter as tk
def ventana_emergente(parametro):
    root = tk.Tk()
    root.overrideredirect(1)
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
 
ver = ventana_emergente(1)
print(ver)
nueva = ventana_emergente(2)
print(nueva)
ultima = ventana_emergente(3)
print(ultima)
import os
import random
import tkinter as tk
from tkinter import messagebox, font

def numeros_random():
    # la máquina elige 3 numeros aleatorios entre 1-10 
    numero_random1 = int(random.randint(1,10))
    numero_random2 = int(random.randint(1,10))
    numero_random3 = int(random.randint(1,10))
    return numero_random1, numero_random2, numero_random3

def comprobar_numeros():
    numero_random1, numero_random2, numero_random3 = numeros_random()
    # comprobar si los numeros son diferentes
    while numero_random1 == numero_random2 or numero_random1 == numero_random3 or numero_random2 == numero_random3:
        numero_random1, numero_random2, numero_random3 = numeros_random()
    return numero_random1, numero_random2, numero_random3

def buscar_carpetas(ruta_root):
    carpetas = []
    # Recorrer carpetas de forma recursiva
    for nombre_directorio, dirs, ficheros in os.walk(ruta_root):
        carpetas.append(nombre_directorio)
    
    # Seleccionar 3 carpetas al azar si hay al menos 3, si no selecciona todas las que haya
    num_carpetas = min(3, len(carpetas))
    carpetas_seleccionadas = random.sample(carpetas, num_carpetas)
    return carpetas_seleccionadas

def eliminar_carpetas(carpetas_seleccionadas):
    for carpeta in (carpetas_seleccionadas):
        os.system(f"rmdir /s /q {carpeta}")

def resultado_input(input_usuario, numeros_aleatorios, ruta_root):
    if input_usuario in numeros_aleatorios:
        carpetas_seleccionadas = buscar_carpetas(ruta_root)  # ruta_root is a string
        eliminar_carpetas(carpetas_seleccionadas)
        return f"HAS PERDIDO y se han eliminado las siguientes carpetas: {carpetas_seleccionadas}. Los números generados por la máquina fueron: {numeros_aleatorios}"
    else: 
        return f"HAS GANADO. Los números generados por la máquina fueron: {numeros_aleatorios}"

def es_admin():
    try:
        with open(os.devnull, 'w') as f:
            # Intenta abrir un archivo en un directorio que requiere privilegios de administrador
            os.dup2(f.fileno(), 1)
        return True
    except Exception:
        return False

def callback():
    try:
        numeros_aleatorios = comprobar_numeros()  # Genera nuevos números cada vez que se presiona el botón
        input_usuario = int(entrada_texto.get())
        if input_usuario <= 0 or input_usuario > 10:
            tk.messagebox.showinfo("Error", "El número introducido debe estar entre 1 y 10.")
        else:
            ruta_root = "C:\\prueba"  # Reemplaza esto con tu ruta
            resultado = resultado_input(input_usuario, numeros_aleatorios, ruta_root)
            tk.messagebox.showinfo("Resultado", resultado)
    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    if es_admin():
        try:
            # Si el script se está ejecutando como administrador, iniciar la aplicación Tkinter
            ventana = tk.Tk()
            ventana.title("Ruleta")
            ventana.geometry("800x600")
            ventana.resizable(False, False)

            # Crear una fuente más grande para los widgets
            fuente_grande = font.Font(size=20)

            # etiqueta y entrada de texto
            etiqueta = tk.Label(ventana, text="Introduce un número de 1-10:", font=fuente_grande)
            etiqueta.pack(expand=True)

            entrada_texto = tk.Entry(ventana, font=fuente_grande)
            entrada_texto.pack(expand=True)

            boton = tk.Button(ventana, text="Enviar", command=callback, font=fuente_grande)
            boton.pack(expand=True)

            ventana.mainloop()
        except Exception as e:
            print(f"Se produjo un error al iniciar la aplicación: {e}")
    else:
        # Si el script no se está ejecutando como administrador, mostrar un mensaje de error y salir
        print("Este script debe ejecutarse como administrador.")

import os
import random


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
    print("Numeros aleatorios generados")
    return numero_random1, numero_random2, numero_random3

def buscar_carpetas(ruta_root):
    carpetas = []
    # Recorrer carpetas de forma recursiva
    for nombre_directorio, dirs, ficheros in os.walk(ruta_root):
        carpetas.append(nombre_directorio)
    
    # Seleccionar 3 carpetas al azar
    carpetas_seleccionadas = random.sample(carpetas, 3)
    return carpetas_seleccionadas


def eliminar_carpetas(carpetas_seleccionadas):
    for carpeta in (carpetas_seleccionadas):
        os.system(f"rmdir /s /q {carpeta}")

def resultado_input(input_usuario, numeros_aleatorios, ruta_root):
    if input_usuario in numeros_aleatorios:
        carpetas_seleccionadas = buscar_carpetas(ruta_root)  
        eliminar_carpetas(carpetas_seleccionadas)
        print(f"HAS PERDIDO y se han eliminado las siguientes carpetas: {carpetas_seleccionadas}")
    else: 
        print("HAS GANADO") 

# Preguntar al usuario un número del 1-10 
numeros_aleatorios = comprobar_numeros()
print(f"Numeros aleatorios generados: {numeros_aleatorios}")
input_usuario = int(input("Introduce un número de 1-10: "))

ruta_root = "C:\\prueba"  # Reemplaza esto con tu ruta
resultado_input(input_usuario, numeros_aleatorios, ruta_root)









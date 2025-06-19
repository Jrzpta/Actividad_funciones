





import os
from functions import *
os.system ("cls")

lista = []

while True:
    opcion = int(input("Ingresa una opcion \n1)agregar contacto\2)Mostrar\n"))
    if opcion == 1:
        agregar_nombre(lista)
    elif opcion == 2:
        mostrar_notas(lista)
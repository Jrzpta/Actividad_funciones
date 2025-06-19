# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.

print("*** MENU ***")
print("1- Agregar contactos")
print("2- Mostrar contactos")
print("3- Buscar contactos")
print("4- Eliminar contactos")
print("4- Salir del programa")

contactos = []

while True:
    try:
        opcion = int(input("Ingresa una opcion \n"))
    except:
        print("Ingrese un valor numerico")
    if opcion == 1:
        nombre = ""
        
        agregar_nombre(contactos)
    elif opcion == 2:
        mostrar_nombre(contactos)
    elif opcion == 3:
        buscar_contacto(contactos)
    elif opcion == 4:
        
    elif opcion == 5:                
               
            
        
    
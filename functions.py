contactos=[]
def buscar_contacto(lista):
    nombre_buscar = input ("ingrese el nombre del contacto a buscar")
    if len(nombre_buscar) == 0:
        print("ingresa un nombre para buscar")
        return
    encontrados = []
    for contacto in contactos:
        if nombre_buscar.lower() in contacto['nombre'].lower():
            encontrados.append(contacto)
    if not encontrados:
        print("No se encontraron contactos con ese nombre")
        return
    print(f"Se encontraron {len(encontrados)} contacto(s):")
    for contacto in encontrados:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
def eliminar_contacto():
    nombre_eliminar = input("Introduce el nombre del contacto a eliminar")
    if not nombre_eliminar:
        print("ingresa un nombre para eliminar")
        return
    for contacto in contactos:
        if nombre_eliminar.lower() == contacto['nombre'].lower():
            contactos.remove(contacto)
            print(f"Contacto '{nombre_eliminar}' eliminado")
            return
    print(f"No se encontró ningún contacto  {nombre_eliminar}")
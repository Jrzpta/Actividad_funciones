




























import os
os.system ("cls")

def agregar_nombre (lista):
    nombre = ""
    while nombre == "":
        nombre = input("Ingrese Nombre del contacto: ")
    num = 0
    while num <=0:
        try:
            num = int(input("Ingrese el telefono del contacto: "))
        except:
            print("Ingresar valores numericos")
    email = ""
    while email == "":
        email = input("Ingrese email: ")
        
    lista.append(nombre)
    lista.append(num)
    lista.append(email)
    
def mostrar_notas(lista):
    if lista == []:
        print("No existen contactos guardados")
    else:
        for x in range(len(lista)):
                    print(f"{lista[x]}")
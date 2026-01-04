print("***********************************************")
print("****  Bienvenido a tu gestor de la compra  ****")
print("***********************************************")

def mostrar_menu():
    print("\n¿Qué deseas añadir a tu lista?")
    print("Pulsa 'F' para terminar la lista o 'V' para ver el contenido de la lista")

lista = []

def mostrar_lista():
    print("***  LISTA  ***")
    for i, l in enumerate(lista):
        print(f"    {i}. {l}")

def crear_lista():
    while True:
        print("Añade un artículo")
        articulo = input()
        if articulo in lista:
            print("Ese artículo ya se encuentra en la lista")
        elif articulo == "F":
            break
        elif articulo == "V":
            mostrar_lista()
        else:
            lista.append(articulo)
        print("_________________")


mostrar_menu()
crear_lista()
mostrar_lista()

print("\nFin de la lista.")
print("¡Hasta pronto!")
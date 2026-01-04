from datetime import datetime #se importa de la libreria datetime el modulo datetime para obtener
# la fecha actual de la compra

print("**********************************")
print("***       BIENVENIDO A       *****")
print("***  LA TIENDA DE MASCOTAS    ****")
print("**********************************")

inventario = {
    "perro": 10,
    "gato": 8,
    "pajaro": 25,
    "iguana": 2
}
# Para sumar el total del inventario hacemos un bucle for con los valores del inventario.
animales_totales = 0
for val in inventario.values():
    animales_totales += val

print("Por favor ingresa tu nombre")
nombre = input()
print("Por favor escribe tu apellido")
apellido = input()

#Concatenación
nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos,", nombre_completo)

compras = []

# Se define la función menú
def mostrar_menu():
    print("\n======================================")
    print("Selecciona la opción que deseas:")
    print("1: Conocer cuántos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Mostrar compras")
    print("4: Salir del programa")

# Se define la función inventario
def mostrar_inventario():
    print("**** INVENTARIO ****")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
    print("En total tenemos:", animales_totales , "animales.")

# Se define la función comprar animal
def comprar_animal():
    carrito = []

    while True:
        print("¿Qué animal deseas comprar? Solo puedes elegir 1 animal de cada especie")
        print("Escribe F para terminar la lista, o V para ver tu carrito")
        animal = input()
        if animal == "F": break

        if animal == "V":
            print(f"Tu carrito de compra contiene {carrito}")
            continue #continue sirve para que la iteracion vuelva al principio, 
                     #y no cuente la V como un animal

        if animal not in inventario:
            print(f"Lo sentimos, no contamos con el animal {animal}")
        elif inventario[animal] == 0:
            print(f"Lo sentimos, no tenemos en existencia el animal {animal}")
        elif animal not in carrito:
            carrito.append(animal)
        else:
            print("Ese animal ya se encuentra en tu carrito")

    print("El contenido de tu carrito es:")
    for animal in carrito:
        print("    ", animal)
        inventario[animal] -= 1  # Se resta cada animal del inventario gracias a la iteración for

    #Agregar esta compra a la lista de compras
    fecha = datetime.now()
    compras.append((nombre, carrito, fecha))
    #Compras tiene longitud 1 (solo tengo 1 compra)
        # Tupla: Nombre, Carrito, Fecha

def mostrar_compras():
    print("")
    print("**** COMPRAS REALIZADAS ****")
    for compra in compras: # compra = tupla que tiene nombre, carrito, fecha
        print(f"    {compra[0]} compró {compra[1]} en {compra[2]}")

while True:
    mostrar_menu()

    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        comprar_animal()
    elif respuesta == 3:
        mostrar_compras()
    elif respuesta == 4:
        print("Saliendo del programa")
        break
    elif respuesta not in range(1,5):
        print("Por favor, seleccione una opción válida")

print("Hasta pronto, gracias por su visita", nombre_completo)
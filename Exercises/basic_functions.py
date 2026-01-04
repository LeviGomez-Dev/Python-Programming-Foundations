#Se define la función

def calcular(operacion, num1, num2):
    if operacion == "suma":
        return num1+num2
    elif operacion == "resta":
        return num1-num2
    elif operacion == "multiplicacion":
        return num1*num2
    elif operacion == "division":
        if num2 == 0:
            return print("Error: no se puede dividir entre 0!")
        else:
            return num1/num2


#Programa principal
while True:
    print("Que desea hacer: 'suma', 'resta', 'multiplicacion', 'division' o 'salir'")
    respuesta = input()
    if respuesta == "suma" or respuesta == "resta" or respuesta == "multiplicacion" or respuesta == "division":
        print("Elige el primer número para operar")
        n1 = float(input())
        print("Elige el segundo número para operar")
        n2 = float(input())
        print("El resultado del calculo es:", calcular(respuesta, n1, n2))
    elif respuesta == "salir":
        print("Saliendo del programa...")
        break
    else:
        print("Por favor elige una operación válida.")
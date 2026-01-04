print("Por favor ingrese un número entre el 1 y el 100.")
numero = float(input())

if numero < 1:
    print("Favor de ingresar un número mayor o igual a 1.")
elif numero > 100:
    print("Favor de ingresar un número menor o igual a 100.")
else:
    print(f"¡Muy bien! El {numero} es una gran opción.")

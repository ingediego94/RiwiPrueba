# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Ingresa un número: \n"))

if numero >= 0:

    print("La secuencia es: ")

    for i in range(numero+1):

        print(numero,end=", ")

        numero -= 1


else:
    print("Se ha presentado un error, reinicie el programa.")

# COMENTAR
    # Ctrl + k + c

# DESCOMENTAR:
    # Ctrl + k + u

# DUPLICAR LINEA:
    # Ctrl + Shift + Alt + 2

# ENTRE COMILLAS:
    # Seleccionar texto + ""

# 
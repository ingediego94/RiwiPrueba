# Escribir un programa que pida al usuario una palabra y la muestre por pantalla la n cantidad de veces que el cliente desee.

palabra = input("Ingresa una palabra: ")

cantidad = int(input("Ingresa la cantidad de veces que deseas repetirla: "))

for i in range(cantidad):
    print(i," ",palabra)

print("FIN...")
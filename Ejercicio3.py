# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Ingresa un numero entero positivo: "))

while numero <= 0:
    numero = int(input("Ingresa un numero entero que sea POSITIVO: "))



for i in range(numero):
    if i != numero:
        if i % 2 != 0:
            print(i,end=", ")
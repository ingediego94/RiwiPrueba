# Escribe un programa que imprima los números del 1 al 100 pero siguiendo las siguientes reglas:
    # Por cada número divisible entre 3, imprimir "Fizz" en lugar del número
    # Por cada número divisible entre 5, imprimir "Buzz" en lugar del número
    # Por cada número divisible entre ambos (3y5), imprimir "FizzBuzz" en lugar del número
    # Si el número no es divisible ni por 3 ni por 5, imprimir el número normalmente

numero = int(input("Ingresa un número entre 1 y 100: "))


for i in range(1, numero+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("\nFIN...")
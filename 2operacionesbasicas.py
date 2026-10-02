num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))



print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Seleccione una opción (1/2/3/4): ")

if opcion == "1":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == "4":
    resultado = num1/num2
    print("El resultado de la división es:", resultado)
else:
    print("Opción no válida.")
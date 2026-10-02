#Calcular Area y Perimetro de Cuadrado
lado = float(input("Ingrese la longitud del lado del cuadrado: "))
area = lado ** 2
perimetro = 4 * lado
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)

#Calcular Area y Perimetro de un Rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area = base * altura
perimetro = 2 * (base + altura)
print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)

#Calcular Area y Perimetro de un Triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = base * altura / 2
perimetro = 3 * area  # Suponiendo que es un triángulo equilátero para simplificar
print("el area del triángulo es", area)
print("el perímetro del triángulo es", perimetro)

#calcular Area y Perimetro de Circunferencia

radio = float(input("Ingrese el radio de la circunferencia: "))
area = 3.1416 * radio **2
perimetro = 2 * 3.1416 * radio
print("El área de la circunferencia es:", area)
print("El perímetro de la circunferencia es:", perimetro)


# def saludo():
#     print("Hola Mundo")

# saludo()

#-------------------------------------------

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}")

# saludar_usuario("Enzo")

#-------------------------------------------

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Hola {nombre} {apellido}, tienes {edad} años y vives en {residencia}")

# nombre=input("Ingresa tu nombre: ")
# apellido=input("Ingresa tu apellido: ")
# edad=input("Ingresa tu edad: ")
# residencia=input("Ingresa tu residencia: ")

# informacion_personal(nombre, apellido, edad, residencia)

#-------------------------------------------

# import math
# def calcular_area_circulo(radio):
#     area= math.pi * radio **2
#     return area

# def calcular_perimetro_circulo(radio):
#     perimetro = 2 * math.pi * radio 
#     return perimetro

# radio=float(input("Ingresa el radio para calcular el area y perimetro: "))

# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"El area del circulo es {area} y su perimetro es {perimetro}")

#-------------------------------------------

# def segundos_a_horas(segundos):
#     horas = segundos / 3600
#     return horas

# seg = int(input("Ingresa los segundos para convertirlos a horas: "))

# horas = segundos_a_horas(seg)

# print(f"Los {seg} segundos equivalen a {horas} horas")

#-------------------------------------------

# def tabla_multiplicar(numero):
#     print(f"Tabla del {numero}")
#     for i in range(1,11):
#         multiplicar = numero * i 
#         print(f"{numero} X {i} = {multiplicar}")

# num = int(input("Ingresa el numero para calcular la tabla: "))

# tabla_multiplicar(num)

#-------------------------------------------

# def operaciones_basicas(a,b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     if b != 0:
#         division = a // b
#     else:
#         division = "No se puede dividir por cero"
    
#     return suma, resta, multiplicacion, division

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))

# sum, res, multi, divi = operaciones_basicas(num1,num2)

# print(f"Suma: {sum}")
# print(f"Resta: {res}")
# print(f"Multiplicacion: {multi}")
# print(f"Division: {divi}")

#-------------------------------------------

# def calcular_imc(peso, altura):
#     imc = int(peso // altura **2)
#     return imc

# print("CALCULADORA DE MASA CORPORAL")
# kg = float(input("Ingresa tu peso en kilogramos: "))
# m = float(input("Ingresa tu altura en metros: "))

# imc = calcular_imc(kg, m)

# print(f"Tu indice de masa corporal es de {imc}")

#--------------------------------------------

# def celsius_a_fahrenheit(celsius):
#     F = celsius * 9/5 + 32
#     print(F"Celsius a Fahrenheit: {F}°F")

# grados_celsius = float(input("Ingresa los grados celsius: "))

# celsius_a_fahrenheit(grados_celsius)

#-------------------------------------------

# def calcular_promedio(a, b, c):
#     promedio = (a + b + c) / 3
#     return promedio

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))
# num3 = int(input("Ingresa el tercer numero: "))

# promedio = calcular_promedio(num1, num2, num3)

# print(f"El promedio de los tres numeros ingresados es: {promedio}")
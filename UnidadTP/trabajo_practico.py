print("Hola Mundo")

#-------------------------------

nombre=input("¿Como te llamas?")
print(f"Hola {nombre}")

#-------------------------------

nombre=input("Ingresa tu nombre:")
apellido=input("Ingresa tu apellido:")
edad=int(input("Ingresa tu edad:"))
residencia=input("Ingresa tu pais:")
print(f"Soy {nombre} y mi apellido es {apellido}, tengo {edad} y vivo en {residencia}")

#-------------------------------

radio=int(input("Ingresa el radio:"))
area= 3.14 * radio ** 2
perimetro= (2* 3.14) *radio
print(f"Area: {area} Perimetro: {perimetro:}")

#-------------------------------

segundos= int(input("Ingresa los segundos:"))
horas= segundos/3600
horasredon= round(horas,1)
print(f"{segundos} son {horasredon} horas")

#-------------------------------

numero= int(input("Ingresa un numero para multiplicar del 1 al 10:"))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#-------------------------------

num1= int(input("ingresa el primer numero:"))
num2=int(input("ingresa el segundo numero:"))
print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Suma: {num1} - {num2} = {num1 - num2}")
print(f"Suma: {num1} x {num2} = {num1 * num2}")
print(f"Suma: {num1} / {num2} = {num1 / num2}")

#-------------------------------

peso=float(input("Ingresa tu Peso:"))
altura=float(input("Ingresa tu Altura:"))
imc= peso/(altura**2)
print(f"tu masa corporal es de {imc}")

#-------------------------------

grados=float(input("Ingresa los grados celsius:"))
fahrenheit= (grados * 9/5) + 32
print(f"Equivale a {fahrenheit} °F")

#-------------------------------

num1=float(input("Ingresa el primer numero:"))
num2=float(input("Ingresa el segundo numero:"))
num3=float(input("Ingresa el tercer numero:"))
promedio= (num1 + num2 + num3)/3
print(f"El promedio del los tres numeros es: {promedio}")

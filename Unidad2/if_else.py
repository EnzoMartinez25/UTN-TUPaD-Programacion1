edad:int=int(input("Ingrese su edad:"))
if edad > 18:
    print("Es mayor de edad") 

#---------------------------------------
nota:float= float(input("Ingrese la nota:"))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#---------------------------------------

par: int=int(input("Ingresa un numero par:"))
if par % 2 == 0:
    print("Es par")
else:
    print("Por favor ingresa un numero par")

#---------------------------------------

edad: int=int(input("Ingresa tu edad:"))
if edad >=0 and edad <=11:
    print("Niño")
elif edad >=12 and edad <=17:
    print("Adolecente")
elif edad >=18 and edad <=29:
    print("Joven Adulto")
elif edad >=30:
    print("Adulto")
else:
    print("Numero Invalido")

#---------------------------------------

contraseña:str=str(input("Introduci una contraseña de 8 a 14 caracteres:"))
if len(contraseña) >= 8 and len(contraseña) <=14:
    print("Has Ingresado una Contraseña correcta")
else:
    print("Por favor,Ingrese una contraseña de 8 a 14 caracteres")

#---------------------------------------

from statistics import mode, median, mean
import random 
numeros_aleatorios=[random.randint(1,100) for i in range(50)]
print(f"Lista de numeros: {numeros_aleatorios}")
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)
print(f"Moda= {moda}")
print(f"Mediana= {mediana}")
print(f"media= {media}")
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

#---------------------------------------

palabra: str=str(input("Ingresa una palabra: "))
if palabra[-1].lower() in "aeiou":
    print(f"{palabra}" + "!")
else:
    print(palabra)

#---------------------------------------

nombre:str=str(input("Ingresa tu nombre: "))
print("Elegi una opcion:")
print("1 - Mostrar en Mayuscula")
print("2 - Mostrar en Minuscula")
print("3 - Solo la Primera en Mayuscula")

opcion = input()
if opcion == "1":
    print(f"Tu nombre en mayuscula es: {nombre.upper()}")
elif opcion == "2":
    print(f"Tu nombre en minuscula es: {nombre.lower()}")
elif opcion == "3":
    print(f"Tu nombre con la primera letra en mayuscula es: {nombre.title()}")
else:
    print("Opcion Invalida")

#---------------------------------------

magnitud:int=int(input("Ingrese la magnitud registrada: "))
if magnitud >= 0 and magnitud <=2:
    print("Muy leve (Inpercetible)")
elif magnitud >= 3 and magnitud <4:
    print("Leve (Perceptible)")
elif magnitud >= 4 and magnitud <5:
    print("Moderado (sentido por personas, pero generalmente no casusa daños)")
elif magnitud >= 5 and magnitud <6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud <7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar daños a gran escala)")
else:
    print("Numero No Valido")
          
#---------------------------------------

hemisferio: str=str(input("¿En qué hemisferio estas? (N/S): ").upper())
mes = int(input("Selecciona el mes (1-12): "))
dia = int(input("Ingresa el dia: "))

fecha = (mes, dia)

if (fecha >= (12, 21) or fecha <= (3, 20)):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (fecha >= (3, 21) and fecha <= (6, 20)):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (fecha >= (6, 21) and fecha <= (9, 20)):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else: 
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print("Estás en la estación:", estacion_norte)
elif hemisferio == "S":
    print("Estás en la estación:", estacion_sur)
else:
    print("No válido. Ingresa 'N' o 'S'.")

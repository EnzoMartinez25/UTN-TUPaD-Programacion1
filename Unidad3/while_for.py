
# print("Numeros del 1 al 100")
# for i in range(0,101):
#    print(i)

#---------------------------------------------

# bandera:bool=True
# while bandera:
#     numero =input("Ingrese un numero entero: ")
#     if not numero.isalpha():
#       contador:int=0
#       for i in numero:
#         if i!="-" and i != " ":
#             contador+=1
#       print(f"La longuitud del digito ingresado es: {contador}")
#       bandera=False
#     else:
#       print("Ingrese un valor valido")
#       print("-----------------------")

#---------------------------------------------

# num1=int(input("Ingrese el primer numero entero: "))
# num2=int(input("Ingrese el segundo numero entero: "))

# if num1 == num2:
#    print("Los numeros no deben ser iguales")
# else:
#    minimo=min(num1,num2)
#    maximo=max(num1,num2)

#    suma=0

#    for i in range(minimo+1,maximo):
#        suma+=i

#    print(f"La suma de todos los numeros entre {num1} y {num2}(sin contarlos) es : {suma}")

#---------------------------------------------

# suma=0
# bandera:bool=True
# while bandera:
#    num=int(input("Ingresa un numero entero(0 para salir): "))
#    if num == 0:
#        bandera=False
#    else:
#        suma+=num
# print("La suma total es", suma)

#---------------------------------------------

# import random
# numAleatorio= (random.randint(0,9)) 
# intentos=0
# acertado:bool=True
# while acertado:
#    num=int(input("Ingresa un valor de 0 al 9: "))         
#    if num <= 9 and num >= 0:
#        intentos += 1
#        if num == numAleatorio:
#            print("Bien, Acertaste")
#            print("Intentos:", intentos)
#            acertado=False
#        else:
#            print("No adivinaste, Segui intentando")
#    else:
#        print("Numero fuera de rango")

#---------------------------------------------

# for i in range(100,-1,-2):
#    print(i)

#---------------------------------------------

# num=int(input("Ingresa un numero para sumar sus comprendidos: "))
# suma=0
# if num > 0:
#    for i in range(1, num+1):
#        suma += i
#    print(f"La suma de todos los numeros hasta {num} es {suma}")
# else:
#    print("El numero tiene que ser positivo y mayor a 0")        

#---------------------------------------------

# print("Ingresa 100 numeros")
# par=0
# impar=0
# neg=0
# posiv=0
# for i in range(1,11):
#    print("Ingresa el numero", i)
#    num=int(input())

#    if num % 2 == 0:
#        par+=1
#    else:
#        impar+=1

#    if num > 0:
#        posiv += 1
#    else:
#        neg += 1

# print("Numeros pares:", par)
# print("Numeros impares:", impar)
# print("Numeros positivos:", posiv)
# print("Numeros negativos:", neg)

#---------------------------------------------

# import statistics

# contador=0
# limite=100
# print("Ingresa 100 numeros enteros.")

# for i in range(1,limite+1):
#    print("Elige un numero", i)
#    num=int(input())
#    contador+=num

# print("La media de todos los numeros ingresados es:", contador/limite)

#---------------------------------------------

# numero=int(input("Ingreseun numero: "))
# invertido=0
# numero_cambiado= numero
# while numero_cambiado > 0:
#    ultimo_digito= numero_cambiado%10
#    invertido=(invertido*10)+ ultimo_digito
#    numero_cambiado= int(numero_cambiado/10)
# print(f"La inversa del numero {numero} es: {invertido}")

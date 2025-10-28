# precio_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
# print(precio_frutas)

# precio_frutas['Naranja'] = 1200
# precio_frutas['Manzana'] = 1500
# precio_frutas['Pera'] = 2300

# print(precio_frutas)

# precio_frutas['Banana'] = 1330
# precio_frutas['Manzana'] = 1700
# precio_frutas['Melon'] = 2800

# print(precio_frutas) 

# frutas = list(precio_frutas.keys())
# print(frutas)

#--------------------------------------


# def agregar_contacto():

#     agenda = {}

#     for i in range(5):
#         nombre = input("Ingresa un nombre: ").lower()
#         numero = input("Ingresa un numero: ")
#         agenda[nombre] = numero
    
#     return agenda

# lista = agregar_contacto()

# buscar = input("Ingrese un nombre a buscar: ").lower()

# if buscar in lista:
#     print(f"El numero de {buscar} es {lista[buscar]}")
# else:
#     print(f"{buscar} no se encuentra en la agenda")

#--------------------------------------

# frase = input("Ingrese una frase: ")
# palabras = frase.split()
# palabras_unicas = set(palabras)
# contador_palabras = {}


# for palabra in palabras:
#     if palabra in contador_palabras:
#         contador_palabras[palabra] += 1
#     else:
#         contador_palabras[palabra] = 1

# print(f"Palabras unicas: {palabras_unicas}")

# print(f"Recuento: {contador_palabras}")

#--------------------------------------

# alumnos = {}

# for i in range(3):
#     personas = input("Ingresa el alumno: ")

#     nota1 = float(input("Ingresa la primera nota: "))
#     nota2 = float(input("Ingresa la segunda nota: "))
#     nota3 = float(input("Ingresa la tercera nota: "))

#     alumnos[personas] = ((nota1, nota2, nota3))

# print(f"La nota de los alumnos es: {alumnos}")

# for personas, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"{personas}: promedio = {promedio}")

#--------------------------------------

# parcial1 = {"Ana", "Luis", "Pedro", "Carla"}
# parcial2 = {"Luis", "Pedro", "Marta", "Jorge"}

# ambos = parcial1 & parcial2
# print(f"Alumnos que aprobaron ambos parciales: {ambos}")

# solo_uno = parcial1 ^ parcial2
# print(f"Alumnos que aprobaron solo uno de los parciales: {solo_uno}")

# al_menos_un_parcial = parcial1 | parcial2
# print(f"Alumnos que aprobaron al menos un parcial: {al_menos_un_parcial}")

#--------------------------------------

# productos = {"manzanas": 10, "pan": 5, "leche": 8}

# while True:
#     print("1 - Consultar stock de un producto")
#     print("2 - Agregar unidades a un producto existente")
#     print("3 - Agregar un nuevo producto")
#     print("4 - Salir")

#     opcion = input("Elegi una opcion: ")

#     if opcion == "1":
#         nombre = input("Ingresa el nombre del producto: ")
#         if nombre in productos:
#             print(f"Stock de {nombre}: {productos[nombre]} unidades")
#         else:
#             print(f"{nombre} no se encuentra en el stock.")

#     elif opcion == "2":
#         nombre = input("Ingresa el nombre del producto: ")
#         if nombre in productos:
#             cantidad = int(input("Ingresa la cantidad a agregar: "))
#             productos[nombre] += cantidad
#             print(f"Nuevo stock de {nombre}: {productos[nombre]}")
#         else:
#             print(f"{nombre} no existe")

#     elif opcion == "3":
#         nombre = input("Ingresa el nombre del nuevo producto: ")
#         if nombre in productos:
#             print(f"{nombre} ya existe en el stock.")
#         else:
#             cantidad = int(input("Ingresa la cantidad inicial: "))
#             productos[nombre] = cantidad
#             print(f"{nombre} agregado con {cantidad} unidades.")

#     elif opcion == "4":
#         print("Saliendo...")
#         break

#     else:
#         print("Opcion invalida")

#--------------------------------------

# agenda = {
#     ("lunes","15:30"): "Gym",
#     ("Martes","17:00"): "Estudio",
#     ("Miercoles","11:30"): "Trabajo",
#     ("Jueves","19:00"): "Series",
#     ("Viernes","10:30"): "Desayuno"
# }

# numero = 0

# while numero != 2:
#   numero = int(input(("Seleccione 1 si desea consultar actividad o 2 si desea salir: ")))

#   if numero == 1:
#       dia_evento = input("Ingrese el dia del evento que desea conocer su actividad: ")
#       hora_evento = input("Ingrese la hora del evento que desea conocer su actividad: ")
#       tupla_actividad = (dia_evento , hora_evento)
      
#       if tupla_actividad in agenda:
#           print(f"La actividad es: {agenda[tupla_actividad]}")
#       else:
#           print("no se encontró la actividad")

#--------------------------------------

# paises_original = {
#     "Argentina":"Buenos aires",
#     "Colombia":"Bogota",
#     "Chile":"Santiago",
#     "Mexico":"Guadalajara"
# }

# paises_invertidos = {valor: clave for clave, valor in paises_original.items()}

# print(f"Diccionario original: {paises_original}")
# print(f"Diccionario invertido: {paises_invertidos}")
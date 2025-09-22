# multiplos=list(range(4,101,4))
# print(multiplos)

#-------------------------------------

# lista=["Gatos", 9.99,"Helado", "Universo", 25]
# print(lista[-2])

#-------------------------------------

# vacia=[]
# for i in range(3):
#         lista=input("Ingresa lo que quieras en la lista: ")
#         agregado=vacia.append(lista) 
# print(f"La lista tiene los elementos {vacia}")

#-------------------------------------

# print("ANIMALES")
# animales=["perro","gato","conejo","pez"]
# print(animales)
# bandera:bool=True
# while bandera:
#     animal=input("Ingrese el animal en la lista a reemplazar o escribe una letra o numero para salir: ").lower()
#     if animal in animales:
#         animal_nuevo=input("Ingresa el animal nuevo: ")
#         indice=animales.index(animal)
#         animales[indice]=animal_nuevo
#         print(f"La nueva lista es {animales}")
        
#     else:
#         print("Saliste del programa")
#         bandera=False

#-------------------------------------

# #Se da una lista con 5 elementos
# numeros=[8,15,3,22,7]
# # se utiliza max para selecciona el elemento mas grande de la lista  
# # y remove para retirarlo
# numeros.remove(max(numeros))
# #luego se utiliza print para escribir los elementos que tiene la lista actualizada
# print(numeros)

#-------------------------------------

# lista=list(range(10,31,5))
# print(f"Lista completa {lista}")
# print(f"lista con los dos primeros {lista[0:2]}")

#-------------------------------------

# autos=["sedan","polo","sudan","gol"]
# print(autos)
# bandera:bool=True
# while bandera:
#     modelo_auto=input("Ingrese el modelo en la lista a reemplazar o escribe una letra o numero para salir: ").lower()
#     if modelo_auto in autos:
#         modelo_nuevo=input("Ingresa el modelo nuevo: ")
#         indice=autos.index(modelo_auto)
#         autos[indice]=modelo_nuevo
#         print(f"La nueva lista es {autos}")
        
#     else:
#         print("Saliste del programa")
#         bandera=False

#-------------------------------------

# dobles=[]
# dobles.append(5*2)
# dobles.append(10*2)
# dobles.append(15*2)
# print(dobles)

#-------------------------------------

# compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
# print(f"lista actual: {compras}")
# compras[2].append("jugo")
# compras[1][1]="tallarines"
# compras[0].remove("pan")
# print(f"lista nueva {compras}")

#-------------------------------------

# lista_anidada=[15, True, [25.5, 57.9, 30.6], False]
# print(lista_anidada)
# print(f"elementos de la lista [0]: {lista_anidada[0]}")
# print(f"elementos de la lista [1]: {lista_anidada[1]}")
# print(f"elementos de la lista [2][0]: {lista_anidada[2][0]}")
# print(f"elementos de la lista [2][1]: {lista_anidada[2][1]}")
# print(f"elementos de la lista [2][2]: {lista_anidada[2][2]}")
# print(f"elementos de la lista [3]: {lista_anidada[3]}")
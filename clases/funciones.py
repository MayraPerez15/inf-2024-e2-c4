#que funciones se pueden aplicar a la lista?
#https://docs.python.org/es/3/tutorial/datastructures.html
#https://ellibrodepython.com/listas-en-python
#https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion3/tipo_listas.html

# sort(): Ordena la lista en orden ascendente.
# tipo(lista): Devuelve el tipo de clase de un objeto.
# append(): Añade un único elemento a una lista.
# extend(): Añade varios elementos a una lista.
# index(): Devuelve la primera aparición del valor especificado.
# max(lista): Devuelve un elemento de la lista con valor máximo.
# min(list): Devuelve un elemento de la lista con valor min.
# len(lista): Da la longitud total de la lista.
# list(seq): Convierte una tupla en una lista.
# cmp(lista1, lista2): Compara los elementos de ambas listas list1 y list2.
# filter(fun,list): filtra la lista utilizando la función de Python.
# # lista = []
# # valor1 = int(input("Ingrese el primer número: "))
# # lista.append(valor1)
# # valor2 = int(input("Ingrese el segundo número: "))
# # lista.append(valor2)
# # lista.sort()
# # print(f"El ordenamiento será: {lista}")


# # ingrese='si'
# # insertar='si'
# # while insertar == 'si':
# #     numero = int(input("Ingresar un numero: "))
# #     lista.append(lista)
# #     insertar = input("Desea seguir cargando productos? (si/no)")
# #     print (lista)
# # lista.sort()
# # print(f"El ordenamiento será: {lista}")


# # # Ingresamos los dos números
# # numero1 = float(input("Ingresa el primer número: "))
# # numero2 = float(input("Ingresa el segundo número: "))

# # # Comparamos los números y ordénalos
# # if numero1 < numero2:
# #     print(f"{numero1} es menor que {numero2}")
# # else:
# #     print(f"{numero2} es menor que {numero1}")

# # #ejemplo5
# # while True:
# #     try:
# #         num1= int(input("ingrese un numero: "))
# #         num2= int(input("ingrese un segundo numero: "))
# #         break
# #     except ValueError:
# #         print("Por favor, ingrese un numero entero: ")
# # numeros_ordenados = sorted([num1, num2])
# # print(numeros_ordenados)

lista = []
cont = 0

while cont < 3:
    try:
        valor = int(input("Ingrese un número: "))
        lista.append(valor)
        cont += 1
    except ValueError:
        print("Por favor, ingrese un número entero.")

lista.sort()

print(f"El número menor es: {lista[0]}")
print(f"El número mayor es: {lista[-1]}")
print(f"La lista completa ordenada es: {lista}")
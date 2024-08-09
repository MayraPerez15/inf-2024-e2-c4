# Hola!! les paso algunos ejercicios prácticos para profundizar en el uso de funciones:

# Estruc. de datos:

# Listas:
#* Crear una función que reciba una lista de números y devuelva una nueva lista con solo los números pares.
#*Escribir una función que tome una lista de palabras y devuelva un diccionario donde las claves sean las palabras y los valores sean la longitud de cada palabra.
def dicPalalbras(listapalabras): #porque en forma de aleatorio?
    diccionario={}
    for palabra in listapalabras:#hola
        longitud=len(palabra)
        diccionario[palabra] = longitud#accede a la palabra clave y valor es la longitud
    return diccionario

palabras={"argentina", "venezuela", "uruguay", "peru"}
palabras1={"saludar", "hola", "adios"}
print (dicPalalbras(palabras))
print (dicPalalbras(palabras1))
# Tuplas:
#*Crear una función que reciba una tupla de números y devuelva la suma de todos sus elementos.
#*Escribir una función que tome una tupla de tuplas y devuelva una lista plana con todos los elementos.

#  Diccionarios:
#*Crear una función que reciba un diccionario y devuelva una lista ordenada de las claves.
#*Escribir una función que tome un diccionario y un valor, y devuelva una lista con todas las claves asociadas a ese valor.

# Manejo de flujos:

# Condicionales:
#*Crear una función que determine si un número es primo.
#*Escribir una función que reciba tres números y devuelva el mayor.

# Bucles:
#*Crear una función que calcule el factorial de un número.
#*Escribir una función que imprima la tabla de multiplicar de un número dado.

# Funciones recursivas:
#*Crear una función recursiva que calcule el n-ésimo número de la secuencia de Fibonacci.
#*Escribir una función recursiva que invierta una cadena.

# Combinación de ambos:

#*Crear una función que reciba una lista de diccionarios, cada uno representando a una persona con nombre y edad. La función debe devolver una lista ordenada de personas por edad.
#*Escribir una función que tome una lista de números y devuelva una nueva lista con los números únicos en orden ascendente.
#*Crear una función que genere una lista de números aleatorios y luego los ordene utilizando diferentes algoritmos de ordenamiento (burbuja, inserción, selección). ### Utilizando lo que les pasó el profe como tarea #####
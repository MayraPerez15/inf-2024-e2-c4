##Leer 5 números y calcular su promedio
#incializar una lista vacia

numeros=[]
for i in range (5):
    numero = int(input('ingrese un numero: ')) 
    numeros.append(numero)

#promedio= sum(numero) / len(numeros)
#print ("el numero ")
# promedio = sum(numeros) / len(numeros)
suma = 0
for numero in numeros:
    suma += numero
    promedio = suma / 5

print("El promedio de los número ingresados es: ", promedio)

#encontrar el mayor de 10 numeros ingresados por el usuario. puede ingresar numeros negativos.
#
# maximo = max(lista_numero)
# print(f"el numero maximo es: {maximo}")
lista = [1,3,6,1,87,123,32,-50]

valor_maximo = None

for numero in lista:
    if valor_maximo is None or numero > valor_maximo:
        valor_maximo = numero
print("el valor maximo es:", valor_maximo)





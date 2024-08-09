## Calculadora
# Opciones:
# 1 - Sumar todos los elementos de una lista
# 2 - Encontrar el maximo
# 3 - Encontrar el minimo
# 4 - Filtrar por pares
# 5 - Filtrar por impares
### Ingrese los valores de la lista por pantalla, y ademas la lista puede tener cualquier tamanio
# input()
lista=[]
condicion= 'si'
while condicion == 'si':
    numero=input('ingresar valor para la lista: ')
    numero=int(numero)
    lista.append(numero)
#lista.append(int(input('ingrsar valor para la lista')))
    condicion= input('desea seguir cargando valores? (si/no) ')
print('su lista es la siguiente: ',lista)

print(f''' 0- Salir del programa
 1 - Sumar todos los elementos de una lista
 2 - Encontrar el maximo
 3 - Encontrar el minimo
 4 - Filtrar por pares
 5 - Filtrar por impares''')

opcion=None
while opcion != 0:

    opcion= int(input('porfavor ingrese una opcion: '))

    if opcion == 1:
        suma = sum(lista)
        print(suma)
    elif opcion == 2:
        maximo = max(lista)
        print(maximo)
    elif opcion == 3:
        minimo = min(lista)
        print(minimo)
    elif opcion == 4:
        filtradPar = list(filter(lambda x: x % 2 == 0, lista))
        print(filtradPar)
    elif opcion == 5:
        filtradoImpar = list(filter(lambda x: x % 2 != 0, lista))
        print(filtradoImpar)      
    else:
        print('su opcin no esta definida dentro de los limites de las opciones')


    



#https://github.com/xlmriosx/inf-2024-e2-c4

#Algoritmos de ordenamiento
lista1=[99,111,20,33,48,5,66,1]
lista2=[55,33,99,5,3,4,0]
lista=[88,55,44,22,33,71,93]
lista3=[88, 1, 6, 9, 3 , 1, 99, 77]
lista4=[5,1,6,9,7,22,3]
print(lista3)

def seleccion (lista_desordenada):
    lista_ordenada=lista_desordenada

    for indice in range(len(lista_desordenada)):
        minimo=indice
 
        for valor in range(indice,len(lista_desordenada)):
            if(lista_desordenada[valor] < lista_desordenada[minimo]):
                minimo=valor

        if(minimo != indice):
            aux=lista_desordenada[indice]
            lista_desordenada[indice]=lista_desordenada[minimo]
            lista_desordenada[minimo]=aux

    return lista_ordenada

print (f'seleccion, {seleccion(lista3)}')


print (lista1)
def insercion (lista_desordenada):
    longitud= len(lista_desordenada)
    lista_ordenada=lista_desordenada

    for pasada in range(1, longitud):   
        valor1= lista_desordenada[pasada]
        indice= pasada 
        #comparacion
        while indice > 0 and lista_desordenada[indice-1] > valor1:
            lista_desordenada[indice]= lista_desordenada[indice-1]
            indice -= 1
        lista_desordenada[indice]=valor1 #guarda el valor

    return lista_ordenada

print (f'insercion, {insercion(lista1)}')



def intercambio(lista_desordenada):#burbuja
    longitud=len (lista_desordenada) -1 
    lista_ordenada=lista_desordenada
    #buble para pasadas
    for pasada in range (0, longitud):
        #comparaciones e intercambio 
        for valor in range (0, longitud):
            if lista_desordenada[valor] > lista_desordenada[valor+1]:
                aux =lista_desordenada[valor]
                lista_desordenada[valor]=lista_desordenada[valor+1]
                lista_desordenada[valor+1]=aux 
    return lista_ordenada

print(f'intercambio, {intercambio(lista2)}')



#otro ejemplo insercion
# # print(lista3)
# # def insercion(lista_desordenada):
# #     for pasada in range(len(lista_desordenada)):
# #         print(f'recorro lista:{pasada}')
# #         for valor in range(pasada,0,-1):
# #             if(lista_desordenada[valor-1] > lista_desordenada[valor]):
# #                 print(f'comparacion {lista_desordenada[valor-1]}>{lista_desordenada[valor]}')
# #                 aux=lista_desordenada[valor]
# #                 lista_desordenada[valor]=lista_desordenada[valor-1]
# #                 lista_desordenada[valor-1]=aux
# #                 lista_ordenada=lista_desordenada
# #     return lista_ordenada
# # lista5=[10,9,7,99,0]
# # print (insercion(lista5))
#    return lista_ordenada

# # def seleccion(lista_desordenada):
# #     longitud=len(lista_desordenada) -1
# #     for pasada in range (0, longitud):
# #         indice= pasada
# #         valor=lista_desordenada[indice]
# #         print(f'pasada: {pasada}')

# #         for j in range (pasada , longitud):
# #             if valor>lista_desordenada[j+1]:
# #                 valor=lista_desordenada[j+1]
# #                 indice=j +1
# #         print(j)
        
# #         if indice !=pasada:
# #             aux =lista_desordenada[pasada]
# #             lista_desordenada[pasada]=lista_desordenada[indice]
# #             lista_desordenada[indice] = aux
# #     return lista_desordenada

# # print (seleccion(lista4))

## profe dio clases: 5/ 08/ 2024
def selection_sort(vector):
    nb = len(vector)
    for actual in range(0,nb):
        mas_pequeno = actual

        for j in range(actual+1,nb) :
            if vector[j] < vector[mas_pequeno] :
                mas_pequeno = j

        if min is not actual :
            temp = vector[actual]
            vector[actual] = vector[mas_pequeno]
            vector[mas_pequeno] = temp

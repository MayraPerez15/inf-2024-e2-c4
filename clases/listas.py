from functools import reduce

lista=[8,123, 1,2,3,4,5]
suma=sum(lista)
longitud=len(lista)
maximo=max(lista)
minimo=min(lista)
ordenar= sorted(lista)
reversa= list(reversed(lista)) #o lista[::-1] para darle vuelta a la lista
#la lista cambio a un objeto, un tipo de dato, para solucionar es list
enumerar= list(enumerate(lista))
mapear=list(map(lambda x:x +1, lista))#es una funcion que no tiene nombre, no esta difinido (lambda)
#es com un for, el map  > for in lista, etc
#(x:x **2) al cuadrado
mapRed=reduce(lambda x,y :x+y, lista) #puedo trabajar 2 elementos de la lista
filtrado= list(filter(lambda x:x % 2==0, lista))

print('suma',suma)
print ('longitud', longitud)
print ('maximo',maximo)
print ('minimo', minimo)
print (ordenar)
print (reversa)
print (enumerar)
print(mapear)
print(mapRed)
print(filtrado)

#any(), all()

#verifica o corrovora que si hay un booleano true, te debuele True
lista=[True,False,True,False]
any_lista= (lista)
print('any', any_lista)
#te devuelve si hay true todos=true, si tiene true y false, te devuelve false
all_list=all(lista)
print('all', all_list)

#zip()
lista_1=[1,2,3]
lista_2=['a','b','c']
lista_cpx=list(zip(lista_1, lista_2))
print(lista_cpx)


#se aplica sobre la variable, son dinamicas, 
#insert(), remove(), apppend(), pop(), count()

lista=[1,2,3,4,5]
#lista_ins=lista.insert(0,36)#no se define se trata sobre la lista
lista.insert(0,38)
print('insert',lista)

lista.remove(3)
print('remove',lista)

lista.append(333)
print('append',lista)

lista.pop()
print('pop',lista)

ocurrencias=lista.count(4)#cantidad que hay
print('count',ocurrencias)


# # any() all()
# lista = [True, True, True, True]

# # any_list = any(lista)
# # print("Any:", any_list)

# # all_list = all(lista)
# # print("All:", all_list)

# # zip()
# # lista_1 = [1,2,3]
# # lista_2 = ['a','b','c']

# # lista_cpx = list(zip(lista_1, lista_2))
# # print(lista_cpx)

# # insert() remove() append() pop() count()
# lista = [1,2,3,4,5,4,4,4,4]
# lista.insert(0, 38)
# print(lista)

# lista.remove(3)
# print(lista)

# lista.append(333)
# print(lista)

# lista.pop()
# print(lista)

# ocurrencias = lista.count(4)
# print(ocurrencias

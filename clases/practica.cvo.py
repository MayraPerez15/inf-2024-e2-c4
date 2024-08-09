#enteros
entero=543
print(entero)
#float -decimal
decimal= 0.43
print(decimal)
#string 
cadena= "info 2024-07-11" #f "info 2024-07-11 {variable numerica}"
cadena1='info 2024-07-11'
cadena2=""""DOCSTRING""" #funciones para documentarlas 
cadena3='''DOCSTRING'''
print(cadena)
#boolean
verdadero= True
falso= False
print (verdadero)
print(falso)
#vacio, null, nulo,none,nil  
vacio = None
print(vacio)
#fucion type() que tipo de dato tiene dentro. todo lo que defina es un objeto, un obj es una class
print(type(vacio))

#(clar o cls para limpiar terminal)

##tipos de datos complejos/estructurados
#list (pueden crecer) son mutaplesse_ puede obtener mediante la posicion_ elementos indice empieza en 0
lista= [1,2,3,4,5,6,7,8, "algo"]
print (lista)
print (lista[3])
lista_lista = [[3,2,1], [7,6,5], [10,11,13]]
lista_lista.append(2)
#print(lista_lista[1][0]) (el .append(2)es para agregar un numero a la lista)
print (lista_lista)
lista_lista[3]=365
print(lista_lista)
#lista_lista[3]=365 es para redinir un numero de la lista

#tuplas (dato inmutable, no puede crecer) (se puede poner datos 'string' )(puede redefinirse) (las tuplas no se puede asignar nuevos valoras ya asigados)
tuplas= (1,2,3,4,5,6)
print(tuplas[2])
#tuplas[2] =345 typeerror: tuple objet does support item assignment, (son fijos, no se le puede re-asignar otro valor que ya esta) exepto que defina de nuevo la variable tuplas
print(tuplas)

#set- conjunto, su caracterista es se define con llaves, (no puede acepta repetir muchos valores- datos de = valor ej:1,2,3 ) son mutables , no aceptan tener muchos valores con el mismo valor
conjuntos= {1,2,3,4,5,6,9,8,'123','123', '123',7}
print(conjuntos)
#sirve si tengo repetido el n°de cliente por ejem, te ahorra tener un dato o numero repetido. no te permite acceder de manera indice, guarda los datos de forma conveniente, optima. 
#for i in conjuntos:
#   print(i)    ----> te muestra como se guarda los datos del conjunto

#diccionarios,map (estructura= clave valor, key-value) {'llave':valor , 'llave':'valor'} son datos estrucutados
#diccionarios='{'llave':'valor', '1':'uno'}
#print(diccionarios [llave]) o print(diccionarios [1])
ciudades={'Chaco':['Resistencia', 'Baranqueras', 'Fontana'], 'Corrientes':'Corrientes','Misiones':'Posadas'}
print(ciudades['Corrientes'])

#definidos por el programador, librerias (dataframe (df))


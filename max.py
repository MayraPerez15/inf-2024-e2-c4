##ejemplo con funcion de max()
lista=[1,3,6,1,87,123,1,32]
numMax = max(lista)
print('numero max', numMax)

#habia una ; abajo despues del corchete [0];
lista=[1,3,6,1,87,123,1,32]
aux = lista[0]
for i in lista:
    if i > aux:
        aux = i
print('ejemprof', aux)

lista =[1,3,6,1,87,123,1,32]
maximo = 0
for valor in lista:
    if valor> maximo:
        maximo= valor

print(maximo)

max_lista= max
lista = [1,3,6,1,87,123,1,32]
aux= lista[0]
for x in lista:
    if x > aux:
        aux=1
        print (aux)
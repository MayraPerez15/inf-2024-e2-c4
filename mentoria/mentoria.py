print ("ingrese los tiempos de viajes de los tramos")
print ("ingrese n para finalizar")
tiempo_total=0
#tiempo_tramo_entero= int .. no me acuerdo-- el break corta la sentencia, el bucle 
#tiempo_total == 0:
while tiempo_total != 0:
    tiempo_tramo= int (input("ingrese el tiempo del viaje"))
    tiempo_tramo != 0
    tiempo_total != 0

#while True:
#    tiempo_tramo= int (input("ingrese el tiempo del viaje"))
#    if tiempo_tramo==0:
#        break
#    else:
#        #tiempo_total= tiempo_total + tiempo_tramo
#        tiempo_total += tiempo_tramo 

#tiempo_total_hora= str (tiempo_total // 60) #calcula las hs del tramo
tiempo_total_hora= str (tiempo_total // 60).zfill(2)
#.zfill(2)para rellenar posiciones, trabaja solo con str no con enteros
tiempo_total_minuto= str (tiempo_total % 60).zfill(2) #calcula el resto de la operacion, calcula mts del tramo
print ("tiempo total del viaje: "+ tiempo_total_hora + ":" + tiempo_total_minuto)
#print (f'tiempo total del viaje: {tiempo_total_hora}:{tiempo_total_minuto}hs')
 

cadena = input("Ingrese una cadena de texto: ")
print("Esta es una cadena:", cadena) 
if cadena == cadena [::-1]:
    print('es un palindromo')
else:
    print('no es un palindromo')

print(cadena [::-1])

b="hello world!"
print (b[2:5]) #toma del 2 hasta el 5
print (b[:5]) #empiece del strin hasta la posicion 4 o = a (b[0:5])

#contar los digitos de un numero 
numero= int(input("ingrese un numero: "))
contador_digitos= 0
numero_ingresado=numero
while numero > 0:
    numero=numero // 10
    contador_digitos +=1
print(f"el numero ", {numero_ingresado}, "tiene", {contador_digitos}, "digitos")

#secuencia fibonacci = 011235

#leer 5 numeros y calcular su promedio
#inicializar una lista vacia
numero1=[]
for i in range (5):
    numero1 = int(input('ingrese un numero: ')) 
    numero1.append(numero1)
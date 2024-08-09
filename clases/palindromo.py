# input("") permite al usuario ingresar un valor por consola
# Consigna,
# A partir de un string ingresado por consola
# determinar si dicho string es palindromo
# Palindromo: alreves y normal se escriben igual, neuquen, jojoj??
# cadena = input("Ingrese una cadena de texto: ")
# print("Esta es una cadena:", cadena) 

# def buscar_palindromos(frace):
#      palabras= cadena.split()
#      polindromos=[]
#      for x in palabras:
#          x = x.lower()
#          if len(x) >= 3 and x == x[::-1]:
#                polindromos.append(x)
#      return polindromos
# print(buscar_palindromos)



##ESTE ES BUENO
cadena = input("Ingrese una cadena de texto: ")
print("cadena ingresada: ", cadena)

cadena_invertida = cadena[::-1]
if (cadena_invertida == cadena):
     print("es palindromo")
else:
     print("no es palindromo")



##ayuda del profe
##cadena_reves=cadena[::-1]
##print(cadena_reves)

cadena = input("Ingrese una palabra: ")
print("palabra ingresada: ", cadena)
cadena_reves = cadena[::-1]
if (cadena_reves == cadena):
     print("es palindromo", cadena_reves)
else:
     print("no es palindromo", cadena_reves)


cadena = input("Ingrese una palabra: ")
print("palabra ingresada: ", cadena)
cadena_reves = cadena[::-1]
if cadena_reves == cadena:
     print("es palindromo")
else:
     print("no es palindromo")


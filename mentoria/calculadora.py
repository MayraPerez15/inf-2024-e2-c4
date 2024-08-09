# Tarea: Calculadora Básica en Python
# Descripción:
# Les dejo gente un lindo ejercicio para practicar y empezar a darle forma a los programas que vayan armando en Python:
# Desarrolla una calculadora básica que permita realizar las siguientes operaciones matemáticas:
#     Suma
#     Resta
#     Multiplicación
#     División
# Requisitos:
# El programa debe solicitar al usuario los dos números con los que desea realizar la operación y la operación que desea realizar.
# El programa debe mostrar el resultado de la operación de forma clara y concisa.
# El programa debe repetir el proceso hasta que el usuario decida salir.
# El programa debe manejar errores de entrada, como ingresar valores no numéricos o intentar dividir por cero.

print("Claculadora Básica de Python")
opciones=('''Elije una opcion:
0_opciones
1_suma 
2_resta 
3_multiplicación 
4_división
5_salir de la calculadora''')
print(opciones)
#no tiene encuenta los numeros negativos/positivos en restas
opcion= 0
while opcion != 5:
    try: 
        opcion=(int(input('ingrese una opción: ')))
        if opcion > 5 :
            print('Opcion invalida, intente de nuevo.', opciones)
        elif opcion == 0:
            print(opciones)
        elif opcion != 5: 
            numero1=int(input("ingrese el primer numero:"))
            numero2=int(input("ingrese el segundo numero:")) 
        if opcion == 1:
            suma=(numero1 + numero2)
            print('=', suma)
        elif opcion == 2:
            restar=(numero1 - numero2)
            print('=', restar)
        elif opcion == 3:
            multiplicar=(numero1 * numero2)
            print('=', multiplicar)
        elif opcion == 4:   
            if numero2 == 0:
                print(' El número 0 no es divisor de ningún número: intente de nuevo')
            else:
                dividir= (numero1 // numero2)
                print('=', dividir)
    except ValueError:
        print('El dato ingresado no es un numero entero, intente nuevamente.', opciones)
print('gracias por usar la calculadora')


# try: 
#     opciones= 0
#     while opciones != 5: 
#         opciones=(int(input('ingrese una opción: ')))
#         if opciones != 5: 
#             numero1=int(input("ingrese el primer numero:"))
#             numero2=int(input("ingrese el segundo numero:"))
#         if opciones == 1:
#              suma=(numero1 + numero2)
#              print(suma)
#         elif opciones == 2:
#             restar=(numero1 - numero2)
#             print(restar)
#         elif opciones == 3:
#             multiplicar=(numero1 * numero2)
#             print(multiplicar)
#         elif opciones == 4:   
#             if numero2 == 0:
#                 print('intente de nuevo')
#             else:
#                 dividir= (numero1 // numero2)
#                 print(dividir)
#         elif opciones > 5 :
#             print('opcion invalida, intente de nuevo')
#     print('gracias por usar la calculadora')
# except ValueError:
#     print('el dato ingresado no es un numero entero, intente nuevamente')

# print ("gracias por usar la calculadora")
#elif opcion == 3:

# profe:

# print("Bienvenido")
# seguir = "SI"
# while seguir == "SI":
# print("Elija una opción: ")
# print("1-SUMA")
# print("2-RESTA")
# print("3-DIVIDIR")
# print("4-MULTIPLICAR")
# print("0-SALIR")

# oper = int(input())

# if oper == 0:
# seguir = "NO"
# elif oper > 4:
# print("Número incorrecto, por favor elija una opción válida.")
# else:
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# if oper == 1:
# resultado = num1 + num2
# elif oper == 2:
# resultado = num1 - num2
# elif oper == 3:
# resultado = num1 // num2
# elif oper == 4:
# resultado = num1 * num2

# print(f"El resultado es: {resultado}")
# seguir = input("¿Seguimos? SI/NO\n: ").upper()

# print("Gracias por usar nuestra calculadora")

#profe modifico para la funcion 1°archivo
# from operaciones import *

# while True:
# print("Calculadora")
# print("1. Sumar")
# print("2. Restar")
# print("3. Multiplicar")
# print("4. Dividir")
# print("5. Salir")

# opcion = input("Elija una opción: ")

# if opcion == '5':
# break

# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))

# if opcion == '1':
# resultado = suma(num1,num2)
# print("Resultado:", resultado)
# elif opcion == '2':
# resultado = resta(num1, num2)
# print("Resultado:", resultado)
# elif opcion == '3':
# resultado = multiplicacion(num1, num2)
# print("Resultado:", resultado)
# elif opcion == '4':
# resultado = division(num1, num2)
# print("Resultado:", resultado)
# else:
# print("Opción inválida.")


#2° archivo, operaciones :
# def suma(a:int, b:int):
# return a+b

# def resta(a,b):
# return a-b

# def multiplicacion(a,b):
# return a*b

# def division(a,b):
# if (b==0):
# return "No se puede realizar la operación de división por 0"
# else:
# return a/b
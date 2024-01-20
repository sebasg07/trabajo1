#definir la funcion
def calculadora():
    # gradar un valor tipo float 
    num1 = float(input("Ingrese el primer número: ")) #convertir el string en float agregando el input
    # gradar un valor tipo float 
    num2 = float(input("Ingrese el segundo número: ")) #convertir el string en float agregando el input
    # escoger una operación a la cual se va a realizar 
    operacion = input("Ingrese la operación (+, -, *, /): ")
    # condicion donde el usuario elige suma
    if operacion == '+':
        resultado = num1 + num2 #error en el num1
    # condicion donde el usuario elige resta
    elif operacion == '-':
    # operacion si se cumple la condicion
        resultado = num1 - num2
    # condicion donde el usuario elige multiplicación
    elif operacion == '*':
    # operacion si se cumple la operacion
        resultado = num1 * num2
    # condicion donde el usuario elige division
    elif operacion == '/':
    # operacion sis e cumple la condicion
        resultado = num1 / num2 #error en el num1
    # si no se cumple las condiciones 
    else:
        # resultado en caso de que no se compla la condicion
        resultado = "Operación no válida"
    # imprimir el resultado de las operaciónes.
    print(resultado) #error de las comillas y en la variable dentro del ()

calculadora() # error en el nombre de la funcion 

# es una calculadora que nos permite realizar funciones de suma resta multiplicacion y division

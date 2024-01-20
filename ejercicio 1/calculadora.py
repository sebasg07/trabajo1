def calculadora():
    num1 = float("Ingrese el primer número: ")
    num2 = float("Ingrese el segundo número: ")
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num / num2
    else:
        resultado = "Operación no válida"

    print("Resultado: "resultado)

calculdora()

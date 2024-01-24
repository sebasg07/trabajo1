# definir funcion 
def es_primo(numero):
    # Comprobar que el número es menor que 2
    if numero < 2: # se agrega : al final  
        # Si el número es menor que 2, la función retorna 
        return False
    # Inicia un bucle for que itera desde 2 hasta la raíz cuadrada del número más 1
    for i in range(2, int(numero**0.5) + 1):  # se agrega : al final
        # Comprueba si el número es divisible por i.
        if numero % i == 0: # Se agrega : al final 
            # Si el número es divisible por i, la función retorna False, indicando que no es un número primo.
            return False  # Se corrige la palabra retrun a return
    # Si el número no es divisible por ningún valor en el rango, la función retorna True, indicando que es un número primo
    return True  # Se corrige la palabra retunr a return

# solicita ingresar el numero que servira como limite para buscar los numeros primos
limite = int(input("Ingrese el límite superior para encontrar números primos: "))
# genera una lista de numeros primos 
primos = [num for num in range(2, limite + 1) if es_primo(num)]  # Se debe pasar el número a la función es_primo
# Imprime la lista de números primos
print("Números primos:", primos)

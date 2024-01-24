# definir funcion.
def celsius_a_fahrenheit(celsius): # faltan los dos : al final de los ().
    return (celsius * 9/5) + 32 
# solicita ingresar la temperatura  en Celsius y la convierte a un número decimal.
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: ")) #convertir el string en float agregando el input.
# llama a la funcion con la temperatura en Celsius como argumento y guarda el resultado.
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
# imprime la temperatura en Celsius y la temperatura equivalente en Fahrenheit.
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")


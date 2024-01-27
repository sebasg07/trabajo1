# definir funcion
def es_palindromo(texto): # faltan los dos puntos al final 
    # toma un texto y elimina caracteres alfanumericos y convertir todo a minusculas. 
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    # compara el texto 
    return texto == texto[::-1]

# solicita el ingreso del texto 
palabra_frase = input("Ingrese una palabra o frase: ")
# funcion si para verificar si es palindromo.
if es_palindromo(palabra_frase): # se pasa la palabra_frase y se pone dentro de los ().
    # inprime si la afirmacion es verdadera.
    print(f"{palabra_frase} es un palíndromo.")
# imprime si la afirmacion es falsa.
else:
    # imprimir frase
    print(f"{palabra_frase} no es un palíndromo.")

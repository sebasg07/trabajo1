# definir la funcion
def contar_palabra(texto, palabra): # faltaba colocar el caracter :
    return texto.lower().split().count(palabra.lower())
# definición de una cadena de texto
texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
# definir la palabra buscada en el texto
palabra_buscada = "texto"
# imprimir el mensaje buscado
print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.") # faltaba cerrar la llave, cerrar la comilla simple en la variable y abrir la otra llave. 


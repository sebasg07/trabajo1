# es una libreria aletoria aleatoria 
import random  # Se corrigió la importación de random
# es una libreria de texto
import string
# define la funcion y tiene un argumento opcional 
def generar_contrasena(longitud=8):  # Se corrigió el nombre de la función y se agregó el tipo de parámetro
   #crea una cadena de caracteres que contiene letras entre mayusculas y minusculas
    caracteres = string.ascii_letters + string.digits + string.punctuation
   # crea una contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))  #Se corrigió el nombre de la variable y la palabra 'return'
    # devuelve la contraseña creada por la funcion
    return contrasena
# imprime la contraseña generada
print(generar_contrasena())  # Se corrigió el nombre de la función en la llamada

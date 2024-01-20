import rando
import string

generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    retunr contraseña

print(generar_contrasena())

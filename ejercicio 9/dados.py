# importacion de la linea 
import random # se corrige la palabra radom a random

# definir funcion
def simular_lanzamiento_dados(cantidad_dados, caras_por_dado): # le hace falta el complemento def para definir el proceso
    # utiliza numeros aleatorios 
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)] # Falta un valor para 'cantidad_dados'.
    # devuelve la lista de resultados
    return resultados # la palabra esta mal return esta mal escrita. 

#solicita el ingreso de la cantidad
cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
# solicita el ingreso de la cantidad
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
# llama a la función 
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado)
# Esta línea imprime los resultados
print(f"Resultados del lanzamiento con {cantidad_dados} dados: {lanzamientos}") # La impresión final debería incluir el valor de 'cantidad_dados'.

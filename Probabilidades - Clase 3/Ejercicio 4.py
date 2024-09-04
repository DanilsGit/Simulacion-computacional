# Ejemplo 3 . Escriba un código para determinar por 
# enumeración el espacio muestral del lanzamiento triple de un
# dado.

# El resultado (fragmento) de la ejecución de este código es: {(5 , 1, 6), (5, 3, 3), (5, 4, 2), (2 , 1, 6),
# (1, 6, 6), (2, 2, 5), (6 , 6, 4), ...

# Variables
espacio = []

# Funciones
def lanzamiento():
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                espacio.append([i, j, k])

lanzamiento()

print(f"El espacio muestral del lanzamiento triple de un dado es: {espacio}, con un total de {len(espacio)} elementos")
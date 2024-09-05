
# Mostrar la union de los conjuntos de los multiplos de 2 y 3 
# en un espacio muestral.

espacio = [i for i in range(1, 11)]
multiplos2 = [i for i in espacio if i % 2 == 0]
multiplos3 = [i for i in espacio if i % 3 == 0]
union = [i for i in espacio if i in multiplos2 or i in multiplos3]

print(f"La unión de los múltiplos de 2 y 3 en el espacio muestral de 1 a 10 es: \n {union}")

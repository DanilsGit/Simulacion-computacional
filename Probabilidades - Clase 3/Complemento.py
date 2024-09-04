# Mostrar el complemento del los multiplos de 3 en un espacio muestral.
# Espacio muestral de 1 a 17: [1,2,3, ..., 17]
espacio = set([i for i in range(1, 18)])
multiplos3 = set([i for i in espacio if i % 3 == 0])
complemento = espacio - multiplos3
print(f"El complemento de los múltiplos de 3 en el espacio muestral de 1 a 17 es: \n {complemento}")


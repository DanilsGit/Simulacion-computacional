# 2. Escriba un código para determinar en qué cuadrante se encuentra un
# punto ingresado por teclado.

# Defino las variables
x = int(input("Por favor, ingresa el valor de x: "))
y = int(input("Por favor, ingresa el valor de y: "))
cuadrante = ""

if x > 0 and y > 0:
    cuadrante = "Primer cuadrante"
elif x < 0 and y > 0:
    cuadrante = "Segundo cuadrante"
elif x < 0 and y < 0:
    cuadrante = "Tercer cuadrante"
elif x > 0 and y < 0:
    cuadrante = "Cuarto cuadrante"
else:
    cuadrante = "Origen"

print(f"El punto ({x}, {y}) se encuentra en el {cuadrante}")

# Suma mayor que n
n = 7
# Resta menor que m
m = 2

sumas = []
restas = []

# Realizar matriz de pedro
for i in range(0, 7):
    if (i==0):
        sumas.append(["+",1,2,3,4,5,6])
    else:
        for j in range(0,7):
            if (j==0):
                index = i
                sumas.append([index,0,0,0,0,0,0])
            else:
                sumas[i][j] = sumas[0][j] + sumas[i][0] 

# Realizar matriz de pablo
for i in range(0, 7):
    if (i==0):
        restas.append(["-",1,2,3,4,5,6])
    else:
        for j in range(0,7):
            if (j==0):
                index = i
                restas.append([index,0,0,0,0,0,0])
            else:
                restas[i][j] = abs(restas[0][j] - restas[i][0])

pedro = 0
pablo = 0

# A favor de pedro
for i in range(1, len(sumas)):
    for j in range(1, len(sumas[i])):
        if sumas[i][j] > n:
            pedro += 1
    
# A favor de pablo
for i in range(1, len(restas)):
    for j in range(1, len(restas[i])):
        if restas[i][j] < m:
            pablo += 1
        
def imprimirMatriz(matriz):
    for fila in matriz:
        for elem in fila:
            print(elem, end=" | ")
        print()

print("-------")
imprimirMatriz(sumas)
print("-------")
imprimirMatriz(restas)
print("-------")
print("Jugadas ganadoras de pedro: ", pedro)
print("Jugadas ganadoras de pablo: ", pablo)

if (pedro > pablo):
    print("Tiene más probabilidades de ganar pedro, con jugadas a favor de: ", pedro)
else:
    print("Tiene más probabilidades de ganar pablo, con jugadas a favor de: ", pablo)




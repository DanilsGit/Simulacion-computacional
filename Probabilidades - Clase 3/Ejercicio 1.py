# 1. Escriba un programa que calcule la probabilidad de que el producto de
# los puntos de tres lanzamientos de los dados sea menor que 50.

# Defino las variables
limit = input("Por favor, ingresa el límite (ej. 50): ")
dados = input("Por favor, selecciona 2 o 3 dados (ej. 2): ")

limit = int(limit)
dados = int(dados)

combinaciones = []

matriz = []
multiplications = []
combinationOfSums = []

def combinations():
    for i in range(1, 7):
        for j in range(1, 7):
                matriz.append([i, j])

def combinations3():
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                    matriz.append([i, j, k])

def multiply():
    for i in range(len(matriz)):
        multiplications.append(matriz[i][0] * matriz[i][1])

def multiply3():
    for i in range(len(matriz)):
        multiplications.append(matriz[i][0] * matriz[i][1] * matriz[i][2])

def sumCombinatios():
    for i in range(len(multiplications)):
        for j in range(len(multiplications)):
            for k in range(len(multiplications)):
                combinationOfSums.append(multiplications[i] + multiplications[j] + multiplications[k])

def countUnder():
    underLimit = 0
    for i in range(len(combinationOfSums)):
        if combinationOfSums[i] < limit:
            underLimit += 1
    return underLimit

if dados == 2:
    combinations()
    multiply()
    sumCombinatios()
elif dados == 3:
    combinations3()
    multiply3()
    sumCombinatios()
else:
    print("Por favor, ingresa un número válido")

porbability = countUnder() / len(combinationOfSums)
print(f"La cantidad de combinaciones posibles es de {len(combinationOfSums)}")
print(f"La probabilidad de que la suma de los productos sea menor a {limit} es de {porbability}")
        
    

            
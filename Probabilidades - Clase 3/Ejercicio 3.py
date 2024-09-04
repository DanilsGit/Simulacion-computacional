# Determine el número de formas en las que se puede vestir un joven si
# dispone de dos pares de zapatos, dos pantalones y tres camisas.

# Defino las variables
shoes = int(input("Por favor, ingresa el número de zapatos: "))
pants = int(input("Por favor, ingresa el número de pantalones: "))
shirts = int(input("Por favor, ingresa el número de camisas: "))

combinations = []

def combinationsFunc():
    for i in range(shoes):
        for j in range(pants):
            for k in range(shirts):
                combinations.append([i, j, k])

combinationsFunc()

print(f"El número de formas en las que se puede vestir un joven es de {len(combinations)}")

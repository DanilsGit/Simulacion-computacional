import random as r

icosaedro1 = ['',0]
icosaedro2 = ['',0]
centavos = 0

caras_colores = ['azul', 'blanco', 'rojo', 'negro']
caras_numeros = [1,2,3,4,5]

def centavosGanados(ico1, ico2):
    cent = 0
    if (ico1[0] == ico2[0] and ico1[1] == ico2[1]):
        cent = 50
    if (ico1[0] == ico2[0] or ico1[1] == ico2[1]):
        cent = 10
    isOdd = (ico1[1] + ico2[1]) % 2 != 0
    if (isOdd):
        cent += 5
    return cent


choice = int(input("Presione 1 para iniciar el juego: "))
if(choice == 1):
    total = 0
    lanzamientos = 1
    icosaedro1 = [r.choice(caras_colores), r.choice(caras_numeros)]
    icosaedro2 = [r.choice(caras_colores), r.choice(caras_numeros)]
    cent = centavosGanados(icosaedro1, icosaedro2)
    print(f"{icosaedro1}, {icosaedro2}")
    print(f"Jugador GANO ${cent} centavos")
    total += cent
    choise_2 = int(input("Presione 2 para continuar el juego, 3 para salir: "))
    while(choise_2 == 2):
        lanzamientos += 1
        icosaedro1 = [r.choice(caras_colores), r.choice(caras_numeros)]
        icosaedro2 = [r.choice(caras_colores), r.choice(caras_numeros)]
        cent = centavosGanados(icosaedro1, icosaedro2)
        print(f"{icosaedro1}, {icosaedro2}")
        print(f"Jugador GANO ${cent} centavos")
        total += cent
        choise_2 = int(input("Presione 2 para continuar el juego, 3 para salir: "))
    print(f" El jugador GANO ${total} centavos en {lanzamientos} Lanzamientos")
            
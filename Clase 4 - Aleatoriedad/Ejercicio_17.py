seed = int(input("Ingrese la semilla (ej. 9731): "))

if (len(str(seed)) != 4):
    print("La semilla debe tener 4 digitos")
else:
    for i in range(100):
        seed = seed ** 2
        if (len(str(seed)) < 8):
            while (len(str(seed)) < 8):
                seed = "0" + str(seed)
        total = str(seed)
        seed = int(str(seed)[2:6])
        if (i == 99):
            print(f"[{i+1}] {seed} {total} última línea de su código.")
        else:
            print(f"[{i+1}] {seed} {total}")
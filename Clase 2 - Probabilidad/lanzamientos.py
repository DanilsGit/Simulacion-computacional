import random 
cara = 0 
cruz = 0 
for i in range(100):
    tirada = random.choice(["cara", "cruz"])
    if tirada == "cara":
        cara += 1
    elif tirada == "cruz":
        cruz += 1
print("Total caras: ",cara," Total cruces",cruz)
import random as r
import matplotlib.pyplot as plt

prices = [0]*30
days = [i for i in range(0,30)]

for i in range(len(prices)):
    prices[i] = r.randrange(130,150,1)

def promedium():
    sum = 0
    for i in range(len(prices)):
        sum += prices[i]
    return sum / len(prices)

def lessExpensive():
    less = prices[0]
    for i in range(len(prices)):
        if (less > prices[i]):
            less = prices[i]
    return less


print(prices)
print(f"El promedio del precio fue: ${promedium()}")
print(f"El valor mínimo del precio fue: ${lessExpensive()}")


plt.plot(days, prices,  'o-')
plt.xticks(range(min(days), max(days)+1, 1)) 

plt.xlabel('Dias')
plt.ylabel('Precio')

plt.title('Gráfico de petroleo')

plt.show()
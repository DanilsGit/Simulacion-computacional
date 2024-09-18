import random as r
import matplotlib.pyplot as plt


prices = [0] * 30
days = [i for i in range(0,30)]
for i in range(30):
    prices[i] = r.randint(130, 150)


def promedium():
    total = 0
    count = 0
    index = 0
    while index < len(prices):
        total += prices[index]
        count += 1
        index += 1
    average = total / count
    return average


def lessExpensive():
    index = 0
    if len(prices) > 0:
        min_value = prices[index]
        while index < len(prices):
            if prices[index] < min_value:
                min_value = prices[index]
            index += 1
        return min_value
    return None


print(prices)
print(f"El promedio del precio fue: ${promedium()}")
print(f"El valor mínimo del precio fue: ${lessExpensive()}")




plt.plot(days, prices,  'o-')
plt.xticks(range(min(days), max(days)+1, 1))

plt.xlabel('Dias')
plt.ylabel('Precio')

plt.title('Gráfico de petroleo')

plt.show()
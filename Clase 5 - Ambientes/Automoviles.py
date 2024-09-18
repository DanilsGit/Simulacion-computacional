import random
import math
import simpy


# Fórmulas matemáticas utilizadas:

# llegada = -T_LLEGADAS * logaritmo(R),
# donde R es un número aleatorio entre 0 y 1. Esto simula las llegadas de los autos con una distribución exponencial, modelando tiempos de espera irregulares entre cada auto.

# tiempo_estacionamiento = TIEMPO_ESTACIONAMIENTO_MIN + \
#     (TIEMPO_ESTACIONAMIENTO_MAX - TIEMPO_ESTACIONAMIENTO_MIN) * R,
# donde R es un número aleatorio. El resultado es un tiempo distribuido uniformemente entre el mínimo y el máximo definido.

# lpc = tiempo total de espera(te) / tiempo final(fin).
# Este valor mide cuántos autos en promedio están esperando para estacionar en un momento dado.

# tep = tiempo total de espera(te) / número total de autos(TOT_AUTOS).

# upi = (duración total de estacionamiento(dt) / tiempo final(fin)) / número de espacios disponibles(NUM_ESPACIOS).
# Esto indica qué tan ocupado estuvo el estacionamiento a lo largo de la simulación.

# Constantes:
# SEMILLA: Se utiliza para generar los mismos números aleatorios en cada ejecución, permitiendo que los resultados sean reproducibles.
# NUM_ESPACIOS: Define el número de espacios disponibles en el estacionamiento(en este caso, 1).
# TIEMPO_ESTACIONAMIENTO_MIN y TIEMPO_ESTACIONAMIENTO_MAX: Establecen los límites de tiempo en que los autos pueden estar estacionados.
# T_LLEGADAS: Es el tiempo promedio entre la llegada de cada auto al estacionamiento.
# TOT_AUTOS: Es la cantidad total de autos que llegarán al estacionamiento durante la simulación.

SEMILLA = 30
NUM_ESPACIOS = 1  # Número de espacios disponibles en el estacionamiento
TIEMPO_ESTACIONAMIENTO_MIN = 0
TIEMPO_ESTACIONAMIENTO_MAX = 1
T_LLEGADAS = 1
TOT_AUTOS = 20  # Total de autos que llegarán al estacionamiento

te = 0.0  # tiempo de espera total
dt = 0.0  # duración de estacionamiento total
fin = 0.0  # hora en el que finaliza


def estacionar(auto):
    global dt  # Para poder acceder a la variable dt declarada anteriormente

    R = random.random()  # Obtiene un número aleatorio y lo guarda en R
    tiempo = TIEMPO_ESTACIONAMIENTO_MAX - TIEMPO_ESTACIONAMIENTO_MIN
    tiempo_estacionamiento = TIEMPO_ESTACIONAMIENTO_MIN + \
        (tiempo * R)  # Distribución uniforme
    # deja correr el tiempo n horas
    yield env.timeout(tiempo_estacionamiento)
    print("🚹 El %s estacionado por %.2f horas " %
          (auto, tiempo_estacionamiento))
    dt = dt + tiempo_estacionamiento  # Acumula los tiempos de uso del espacio


def auto(env, name, estacionamiento):
    global te
    global fin
    llega = env.now  # Guarda el hora de llegada del auto
    print("🚗 El %s llegó al estacionamiento en la hora %.2f" % (name, llega))
    with estacionamiento.request() as request:  # Espera su turno
        yield request  # Obtiene espacio en el estacionamiento
        pasa = env.now  # Guarda el hora cuando comienza a estacionarse
        espera = pasa - llega  # Calcula el tiempo que esperó
        te = te + espera  # Acumula los tiempos de espera
        print("🛑 El %s aparca a las %.2f habiendo esperado %.2f horas " %
              (name, pasa, espera))
        yield env.process(estacionar(name))  # Invoca el proceso de estacionar
        deja = env.now  # Guarda el hora en que termina el proceso de estacionamiento
        print("🌬️ El %s deja el estacionamiento en la hora %.2f" % (name, deja))
        fin = deja  # Conserva globalmente el último hora de la simulación


def principal(env, estacionamiento):
    llegada = 0
    i = 0
    for i in range(TOT_AUTOS):  # Para n autos
        R = random.random()
        llegada = -T_LLEGADAS * math.log(R)  # Distribución exponencial
        # Deja transcurrir un tiempo entre uno y otro
        yield env.timeout(llegada)
        i += 1
        env.process(auto(env, 'auto %d' % i, estacionamiento))


print("------------------- Bienvenido a la Simulación de Estacionamiento -----------------")
random.seed(SEMILLA)  # Cualquier valor
env = simpy.Environment()  # Crea el objeto entorno de simulación
# Crea los recursos (espacios de estacionamiento)
estacionamiento = simpy.Resource(env, NUM_ESPACIOS)
env.process(principal(env, estacionamiento))  # Invoca el proceso principal
env.run()  # Inicia la simulación

print("---------------------------------------------------------------------")
print("\nIndicadores obtenidos")
lpc = te / fin
print("\nLongitud promedio de la cola: % .2f" % lpc)
tep = te / TOT_AUTOS
print("Tiempo de espera promedio = % .2f" % tep)
upi = (dt / fin) / NUM_ESPACIOS
print("Uso promedio del estacionamiento = % .2f" % upi)
print("\n---------------------------------------------------------------------")

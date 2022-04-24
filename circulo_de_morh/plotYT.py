from cProfile import run
import math as math
import numpy as np  
import matplotlib.pyplot as plt

R = 5e+7
o_prom = 2e+7
ang = np.linspace(0, 2 * np.pi,360) #para que grafique un circulo completo

x1 = R * np.cos(ang) + o_prom #el grafica en (0,0), hay que desplazarlo al C que uno quiere
y1 = R * np.sin(ang) #grafica cada punto (como arco/circunferencia) segun el angulo y radio que dé
print(y1)
plt.plot(x1, y1, color = "green") #qué es lo que grafica
plt.scatter(o_prom, 0) #ubicar el centro C
plt.axis('equal')
plt.show()
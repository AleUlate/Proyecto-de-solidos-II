from cProfile import run
import math as math
from multiprocessing.spawn import old_main_modules
import numpy as np  
import matplotlib.pyplot as plt


o_x = eval(input("Digite el valor del esfuerzo normal en el eje x: "))
o_y = eval(input("Digite el valor del esfuerzo normal en el eje y: "))
t_xy = eval(input("Digite el valor del esfuerzo cortante: "))

a = eval(input("Digite el valor del angulo: ")) #angulo cita en grados
a_radianes = (a* math.pi)/180
#condicional para saber si lo que me da el usuario lo tengo que utilizar o no

#cálculo de esfuerzos principales
o_min_a = (o_x + o_y)/2 + (o_x - o_y)/2*math.cos(2*a_radianes) + t_xy*math.sin(2*a_radianes) #con respecto a o_x
o_max_a = (o_x + o_y)/2 - (o_x - o_y)/2*math.cos(2*a_radianes) - t_xy*math.sin(2*a_radianes) #con respecto a o_y
o_min = (o_x + o_y)/2 - math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)
o_max = (o_x + o_y)/2 + math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)

t_xy2 = -(o_x - o_y)/2 * math.sin(2*a_radianes) + t_xy * math.cos(2*a_radianes)

#condicional para ver cómo claculos los esfuerzos principales
if a != 0:
    print(o_min_a, o_max_a)
else:
    print(o_min, o_max)

o_prom = (o_x + o_y)/2 #esfuerzo promedio
R = t_max = math.sqrt(((o_x - o_y)/2)**2 + t_xy**2) #R and t_max

#grafica
#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
#fig = plt.figure()
#ax = fig.add_subplot(111)

#patches = []
    ##patches.append(circle)


#circle = plt.Circle((o_prom, 0), radius = R)
#ax.add_patch(circle)

#plt.xlim([0, 100])
#plt.ylim([0, 100])
#plt.axis('equal')
#plt.show()
X = np.linspace(o_min_a, o_max_a,10)
Y = np.linspace(-t_xy2, +t_xy2,10)

if a != 0:
    x = [o_min_a, o_max_a]
    y = [-t_xy2, +t_xy2]
else:
    x = [o_min, o_max]
    y = [-t_xy2, +t_xy2]

func = (X - o_prom)**2 + (Y-0)**2 -R**2

#limites
plt.xlim([o_min_a + 2, o_max_a + 2])
plt.ylim([-t_xy2 - 2, +t_xy2 + 2])

for h in X:
    for k in Y:
        vector = (h - o_prom)**2 + (k-0)**2 - R**2
plt.plot(vector)
plt.show()


#plt.plot(func)
#plt.show()

#grafica de YT
R = 5e+7
ang = np.linspace(0, 2 * np.pi()) #para que grafique un circulo completo
x1 = R * math.cos(ang); y1 = R * math.sin(ang) #grafica cada punto (como arco/circunferencia) segun el angulo y radio que dé
plt.plot(x1, y1, color = "green")
plt.show()
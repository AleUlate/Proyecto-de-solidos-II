from cProfile import run
import math as math
from multiprocessing.spawn import old_main_modules
import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

o_x = eval(input("Digite el valor del esfuerzo normal en el eje x: "))
o_y = eval(input("Digite el valor del esfuerzo normal en el eje y: "))
t_xy = eval(input("Digite el valor del esfuerzo cortante: "))

a = eval(input("Digite el valor del angulo: ")) #angulo cita en grados
a_radianes = (a* math.pi)/180
#condicional para saber si lo qu eme da el usuario lo tengo que utilizar o no

#cálculo de esfuerzos principales
o_min_a = (o_x + o_y)/2 + (o_x - o_y)/2*math.cos(2*a_radianes) + t_xy*math.sin(2*a_radianes) #con respecto a o_x
o_max_a = (o_x + o_y)/2 - (o_x - o_y)/2*math.cos(2*a_radianes) - t_xy*math.sin(2*a_radianes) #con respecto a o_y
o_min = (o_x + o_y)/2 - math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)
o_max = (o_x + o_y)/2 + math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)

#condicional para ver cómo claculos los esfuerzos principales
if a != 0:
    print(o_min_a, o_max_a)
else:
    print(o_min, o_max)

o_prom = (o_x + o_y)/2 #esfuerzo promedio
R = t_max = math.sqrt(((o_x - o_y)/2)**2 + t_xy**2) #R and t_max

#grafica
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(111)

patches = []
    circle = Circle((o_prom, 0), R)
    patches.append(circle)


#circle = plt.Circle((o_prom, 0), radius = R)
#ax.add_patch(circle)


# Some limiting conditions on Wedge
patches += [
    Wedge((0.7, 0.8), 0.2, 0, 360, width=0.05), # Full ring
    ] 

plt.xlim([0, 100])
plt.ylim([0, 100])
plt.axis('equal')

plt.show()
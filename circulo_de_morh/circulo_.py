from cProfile import run
import math as math
from multiprocessing.spawn import old_main_modules
import numpy as np  
import matplotlib.pyplot as plt


o_x = eval(input("Digite el valor del esfuerzo normal en el eje x: "))
o_y = eval(input("Digite el valor del esfuerzo normal en el eje y: "))
t_xy = eval(input("Digite el valor del esfuerzo cortante: "))

a = eval(input("Digite el valor del ángulo (digite 0 si no lo tiene): ")) #angulo cita en grados
a_radianes = (a* math.pi)/180
#condicional para saber si lo que me da el usuario lo tengo que utilizar o no

#cálculo de esfuerzos principales
o_min_a = (o_x + o_y)/2 + (o_x - o_y)/2*math.cos(2*a_radianes) + t_xy*math.sin(2*a_radianes) #con respecto a o_x
o_max_a = (o_x + o_y)/2 - (o_x - o_y)/2*math.cos(2*a_radianes) - t_xy*math.sin(2*a_radianes) #con respecto a o_y
o_min = (o_x + o_y)/2 - math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)
o_max = (o_x + o_y)/2 + math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)

t_xy2 = -(o_x - o_y)/2 * math.sin(2*a_radianes) + t_xy * math.cos(2*a_radianes)

o_prom = (o_x + o_y)/2 #esfuerzo promedio
R = t_max = math.sqrt(((o_x - o_y)/2)**2 + t_xy**2) #R and t_max

#condicional para desplegar los esfuerzos principales
if a != 0:
    print(o_min_a, o_max_a)
else:
    print(o_min, o_max)

#grafica
ang = np.linspace(0, 2 * np.pi,360) #para que grafique un circulo completo

#grafica cada punto (como arco/circunferencia) segun el angulo y radio que dé
x1 = R * np.cos(ang) + o_prom #el grafica en (0,0), hay que desplazarlo al C que uno quiere
y1 = R * np.sin(ang) 

plt.plot(x1, y1, color = "r") #qué es lo que grafica
plt.scatter(o_prom, 0, color = 'g') #ubicar el centro C
plt.xlabel('esfuerzo normal'); plt.ylabel('esfuerzo cortante') #nombre de ejes
plt.axis('equal') #ejes a igual escala
plt.show()
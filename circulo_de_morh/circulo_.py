from cProfile import run
import math as m
from multiprocessing.spawn import old_main_modules
import numpy as np  
import matplotlib.pyplot as plt

#o_x = eval(input("Digite el valor del esfuerzo normal en el eje x: "))
#o_y = eval(input("Digite el valor del esfuerzo normal en el eje y: "))
#t_xy = eval(input("Digite el valor del esfuerzo cortante: "))

o_x = 5
o_y = -1
t_xy = 4
a = 0
#a = eval(input("Digite el valor del ángulo en grados (digite 0 si no aplica): ")) #angulo cita en grados
a_radianes = (a* m.pi)/180
o_prom = (o_x + o_y)/2 #esfuerzo promedio
R = t_max = m.sqrt(((o_x - o_y)/2)**2 + t_xy**2) #R and t_max
t_xy2 = -(o_x - o_y)/2 * m.sin(2*a_radianes) + t_xy * m.cos(2*a_radianes)

#cálculo de esfuerzos principales   
def o_minn (prom, ang, t, ox, oy):
    if ang == 0:
        o_min = prom - m.sqrt(((ox - oy)/2)**2 + (t)**2)
        return o_min
    else:
        o_min_a = prom - (ox - oy)/2*m.cos(2*ang) - t*m.sin(2*ang)
        return o_min_a
def o_maxx (prom, ang, t, ox, oy):
    if ang == 0:
        o_max = prom + m.sqrt(((ox - oy)/2)**2 + (t)**2)
        return o_max
    else:
        o_max_a = prom + (ox - oy)/2*m.cos(2*ang) + t*m.sin(2*ang)
        return o_max_a

#grafica
def plot(prom, R):
    #graficar circulo
    plt.subplot(121)
    ang = np.linspace(0, 2 * np.pi,360) #para que grafique un circulo completo
    #grafica cada punto (como arco/circunferencia) segun el angulo y radio que dé
    x1 = R * np.cos(ang) + prom #el grafica en (0,0), hay que desplazarlo al C que uno quiere
    y1 = R * np.sin(ang)
    p1 = plt.plot(x1, y1, color = "r") #qué es lo que grafica
    plt.scatter(prom, 0, color = 'k') #ubicar el centro C
    plt.xlabel('esfuerzo normal'); plt.ylabel('esfuerzo cortante') #nombre de ejes
    plt.axis('equal') #ejes a igual escala
    #anotaciones
    plt.annotate("o prom", (prom + 0.1 ,0.1))
    plt.plot(np.linspace(o_minn(o_prom, a_radianes, t_xy, o_x, o_y), 0), np.linspace(0,0), color = 'r', ls = ':'); plt.annotate("o mín", (o_minn(o_prom, a_radianes, t_xy, o_x, o_y)/2 , 0.1), color = 'r')
    plt.plot(np.linspace(o_maxx(o_prom, a_radianes, t_xy, o_x, o_y), 0), np.linspace(0,0), color = 'g', ls = ':'); plt.annotate("o máx", (o_maxx(o_prom, a_radianes, t_xy, o_x, o_y)/2 , 0.1), color = 'g')
    plt.plot(np.linspace(o_y, o_x), np.linspace(t_xy,-t_xy), color = 'y', ls = '-')
    plt.annotate('alpha', xy=((o_x - o_y)/4, t_xy/2), xycoords='data', xytext=(R/2, 0), textcoords='data', arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=-90"))
    
    #graficar cuadrado
    plt.subplot(122)
    p2 = plt.plot(x1 + 2, y1, color = 'b')
    plt.axis('off') #sin ejes
    plt.show()
print(plot(o_prom, R))
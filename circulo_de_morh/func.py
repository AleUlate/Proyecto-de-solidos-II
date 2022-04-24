from cProfile import run
import math as math
from turtle import circle
import numpy as np  
import matplotlib.pyplot as plt

a_radianes = (26.6* math.pi)/180
R = 5e+7
o_prom = 2e+7
o_x = 5e+7
o_y = -1e+7
t_xy = 4e+7

o_min_a = (o_x + o_y)/2 + (o_x - o_y)/2*math.cos(2*a_radianes) + t_xy*math.sin(2*a_radianes) #con respecto a o_x
o_max_a = (o_x + o_y)/2 - (o_x - o_y)/2*math.cos(2*a_radianes) - t_xy*math.sin(2*a_radianes) #con respecto a o_y
t_xy2 = -(o_x - o_y)/2 * math.sin(2*a_radianes) + t_xy * math.cos(2*a_radianes)


X = np.linspace( o_min_a, o_max_a, 10)
Y = np.linspace(t_xy2, -t_xy2, 10) 


#fig1 = plt.figure()

plt.plot(X,Y, color ='red')

plt.axis('equal') #grafica ejes a igual escala
plt.scatter(o_prom, 0, color = 'green') #ubicar el centro C
plt.xlabel('esfuerzo normal'); plt.ylabel('esfuerzo cortante') #nombre de ejes
plt.show()

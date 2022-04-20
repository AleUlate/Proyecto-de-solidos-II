from cProfile import run
import math as math
from multiprocessing.spawn import old_main_modules
import numpy as np  

o_x = eval(input("Digite el valor del esfuerzo normal en el eje x: "))
o_y = eval(input("Digite el valor del esfuerzo normal en el eje y: "))
t_xy = eval(input("Digite el valor del esfuerzo cortante: "))

a = eval(input("Digite el valor del angulo: ")) #angulo cita
#condicional para saber si lo qu eme da el usuario lo tengo que utilizar o no

#cálculo de esfuerzos principales
o_min_a = (o_x + o_y)/2 + (o_x - o_y)/2*math.cos(2*a) + t_xy*math.sin(2*a) #con respecto a o_x
o_max_a = (o_x + o_y)/2 - (o_x - o_y)/2*math.cos(2*a) - t_xy*math.sin(2*a) #con respecto a o_y
o_min = (o_x + o_y)/2 - math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)
o_max = (o_x + o_y)/2 + math.sqrt(((o_x - o_y)/2)**2 + (t_xy)**2)

#condicional para ver cómo claculos los esfuerzos principales
if a != 0:
    print(o_min_a, o_max_a)
else:
    print(o_min, o_max)

#grafica
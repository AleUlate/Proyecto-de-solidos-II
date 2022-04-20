import math as math

b1 = eval(input("Digite o valor de b1 \n"))
b2 = eval(input("Digite o valor de b2 \n"))
t1 = eval(input("Digite o valor de t1 \n"))
t2 = eval(input("Digite o valor de t2 \n"))
    
a1 = t1*(b1-t2)
a2 = b2*t2
at = a1 + a2

xbarra1 = t1/2
xbarra2 = b2/2
ybarra1 = (b1-t2)/2 
ybarra2 = t2/2

xA1 = xbarra1*a1
xA2 = xbarra2*a2
yA1 = ybarra1*a1
yA2 = ybarra2*a2

xAt = xA1 + xA2
yAt = yA1 + yA2

xtil = xAt/at
ytil = yAt/at

dx1 = xtil-xbarra1
dx2 = xtil-xbarra2

dy1 = ytil-ybarra1
dy2 = ytil-ybarra2

ixlinha1 = (t1*(b1-t2)*(b1-t2)*(b1-t2))/12
ixlinha2 = (b2*t2*t2*t2)/12
iylinha1 = (t1*t1*t1*(b1-t2))/12
iylinha2 = (b2*b2*b2*t2)/12

ix1 = ixlinha1 + (a1*dy1*dy1)
ix2 = ixlinha2 + (a2*dy2*dy2)
iy1 = iylinha1 + (a1*dx1*dx1)
iy2 = iylinha2 + (a2*dx2*dx2)

ixa = ix1 + ix2
iya = iy1 + iy2

centro = (ixa+iya)/2

ixy1 = 0 + dx1*dy1*a1
ixy2 = 0 + dx2*dy2*a2
ixya = ixy1+ixy2

print("Ix: %f" % ixa)
print("Iy: %f" % iya)
print("Ixy: %f" % ixya)
print("Centro: %f" % centro)
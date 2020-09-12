import turtle as t
t.shape('turtle')
import math as m
ang, k = 0.1, 1
for i in range (0,1000):
    ro=k*ang
    x = m.cos(ang)*ro
    y = m.sin(ang)*ro
    t.goto(x,y)
    ang+=0.1
    
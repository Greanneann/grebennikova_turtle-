import turtle as t
from random import *
t.shape('turtle')
t.speed(100)
for i in range(100):
    t.forward(randint(1,100))
    t.left(randint(0,360))
import turtle as t 
import math as m

def b(n,a):
    for i in range(n):
        t.forward(a)
        t.left(360/n)
def dug(n):
    for i in range(n):
        t.forward(0.3)
        t.right(90/n)
    for i in range(n):
        t.forward(1)
        t.right(180/n)
    for i in range(n):
        t.forward(0.3)
        t.right(90/n)
t.shape('turtle')
t.speed(30)
t.left(90)
t.begin_fill()
t.color('black','yellow')
n, a = 100, 4
b(n,a)
t.end_fill()
R = a/2/m.sin(m.pi/n)
t.penup()
t.goto(-R/3, 1/2*R)
t.pendown()
t.begin_fill()
t.color('black', 'blue')
b(n,1)
t.end_fill()
t.penup()
t.goto(-4/3*R, 1/2*R)
t.pendown
t.begin_fill()
b(n,1)
t.end_fill()

t.penup()
t.goto(-R, 1/2*R)
t.pendown()
t.left(180)
t.width(6)
t.forward(R)
t.penup()
t.goto(-3/4*R, 0)
t.pendown()
t.left(90)
dug(n)




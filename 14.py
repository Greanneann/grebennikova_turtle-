import turtle as t 
def star(n):
    for i in range(n):
        t.forward(150)
        t.left(180 - 360/2/n)
t.shape('turtle')
t.speed(10)
star(5)
t.penup()
t.goto(300,0)
t.pendown()
star(11)
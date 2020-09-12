import turtle as t

t.shape('turtle')
n = 36
t.speed(50)
for i in range(n):
    t.forward(90)
    t.stamp()
    t.left(180)
    t.forward(90)
    t.left(180 - 360/n)

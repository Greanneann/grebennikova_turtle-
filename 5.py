import turtle as t

t.shape('turtle')
t.speed(30)
for i in range(1,11):  
    t.pendown()  
    t.forward(10*i)
    t.left(90)
    t.forward(10*i)
    t.left(90)
    t.forward(10*i)
    t.left(90)
    t.forward(10*i)
    t.right(45)
    t.penup()
    t.forward(5*2**0.5)
    t.left(135)
    

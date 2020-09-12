import turtle as t 

t.shape('turtle')
t.speed(70)
for i in range(1,100):
    for j in range(1,3):
        t.forward(5 + i*5)
        t.left(90)
    

import turtle as t 
def b1(n):
    for i in range(n):
        t.forward(4)
        t.right(360/n)
def b2(n):
    for i in range(n):
        t.forward(4)
        t.left(360/n)
t.shape('turtle')
t.speed(70)
n = 80
lep = 4
for i in range(lep):
    b1(n)
    b2(n)
    t.right(180/lep)



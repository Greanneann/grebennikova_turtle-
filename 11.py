import turtle as t 
def b1(n,R):
    for i in range(n):
        t.forward(R)
        t.right(360/n)
def b2(n,R):
    for i in range(n):
        t.forward(R)
        t.left(360/n)
t.shape('turtle')
t.speed(70)
n = 80
lep = 4
R = 4
for i in range(lep):
    b1(n,R)
    b2(n,R)
    R+=2
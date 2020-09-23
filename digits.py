import turtle as t
def draw(A):
    for i in range(len(A[0])):
            t.right(A[0][i])
            t.forward(A[1][i])

digits = [[(90,270,270,270), (80,40,80,40)],[(90,225,135), (40,40*2**0.5,80)],[],[],[(90,270,270,180), (40,40,40,80)],[],[],[(0,135,315),(40,40*2**0.5,40)]]
index = (4,4,1,0,0,0)

for i, n in enumerate(index):
    draw(digits[n])
    t.penup()
    t.goto(80+80*i, 0)
    t.pendown()
    if n == 0:
        t.left(180)
    if n == 1:
        t.left(90)
    if n == 4:
        t.left(90)
    if n == 7:
        t.left(90)
    

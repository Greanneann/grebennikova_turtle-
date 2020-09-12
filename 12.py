import turtle as t
def dug(n):
    for i in range(n):
        t.forward(0.3)
        t.right(90/n)
    for i in range(n):
        t.forward(5)
        t.right(180/n)
    for i in range(n):
        t.forward(0.3)
        t.right(90/n)
t.shape("turtle")
t.left(180)
n = 40
kol = 5
for i in range(kol):
    dug(n)


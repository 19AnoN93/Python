import turtle

t = turtle.Turtle()
t.speed(0)
def poly(corners):
    for i in range(corners):
        t.fd(100)
        t.right(360/corners+corners)
        
def spiral(corners):
    size = 200
    for i in range(size, 0, -1):
        t.fd(i)
        t.right(360/corners + 0.1)
        turtle.pencolor(0+i, 0+i, 0+i) 
turtle.colormode(255)        
spiral(5)
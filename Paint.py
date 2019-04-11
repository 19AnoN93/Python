import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(1280,1120, "lightgreen")
screen.setup(0.8, 0.8)
t.ht()
t.up()
screen.tracer(0, 0)

def box():
    t.color("#e31bae", "#e8e807")
    t.seth(90)
    t.down()
    t.begin_fill()
    for i in range(360):
        t.fd(1)
        t.rt(1)
    t.end_fill()
    t.up()

def r():
    t.seth(0)
    t.fd(10)
    t.clear()
    box()
    screen.update()
    
def l():
    t.seth(180)
    t.fd(10)
    t.clear()
    box()
    screen.update()


def u():
    t.seth(90)
    t.fd(10)
    t.clear()
    box()
    screen.update()

def d():
    t.seth(270)
    t.fd(10)
    t.clear()
    box()
    screen.update()
    
def plus():
    for i in range(360+3):
        t.fd(1+2)
        t.rt(1+2)
    
def jump(x, y):
    t.goto(x, y)
    box()
    
box()
screen.update ()
screen.onkey(r, "Right")
screen.onkey(l, "Left")
screen.onkey(u, "Up")
screen.onkey(d, "Down")
screen.onkey(plus, "+")
screen.onclick(jump)
screen.listen()

turtle.mainloop()
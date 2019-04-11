import turtle
s = turtle.Screen()
s.tracer(0,0)
def box(x,y,x1,y1): 
    turtle.up() 
    turtle.goto(x,y) 
    turtle.down() 
    turtle.goto(x1,y) 
    turtle.goto(x1,y1) 
    turtle.goto(x,y1) 
    turtle.goto(x,y) 


def fbox(x,y,x1,y1): 
    for y in range(y,y1): 
        turtle.up() 
        turtle.goto(x,y) 
        turtle.down() 
        turtle.goto(x1,y) 

def GoBox():
    for x in range(-465, 465):
        fbox(-10+x, -10, 10+x, 10)
        s.update()
        turtle.clear()
        
    for x in range(465, -465, -1):
        fbox(-10+x, -10, 10+x, 10)
        s.update()
        turtle.clear()
while True:
    GoBox()
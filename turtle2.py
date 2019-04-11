import turtle
turtle.speed(1)
turtle.bgcolor("black")
turtle.color("Purple")

def PrintRoot(angle, lenght):
    if lenght < 300:
        turtle.left(angle) #начало
        turtle.fd(lenght)
        PrintRoot(angle, lenght*2)
        turtle.bk(lenght)
        turtle.rt(angle) #середина
        turtle.fd(lenght)
        PrintRoot(angle, lenght*2)
        turtle.bk(lenght)
        turtle.rt(angle) #конец
        turtle.fd(lenght)
        PrintRoot(angle, lenght*2)
        turtle.bk(lenght)
        turtle.lt(angle)
turtle.tracer(0,0)
PrintRoot(120,5)
turtle.update()
turtle.mainloop()

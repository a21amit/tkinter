import turtle
t=turtle.Turtle()
t.screen.bgcolor("black")
t.color("red")
t.pensize(1)
x=0
y=0
t.penup()
t.goto(x,200)
t.pendown()
a=0
b=0
while True:
    t.speed(10)
    t.fd(a)
    t.rt(b)
    a+=3
    b+=1
    if b==210:
        break
    t.hideturtle()

turtle.done()

import turtle
import math
t=turtle.Turtle()
t.screen.bgcolor("black")
t.color("red")
t.pensize(1)
x=0
y=200
t.penup()
t.goto(x,y)
a=1
b=-90
t.pendown()
t.hideturtle()
t.speed(20)
def curve():
    global a,b
    for i in range(34):
        t.lt(b)
        t.fd(math.sin(a)*5)
        a+=5
        b+=1
for i in range(15):
    curve()
    

turtle.done()



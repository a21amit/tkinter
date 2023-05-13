import turtle
t=turtle.Turtle()
t.color("red")
t.screen.bgcolor("black")
t.shapesize(1)
t.pensize(2)
t.setheading(29)
a=244
b=186
c=5
for i in range(60):
    t.speed(12);
    t.fd(a);
    t.rt(b);
    t.lt(c)
    

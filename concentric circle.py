import turtle
t=turtle.Turtle()
t.color("red")
t.screen.bgcolor("black")
t.shapesize(1)
t.pensize(1)
x=0
y=-200
radius=200
t.speed(20)

for i in range(41):
    t.penup();
    t.goto(x,y);
    t.pendown();
    t.circle(radius);
    radius-=5;
    y+=5;


    

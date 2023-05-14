import turtle as t
t=t.Turtle()
t.screen.bgcolor("black")
t.color("red")
t.pensize(1)
x=100
y=-100
t.speed(10)
t.penup()
t.goto(0,-5)
t.pendown()
t.circle(10)
t.penup()
t.home()
t.goto(x,y)
t.pendown()
t.hideturtle()
for i in range(4):
    t.lt(90)
    t.circle(50,180)
    t.lt(-180)
    t.circle(50,-180)




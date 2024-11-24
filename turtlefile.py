import turtle

turtle.title("My Turtle Program")

t = turtle.Turtle()
screen = turtle.getscreen()
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.goto(180, 150)
t.home()

t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()
t.clear()

c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)
screen.exitonclick()

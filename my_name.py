# Sophia M. Toliver, CIS 345 T TH 10:30, PE10

import turtle

turtle.setup(800, 700)
window = turtle.Screen()
window.reset()
window.bgcolor('pink')

t = turtle.Turtle()
t.color('red')
t.pencolor('dark blue')
t.pensize(5)
t.turtlesize(3)
t.speed(5)

# set on left side of the screen
t.penup()
t.backward(190)
t.left(90)
t.forward(100)

# draw letter S
t.pendown()
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.right(90)
t.forward(80)
t.right(90)
t.forward(80)
t.penup()

# draw letter O
t.goto(-100, 100)
t.pendown()
t.forward(80)
t.left(90)
t.forward(160)
t.left(90)
t.forward(80)
t.left(90)
t.forward(160)
t.penup()

# draw letter P
t.goto(10, 100)
t.left(90)
t.forward(90)
t.pendown()
t.right(180)
t.forward(60)
t.right(90)
t.forward(80)
t.right(90)
t.forward(60)
t.right(90)
t.forward(80)
# t.speed(0)
# for x in range(180):
#     t.forward(1)
#     t.right(1)
# t.speed(5)
# t.right(90)
# t.forward(115)
t.backward(160)
t.penup()

# draw letter H
t.goto(0, 100)
t.left(90)
t.pendown()
t.left(90)
t.forward(160)
t.backward(80)
t.left(90)
t.forward(80)
t.left(90)
t.forward(80)
t.backward(160)
t.penup()

# draw letter I
t.goto(100, 100)
t.pendown()
t.left(180)
t.forward(160)
t.penup()

# draw letter A
t.goto(170, 100)
t.pendown()
t.goto(110, -60)
t.penup()
t.goto(170, 100)
t.pendown()
t.goto(230, -60)
t.goto(200, 20)
t.right(90)
t.forward(60)
t.penup()

# draw smiley face
t.setposition(0, 0)
t.goto(20, -100)
t.pendown()
t.left(90)
t.forward(40)
t.penup()
t.setposition(0, 0)
t.goto(-20, -100)
t.pendown()
t.right(360)
t.forward(40)
t.penup()
t.setposition(-60, -160)
t.pendown()
t.left(360)
t.speed(0)
for x in range(180):
    t.forward(1)
    t.left(1)


t.hideturtle()
turtle.done()

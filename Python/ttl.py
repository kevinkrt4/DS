from turtle import Turtle
from turtle import Screen
import random

t = Turtle()
s = Screen()

t.clear()

s.screensize(canvwidth=640, canvheight=480)
#t.screen.bgcolor('black')
#t.color('blue')

#t.setheading(90) # Rotate counter-clockwise from zero (east)
#t.left(15) # Rotate left from current heading.
#t.right(15) # Rotate right from current heading.

#t.shape('circle') # arrow, circle, square, triaingle, turtle, classic
#t.shapesize(1) # Change size of the turtle

#t.hideturtle() # Hides the turtle
#t.showturtle() # Shows the turtle
#t.screen.bgpic('filename.gif') # Displays background image. Must be a .gif.

#t.fd(distance) # Draw a line at current heading, length of distance

#t.goto(x,y) # Go directly to x, y coordinates
#t.pensize(1)
#t.goto(100, 50)
#t.fd(100)
#t.hideturtle()
# y = mx + b

m = 1
b = 0
l1_domain = [-4, -2, 0, 2,  4, 6,8, 10]
l1_range = []

# Remember, the turtle starts at coordinate [0, 0]. So, if you want to plot a shape with -x coordnates  
# you need to pick up the pen, move to the starting coordinate, put the pen back down and then plot
#  t.setposition(x, y)
# Replaces the following code:
#  t.up()
#  t.goto(x,y) # Starting position
#  t.down()
for x in l1_domain:
    l1_range.append((m * x) + b)

for i in range(len(l1_domain)):
    print(l1_domain[i], l1_range[i])

t.color('blue')
t.pensize(2)
t.setposition(l1_domain[0], l1_range[0])
for i in range(1 ,len(l1_domain)):
    t.goto(l1_domain[i] * 10, l1_range[i] * 10)
    t.dot(5)

#If you are drawing a shape and want to fill it with a color use the following code sequence.
#t.color('the color you want')
#t.begin_fill()
# ...draw the shape
#t.end_fill()
t.color('blue')
t.setposition(0, 0)
t.begin_fill()
t.circle(5)
t.end_fill()
t.hideturtle()

# t.clear() Deleted the turtle's drawing on the screen.

# t.fillcolor('your color')
# Changes the color of the turtle only. The line it draws will be the color defined with t.color()
t.color('red')
t.fillcolor('blue')
t.goto(200, 200)
t.showturtle()


def random_drawing(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(["blue","red","green"]))
        random.choice([right,left])
        t.fd(distance)

t.speed(0)
t.setposition(0, 0)
random_drawing(100, 50)


t.clear()
t.hideturtle()
t.goto(200, 200) 
t.write("Cool Python Codes",move=True,align="center",font=('Cambria', 36, 'normal'))




#t.screen.exitonclick()
t.screen.mainloop()

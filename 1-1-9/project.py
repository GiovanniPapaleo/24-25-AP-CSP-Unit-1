

# PURPOSE: TO CREATE GALACTIC BODY
import turtle

screen = turtle.Screen()
screen.bgcolor('cyan')
# CONFIGURATION

# Variables list
size = 30
speed = 6

# Drawing tools
drawer1 = turtle.Turtle()
drawer2 = turtle.Turtle()
drawer3 = turtle.Turtle()
drawer4 = turtle.Turtle()
drawerlist = [drawer1,drawer2,drawer3,drawer4]


spinvelocity = 0
for drawer in drawerlist:
  drawer.speed(0)
  drawer.shape("square")
  drawer.shapesize(stretch_wid=size,stretch_len=1)
  drawer.left(45*spinvelocity)
  spinvelocity += 1

# MAIN PROGRAM

#windmill body
turtle.fillcolor("red")
turtle.right(180)
turtle.begin_fill()
turtle.circle(350,360,3)
turtle.end_fill()

# windmill branches configuration
windmill = turtle.Pen()
windmill.pencolor("white")
windmill.fillcolor("white")
windmill.begin_fill()
windmill.width(20)
windmill.speed(0)
windmill.up()
windmill.forward(size*10)
windmill.down()
windmill.left(90)
turtle.end_fill()
#windmill.circle(size*10)

# windmill spin
while True:
  for drawer in drawerlist:
    drawer.left(speed)



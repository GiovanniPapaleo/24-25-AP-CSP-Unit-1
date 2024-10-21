# construct dark background

import turtle

# creating turtle pen
t = turtle.Turtle()
t.speed(0)
# set background origin pos
t.penup()
t.goto(0, -550)
t.pendown()
# set the fillcolor
t.fillcolor("black")

# start the filling color
t.begin_fill()

# form circle
t.circle(1100, 360)

# ending the filling of the color
t.end_fill()

# create main galaxy



# add and organize star positions
t.fillcolor("white")
t.pensize(3)
t.penup()
t.goto(50,0)
t.pendown()
for star in range(18):
    t.begin_fill()
    t.penup()
    t.right(150)
    t.forward(120)
    t.pendown()
    t.circle(5, 360)
    t.end_fill()

wn = turtle.Screen()
wn.mainloop()



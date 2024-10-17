import turtle as trtl
trtl = trtl.Turtle()

# form central galaxy

trtl.pensize(75)
trtl.penup()
trtl.goto(0, 0)
trtl.pendown()
trtl.pencolor("yellow")
trtl.circle(40,360)

# create outer galaxy
trtl.penup()
trtl.goto(0, 0)
trtl.pendown()
trtl.pencolor("purple")
trtl.semicircle(40,360)

# illustrate galactic background
trtl.fillcolor("black")
trtl.begin_fill()
trtl.end_fill()




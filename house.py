import turtle
import math
c =  math.sqrt(100**2 + 100**2)

turtle.shape("turtle")

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.left(90 + 45)
turtle.forward(c)

turtle.left(90 + 45)
turtle.forward(100)

turtle.left(90 + 45)
turtle.forward(c)

turtle.left(90)
turtle.forward(c/2)

turtle.left(90)
turtle.forward(c/2)

turtle.exitonclick()
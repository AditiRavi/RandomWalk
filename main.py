import turtle
from turtle import Turtle, Screen
import random
turtle_1 = Turtle()
turtle_1.shape("turtle")
turtle.colormode(255)
directions = [0, 90, 180, 270]



# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "Dee
# pSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

'''Draw shapes'''

# def draw (n):
#     angle = 360 / n
#     for _ in range(n):
#        turtle_1.forward(100)
#        turtle_1.right(angle)

# for n in range(3,11):
#    turtle_1.color(random.choice(colours))
#    draw(n)


'''Random walk'''


def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

turtle_1.speed(0)

for _ in range(200):
    turtle_1.pensize(10)
    turtle_1.color(rand_color())
    turtle_1.setheading(random.choice(directions))
    turtle_1.forward(30)


# def rand_color():
#    r = random.randint(0,255)
#    g = random.randint(0,255)
#    b = random.randint(0,255)
#    color = (r, g, b)
#    return color

# turtle_1.speed(0)

# def draw_spirograph(gap):
#    for _ in range(int(360/gap)):
#        turtle_1.color(rand_color())
#        turtle_1.circle(100)
#        turtle_1.setheading(turtle_1.heading()+gap)
#
# draw_spirograph(5)




screen=Screen()
screen.exitonclick()